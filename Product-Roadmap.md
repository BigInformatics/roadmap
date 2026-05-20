# Product Roadmap — JSON Schema

This document describes the data format for the `Product-Roadmap.html` interactive roadmap artifact. The machine-readable JSON Schema is stored in `roadmap.schema.json`.

The roadmap schema supports every JSON shape the app imports/exports: a single product roadmap object, an array of product roadmap objects, or the wrapped `{ "documents": [...] }` export that preserves enabled/toggle state. Timeline range dates use `"Mon YYYY"`; deliverable due dates use the product schema's `dueDates` array.

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
- Use the product color swatches or hex input on each card to set the product-level `color` used by list-view row bars.
- Enabled products render together as separate swimlanes on the same timeline.
- Disabled products stay saved locally but are hidden from the roadmap view.
- The header view toggle switches between the month grid and a chronological linear due-date list. The Month and Year dropdown filters apply to both views.

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
  "order": 1,
  "color": "#3b82f6",
  "deliverables": [
    {
      "id": "bp-001",
      "title": "API Authentication",
      "owner": "Engineering Team",
      "status": "in-progress",
      "start": "May 2026",
      "end": "Jun 2026",
      "desc": "Implement OAuth2 and JWT token management for API endpoints.",
      "tags": ["api", "security"],
      "favorite": true,
      "dueDates": [
        { "date": "05/15/2026", "status": "in-progress", "note": "Token endpoint handoff.", "actions": [
          { "name": "Architecture review", "note": "Security sign-off captured.", "timestamp": "2026-05-12 14:30:00 ET" }
        ] },
        { "date": "06/30/2026", "status": "not-started", "note": "", "actions": [] }
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
| `order` | No | number | Optional product display order. Lower numbers render first in product toggles, grid swimlanes, and list-view grouping. Products without `order` keep a stable fallback order after ordered products. |
| `color` | No | string | Optional 6-digit hex color such as `#3b82f6`. The edit drawer provides default swatches and a custom hex input; list-view rows show this product color as a 10px bar on the far left. |
| `deliverables` | **Yes** | array | List of deliverables. |

---

## Deliverable Object

| Field | Required | Type | Description |
|---|---|---|---|
| `id` | **Yes** | string | Unique deliverable identifier within the product roadmap. The UI can generate values like `bp-003`; existing data may use shorter IDs like `bp-1`. |
| `title` | **Yes** | string | Deliverable title. Displayed in the timeline block and detail panel. |
| `owner` | **Yes** | string | Owner responsible for this deliverable. |
| `status` | **Yes** | enum | Overall task status. Values: `not-started`, `in-progress`, `at-risk`, `blocked`, `completed`, `on-hold`, `cancelled`. Individual due-date chips use `dueDates[].status`. |
| `start` | **Yes** | string | Planned start month in `"Mon YYYY"` format. |
| `end` | **Yes** | string | Planned end month in `"Mon YYYY"` format. Must be `>=` `start` chronologically. |
| `desc` | **Yes** | string | Detailed description, requirements, or submission rules. |
| `tags` | No | array or string | Optional labels for filtering. Arrays such as `["api", "security"]` and comma-separated strings are normalized by the UI. The header **Tags** toggle makes the search box match tags only. |
| `favorite` | No | boolean | Optional task star. `true` marks a task as a favorite; the header **Favorites** toggle filters to favorites only. |
| `dueDates` | **Yes** | array | Preferred list of due date objects with `date`, `status`, `note`, and optional `actions`. Legacy `MM/DD/YYYY` strings are migrated automatically. Parseable dates render into timeline month chips. |
| `notes` | **Yes** | array | Additional comments, attachments, metadata, or status-change notes. |

---

## Due Date Rendering

Each deliverable can have one or more values in `dueDates`. Preferred entries are objects so each date can track status, a note, and optional timestamped actions independently:

```json
"dueDates": [
  {
    "date": "05/15/2026",
    "status": "in-progress",
    "note": "Token endpoint handoff.",
    "actions": [
      { "name": "Architecture review", "note": "Security sign-off captured.", "timestamp": "2026-05-12 14:30:00 ET" }
    ]
  },
  { "date": "06/30/2026", "status": "not-started", "note": "", "actions": [] }
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
5. Click a due-date chip to open the drawer for that specific date, update its status, save a date-specific note, and optionally add a due-date action with name, note, and automatic timestamp.
6. Click a month heading to filter the roadmap to tasks with due dates in that month/year and highlight the column green; use **Clear date** to remove the filter.
7. Use the header Month and Year dropdowns to filter both the grid and linear list. Year with All Months shows all due dates in that year; Month + Year narrows to that month; Month without Year matches that month across all years.
8. Use the header search box to filter tasks by phrase across title, owner, description, status, notes, due dates, and optional tags. Toggle **Tags** to search tags only.
9. Toggle **Favorites** to show only tasks with `favorite: true`; this works in both grid and linear views.
10. Switch to the linear view to see due-date items sorted chronologically; rows include a 10px product-color bar, rows due in the current week are highlighted in gold, and each row remains clickable/editable.

---

## Saved Document Set

When you download all roadmap data, the export uses this wrapper so product toggle state can be preserved. `roadmap.schema.json` validates this wrapper as well as single-product objects and arrays of product objects:

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
        "order": 1,
        "color": "#3b82f6",
        "deliverables": []
      }
    }
  ]
}
```

For normal editing, you usually only edit the **product object** inside each card, not the wrapper. Raw JSON is hidden by default; use **Edit JSON** only when direct data changes are needed. **Add Deliverable** appends a normalized deliverable object into the selected product's `deliverables` array. **Load JSON Document** accepts every top-level shape covered by `roadmap.schema.json`: a single product object, an array of product objects, or this wrapped export format.

---

## Date Formats

### Timeline Range Dates

`start` and `end` use **`"Mon YYYY"`** where:

- `Mon` is `Jan`, `Feb`, `Mar`, `Apr`, `May`, `Jun`, `Jul`, `Aug`, `Sep`, `Oct`, `Nov`, or `Dec`
- `YYYY` is the four-digit year

The default timeline supports **January 2026 through December 2032**.

### Due Dates

`dueDates` prefers objects with a parseable `date`, a per-date `status`, a free-text `note`, and optional `actions`. Each `actions[]` entry supports `name`, `note`, and `timestamp`; actions added from the UI are stamped automatically when saved. If `status` or `note` are omitted, the UI normalizes them with a fallback status and empty note.

Examples:

- `{ "date": "05/15/2026", "status": "in-progress", "note": "Token endpoint handoff." }` renders in the `May 2026` column with the in-progress chip color
- `{ "date": "12/01/2028", "status": "completed", "note": "Accepted.", "actions": [{ "name": "Notify stakeholders", "note": "Shared completion summary.", "timestamp": "2026-05-12 14:30:00 ET" }] }` renders in the `Dec 2028` column with the completed chip color
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
10. Add optional product-level `order` values when you need a fixed sequence across multiple product documents, and product-level `color` values when you want list rows color-coded by product.
11. Click a month heading or use the Month/Year dropdowns to filter due dates in both grid and list views; use search to filter tasks by phrase or tag.
12. Toggle **Favorites** to show starred tasks only.
13. Click **Download Enabled JSONs** or **Download All JSONs** to export backups.
14. Click **Clear Cache** in the drawer to reset to embedded defaults.

---

## Tips

- Use one JSON card per product.
- Keep `id` values unique within each product roadmap.
- Use product-level `order` values to control display order when loading multiple product documents.
- Use product-level `color` values to control the list-view row bar color; the editor accepts default swatches or a custom 6-digit hex code.
- Keep `start` and `end` within the supported range: Jan 2026 – Dec 2032.
- Use `dueDates` for concrete submission dates; each due date can carry its own status and note.
- Use optional `tags` for searchable labels and optional `favorite: true` for starred tasks.
- Use `desc` for coordination context — blockers, dependencies, definition of done.
- To change the date range, edit the year loop in the `MONTHS` generator at the top of the HTML file.
