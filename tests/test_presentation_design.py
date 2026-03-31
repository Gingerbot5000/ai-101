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
            "--deck-max-width:",
            "--slide-frame-max-height:",
            "--slide-padding-x:",
            "--slide-padding-top:",
            "--slide-padding-bottom:",
            "--hero-rainbow:",
            "--hover-lift:",
        ):
            self.assertIn(marker, INDEX_HTML)
        self.assertIn(".slide {", INDEX_HTML)
        self.assertIn("padding: var(--slide-padding-top) var(--slide-padding-x) var(--slide-padding-bottom);", INDEX_HTML)
        self.assertIn("overflow: hidden;", INDEX_HTML)
        self.assertIn("max-height: var(--slide-frame-max-height);", INDEX_HTML)
        self.assertIn("height: var(--slide-frame-max-height);", INDEX_HTML)
        self.assertIn(".gradient-text {", INDEX_HTML)
        self.assertIn("background: var(--hero-rainbow);", INDEX_HTML)

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
        for marker in (
            ".story-tag:hover",
            ".story-tag:focus-visible",
            ".editorial-callout-block:hover",
            ".specialist-nav-btn:hover",
            ".specialist-nav-btn:focus-visible",
            ".specialist-dot:hover",
            ".prompt-asset-card:hover",
            ".prompt-asset-card:focus-within",
            ".callback-cta-card:hover",
            ".callback-cta-card:focus-within",
            "transform: var(--hover-lift);",
            "transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease, background-color 0.18s ease, filter 0.18s ease;",
        ):
            self.assertIn(marker, INDEX_HTML)

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
