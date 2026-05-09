# Product Roadmap

A lightweight, interactive product roadmap template rendered entirely in a single HTML file.

## Features

- **Single-file** — no build step, no server, no dependencies. Open the HTML in any browser.
- **Interactive timeline** — swimlane view with years, months, and status-colored deliverable blocks spanning 2026–2032.
- **Provided product schema support** — product JSON documents include `project`, `title`, `subtitle`, `lastUpdated`, `owner`, and `deliverables`.
- **Due-date rendering** — parseable `MM/DD/YYYY` due dates appear as chips in the matching `Mon YYYY` month column using each due date's own status color; no long start-to-end task bars are drawn.
- **Per-date status + notes** — each `dueDates[]` item can store its own `status` and `note`; legacy string due dates are migrated automatically.
- **Multiple product JSON documents** — each product has its own JSON card in the edit drawer.
- **Product toggles** — turn product roadmaps on/off and render enabled products together on one timeline.
- **Current month highlight** — the present month is highlighted in gold on the timeline.
- **Month filtering** — click a month column heading to highlight that column green and show only tasks with due dates in that month; clear it with the chip in the header.
- **Search filtering** — use the header search box to filter tasks by phrase.
- **Live editing** — click **Edit Data** to paste or update product roadmap JSON and re-render instantly.
- **localStorage caching** — save your product JSON documents and toggle states locally; survives page reloads. **Clear Cache** resets to defaults.
- **Status changes + notes** — click a due-date chip, change that date's status, and enter a date-specific note.
- **Filtering** — filter visible deliverables by task or due-date status across all enabled products.
- **Stats dashboard** — at-a-glance counts for enabled products, total deliverables, in-progress, at-risk, blocked/on-hold, completed, and due-this-month.
- **Dark theme** — clean, modern design.

## Quick Start

1. Open `Product-Roadmap.html` in a browser.
2. Click **Edit Data**.
3. Add or edit one product JSON document per card.
4. Check/uncheck product cards to toggle products on/off.
5. Click **Save & Render** — data and toggle states auto-save to `localStorage`.
6. Use **Download Enabled JSONs** or **Download All JSONs** to export backups.
7. Click **Clear Cache** to reset to embedded defaults.

## Product JSON Schema

Each editor card contains one product roadmap JSON document:

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

Schema status values: `not-started`, `in-progress`, `at-risk`, `blocked`, `completed`, `on-hold`, `cancelled`.

Machine-readable schema: `roadmap.schema.json`.

Timeline date format: `"Mon YYYY"` — e.g., `"Jun 2027"`, `"Dec 2028"`.

Due date format: preferred `dueDates` entries are objects with `date`, `status`, and `note`. Legacy `"MM/DD/YYYY"` string entries are still accepted and migrated by the UI.

See `Product-Roadmap.md` for the full schema documentation.

## Due Dates

`dueDates` are rendered as deliverable boxes in the timeline:

1. As small chips in the matching timeline month column when the value is a parseable `MM/DD/YYYY` date
2. No long grey start-to-end duration bar is drawn

Example: `"05/15/2026"` appears as a deliverable chip in the `May 2026` month column.

## Multi-Product Workflow

Downloads use a wrapper so toggle state can be preserved:

```json
{
  "documents": [
    {
      "id": "backend-platform",
      "enabled": true,
      "data": { "project": "Backend Platform", "deliverables": [] }
    }
  ]
}
```

For day-to-day editing, use one product JSON object per editor card.

## Customization

- **Products** — add one product JSON document per editor card.
- **Visibility** — use product checkboxes to toggle swimlanes on/off.
- **Title/Subtitle** — set `title` and `subtitle` in product JSON. The first enabled product controls the page title.
- **Date range** — edit the year loop in the `MONTHS` generator at the top of the HTML (default: 2026–2032).
- **Theme** — adjust the CSS variables in the `:root` block.

## Files

| File | Description |
|---|---|
| `Product-Roadmap.html` | The interactive roadmap artifact |
| `Product-Roadmap.md` | Schema and workflow documentation |
| `roadmap.schema.json` | Machine-readable JSON Schema for product roadmap documents |

## License

See `LICENSE`.
