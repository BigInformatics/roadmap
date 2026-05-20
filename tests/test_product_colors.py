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

    def test_view_toggle_shows_destination_icon_and_label(self):
        html = text(HTML)
        self.assertIn("const targetView = currentView === 'grid' ? 'linear' : 'grid';", html)
        self.assertIn("targetView === 'grid' ? gridIcon() : listIcon()", html)
        self.assertIn("Switch to Grid View", html)
        self.assertIn("Switch to List View", html)

    def test_schema_allows_optional_product_color(self):
        schema = text(SCHEMA)
        self.assertIn('"color"', schema)
        self.assertIn('"pattern": "^#([A-Fa-f0-9]{6})$"', schema)


if __name__ == "__main__":
    unittest.main()
