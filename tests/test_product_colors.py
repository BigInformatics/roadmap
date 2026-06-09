from pathlib import Path
import unittest

HTML = Path(__file__).resolve().parents[1] / "Product-Roadmap.html"
SCHEMA = Path(__file__).resolve().parents[1] / "roadmap.schema.json"


def text(path):
    return path.read_text(encoding="utf-8")


class ProductColorFeatureTests(unittest.TestCase):
    def test_product_color_helpers_and_defaults_are_present(self):
        html = text(HTML)
        self.assertIn("const DEFAULT_PRODUCT_COLORS", html)
        self.assertIn("function normalizeProductColor", html)
        self.assertIn("function productColor", html)
        self.assertIn("#3b82f6", html)

    def test_editor_exposes_product_color_picker_and_hex_input(self):
        html = text(HTML)
        self.assertIn("data-color-swatch", html)
        self.assertIn("data-product-color", html)
        self.assertIn("Product Color", html)
        self.assertIn("Hex code", html)

    def test_linear_list_rows_render_product_color_bar(self):
        html = text(HTML)
        self.assertIn(".linear-product-bar", html)
        self.assertIn('style="--product-color:${escapeHtml(productColor(item.doc))}"', html)
        self.assertIn("linear-product-bar", html)

    def test_direct_view_buttons_show_icons_and_active_state(self):
        html = text(HTML)
        self.assertIn('data-view-mode="grid"', html)
        self.assertIn('data-view-mode="linear"', html)
        self.assertIn('data-view-mode="timeline"', html)
        self.assertIn("viewIcon(view)", html)
        self.assertIn("btn.classList.toggle('active', currentView === view)", html)
        self.assertIn("Grid View", html)
        self.assertIn("List View", html)

    def test_schema_allows_optional_product_color(self):
        schema = text(SCHEMA)
        self.assertIn('"color"', schema)
        self.assertIn('"pattern": "^#([A-Fa-f0-9]{6})$"', schema)

    def test_schema_allows_review_status(self):
        schema = text(SCHEMA)
        self.assertIn('"review"', schema)


if __name__ == "__main__":
    unittest.main()
