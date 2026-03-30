$imgDir = "04_projects/ai-101/assets/images"
New-Item -ItemType Directory -Path $imgDir -Force | Out-Null
$queries = @(
  @{name='hero-ai.jpg'; q='artificial intelligence future digital'},
  @{name='people-collab.jpg'; q='team collaboration laptop office'},
  @{name='small-business.jpg'; q='small business owner storefront'},
  @{name='library-learning.jpg'; q='library reading learning'},
  @{name='data-analytics.jpg'; q='data analytics dashboard business'},
  @{name='coding-dev.jpg'; q='software developer coding computer'},
  @{name='creative-studio.jpg'; q='creative design studio'},
  @{name='automation-workflow.jpg'; q='automation workflow technology'},
  @{name='job-interview.jpg'; q='job interview office meeting'},
  @{name='marketing-campaign.jpg'; q='marketing campaign digital'}
)
$attrib = @('# AI 101 Imagery Sources (Openverse)','',"Downloaded: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",'','Fields: file | title | creator | license | source | image_url')
foreach($item in $queries){
  $api = "https://api.openverse.org/v1/images/?q=$([uri]::EscapeDataString($item.q))&page_size=25"
  try { $res = Invoke-RestMethod -Uri $api -Headers @{ 'User-Agent'='AI101DeckBuilder/1.0' } -ErrorAction Stop } catch { $attrib += "- $($item.name) | FAILED_API | | | $api | $($_.Exception.Message)"; continue }
  $saved = $false
  foreach($r in $res.results){
    $imgUrl = $r.url
    if(-not $imgUrl){ continue }
    if($imgUrl -notmatch '\.(jpg|jpeg|png)(\?|$)'){ continue }
    $out = Join-Path $imgDir $item.name
    try {
      Invoke-WebRequest -Uri $imgUrl -OutFile $out -MaximumRedirection 5 -Headers @{ 'User-Agent'='Mozilla/5.0' } -ErrorAction Stop
      $len = (Get-Item $out).Length
      if($len -lt 20000){ Remove-Item $out -Force; continue }
      $attrib += "- $($item.name) | $($r.title) | $($r.creator) | $($r.license) | $($r.foreign_landing_url) | $imgUrl"
      $saved = $true
      break
    } catch {
      continue
    }
  }
  if(-not $saved){ $attrib += "- $($item.name) | FAILED_DOWNLOAD | | | $api | no valid image found" }
}
$attrib | Set-Content -Path (Join-Path $imgDir 'SOURCES.md')
Get-ChildItem $imgDir | Select-Object Name,Length | Sort-Object Name
