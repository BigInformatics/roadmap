# Product Roadmap — JSON Schema

This document describes the data format for the `Product-Roadmap.html` interactive roadmap artifact.

All roadmap dates use `"Mon YYYY"` format, e.g. `"Jun 2027"`, `"Apr 2026"`.

---

## Mental Model

The page manages a **set of independent product roadmap JSON documents**.

In the **Edit Data** drawer:

- Each product gets its own JSON card/text area.
- Each card contains one product roadmap object.
- Use the checkbox on each card to toggle that product on/off.
- Enabled products render together as separate swimlanes on the same timeline.
- Disabled products stay saved locally but are hidden from the roadmap view.

The page saves the document set and toggle states to `localStorage`.

---

## Saved Document Set

When you download all roadmap data, the export uses this wrapper:

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

### Document Wrapper

| Field | Required | Type | Description |
|---|---|---|---|
| `id` | No | string | Stable local identifier for the product document. Auto-generated from `project` if omitted. |
| `enabled` | No | boolean | Whether this product renders on the timeline. Defaults to `true`. |
| `data` | **Yes** | object | One product roadmap object. |

For normal editing, you usually only edit the **product object** inside each card, not the wrapper.

---

## Product Roadmap Object

Each editor card contains one product object like this:

```json
{
  "project": "Backend Platform",
  "title": "Product Roadmap",
  "subtitle": "Interactive Deliverables & Timeline",
  "lastUpdated": "2026-05-08 14:30:00 ET",
  "owner": "Engineering Team",
  "deliverables": [
    {
      "id": "bp-1",
      "title": "API Authentication",
      "owner": "Engineering Team",
      "status": "in-progress",
      "start": "May 2026",
      "end": "Jun 2026",
      "desc": "Implement OAuth2 and JWT token management for API endpoints.",
      "notes": [
        "2026-05-01T10:00:00Z | in-progress | Started OAuth2 implementation"
      ]
    }
  ]
}
```

| Field | Required | Type | Description |
|---|---|---|---|
| `project` | **Yes** | string | Product name. Displayed as the swimlane header and toggle label. |
| `title` | No | string | Page title. The first enabled product provides the page title. Falls back to `"Product Roadmap"`. |
| `subtitle` | No | string | Subtitle text when one product is enabled. With multiple products enabled, the subtitle shows the enabled product count. |
| `lastUpdated` | No | string | Last update timestamp in Eastern timezone (`YYYY-MM-DD HH:mm:ss ET`). Auto-generated on save. |
| `owner` | No | string | Default owner for deliverables. Shown in the swimlane header. |
| `deliverables` | **Yes** | array | List of deliverables. Can be `[]`. |

---

## Deliverable Object

| Field | Required | Type | Description |
|---|---|---|---|
| `id` | **Yes** | string | Unique identifier. Example: `bp-1`, `wa-001`. |
| `title` | **Yes** | string | Deliverable name. Displayed in the timeline block and detail panel. |
| `owner` | No | string | Owner name. Falls back to product-level `owner`. |
| `status` | **Yes** | enum | One of: `not-started`, `in-progress`, `at-risk`, `blocked`, `completed`. |
| `start` | **Yes** | string | Start date in `"Mon YYYY"` format. |
| `end` | **Yes** | string | End date in `"Mon YYYY"` format. Must be `>=` `start` chronologically. |
| `desc` | No | string | Description displayed in the detail panel. |
| `notes` | No | array | Array of status-change notes with timestamps. Auto-appended when you change status. |

---

## Date Format

All `start` and `end` values use **`"Mon YYYY"`** where:

- `Mon` is the three-letter month abbreviation: `Jan`, `Feb`, `Mar`, `Apr`, `May`, `Jun`, `Jul`, `Aug`, `Sep`, `Oct`, `Nov`, `Dec`
- `YYYY` is the four-digit year

The default timeline supports **January 2026 through December 2032**.

Examples:

- `"Jan 2026"`
- `"Dec 2028"`
- `"Mar 2031"`

---

## Status Values

| Status | Visual Treatment |
|---|---|
| `not-started` | Gray block |
| `in-progress` | Teal block with glow dot |
| `at-risk` | Red block with glow dot |
| `blocked` | Dashed red block |
| `completed` | Green block |

---

## Workflow

1. Open `Product-Roadmap.html` in a browser.
2. Click **Edit Data**.
3. Add one product JSON document per card.
4. Check or uncheck product cards to toggle products on/off.
5. Click **Save & Render**.
6. The enabled products render together as separate swimlanes.
7. Click **Download Enabled JSONs** or **Download All JSONs** to export backups.
8. Click **Clear Cache** to reset to embedded defaults.

---

## Features

### Multiple Product JSON Documents

The editor is organized around separate product JSON documents. This keeps each product's roadmap portable and lets you combine several products into one consolidated timeline.

### Product Toggle Controls

Product toggles appear both above the roadmap and inside the edit drawer. Toggle states are saved to `localStorage`.

### Current Month Highlight

The present month is highlighted with a golden background on the timeline.

### localStorage Caching

When you click **Save & Render**, all product JSON documents and toggle states are cached to `localStorage`. On page reload, cached data is restored automatically.

### Status Change + Notes

Click a deliverable to open details. You can change status and add a status note. On save, the note is appended to the deliverable's `notes` array and the product document is updated.

---

## Tips

- Use one JSON card per product.
- Keep `id` values unique within each product roadmap.
- Keep `start` and `end` within the supported range: Jan 2026 – Dec 2032.
- Use `desc` for coordination context — blockers, dependencies, definition of done.
- To change the date range, edit the year loop in the `MONTHS` generator at the top of the HTML file.
