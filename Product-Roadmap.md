# Product Roadmap — JSON Schema

This document describes the data format for the `Product-Roadmap.html` interactive roadmap artifact.

All dates use `"Mon YYYY"` format (e.g., `"Jun 2027"`, `"Apr 2026"`).

---

## Top-Level Structure

The roadmap is a **JSON array** of project objects.

```json
[
  {
    "project": "Backend Platform",
    "title": "Platform Core Roadmap",
    "subtitle": "2026 Engineering Priorities",
    "lastUpdated": "2026-05-08 14:30:00",
    "owner": "Engineering Team",
    "deliverables": [
      {
        "id": "bp-1",
        "title": "API Authentication",
        "owner": "Engineering",
        "status": "in-progress",
        "start": "May 2026",
        "end": "Jun 2026",
        "desc": "Implement OAuth2 and JWT token management for all API endpoints.",
        "notes": [
          "2026-05-01T10:00:00Z | In Progress | Started OAuth2 implementation"
        ]
      }
    ]
  }
]
```

---

## Project Object

| Field | Required | Type | Description |
|---|---|---|---|
| `project` | **Yes** | string | Product or initiative name. Displayed as the swimlane header. |
| `title` | No | string | Page title. Displayed in browser tab and page header. Falls back to `"Product Roadmap"`. |
| `subtitle` | No | string | Subtitle text. Falls back to `"Interactive Deliverables & Timeline"`. |
| `lastUpdated` | No | string | Last update timestamp in Eastern timezone (`YYYY-MM-DD HH:mm:ss`). Auto-generated. Displays next to subtitle. |
| `owner` | No | string | Default owner for deliverables. Shown in swimlane header. |
| `deliverables` | **Yes** | array | List of deliverables. Can be `[]`. |

---

## Deliverable Object

| Field | Required | Type | Description |
|---|---|---|---|
| `id` | **Yes** | string | Unique identifier across the entire roadmap. Example: `bp-1`, `wa-001`. |
| `title` | **Yes** | string | Deliverable name. Displayed in the timeline block and detail panel. |
| `owner` | No | string | Owner name. Falls back to project-level `owner`. |
| `status` | **Yes** | enum | One of: `not-started`, `in-progress`, `at-risk`, `blocked`, `completed`. |
| `start` | **Yes** | string | Start date in `"Mon YYYY"` format. |
| `end` | **Yes** | string | End date in `"Mon YYYY"` format. Must be `>=` `start` chronologically. |
| `desc` | No | string | Description displayed in the detail panel. |
| `notes` | No | array | Array of status-change notes with timestamps. Auto-appended when you change status. Format: `"YYYY-MM-DDTHH:mm:ssZ | status | note text"`. |

---

## Date Format

All `start` and `end` values use **`"Mon YYYY"`** where:
- `Mon` is the three-letter month abbreviation: `Jan`, `Feb`, `Mar`, `Apr`, `May`, `Jun`, `Jul`, `Aug`, `Sep`, `Oct`, `Nov`, `Dec`
- `YYYY` is the four-digit year

The default timeline supports **January 2026 through December 2032** (84 months).

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

## Features

### Current Month Highlight
The present month is highlighted with a golden background on the timeline so you can see "today" at a glance.

### localStorage Caching
When you click **Save & Render**, the current roadmap data is automatically cached to `localStorage`. On page reload, cached data is restored automatically. Click **Clear Cache** in the controls to reset to embedded defaults.

### Multiple Roadmaps
The edit drawer supports multiple roadmap objects in the JSON array. Switch between them in the editor and each can be saved/downloaded independently.

### Status Change + Notes
When you click a deliverable and the detail panel opens, you can:
1. Click a **status button** to change the deliverable's status
2. Enter an optional **note** documenting the reason
3. On save, the note is appended to the deliverable's `notes` array with an ISO timestamp
4. The in-memory JSON is updated for the product

---

## Workflow

1. Open `Product-Roadmap.html` in a browser.
2. Click **Edit Data**.
3. Paste your JSON using `"Mon YYYY"` date format.
4. Click **Save & Render** — data auto-saves to `localStorage`.
5. Click **Download JSON** to export a backup.
6. Click **Clear Cache** to reset to embedded defaults.

---

## Tips

- `id` values must be unique across **all** deliverables, not just within one product.
- Keep `start` and `end` within the supported date range (Jan 2026 – Dec 2032).
- Use `desc` for coordination context — blockers, dependencies, definition of done.
- Status change notes are stored in `notes` array with `YYYY-MM-DDTHH:mm:ssZ | status | note` format.
- To change the date range, edit the year loop in the `MONTHS` generator at the top of the HTML file.
