from pathlib import Path
import unittest

HTML = Path(__file__).resolve().parents[1] / "Product-Roadmap.html"


def html_text():
    return HTML.read_text(encoding="utf-8")


class MatrixViewFeatureTests(unittest.TestCase):
    def test_matrix_view_control_is_present(self):
        html = html_text()
        self.assertIn('data-view-mode="matrix"', html)
        self.assertIn("matrixViewIcon", html)
        self.assertIn("currentView === 'matrix'", html)
        self.assertIn("renderCoordinationMatrix", html)

    def test_matrix_helpers_and_default_tags_are_present(self):
        html = html_text()
        self.assertIn("DEFAULT_COORDINATION_TAGS", html)
        self.assertIn("'integration'", html)
        self.assertIn("'validation'", html)
        self.assertIn("function collectMatrixItems", html)
        self.assertIn("function isCoordinationRelevant", html)
        self.assertIn("function isRoutineCadence", html)
        self.assertIn("function buildMatrixPhases", html)
        self.assertIn("function groupMatrixItems", html)

    def test_matrix_controls_support_low_noise_options(self):
        html = html_text()
        self.assertIn('id="matrixPhaseMode"', html)
        self.assertIn('value="auto"', html)
        self.assertIn('value="quarter"', html)
        self.assertIn('value="federal-fy"', html)
        self.assertIn('value="year"', html)
        self.assertIn('id="btnMatrixHideRoutine"', html)
        self.assertIn('id="btnMatrixStrict"', html)
        self.assertIn("let matrixHideRoutine = true;", html)
        self.assertIn("let matrixStrictMode = false;", html)

    def test_matrix_supports_federal_fiscal_year_quarters(self):
        html = html_text()
        self.assertIn("function federalFiscalQuarterLabel", html)
        self.assertIn("function federalFiscalQuarterStartDate", html)
        self.assertIn("date.getMonth() >= 9 ? date.getFullYear() + 1", html)
        self.assertIn("Q${quarter} FY ${String(fiscalYear).slice(-2)}", html)
        self.assertIn("Federal FY • Starts ${formatQuarterStartDate", html)
        self.assertIn("1: new Date(fiscalYear - 1, 9, 1)", html)
        self.assertIn("2: new Date(fiscalYear, 0, 1)", html)
        self.assertIn("3: new Date(fiscalYear, 3, 1)", html)
        self.assertIn("4: new Date(fiscalYear, 6, 1)", html)
        self.assertIn("'federal-fy'", html)

    def test_matrix_honors_existing_filters_and_opens_detail_drawer(self):
        html = html_text()
        self.assertIn("filter(deliverableMatchesFilters)", html)
        self.assertIn("visibleDueDates(del)", html)
        self.assertIn("doc.data.coordinationGroup || productName(doc)", html)
        self.assertIn("openDetail(match.del, match.doc, match.dueDate)", html)

    def test_matrix_groups_repeated_due_dates_unless_status_breakout_matters(self):
        html = html_text()
        self.assertIn("function groupMatrixCellItems", html)
        self.assertIn("MATRIX_BREAKOUT_STATUSES", html)
        self.assertIn("function matrixGroupBreakoutKey", html)
        self.assertIn("matrix-count-badge", html)
        self.assertIn("matrix-date-chip", html)
        self.assertIn("due dates", html)

    def test_matrix_highlights_current_phase_column(self):
        html = html_text()
        self.assertIn("function isCurrentMatrixPhase", html)
        self.assertIn("phase.matches(now)", html)
        self.assertIn("current-phase", html)
        self.assertIn("matrix-current-label", html)
        self.assertIn('aria-current=\"date\"', html)
        self.assertIn("Current</div>", html)

    def test_matrix_is_self_contained_without_external_dependencies(self):
        html = html_text()
        self.assertNotIn("https://d3js.org", html)
        self.assertNotIn("cdn.jsdelivr", html)
        self.assertNotIn("unpkg.com", html)
        self.assertIn("matrix-board", html)
        self.assertIn("matrix-item", html)


if __name__ == "__main__":
    unittest.main()
