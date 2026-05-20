from pathlib import Path
import unittest

HTML = Path(__file__).resolve().parents[1] / "Product-Roadmap.html"


def html_text():
    return HTML.read_text(encoding="utf-8")


class TimelineViewFeatureTests(unittest.TestCase):
    def test_third_timeline_view_controls_are_present(self):
        html = html_text()
        self.assertIn("timelineViewIcon", html)
        self.assertIn("viewLabel(view) { return view === 'timeline' ? 'Timeline View'", html)
        self.assertIn("currentView === 'timeline'", html)
        self.assertIn("renderD3Timeline", html)

    def test_timeline_grouping_supports_unified_and_product(self):
        html = html_text()
        self.assertIn('id="timelineGrouping"', html)
        self.assertIn('value="unified"', html)
        self.assertIn('value="product"', html)
        self.assertIn("timelineGrouping === 'product'", html)
        self.assertIn("groupTimelineItems", html)

    def test_tag_picker_filters_exact_tags(self):
        html = html_text()
        self.assertIn('id="tagFilter"', html)
        self.assertIn("selectedTagFilter", html)
        self.assertIn("populateTagFilterControls", html)
        self.assertIn("deliverableMatchesSelectedTag", html)

    def test_timeline_is_self_contained_without_cdn_scripts(self):
        html = html_text()
        self.assertNotIn("https://d3js.org", html)
        self.assertNotIn("cdn.jsdelivr", html)
        self.assertNotIn("unpkg.com", html)
        self.assertIn("const d3Timeline", html)
        self.assertIn("createElementNS('http://www.w3.org/2000/svg'", html)

    def test_timeline_renders_svg_nodes_and_opens_existing_detail_drawer(self):
        html = html_text()
        self.assertIn("d3-timeline-svg", html)
        self.assertIn("timeline-node", html)
        self.assertIn("timeline-group-label", html)
        self.assertIn("openDetail(item.del, item.doc, item.dueDate)", html)


if __name__ == "__main__":
    unittest.main()
