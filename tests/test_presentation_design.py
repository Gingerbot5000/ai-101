import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX_HTML = (ROOT / "index.html").read_text(encoding="utf-8")


class PresentationDesignTests(unittest.TestCase):
    def test_font_stack_and_palette_stay_on_refreshed_system(self):
        self.assertIn("Space+Grotesk", INDEX_HTML)
        self.assertIn("Instrument+Sans", INDEX_HTML)
        self.assertIn("--accent: #8bd6ff;", INDEX_HTML)
        self.assertIn("--accent-warm: #d7a65a;", INDEX_HTML)
        self.assertIn("--bg-base: #060a12;", INDEX_HTML)

    def test_deck_now_has_nine_slides_in_sequence(self):
        slide_ids = re.findall(r'<div class="slide(?: active)?" data-slide="(\d+)">', INDEX_HTML)
        self.assertEqual([str(i) for i in range(9)], slide_ids)
        self.assertIn('id="navIndicator">1 / 9<', INDEX_HTML)
        for marker in (
            ">01 / My Story<",
            ">02 / Science Proof<",
            ">03 / Core Assistants<",
            ">04 / Tools<",
            ">05 / Applications<",
            ">06 / Prompt Lab<",
            ">07 / Safety<",
            ">08 / Tonight<",
        ):
            self.assertIn(marker, INDEX_HTML)

    def test_story_cards_match_updated_personal_examples(self):
        for marker in (
            "Grammy-winner visuals",
            "Fatboy Slim",
            "Built real business websites",
            "Designed and shipped several live sites for businesses",
            "Started my own company",
            "Designed apps and games",
            "full dev team before",
        ):
            self.assertIn(marker, INDEX_HTML)

    def test_science_slide_adds_the_math_reasoning_breakthrough(self):
        for marker in (
            "grid-template-columns: repeat(4, 1fr);",
            'id="p5-box-4"',
            "Proof Assistant",
            "Terence Tao",
            "ready for primetime",
            "The frontier moved from search to reasoning.",
        ):
            self.assertIn(marker, INDEX_HTML)

    def test_big_three_cards_have_accents_and_2026_copy(self):
        for marker in (
            "--card-accent: #10B981;",
            "--card-accent: #8BD6FF;",
            "--card-accent: #D7A65A;",
            "Claude Code",
            "AI Studio",
            "Search-connected answers",
        ):
            self.assertIn(marker, INDEX_HTML)

    def test_additional_tools_slide_is_rendered_from_tool_wall_data(self):
        for marker in (
            'class="tool-wall" id="toolWall"',
            'class="tool-info-card" id="toolInfoCard"',
            "const toolWallData = [",
            "name: 'Suno'",
            "name: 'NotebookLM'",
            "name: 'Claude Code'",
            "name: 'Codex'",
            "name: 'AntiGravity'",
            "name: 'DeepSeek'",
            "renderToolWall()",
            "showToolInfo(",
            "scheduleToolInfoHide(",
        ):
            self.assertIn(marker, INDEX_HTML)

    def test_removed_intermediate_slide_systems_are_gone(self):
        for marker in (
            "Education Proof",
            "Tool Map",
            "specialist-carousel",
            "renderSpecialistCarousel",
            "specialistState",
            "specialistItems",
            "orbital-diagram",
            "orbital-core",
            "editorial-callout-shell",
        ):
            self.assertNotIn(marker, INDEX_HTML)

    def test_prompt_safety_and_closing_indices_shift_forward_cleanly(self):
        for marker in (
            '.slide[data-slide="6"] .prompt-example {',
            '<div class="slide" data-slide="6">',
            '<div class="slide" data-slide="7">',
            '<div class="slide" data-slide="8">',
            '.slide.active[data-slide="7"] .safety-shield {',
            '.slide.active[data-slide="8"] .callback-cta-card {',
        ):
            self.assertIn(marker, INDEX_HTML)

    def test_polish_updates_hover_system_and_title_date(self):
        for marker in (
            "Updated April 2, 2026",
            ".story-highlight-card:hover {",
            ".assistant-card:hover,",
            ".use-case-cluster:hover {",
            ".safety-shield:hover {",
            ".tonight-card:hover {",
            ".callback-cta-card .subtitle {",
            "overflow-wrap: break-word;",
        ):
            self.assertIn(marker, INDEX_HTML)


if __name__ == "__main__":
    unittest.main()
