param(
    [string]$PromptFile = (Join-Path $PSScriptRoot "nano-banana2-practical-use-prompts.json"),
    [string]$OutputDir = (Join-Path $PSScriptRoot "..\assets\images\generated\practical-use-cases"),
    [ValidateSet("nano-banana-pro", "nano-banana", "nano-banana-flash")]
    [string]$Model = "nano-banana-pro",
    [int]$PollSeconds = 3,
    [int]$TimeoutSeconds = 300
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -Path $PromptFile)) {
    throw "Prompt file not found: $PromptFile"
}

$apiKey = $env:KREA_API_KEY
if ([string]::IsNullOrWhiteSpace($apiKey)) {
    throw "Missing KREA_API_KEY. Set it in this shell before running."
}

$apiBase = "https://api.krea.ai"
$generateUrl = "$apiBase/generate/image/google/$Model"
$headers = @{
    Authorization = "Bearer $apiKey"
}

$prompts = Get-Content -Path $PromptFile -Raw | ConvertFrom-Json
if (-not $prompts) {
    throw "No prompts found in: $PromptFile"
}

New-Item -Path $OutputDir -ItemType Directory -Force | Out-Null

$manifest = New-Object System.Collections.Generic.List[object]
$total = @($prompts).Count
$index = 0

foreach ($item in $prompts) {
    $index++
    $id = if ($item.id) { [string]$item.id } else { "prompt-$index" }
    $id = ($id -replace "[^a-zA-Z0-9_-]", "_")
    $category = if ($item.category) { [string]$item.category } else { "Uncategorized" }

    Write-Host ("[{0}/{1}] Generating {2} ({3})..." -f $index, $total, $id, $category)

    $width = if ($item.width) { [int]$item.width } else { 1024 }
    $height = if ($item.height) { [int]$item.height } else { 1024 }
    $batchSize = if ($item.batchSize) { [int]$item.batchSize } else { 1 }

    $body = @{
        prompt = [string]$item.prompt
        width = $width
        height = $height
        batchSize = $batchSize
    }

    if ($item.negative_prompt) { $body.negativePrompt = [string]$item.negative_prompt }
    if ($item.imageUrls) { $body.imageUrls = $item.imageUrls }
    if ($item.styleImages) { $body.styleImages = $item.styleImages }
    if ($item.aspectRatio) { $body.aspectRatio = [string]$item.aspectRatio }

    try {
        $job = Invoke-RestMethod -Method Post -Uri $generateUrl -Headers $headers -ContentType "application/json" -Body ($body | ConvertTo-Json -Depth 10)
    }
    catch {
        Write-Warning ("Failed to submit {0}: {1}" -f $id, $_.Exception.Message)
        $manifest.Add([pscustomobject]@{
            id = $id
            category = $category
            status = "submit_failed"
            error = $_.Exception.Message
            files = @()
        })
        continue
    }

    $jobId = [string]$job.job_id
    $status = [string]$job.status
    $result = $null
    $deadline = (Get-Date).AddSeconds($TimeoutSeconds)

    while ((Get-Date) -lt $deadline) {
        Start-Sleep -Seconds $PollSeconds
        $jobData = Invoke-RestMethod -Method Get -Uri "$apiBase/jobs/$jobId" -Headers $headers -TimeoutSec 60
        $status = [string]$jobData.status
        Write-Host ("  status: {0}" -f $status)

        if ($status -eq "completed") {
            $result = $jobData.result
            break
        }

        if ($status -eq "failed" -or $status -eq "cancelled") {
            break
        }
    }

    if ($status -ne "completed" -or -not $result) {
        Write-Warning ("Job did not complete for {0}. Final status: {1}" -f $id, $status)
        $manifest.Add([pscustomobject]@{
            id = $id
            category = $category
            status = $status
            error = "Job not completed"
            files = @()
        })
        continue
    }

    $urls = @($result.urls)
    if ($urls.Count -eq 0) {
        Write-Warning ("No URLs returned for {0}" -f $id)
        $manifest.Add([pscustomobject]@{
            id = $id
            category = $category
            status = "completed_no_urls"
            error = "No output URLs"
            files = @()
        })
        continue
    }

    $savedFiles = @()
    $imgIndex = 0
    foreach ($url in $urls) {
        $imgIndex++
        $ext = ".png"
        try {
            $uri = [Uri]$url
            $pathExt = [System.IO.Path]::GetExtension($uri.AbsolutePath)
            if (-not [string]::IsNullOrWhiteSpace($pathExt)) {
                $ext = $pathExt
            }
        }
        catch {
            $ext = ".png"
        }

        $fileName = "{0}-{1:D2}{2}" -f $id, $imgIndex, $ext
        $destPath = Join-Path $OutputDir $fileName
        Invoke-WebRequest -Uri $url -OutFile $destPath -TimeoutSec 180
        $savedFiles += $destPath
        Write-Host ("  saved: {0}" -f $destPath)
    }

    $manifest.Add([pscustomobject]@{
        id = $id
        category = $category
        status = "completed"
        job_id = $jobId
        files = $savedFiles
    })
}

$manifestPath = Join-Path $OutputDir "manifest.json"
$manifest | ConvertTo-Json -Depth 8 | Set-Content -Path $manifestPath -Encoding UTF8
Write-Host ("Done. Manifest: {0}" -f $manifestPath)
