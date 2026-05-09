# Product Roadmap

A lightweight, interactive product roadmap template rendered entirely in a single HTML file.

## Features

- **Single-file** — no build step, no server, no dependencies. Open the HTML in any browser.
- **Interactive timeline** — swimlane view with years, months, and status-colored deliverable blocks spanning 2026–2032.
- **Multiple product JSON documents** — each product has its own JSON card in the edit drawer.
- **Product toggles** — turn product roadmaps on/off and render enabled products together on one timeline.
- **Current month highlight** — the present month is highlighted in gold on the timeline.
- **Live editing** — click **Edit Data** to paste or update product roadmap JSON and re-render instantly.
- **localStorage caching** — save your product JSON documents and toggle states locally; survives page reloads. **Clear Cache** resets to defaults.
- **Status changes + notes** — click a deliverable, change its status, enter a note. Notes are timestamped and appended to the deliverable history.
- **Filtering** — filter visible deliverables by status across all enabled products.
- **Stats dashboard** — at-a-glance counts for enabled products, total deliverables, in-progress, at-risk, blocked, completed, and due-this-month.
- **Dark theme** — clean, modern design.

## Quick Start

1. Open `Product-Roadmap.html` in a browser.
2. Click **Edit Data**.
3. Add or edit one product JSON document per card.
4. Check/uncheck product cards to toggle products on/off.
5. Click **Save & Render** — data and toggle states auto-save to `localStorage`.
6. Use **Download Enabled JSONs** or **Download All JSONs** to export backups.
7. Click **Clear Cache** to reset to embedded defaults.

## JSON Schema

The editor is built for **multiple independent product roadmap JSON documents**. Each product document looks like this:

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

Allowed statuses: `not-started`, `in-progress`, `at-risk`, `blocked`, `completed`.

Date format: `"Mon YYYY"` — e.g., `"Jun 2027"`, `"Dec 2028"`.

See `Product-Roadmap.md` for the full schema documentation.

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
| `Product-Roadmap.md` | JSON schema and workflow documentation |

## License

See `LICENSE`.
