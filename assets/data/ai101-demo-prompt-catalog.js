(function () {
    'use strict';

    const LOCAL_ROOT = 'E:/Downloads-Organized/Personal/Adam Gurski Professional AI profile';

    const PROMPT_TYPES = [
        'text_only',
        'search_backed',
        'mock_data',
        'image_edit_single',
        'animation_start_end'
    ];

    const catalog = [
        {
            id: 'logo-01',
            title: 'Summit Premium Logo Creation',
            category: 'Image Editing',
            platform: 'Gemini (Portable)',
            promptType: 'text_only',
            role: 'You are a senior brand identity designer for premium home-service companies.',
            task: 'Create one clean, premium logo image for "Summit Interior and Exterior Painting." Design a single finished primary logo only, centered on a plain white background.',
            context: 'Logo direction: modern, clean, professional, upscale, trustworthy; polished local home-service brand; strong wordmark with a simple integrated emblem; subtle references to painting and home exteriors/interiors, minimal and uncluttered. Avoid cartoon styling, mascots, badges, fake mockups, extra icons, paint splatter, busy detail, and generic clip-art. Prioritize excellent legibility at small sizes for trucks, uniforms, social media, and print. Color palette: navy #0F2A47 primary, sky blue #6CC6FF secondary, white #FFFFFF negative space, muted gold #F5A623 used very sparingly.',
            format: 'Composition rules: one single logo only; balanced, refined, high-end identity; clean vector-style appearance; crisp edges, strong contrast, simple geometry; centered on white background. Do not include extra text, usage notes, multiple variations, monochrome versions, or icon-only versions. Create the final result as a professional logo presentation image showing only this one logo.'
        },
        {
            id: 'img-01',
            title: 'Founder Hero Composite with Premium Brand Art Direction',
            category: 'Image Editing',
            platform: 'Gemini (Portable)',
            promptType: 'image_edit_single',
            role: 'You are a premium ad designer and photo compositor for home-service brands.',
            task: 'Create a finished vertical painting-company advert now using Image 1 (founder portrait) as the identity source and Image 2 (Summit logo) as the branding source.',
            context: 'Use Image 1 to preserve exact founder identity (face, hair, beard, skin tone, expression). Use Image 2 logo styling, colors, and mark placement as the brand reference. Build a polished ad layout with the founder naturally painting in a clean interior scene, clear logo/header area, elegant curved dividers, and premium hierarchy. Include this exact text: "SUMMIT", "INTERIOR & EXTERIOR PAINTING", "Adam", "FOUNDER", "(718) 233-0338", "interioresummitpainting.com", "info@summitpainting.com". The final should match a production-ready commercial advert look.',
            format: 'Execute the edit directly. Return exactly 3 outputs: (1) final branded advert image, (2) short edit summary (max 6 bullets), (3) pass/fail quality checklist for identity accuracy, logo integration accuracy, text legibility, and commercial readiness. Do not write a prompt for another model.',
            requiredAssets: [
                LOCAL_ROOT + '/04_projects/ai-101/assets/images/20211027_145353.jpg',
                LOCAL_ROOT + '/04_projects/ai-101/assets/images/Gemini_Generated_Image_1t02f91t02f91t02 (1).png'
            ],
            fallbackNote: 'If the logo reference image is unavailable, preserve the same composition intent and color direction while generating a clean Summit-style logo lockup inside the advert.'
        },
        {
            id: 'dr-01',
            title: '90-Day Go-To-Market Decision Memo',
            category: 'Deep Research',
            platform: 'Gemini (Portable)',
            promptType: 'text_only',
            role: 'You are a senior market research strategist for residential service businesses.',
            task: 'Produce the final decision-grade 90-day go-to-market memo for launching Summit Interior and Exterior Painting in Springfield/Petersburg, Illinois.',
            context: 'Business objective: choose a launch strategy that can drive qualified quote requests within 90 days. Required coverage: ideal customer profiles, service packaging, pricing positioning, seasonal demand assumptions, local competitive landscape, primary risks, and a phased 30-60-90 execution plan. Constraints: explicitly separate evidence-backed conclusions from assumptions, note research gaps, and avoid vague marketing language.',
            format: 'Return 6 sections in order: Executive decision memo, ICP matrix, Positioning and offer strategy, Risk register with mitigations, 30-60-90 launch plan, Evidence-vs-assumption table. End with a pass/fail acceptance checklist. Do not output a meta-prompt.',
        },
        {
            id: 'ws-01',
            title: 'Local Demand and Competition Signal Pull',
            category: 'Web-Search Data Pull',
            platform: 'Gemini (Portable)',
            promptType: 'search_backed',
            role: 'You are a competitive intelligence analyst preparing a launch dashboard.',
            task: 'Execute live web search now using the provided queries and deliver current demand, competition, and weather-impact signals for Summit Interior and Exterior Painting.',
            context: 'Business objective: gather actionable facts for next-week marketing decisions. Use only live findings with source URLs and exact dates. Include weather-demand impact, active local competitors, and homeowner-intent indicators. Constraints: no fabricated numbers, include confidence labels, and flag sources older than 12 months.',
            format: 'Return 4 blocks: Signal table (metric, value, source, date, confidence), Competitor snapshot table, Top 5 opportunities, Top 5 risks. End with a pass/fail source-integrity checklist. Do not output a prompt template.',
            searchQueries: [
                'Springfield IL interior exterior painting services pricing',
                'Petersburg IL house painting contractor reviews',
                'site:weather.gov Springfield IL monthly outlook'
            ]
        },
        {
            id: 'web-01',
            title: 'Conversion Website Build From Service Brief',
            category: 'Website Coding',
            platform: 'Gemini (Portable)',
            promptType: 'mock_data',
            role: 'You are a senior conversion-focused front-end engineer.',
            task: 'Build a runnable one-page conversion website now for Summit Interior and Exterior Painting using the provided business brief.',
            context: 'Business objective: convert paid/social traffic into quote requests. Hard constraints: semantic HTML5, accessible form labels/errors, mobile-first layout, visible trust signals, clear above-the-fold CTA path, and plain homeowner-friendly copy; use only vanilla HTML/CSS/JS; no placeholders, no TODOs.',
            format: 'Return exactly 5 sections: (1) Project tree, (2) Complete file set in fenced blocks (index.html, styles.css, app.js), (3) Run instructions, (4) Conversion rationale by section, (5) pass/fail acceptance checklist. Do not output instructions for another model.',
            mockData: `BUSINESS BRIEF
Business name: Summit Interior and Exterior Painting
Service area: Springfield, Petersburg, Chatham, Sherman (Illinois)
Primary services:
- Interior repaint (walls, ceilings, trim)
- Exterior repaint (siding, doors, shutters)
- Cabinet refinishing
Guarantees:
- Written quote within 24 hours
- Daily cleanup commitment
- 2-year workmanship warranty
Primary CTA: Request a Free Quote
Secondary CTA: Call Now (217-555-0192)
Brand tone: trustworthy, clean, premium-but-approachable
Testimonials:
- "Crew was on time every day and the finish was flawless." - M. Carter
- "Best communication we have had from any contractor." - J. Delgado`
        },
        {
            id: 'app-01',
            title: 'Room Paint Estimator Single-File App',
            category: 'App Coding',
            platform: 'Gemini (Portable)',
            promptType: 'text_only',
            role: 'You are a senior frontend engineer and UX designer specializing in zero-dependency, high-performance web utilities.',
            task: 'Build a single-file, production-ready "Room Paint Estimator" using HTML5, vanilla JavaScript, and Tailwind CSS (via CDN). The app must be fully self-contained, responsive, and execute deterministic calculations instantly as the user types, with no Submit button.',
            context: 'Math and architecture requirements: accept room length/width/height in feet (decimals allowed). Gross Wall Area = 2*(Length*Height) + 2*(Width*Height). Optional ceiling toggle adds Length*Width. Deductions: doors (21 sq ft each) and windows (15 sq ft each). Net Paintable Area = max(0, Gross Area - Deductions). Paint specs: coats (integer min 1), price per gallon (float), coverage rate editable with default 350 sq ft/gal. Optional primer toggle adds a separate 1-coat primer line item with its own price/coverage. Final calculations: Total Area = Net Paintable Area * Coats; Gallons Needed = ceil(Total Area / Coverage Rate); Total Cost = Gallons Needed * Price per Gallon. UX requirements: real-time reactive updates on input events, modern Tailwind card layout with neutral premium palette, and a sticky desktop results panel (stacked on mobile) that includes an auditable line-item math breakdown.',
            format: 'Output constraints: return exactly ONE runnable HTML file only. Use Tailwind via CDN and place all JavaScript inside a <script> tag at the end of <body>. Do not use React, Vue, build tools, pseudocode, extra explanation, or multiple files.'
        },
        {
            id: 'graph-01',
            title: 'Pricing, Margin, and Capacity Decision Tables',
            category: 'Graph/Table Creation',
            platform: 'Gemini (Portable)',
            promptType: 'mock_data',
            role: 'You are an operations analyst preparing weekly decision visuals for ownership.',
            task: 'Calculate results from the provided jobs dataset and produce final management-ready pricing, margin, and crew-capacity outputs.',
            context: 'Business objective: identify where Summit should raise prices, protect margin, and rebalance crew hours. Constraints: show formulas used, never invent missing values, clearly label assumptions, and compute numeric results directly from the data.',
            format: 'Return 4 sections: Margin table by job type (with computed values), Capacity utilization table by week, Recommended pricing adjustment table, and chart spec block ready to render. End with a pass/fail accuracy checklist for formulas, units, and assumptions. Do not output a prompt template.',
            mockData: `JOBS DATA
job_id,week,service_type,revenue,materials,labor_hours,crew_size
J-101,2026-W14,interior,4200,920,38,2
J-102,2026-W14,exterior,6100,1480,52,3
J-103,2026-W14,cabinet,2800,640,29,2
J-104,2026-W15,interior,3900,880,36,2
J-105,2026-W15,exterior,6800,1650,58,3
J-106,2026-W15,cabinet,3100,710,33,2
Crew weekly capacity hours: 180`
        },
        {
            id: 'pdf-01',
            title: 'Promotional Collateral PDF Package',
            category: 'PDF Creation',
            platform: 'Gemini (Portable)',
            promptType: 'mock_data',
            role: 'You are a direct-response copywriter and print collateral strategist.',
            task: 'Create final print-ready collateral content now for Summit Interior and Exterior Painting: flyer, door hanger, and referral one-pager that can be exported to PDF immediately.',
            context: 'Business objective: drive quote requests from neighborhood distribution and social reposting. Constraints: clear homeowner language, compliant claims, no fake urgency, one consistent offer structure across all pieces, and complete copy (no placeholders).',
            format: 'Return 5 sections: Campaign message hierarchy, finished flyer copy, finished door-hanger copy, finished referral one-pager copy, and print-production spec (paper sizes, margins, type hierarchy, bleed/safe zone). End with a pass/fail print-readiness checklist. Do not output a prompt for another model.',
            mockData: `CAMPAIGN BRIEF
Business: Summit Interior and Exterior Painting
Primary audience: homeowners aged 30-65 in Springfield-area neighborhoods
Core offer: Free color consult + 10% off labor for bookings confirmed this month
Contact:
- Phone: 217-555-0192
- Email: hello@summitpaintingco.com
- Service area mention required: Springfield, Petersburg, Chatham, Sherman
Proof points:
- 2-year workmanship warranty
- Written quote in 24 hours
- Daily cleanup commitment`
        },
        {
            id: 'video-01',
            title: 'Portrait-to-Finished-Advert Continuous Transition',
            category: 'Start/End-Frame Video',
            platform: 'Gemini (Portable)',
            promptType: 'animation_start_end',
            role: 'You are a Veo-style performance ad director and VFX transition supervisor.',
            task: 'Generate an 8-second vertical promo video that starts on the uploaded founder portrait and ends on the uploaded finished advert image, using one continuous-shot transition (no hard cuts).',
            context: 'Business objective: create a high-retention social opener that smoothly moves from personal founder identity to polished branded advert. Hard constraints: 1080x1920, 24fps, 8.0s runtime; keep founder likeness clean in early frames; transition continuously using camera move + paint-sweep/graphic reveal instead of jump cuts; match the final frame composition to the uploaded advert image by 6.5s; hold the final frame clearly from 6.5-8.0s; preserve lighting and camera continuity; no unrelated brands or logos.',
            format: 'Return exactly 4 outputs: (1) final rendered video result, (2) timestamped continuous-shot transition breakdown table (timecode, camera move, reveal cue, continuity check), (3) end-frame text/readability plan, (4) pass/fail quality checklist for likeness preservation, transition smoothness, frame match accuracy, and end-frame readability. Do not output a meta-prompt.',
            requiredAssets: [
                LOCAL_ROOT + '/04_projects/ai-101/assets/images/20211027_145353.jpg',
                LOCAL_ROOT + '/04_projects/ai-101/assets/images/Gemini_Generated_Image_qdri2gqdri2gqdri.png'
            ]
        }
    ];

    function normalizePrompt(item) {
        const promptType = PROMPT_TYPES.includes(item.promptType) ? item.promptType : 'text_only';

        return {
            id: item.id,
            title: item.title || item.id,
            category: item.category || 'General',
            platform: item.platform || 'Any',
            promptType: promptType,
            role: item.role || '',
            task: item.task || '',
            context: item.context || '',
            format: item.format || '',
            requiredAssets: Array.isArray(item.requiredAssets) ? item.requiredAssets.slice() : [],
            searchQueries: Array.isArray(item.searchQueries) ? item.searchQueries.slice() : [],
            mockData: typeof item.mockData === 'string' ? item.mockData : '',
            optionalKreaStarter: item.optionalKreaStarter || null,
            fallbackNote: typeof item.fallbackNote === 'string' ? item.fallbackNote : ''
        };
    }

    const fullCatalog = catalog.map(normalizePrompt);

    window.ai101DemoPromptTypes = PROMPT_TYPES.slice();
    window.ai101DemoPromptCatalog = fullCatalog;
})();
