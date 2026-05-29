from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "Product-Roadmap.html"
WORKFLOW = ROOT / ".github" / "workflows" / "pages.yml"
INDEX = ROOT / "index.html"


def html_text():
    return HTML.read_text(encoding="utf-8")


class MatrixScreenshotExportTests(unittest.TestCase):
    def test_matrix_screenshot_button_is_present_and_matrix_gated(self):
        html = html_text()
        self.assertIn('id="btnMatrixScreenshot"', html)
        self.assertIn('aria-label="Download Matrix Screenshot"', html)
        self.assertIn("downloadImageIcon", html)
        self.assertIn("screenshotBtn.disabled = currentView !== 'matrix'", html)
        self.assertIn("Matrix screenshot is available in Matrix View", html)

    def test_native_canvas_export_is_dependency_free(self):
        html = html_text()
        self.assertIn("function downloadMatrixScreenshot", html)
        self.assertIn("document.createElement('canvas')", html)
        self.assertIn("canvas.toDataURL('image/png')", html)
        self.assertIn("roadmap-matrix-${new Date().toISOString().slice(0, 10)}.png", html)
        self.assertIn("groupMatrixCellItems", html)
        self.assertNotIn("html2canvas", html)

    def test_native_canvas_export_matches_theme_and_expands_groups(self):
        html = html_text()
        screenshot = html[html.index("function downloadMatrixScreenshot") : html.index("function renderD3Timeline")]
        self.assertIn("getComputedStyle(document.body).getPropertyValue(name)", html)
        self.assertIn("getComputedStyle(document.documentElement).getPropertyValue(name)", html)
        self.assertIn("groupedItems.forEach((itemGroup, itemIdx) =>", screenshot)
        self.assertIn("74 + groupMatrixCellItems(group.phases.get(phase.label) || []).length * 62", screenshot)
        self.assertNotIn("groupedItems.slice(0, 4)", screenshot)
        self.assertNotIn("more groups", screenshot)


class GithubPagesPublishingTests(unittest.TestCase):
    def test_pages_workflow_deploys_static_site_from_main(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("name: Publish GitHub Pages", text)
        self.assertIn("branches: [main]", text)
        self.assertIn("actions/configure-pages@v5", text)
        self.assertIn("actions/upload-pages-artifact@v3", text)
        self.assertIn("actions/deploy-pages@v4", text)
        self.assertIn("pages: write", text)
        self.assertIn("id-token: write", text)

    def test_index_redirects_to_roadmap_artifact(self):
        text = INDEX.read_text(encoding="utf-8")
        self.assertIn("Product-Roadmap.html", text)
        self.assertIn("http-equiv=\"refresh\"", text)


if __name__ == "__main__":
    unittest.main()
