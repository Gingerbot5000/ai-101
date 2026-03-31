import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX_HTML = (ROOT / "index.html").read_text(encoding="utf-8")


class PresentationDesignTests(unittest.TestCase):
    def test_font_stack_is_upgraded(self):
        self.assertIn("Space+Grotesk", INDEX_HTML)
        self.assertIn("Instrument+Sans", INDEX_HTML)
        self.assertIn("font-family: 'Instrument Sans', sans-serif;", INDEX_HTML)
        self.assertIn("font-family: 'Space Grotesk', sans-serif;", INDEX_HTML)

    def test_palette_moves_away_from_purple_glass(self):
        self.assertIn("--accent: #8bd6ff;", INDEX_HTML)
        self.assertIn("--accent-warm: #d7a65a;", INDEX_HTML)
        self.assertIn("--bg-base: #060a12;", INDEX_HTML)
        self.assertNotIn("--accent2", INDEX_HTML)

    def test_presentation_fit_tokens_lock_desktop_stage_frame(self):
        for marker in (
            "--deck-max-width: 1440px;",
            "--slide-frame-max-height: calc(var(--viewport-height) - var(--nav-height) - 44px);",
            "--slide-padding-x: clamp(28px, 3vw, 44px);",
            "--slide-padding-top: clamp(18px, 2vh, 28px);",
            "--slide-padding-bottom: calc(var(--nav-height) + clamp(14px, 2vh, 20px));",
            "--hero-rainbow: linear-gradient(135deg, #ffffff 0%, #8bd6ff 38%, #d7a65a 72%, #c084fc 100%);",
            "--hover-lift: translate3d(0, -4px, 0);",
        ):
            self.assertIn(marker, INDEX_HTML)
        self.assertRegex(
            INDEX_HTML,
            r"\.slide \{[\s\S]*?padding: var\(--slide-padding-top\) var\(--slide-padding-x\) var\(--slide-padding-bottom\);[\s\S]*?overflow: hidden;[\s\S]*?\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.slide-inner \{[\s\S]*?max-height: var\(--slide-frame-max-height\);[\s\S]*?height: var\(--slide-frame-max-height\);[\s\S]*?\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.gradient-text \{[\s\S]*?background: var\(--hero-rainbow\);[\s\S]*?\}",
        )

    def test_story_and_evidence_slides_get_density_fit_rules(self):
        self.assertRegex(
            INDEX_HTML,
            r"\.slide\[data-slide=\"0\"\]\s*\{[^}]*padding-top: 16px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.slide\[data-slide=\"1\"\] \.slide-inner\s*\{[^}]*max-width: 1380px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.story-intro-layout\s*\{[^}]*gap: 24px;[^}]*margin-bottom: 20px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.story-highlight-card\s*\{[^}]*padding: 16px 18px;[^}]*border-radius: 16px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.science-timeline\s*\{[^}]*align-items: stretch;[^}]*margin-top: 20px;[^}]*gap: 16px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.node-bottom\s*\{[^}]*padding: 20px 18px;[^}]*max-width: 332px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.editorial-callout-shell\s*\{[^}]*gap: 10px;[^}]*margin-top: 2px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.editorial-callout-block\s*\{[^}]*gap: 8px;[^}]*padding: 18px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.slide\[data-slide=\"0\"\] \.slide-inner,\s*\.slide\[data-slide=\"1\"\] \.slide-inner,\s*\.slide\[data-slide=\"2\"\] \.slide-inner,\s*\.slide\[data-slide=\"3\"\] \.slide-inner\s*\{[^}]*grid-template-rows: auto auto minmax\(0, 1fr\);[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.slide\[data-slide=\"0\"\] \.slide-inner\s*\{[^}]*min-height: var\(--slide-frame-max-height\);[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.hero-vortex-layer\s*\{[^}]*inset: -24px -40px calc\(var\(--nav-height\) \* -1\) -40px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.editorial-stat\s*\{[^}]*font-size: clamp\(32px, 4\.2vw, 54px\);[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.editorial-side-item\s*\{[^}]*gap: 5px;[^}]*padding: 12px 14px;[^}]*\}",
        )

    def test_tool_and_prompt_slides_get_desktop_fit_guards(self):
        desktop_block_start = INDEX_HTML.rfind('@media (min-width: 769px)')
        desktop_block_end = INDEX_HTML.rfind('@media (prefers-reduced-motion: reduce)')
        self.assertGreater(desktop_block_start, INDEX_HTML.rfind('@media (max-width: 640px)'))
        self.assertGreater(desktop_block_end, desktop_block_start)
        desktop_block = INDEX_HTML[desktop_block_start:desktop_block_end]
        self.assertRegex(
            desktop_block,
            r"\.slide\[data-slide=\"4\"\] \.slide-inner,\s*"
            r"\.slide\[data-slide=\"5\"\] \.slide-inner,\s*"
            r"\.slide\[data-slide=\"6\"\] \.slide-inner,\s*"
            r"\.slide\[data-slide=\"7\"\] \.slide-inner,\s*"
            r"\.slide\[data-slide=\"8\"\] \.slide-inner\s*\{[^}]*"
            r"grid-template-rows: auto auto minmax\(0, 1fr\);[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.orbital-diagram\s*\{[^}]*width: min\(760px, 100%\);[^}]*"
            r"min-height: 500px;[^}]*margin: 0 auto;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.assistant-card\s*\{[^}]*gap: 18px;[^}]*padding: 22px 24px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.specialist-card\s*\{[^}]*grid-template-columns: 96px 1fr;[^}]*"
            r"gap: 18px;[^}]*padding: 28px 30px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.use-case-cluster\s*\{[^}]*padding: 18px 18px 16px;[^}]*gap: 8px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.slide\[data-slide=\"8\"\] \.prompt-example\s*\{[^}]*margin-top: 6px;[^}]*"
            r"padding: 10px 12px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.assistant-card-list\s*\{[^}]*gap: 1px;[^}]*border-radius: 24px;[^}]*overflow: hidden;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.assistant-card-orb\s*\{[^}]*width: 76px;[^}]*height: 76px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.assistant-card-orb img\s*\{[^}]*width: 44px;[^}]*height: 44px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.assistant-card-body p\s*\{[^}]*font-size: 14px;[^}]*line-height: 1\.42;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.specialist-carousel-track\s*\{[^}]*min-height: 320px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.specialist-card-logo\s*\{[^}]*width: 78px;[^}]*height: 78px;[^}]*border-radius: 18px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.specialist-card-copy p\s*\{[^}]*font-size: 18px;[^}]*line-height: 1\.5;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.specialist-carousel-controls\s*\{[^}]*gap: 10px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.specialist-nav-btn\s*\{[^}]*min-width: 40px;[^}]*min-height: 40px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.use-case-groups\s*\{[^}]*gap: 12px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.cluster-list\s*\{[^}]*gap: 6px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.cluster-point\s*\{[^}]*grid-template-columns: 44px 1fr;[^}]*gap: 9px;[^}]*padding: 8px 0;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.cluster-point \.use-icon\s*\{[^}]*width: 44px;[^}]*height: 44px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.slide\[data-slide=\"8\"\] \{[^}]*padding: var\(--slide-padding-top\) var\(--slide-padding-x\) var\(--slide-padding-bottom\);[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.slide\[data-slide=\"8\"\] \.slide-inner\s*\{[^}]*max-width: 1320px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.slide\[data-slide=\"8\"\] \.prompt-formula-grid\s*\{[^}]*gap: 8px;[^}]*margin-bottom: 6px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.slide\[data-slide=\"8\"\] \.formula-block\s*\{[^}]*padding: 8px 10px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.slide\[data-slide=\"8\"\] \.prompt-text\s*\{[^}]*min-height: 36px;[^}]*max-height: 92px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.slide\[data-slide=\"8\"\] \.prompt-asset-card\s*\{[^}]*width: 168px;[^}]*\}",
        )
        self.assertRegex(
            desktop_block,
            r"\.slide\[data-slide=\"8\"\] \.prompt-asset-preview\s*\{[^}]*height: clamp\(54px, 7vh, 72px\);[^}]*\}",
        )

    def test_safety_close_and_mobile_rules_preserve_stage_fit(self):
        self.assertRegex(
            INDEX_HTML,
            r"\.slide\[data-slide=\"9\"\] \.slide-inner,\s*\.slide\[data-slide=\"10\"\] \.slide-inner \{[^}]*grid-template-rows: auto auto minmax\(0, 1fr\);[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.safety-shield-grid \{[^}]*gap: 12px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.safety-shield \{[^}]*min-height: 216px;[^}]*padding: 42px 24px;[^}]*gap: 6px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.safety-shield \.safety-icon \{[^}]*width: 48px;[^}]*height: 48px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.callback-montage \{[^}]*min-height: 560px;[^}]*padding: 24px;[^}]*border-radius: 28px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.callback-cta-card \{[^}]*width: min\(980px, 100%\);[^}]*gap: 18px;[^}]*padding: 24px 26px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.callback-cta-card \.cta-grid \{[^}]*gap: 14px;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.link-card\.tonight-card \{[^}]*min-height: 0;[^}]*\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"@media \(max-width: 1180px\) \{[\s\S]*?\.slide \{[^}]*overflow-y: auto;[^}]*\}[\s\S]*?\.slide-inner \{[^}]*max-height: none;[^}]*height: auto;[^}]*\}[\s\S]*?\}",
        )

    def test_deck_expands_to_guided_workshop_story(self):
        slide_ids = re.findall(r'<div class="slide(?: active)?" data-slide="(\d+)">', INDEX_HTML)
        self.assertEqual([str(i) for i in range(11)], slide_ids)
        self.assertIn('id="navIndicator">1 / 11<', INDEX_HTML)
        self.assertIn(">01 / My Story<", INDEX_HTML)
        self.assertIn(">02 / Science Proof<", INDEX_HTML)
        self.assertIn(">03 / Education Proof<", INDEX_HTML)
        self.assertIn(">07 / Applications<", INDEX_HTML)
        self.assertIn(">10 / Tonight<", INDEX_HTML)

    def test_personal_transformation_story_is_now_the_opener(self):
        self.assertRegex(INDEX_HTML, r"Three years ago, I had\s+never built a website")
        self.assertIn("made a video", INDEX_HTML)
        self.assertIn("built a workflow", INDEX_HTML)
        self.assertIn("started a business", INDEX_HTML)
        self.assertIn("designed logos", INDEX_HTML)
        self.assertIn("learn this much this fast", INDEX_HTML)

    def test_two_evidence_slides_anchor_the_credibility_arc(self):
        self.assertIn("AI is accelerating Nobel-scale discovery", INDEX_HTML)
        self.assertIn("AlphaFold", INDEX_HTML)
        self.assertIn("2.2 million", INDEX_HTML)
        self.assertIn("Stanford Tutor CoPilot", INDEX_HTML)
        self.assertIn("Harvard physics trial", INDEX_HTML)
        self.assertIn("structured use helps", INDEX_HTML)
        self.assertIn("unstructured use can backfire", INDEX_HTML)

    def test_overview_and_use_cases_shift_to_grouped_workshop_model(self):
        self.assertIn("Broad assistants", INDEX_HTML)
        self.assertIn("Specialist tools", INDEX_HTML)
        self.assertIn("Local business", INDEX_HTML)
        self.assertIn("Learning and research", INDEX_HTML)
        self.assertIn("Career and work", INDEX_HTML)
        self.assertIn("Personal projects", INDEX_HTML)

    def test_prompt_lab_emphasizes_teach_mode_and_stage_focus(self):
        self.assertIn("Prompt Lab", INDEX_HTML)
        self.assertIn("Teach mode", INDEX_HTML)
        self.assertIn("Operator mode", INDEX_HTML)
        self.assertIn("prompt-stage-panel", INDEX_HTML)
        self.assertIn("prompt-framework-strip", INDEX_HTML)
        self.assertIn("setPromptFocus", INDEX_HTML)
        self.assertIn("prompt-focus-active", INDEX_HTML)

    def test_prompt_formula_keeps_the_four_part_framework(self):
        for marker in ("01", "02", "03", "04"):
            self.assertIn(f'<div class="formula-icon">{marker}</div>', INDEX_HTML)

    def test_close_is_three_curated_actions_with_secondary_contact(self):
        self.assertIn("Try one thing tonight", INDEX_HTML)
        self.assertEqual(INDEX_HTML.count('class="glass link-card tonight-card"'), 3)
        self.assertIn("Ask one research question", INDEX_HTML)
        self.assertIn("Upload one document", INDEX_HTML)
        self.assertIn("Start one practical conversation", INDEX_HTML)
        self.assertIn("Questions? Let's connect.", INDEX_HTML)

    def test_shared_hover_focus_language_covers_major_components(self):
        self.assertRegex(
            INDEX_HTML,
            r"\.story-tag,\s*\.editorial-callout-block,\s*\.specialist-nav-btn,\s*\.specialist-dot,\s*\.prompt-asset-card,\s*\.callback-cta-card\s*\{[\s\S]*?"
            r"transition: transform 0\.18s ease, border-color 0\.18s ease, box-shadow 0\.18s ease, background-color 0\.18s ease, filter 0\.18s ease;[\s\S]*?\}",
        )
        self.assertRegex(
            INDEX_HTML,
            r"\.story-tag:hover,\s*\.story-tag:focus-visible,\s*\.editorial-callout-block:hover,\s*\.editorial-callout-block:focus-within,\s*\.specialist-nav-btn:hover,\s*\.specialist-nav-btn:focus-visible,\s*\.specialist-dot:hover,\s*\.specialist-dot:focus-visible,\s*\.prompt-asset-card:hover,\s*\.prompt-asset-card:focus-within,\s*\.callback-cta-card:hover,\s*\.callback-cta-card:focus-within\s*\{[\s\S]*?transform: var\(--hover-lift\);[\s\S]*?\}",
        )

    def test_visual_overhaul_uses_cinematic_cross_dissolve(self):
        self.assertIn("scale(0.97)", INDEX_HTML)
        self.assertIn("scale(1.03)", INDEX_HTML)
        self.assertIn("blur(2px)", INDEX_HTML)
        self.assertIn("0.6s ease-out", INDEX_HTML)
        self.assertIn("@media (prefers-reduced-motion: reduce)", INDEX_HTML)

    def test_visual_overhaul_adds_slide_specific_layout_systems(self):
        for marker in (
            "hero-vortex-layer",
            "story-thread-layout",
            "editorial-callout-shell",
            "orbital-diagram",
            "assistant-constellation",
            "specialist-carousel",
            "use-case-scene-grid",
            "prompt-card-stack",
            "safety-shield-grid",
            "callback-montage",
        ):
            self.assertIn(marker, INDEX_HTML)

    def test_visual_overhaul_registers_slide_activity_controllers(self):
        self.assertIn("const slideControllers = new Map()", INDEX_HTML)
        self.assertIn("function registerSlideController", INDEX_HTML)
        self.assertIn("function setSlideActivity", INDEX_HTML)
        self.assertIn("heroVortexSketch", INDEX_HTML)
        self.assertIn("assistantConstellationSketch", INDEX_HTML)

    def test_assistant_constellation_cards_stay_wired_to_runtime_hooks(self):
        self.assertRegex(INDEX_HTML, r'class="assistant-card(?: is-active)?" data-assistant="chatgpt"')
        self.assertIn("document.querySelectorAll('.assistant-card')", INDEX_HTML)
        self.assertIn('.assistant-card[data-assistant="${assistantAttractorKey}"] .assistant-card-orb', INDEX_HTML)

    def test_specialist_and_prompt_interactions_get_new_shells(self):
        self.assertIn("specialist-carousel-track", INDEX_HTML)
        self.assertIn("specialist-progress-bar", INDEX_HTML)
        self.assertIn("prompt-stack-position", INDEX_HTML)
        self.assertIn("prompt-stack-formulas", INDEX_HTML)
        self.assertIn("prompt-copy-check", INDEX_HTML)

    def test_safety_and_close_slides_gain_density_and_depth(self):
        self.assertEqual(INDEX_HTML.count('class="glass safety-shield"'), 6)
        self.assertGreaterEqual(INDEX_HTML.count('class="montage-fragment"'), 6)


if __name__ == "__main__":
    unittest.main()
