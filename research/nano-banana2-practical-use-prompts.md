# Nano Banana 2 Prompt Pack (Slide 05 Practical Use Cases)

Coverage matches `05 / Applications` in the deck:
- Hospitality
- Real Estate
- Trades
- Libraries
- Retail
- Job Seekers
- Education
- Healthcare
- Legal

## Style Direction (from your reference images)
Use this exact look across all renders:
- Iridescent liquid-chrome surfaces with cyan, blue, violet, and amber reflections
- Cosmic deep-field atmosphere with nebula dust, star glints, and high contrast
- "AI signal" energy beams and luminous data trails where appropriate
- Cinematic realism, premium editorial framing, no text burned into image

## 1k Output Settings (Krea API)
- `width: 1024`
- `height: 1024`
- `num_images: 1` (or `2` for variations)
- Keep one fixed seed per category to get consistent style families

## Global Style Suffix
Append this to every prompt:

`ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark`

## Global Negative Prompt
`blurry, low quality, cartoon style, flat lighting, muddy colors, noisy artifacts, warped anatomy, extra limbs, bad hands, misshapen faces, text overlay, watermark, logo, frame, border`

## Category Prompts

### 01 Hospitality
`Luxury boutique hotel reception at twilight, concierge using an AI assistant interface to draft multilingual guest messages and itinerary options, polished marble and glass, warm hospitality, subtle floating translation cues, tasteful human interaction, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark`

### 02 Real Estate
`Real estate agent in a sunlit staged home using AI on a tablet to generate listing highlights, neighborhood comps, and marketing copy, clean architecture lines, modern furniture, trustworthy professional tone, subtle holographic data overlays, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark`

### 03 Trades
`Professional tradesperson in a residential mechanical room using AI assisted AR overlays to diagnose wiring and estimate materials, tools neatly organized, safe jobsite realism, strong side lighting, precision craftsmanship, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark`

### 04 Libraries
`Public library innovation desk, librarian helping patrons with AI powered research and summary assistance, books and digital terminals combined, inclusive community atmosphere, knowledge visualized as elegant star map style connections, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark`

### 05 Retail
`Independent shop owner managing inventory and product descriptions with AI, curated shelves, ecommerce and in-store workflow blended, subtle dashboard-like visual overlays for stock and campaigns, energetic commercial scene, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark`

### 06 Job Seekers
`Focused job seeker in a home office practicing interviews with AI coach, resume revisions on screen, confidence and momentum, desk details realistic, soft practical lighting with aspirational tone, subtle feedback graphics in air, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark`

### 07 Education
`Teacher leading an interactive classroom where AI creates adaptive lesson visuals and study support for diverse students, collaborative learning energy, tablets and whiteboard in use, optimistic future-ready environment, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark`

### 08 Healthcare
`Clinician reviewing patient notes with AI summarization assistant in a modern exam room, clear empathetic doctor patient interaction, clean medical environment, calm trustworthy lighting, treatment options visualized as secure data cards, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark`

### 09 Legal
`Attorney in a refined office using AI to analyze case files, contract clauses, and precedents, stacks of documents and laptop, serious professional tone, citation links represented as luminous node network, courtroom-grade confidence, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark`

## API Batch Array (drop into your existing Krea script)
```json
[
  {
    "id": "hospitality",
    "category": "Hospitality",
    "width": 1024,
    "height": 1024,
    "prompt": "Luxury boutique hotel reception at twilight, concierge using an AI assistant interface to draft multilingual guest messages and itinerary options, polished marble and glass, warm hospitality, subtle floating translation cues, tasteful human interaction, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark",
    "negative_prompt": "blurry, low quality, cartoon style, flat lighting, muddy colors, noisy artifacts, warped anatomy, extra limbs, bad hands, misshapen faces, text overlay, watermark, logo, frame, border"
  },
  {
    "id": "real_estate",
    "category": "Real Estate",
    "width": 1024,
    "height": 1024,
    "prompt": "Real estate agent in a sunlit staged home using AI on a tablet to generate listing highlights, neighborhood comps, and marketing copy, clean architecture lines, modern furniture, trustworthy professional tone, subtle holographic data overlays, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark",
    "negative_prompt": "blurry, low quality, cartoon style, flat lighting, muddy colors, noisy artifacts, warped anatomy, extra limbs, bad hands, misshapen faces, text overlay, watermark, logo, frame, border"
  },
  {
    "id": "trades",
    "category": "Trades",
    "width": 1024,
    "height": 1024,
    "prompt": "Professional tradesperson in a residential mechanical room using AI assisted AR overlays to diagnose wiring and estimate materials, tools neatly organized, safe jobsite realism, strong side lighting, precision craftsmanship, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark",
    "negative_prompt": "blurry, low quality, cartoon style, flat lighting, muddy colors, noisy artifacts, warped anatomy, extra limbs, bad hands, misshapen faces, text overlay, watermark, logo, frame, border"
  },
  {
    "id": "libraries",
    "category": "Libraries",
    "width": 1024,
    "height": 1024,
    "prompt": "Public library innovation desk, librarian helping patrons with AI powered research and summary assistance, books and digital terminals combined, inclusive community atmosphere, knowledge visualized as elegant star map style connections, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark",
    "negative_prompt": "blurry, low quality, cartoon style, flat lighting, muddy colors, noisy artifacts, warped anatomy, extra limbs, bad hands, misshapen faces, text overlay, watermark, logo, frame, border"
  },
  {
    "id": "retail",
    "category": "Retail",
    "width": 1024,
    "height": 1024,
    "prompt": "Independent shop owner managing inventory and product descriptions with AI, curated shelves, ecommerce and in-store workflow blended, subtle dashboard-like visual overlays for stock and campaigns, energetic commercial scene, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark",
    "negative_prompt": "blurry, low quality, cartoon style, flat lighting, muddy colors, noisy artifacts, warped anatomy, extra limbs, bad hands, misshapen faces, text overlay, watermark, logo, frame, border"
  },
  {
    "id": "job_seekers",
    "category": "Job Seekers",
    "width": 1024,
    "height": 1024,
    "prompt": "Focused job seeker in a home office practicing interviews with AI coach, resume revisions on screen, confidence and momentum, desk details realistic, soft practical lighting with aspirational tone, subtle feedback graphics in air, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark",
    "negative_prompt": "blurry, low quality, cartoon style, flat lighting, muddy colors, noisy artifacts, warped anatomy, extra limbs, bad hands, misshapen faces, text overlay, watermark, logo, frame, border"
  },
  {
    "id": "education",
    "category": "Education",
    "width": 1024,
    "height": 1024,
    "prompt": "Teacher leading an interactive classroom where AI creates adaptive lesson visuals and study support for diverse students, collaborative learning energy, tablets and whiteboard in use, optimistic future-ready environment, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark",
    "negative_prompt": "blurry, low quality, cartoon style, flat lighting, muddy colors, noisy artifacts, warped anatomy, extra limbs, bad hands, misshapen faces, text overlay, watermark, logo, frame, border"
  },
  {
    "id": "healthcare",
    "category": "Healthcare",
    "width": 1024,
    "height": 1024,
    "prompt": "Clinician reviewing patient notes with AI summarization assistant in a modern exam room, clear empathetic doctor patient interaction, clean medical environment, calm trustworthy lighting, treatment options visualized as secure data cards, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark",
    "negative_prompt": "blurry, low quality, cartoon style, flat lighting, muddy colors, noisy artifacts, warped anatomy, extra limbs, bad hands, misshapen faces, text overlay, watermark, logo, frame, border"
  },
  {
    "id": "legal",
    "category": "Legal",
    "width": 1024,
    "height": 1024,
    "prompt": "Attorney in a refined office using AI to analyze case files, contract clauses, and precedents, stacks of documents and laptop, serious professional tone, citation links represented as luminous node network, courtroom-grade confidence, ultra detailed cinematic realism, iridescent liquid chrome reflections, cosmic deep field background, nebula filaments, starlight sparkle, cyan violet amber color harmony, volumetric light rays, premium presentation composition, high dynamic range, no text, no logo, no watermark",
    "negative_prompt": "blurry, low quality, cartoon style, flat lighting, muddy colors, noisy artifacts, warped anatomy, extra limbs, bad hands, misshapen faces, text overlay, watermark, logo, frame, border"
  }
]
```
