# Product Roadmap — JSON Schema

This document describes the data format for the `Product-Roadmap.html` interactive roadmap artifact. The machine-readable JSON Schema is stored in `roadmap.schema.json`.

The roadmap supports the provided **Project Roadmap Schema** for product documents. Timeline range dates use `"Mon YYYY"`; deliverable due dates use the product schema's `dueDates` array.

---

## Mental Model

The page manages a **set of independent product roadmap JSON documents**.

In the **Edit Data** drawer:

- Each product gets its own JSON card/text area.
- Each card contains one product roadmap object using the schema below.
- Raw JSON is collapsed by default; click **Edit JSON** on a card to reveal the textarea.
- Use **Add Deliverable** on a product card to append a task to that product, including empty newly-created product JSON documents.
- Use **Load JSON Document** to import one or more `.json` files when you do not want to paste JSON manually.
- Use the checkbox on each card to toggle that product on/off.
- Enabled products render together as separate swimlanes on the same timeline.
- Disabled products stay saved locally but are hidden from the roadmap view.
- The header view toggle switches between the month grid and a chronological linear due-date list.

The page saves the document set and toggle states to `localStorage`.

---

## Product Roadmap Object

Each editor card contains one product roadmap JSON object:

```json
{
  "project": "Backend Platform",
  "title": "Product Roadmap",
  "subtitle": "Interactive Deliverables & Timeline",
  "lastUpdated": "2026-05-08 14:30:00 ET",
  "owner": "Engineering Team",
  "deliverables": [
    {
      "id": "bp-001",
      "title": "API Authentication",
      "owner": "Engineering Team",
      "status": "in-progress",
      "start": "May 2026",
      "end": "Jun 2026",
      "desc": "Implement OAuth2 and JWT token management for API endpoints.",
      "dueDates": [
        { "date": "05/15/2026", "status": "in-progress", "note": "Token endpoint handoff." },
        { "date": "06/30/2026", "status": "not-started", "note": "" }
      ],
      "notes": []
    }
  ]
}
```

| Field | Required | Type | Description |
|---|---|---|---|
| `project` | **Yes** | string | Product, project, or contract name. Displayed as the swimlane header and toggle label. |
| `title` | **Yes** | string | Document/page title. The first enabled product controls the page title. |
| `subtitle` | **Yes** | string | Document/page subtitle. With multiple products enabled, the page shows the enabled product count. |
| `lastUpdated` | **Yes** | string | Last update timestamp, e.g. `YYYY-MM-DD HH:mm:ss ET`. Auto-updated on save. |
| `owner` | **Yes** | string | Primary owner or contractor responsible for the roadmap. |
| `deliverables` | **Yes** | array | List of deliverables. |

---

## Deliverable Object

| Field | Required | Type | Description |
|---|---|---|---|
| `id` | **Yes** | string | Unique deliverable identifier, e.g. `bp-001`. The supplied schema pattern is `^[a-z]{2}-\\d{3}$`. |
| `title` | **Yes** | string | Deliverable title. Displayed in the timeline block and detail panel. |
| `owner` | **Yes** | string | Owner responsible for this deliverable. |
| `status` | **Yes** | enum | Overall task status. Values: `not-started`, `in-progress`, `at-risk`, `blocked`, `completed`, `on-hold`, `cancelled`. Individual due-date chips use `dueDates[].status`. |
| `start` | **Yes** | string | Planned start month in `"Mon YYYY"` format. |
| `end` | **Yes** | string | Planned end month in `"Mon YYYY"` format. Must be `>=` `start` chronologically. |
| `desc` | **Yes** | string | Detailed description, requirements, or submission rules. |
| `dueDates` | **Yes** | array | Preferred list of due date objects with `date`, `status`, and `note`. Legacy `MM/DD/YYYY` strings are migrated automatically. Parseable dates render into timeline month chips. |
| `notes` | **Yes** | array | Additional comments, attachments, metadata, or status-change notes. |

---

## Due Date Rendering

Each deliverable can have one or more values in `dueDates`. Preferred entries are objects so each date can track status and a note independently:

```json
"dueDates": [
  { "date": "05/15/2026", "status": "in-progress", "note": "Token endpoint handoff." },
  { "date": "06/30/2026", "status": "not-started", "note": "" }
]
```

Legacy string entries are still accepted and migrated by the UI:

```json
"dueDates": ["05/15/2026", "06/30/2026"]
```

Rendering behavior:

1. The left side of each row shows the deliverable title and owner.
2. The timeline does **not** draw a long start-to-end duration bar.
3. Any `MM/DD/YYYY` due date is converted to its `Mon YYYY` month.
4. Each parsed due date is rendered as a small due-date chip using that due date's own `status` color inside the matching month column.
5. Click a due-date chip to open the drawer for that specific date, update its status, and save a date-specific note.
6. Click a month heading to filter the roadmap to tasks with due dates in that month and highlight the column green; use **Clear month** to remove the filter.
7. Use the header search box to filter tasks by phrase across title, owner, description, status, notes, and due dates.
8. Switch to the linear view to see due-date items sorted chronologically; rows due in the current week are highlighted in gold and remain clickable/editable.

---

## Saved Document Set

When you download all roadmap data, the export uses this wrapper so product toggle state can be preserved:

```json
{
  "documents": [
    {
      "id": "backend-platform",
      "enabled": true,
      "data": {
        "project": "Backend Platform",
        "title": "Product Roadmap",
        "subtitle": "Interactive Deliverables & Timeline",
        "lastUpdated": "2026-05-08 14:30:00 ET",
        "owner": "Engineering Team",
        "deliverables": []
      }
    }
  ]
}
```

For normal editing, you usually only edit the **product object** inside each card, not the wrapper. Raw JSON is hidden by default; use **Edit JSON** only when direct data changes are needed. **Add Deliverable** appends a normalized deliverable object into the selected product's `deliverables` array. **Load JSON Document** accepts a single product object, an array of product objects, or this wrapped export format.

---

## Date Formats

### Timeline Range Dates

`start` and `end` use **`"Mon YYYY"`** where:

- `Mon` is `Jan`, `Feb`, `Mar`, `Apr`, `May`, `Jun`, `Jul`, `Aug`, `Sep`, `Oct`, `Nov`, or `Dec`
- `YYYY` is the four-digit year

The default timeline supports **January 2026 through December 2032**.

### Due Dates

`dueDates` prefers objects with a parseable `date`, a per-date `status`, and a free-text `note`.

Examples:

- `{ "date": "05/15/2026", "status": "in-progress", "note": "Token endpoint handoff." }` renders in the `May 2026` column with the in-progress chip color
- `{ "date": "12/01/2028", "status": "completed", "note": "Accepted." }` renders in the `Dec 2028` column with the completed chip color
- Legacy `"05/15/2026"` entries are migrated to `{ "date": "05/15/2026", "status": <deliverable status>, "note": "" }`

---

## Workflow

1. Open `Product-Roadmap.html` in a browser.
2. Click **Edit Data**.
3. Add one product roadmap JSON document per card, click **Add Deliverable** on a product card, click **Edit JSON** for raw edits, or click **Load JSON Document** to import `.json` files.
4. Check or uncheck product cards to toggle products on/off.
5. Click **Save & Render**.
6. Enabled products render together as separate swimlanes.
7. Use the view toggle to switch between grid view and the chronological linear due-date view.
8. Due dates display as month chips when parseable.
9. Click a due-date chip or linear row to edit that specific due date's status and note.
10. Click a month heading to filter to due dates in that month, or use search to filter tasks by phrase.
11. Click **Download Enabled JSONs** or **Download All JSONs** to export backups.
12. Click **Clear Cache** in the drawer to reset to embedded defaults.

---

## Tips

- Use one JSON card per product.
- Keep `id` values unique within each product roadmap.
- Keep `start` and `end` within the supported range: Jan 2026 – Dec 2032.
- Use `dueDates` for concrete submission dates; each due date can carry its own status and note.
- Use `desc` for coordination context — blockers, dependencies, definition of done.
- To change the date range, edit the year loop in the `MONTHS` generator at the top of the HTML file.
