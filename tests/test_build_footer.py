from pathlib import Path
import re
import unittest

HTML = Path(__file__).resolve().parents[1] / "Product-Roadmap.html"


def html_text():
    return HTML.read_text(encoding="utf-8")


class BuildFooterTests(unittest.TestCase):
    def test_build_datetime_footer_is_present_at_bottom(self):
        html = html_text()
        self.assertIn('class="build-footer"', html)
        self.assertIn('aria-label="Build information"', html)
        self.assertIn('id="buildDatetime"', html)
        self.assertIn('Build datetime:', html)
        self.assertLess(html.index('class="build-footer"'), html.index('<div class="overlay"'))

    def test_build_datetime_uses_utc_iso_datetime_attribute(self):
        html = html_text()
        match = re.search(r'<time id="buildDatetime" datetime="([^"]+)">([^<]+)</time>', html)
        self.assertIsNotNone(match)
        self.assertRegex(match.group(1), r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
        self.assertTrue(match.group(2).endswith(" UTC"))


if __name__ == "__main__":
    unittest.main()
