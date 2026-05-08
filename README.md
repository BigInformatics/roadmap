# Product Roadmap

A lightweight, interactive product roadmap template rendered entirely in a single HTML file.

## Features

- **Single-file** — no build step, no server, no dependencies. Open the HTML in any browser.
- **Interactive timeline** — swimlane view with years, months, and status-colored deliverable blocks spanning 2026–2032.
- **Current month highlight** — the present month is highlighted in gold on the timeline.
- **Live editing** — click **Edit Data** to paste your own roadmap JSON and re-render instantly.
- **localStorage caching** — save your data locally; survives page reloads. **Clear Cache** button resets to defaults.
- **Multiple roadmaps** — define multiple project objects in the JSON array. Toggle between them in the edit drawer.
- **Status changes + notes** — click a deliverable, change its status, enter a note. Notes are timestamped and appended to the deliverable history.
- **Filtering** — filter by product or by status.
- **Stats dashboard** — at-a-glance counts for total, in-progress, at-risk, blocked, completed, and due-this-month.
- **Dark theme** — clean, modern design.

## Quick Start

1. Open `Product-Roadmap.html` in a browser.
2. Click **Edit Data**.
3. Paste your roadmap JSON using `"Mon YYYY"` date format. See `Product-Roadmap.md` for the full schema.
4. Click **Save & Render** — data auto-saves to `localStorage`.
5. Click **Download JSON** to export a backup.
6. Click **Clear Cache** to reset to embedded defaults.

## JSON Schema

The roadmap is an array of **project** objects, each containing deliverables. Optional `title` and `subtitle` customize the page header.

```json
[
  {
    "project": "Backend Platform",
    "title": "Platform Core Roadmap",
    "subtitle": "2026 Priorities",
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
        "desc": "Implement OAuth2 and JWT token management.",
        "notes": [
          "2026-05-01T10:00:00Z | in-progress | Started OAuth2 implementation"
        ]
      }
    ]
  }
]
```

Allowed statuses: `not-started`, `in-progress`, `at-risk`, `blocked`, `completed`.

Date format: `"Mon YYYY"` — e.g., `"Jun 2027"`, `"Dec 2028"`.

See `Product-Roadmap.md` for the full schema documentation.

## Customization

- **Title/Subtitle** — set `title` and `subtitle` fields in the JSON, or leave empty for defaults.
- **Date range** — edit the year loop in the `MONTHS` generator at the top of the HTML (default: 2026–2032).
- **Theme** — adjust the CSS variables in the `:root` block.

## Files

| File | Description |
|---|---|
| `Product-Roadmap.html` | The interactive roadmap artifact |
| `Product-Roadmap.md` | JSON schema documentation |

## License

See `LICENSE`.
