# Product Roadmap — JSON Schema

This document describes the data format for the `Product-Roadmap.html` interactive roadmap artifact.

---

## Top-Level Structure

The roadmap is a **JSON array** of product objects.

```json
[
  {
    "product": "Backend Platform",
    "owner": "Engineering Team",
    "deliverables": [ ... ]
  },
  {
    "product": "Web Application",
    "owner": "Frontend Team",
    "deliverables": [ ... ]
  }
]
```

---

## Product Object

| Field | Required | Type | Description |
|---|---|---|---|
| `product` | **Yes** | string | Product or initiative name. Displayed as the swimlane header. |
| `owner` | No | string | Default owner for deliverables in this product. Shown in the swimlane header. Individual deliverables can override. |
| `deliverables` | **Yes** | array | List of deliverables. Can be `[]` for a product with no committed work yet. |

---

## Deliverable Object

| Field | Required | Type | Description |
|---|---|---|---|
| `id` | **Yes** | string | Unique identifier across the entire roadmap. Example: `bp-1`, `wa-001`. |
| `title` | **Yes** | string | Deliverable name. Displayed in the timeline block and detail panel. |
| `owner` | No | string | Owner name. Falls back to the product-level `owner` if omitted. |
| `status` | **Yes** | enum | One of: `not-started`, `in-progress`, `at-risk`, `blocked`, `completed`. |
| `start` | **Yes** | string | Start month and year in `"Mon YYYY"` format. Example: `"Jun 2027"`, `"Apr 2026"`. |
| `end` | **Yes** | string | End month and year in `"Mon YYYY"` format. Must be `>=` `start` in chronological order. |
| `desc` | No | string | Description or notes. Displayed in the detail panel. |

---

## Date Format

All `start` and `end` values use the format **`"Mon YYYY"`** where:
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

## Minimal Valid Example

```json
[
  {
    "product": "Backend Platform",
    "owner": "Engineering Team",
    "deliverables": [
      {
        "id": "bp-1",
        "title": "API Authentication",
        "owner": "Engineering",
        "status": "in-progress",
        "start": "May 2026",
        "end": "Jun 2026",
        "desc": "Implement OAuth2 and JWT token management for all API endpoints."
      }
    ]
  }
]
```

---

## Workflow

1. Open `Product-Roadmap.html` in a browser.
2. Click **Edit Data**.
3. Paste your JSON into the editor using `"Mon YYYY"` format for dates.
4. Click **Save & Render**.
   - If the JSON is invalid, an alert shows the parse error.
5. Click **Download JSON** to save a backup or version for sharing.

---

## Tips

- `id` values must be unique across **all** products, not just within one product.
- Keep `start` and `end` within the supported date range (Jan 2026 – Dec 2032). Deliverables outside this range will not render a block.
- Use `desc` for context that helps coordinate — blockers, dependencies, definition of done, etc.
- To change the date range, modify the year loop in the `MONTHS` generator at the top of the HTML file.
