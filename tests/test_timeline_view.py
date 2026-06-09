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

    def test_timeline_layout_avoids_card_overlap(self):
        html = html_text()
        self.assertIn("function layoutTimelineItems", html)
        self.assertIn("const cardWidth = 168", html)
        self.assertIn("const cardGap = 14", html)
        self.assertIn("rowEnds.findIndex", html)
        self.assertIn("group.layoutRows", html)
        self.assertNotIn("((itemIdx % 3) - 1) * 28", html)

    def test_timeline_supports_zoomed_timeframes_and_horizontal_scroll(self):
        html = html_text()
        self.assertIn('id="timelineWindow"', html)
        self.assertIn('value="month"', html)
        self.assertIn('value="quarter"', html)
        self.assertIn('value="year"', html)
        self.assertIn('value="all"', html)
        self.assertIn("let timelineWindow = 'all';", html)
        self.assertIn("timelineWindow === 'month' ? 1", html)
        self.assertIn("function timelineVisibleDomain", html)
        self.assertIn("function shiftTimelineWindow", html)
        self.assertIn("data-timeline-pan=\"prev\"", html)
        self.assertIn("data-timeline-pan=\"next\"", html)
        self.assertIn("timeline-scroll-canvas", html)
        self.assertIn("fullDomain[1].getMonth() - months, 1", html)
        self.assertIn("item.parsed >= domain[0] && item.parsed < domain[1]", html)

    def test_list_view_is_default_and_view_buttons_are_direct(self):
        html = html_text()
        self.assertIn("let currentView = 'linear';", html)
        self.assertIn('data-view-mode="grid"', html)
        self.assertIn('data-view-mode="linear"', html)
        self.assertIn('data-view-mode="timeline"', html)
        self.assertIn("document.querySelectorAll('[data-view-mode]')", html)
        self.assertNotIn("function nextViewMode()", html)
        self.assertNotIn("btnViewToggle", html)

    def test_quick_status_actions_support_completed_and_review(self):
        html = html_text()
        self.assertIn('value="review">Review', html)
        self.assertIn("'review':'Review'", html)
        self.assertIn("data-quick-status=\"completed\"", html)
        self.assertIn("data-quick-status=\"review\"", html)
        self.assertIn("function setQuickStatus", html)
        self.assertIn("bindQuickStatusActions(row, item.del, item.doc, item.dueDate)", html)
        self.assertIn("bindQuickStatusActions(chipWrap, del, doc, dueDate)", html)
        self.assertIn(".status-review { background: #ffd6e7;", html)


if __name__ == "__main__":
    unittest.main()
