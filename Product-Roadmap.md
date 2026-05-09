# Product Roadmap — JSON Schema

This document describes the data format for the `Product-Roadmap.html` interactive roadmap artifact.

The roadmap supports the provided **Project Roadmap Schema** for product documents. Timeline range dates use `"Mon YYYY"`; deliverable due dates use the product schema's `dueDates` array.

---

## Mental Model

The page manages a **set of independent product roadmap JSON documents**.

In the **Edit Data** drawer:

- Each product gets its own JSON card/text area.
- Each card contains one product roadmap object using the schema below.
- Use the checkbox on each card to toggle that product on/off.
- Enabled products render together as separate swimlanes on the same timeline.
- Disabled products stay saved locally but are hidden from the roadmap view.

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
        "05/15/2026",
        "06/30/2026"
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
| `status` | **Yes** | enum | Schema values: `not-started`, `in-progress`, `completed`, `on-hold`, `cancelled`. The renderer also keeps backward-compatible visual support for `at-risk` and `blocked`. |
| `start` | **Yes** | string | Planned start month in `"Mon YYYY"` format. |
| `end` | **Yes** | string | Planned end month in `"Mon YYYY"` format. Must be `>=` `start` chronologically. |
| `desc` | **Yes** | string | Detailed description, requirements, or submission rules. |
| `dueDates` | **Yes** | array | List of due dates or scheduling notes. `MM/DD/YYYY` dates are parsed into timeline month chips. Descriptive strings are displayed under the block title and in the detail panel. |
| `notes` | **Yes** | array | Additional comments, attachments, metadata, or status-change notes. |

---

## Due Date Rendering

Each deliverable can have one or more values in `dueDates`.

```json
"dueDates": ["05/15/2026", "06/30/2026", "As needed"]
```

Rendering behavior:

1. All due date strings display **under the deliverable block title** as `Due: ...`.
2. Any `MM/DD/YYYY` date is converted to its `Mon YYYY` month.
3. Each parsed due date is rendered as a small due-date chip inside that month column on the deliverable row.
4. Descriptive strings such as `"As needed"` or `"Weekly from kickoff"` remain visible under the block title and in the detail panel, but are not placed in a specific month unless they contain a parseable `MM/DD/YYYY` date.

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

For normal editing, you usually only edit the **product object** inside each card, not the wrapper.

---

## Date Formats

### Timeline Range Dates

`start` and `end` use **`"Mon YYYY"`** where:

- `Mon` is `Jan`, `Feb`, `Mar`, `Apr`, `May`, `Jun`, `Jul`, `Aug`, `Sep`, `Oct`, `Nov`, or `Dec`
- `YYYY` is the four-digit year

The default timeline supports **January 2026 through December 2032**.

### Due Dates

`dueDates` accepts strings. `MM/DD/YYYY` strings are parsed into timeline month chips.

Examples:

- `"05/15/2026"` renders in the `May 2026` column
- `"12/01/2028"` renders in the `Dec 2028` column
- `"As needed"` displays as text under the block title and in the detail panel

---

## Workflow

1. Open `Product-Roadmap.html` in a browser.
2. Click **Edit Data**.
3. Add one product roadmap JSON document per card.
4. Check or uncheck product cards to toggle products on/off.
5. Click **Save & Render**.
6. Enabled products render together as separate swimlanes.
7. Due dates display under block titles and as month chips when parseable.
8. Click **Download Enabled JSONs** or **Download All JSONs** to export backups.
9. Click **Clear Cache** to reset to embedded defaults.

---

## Tips

- Use one JSON card per product.
- Keep `id` values unique within each product roadmap.
- Keep `start` and `end` within the supported range: Jan 2026 – Dec 2032.
- Use `dueDates` for concrete submission dates and scheduling notes.
- Use `desc` for coordination context — blockers, dependencies, definition of done.
- To change the date range, edit the year loop in the `MONTHS` generator at the top of the HTML file.
