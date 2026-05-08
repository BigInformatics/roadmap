# Product Roadmap

A lightweight, interactive product roadmap template rendered entirely in a single HTML file.

## Features

- **Single-file** — no build step, no server, no dependencies. Open the HTML in any browser.
- **Interactive timeline** — swimlane view with quarters, months, and status-colored deliverable blocks.
- **Live editing** — click **Edit Data** to paste your own roadmap JSON and re-render instantly.
- **Filtering** — filter by product or by status.
- **Stats dashboard** — at-a-glance counts for total, in-progress, at-risk, blocked, completed, and due-this-month.
- **Dark theme** — clean, modern design with no design slop.

## Quick Start

1. Open `Product-Roadmap.html` in a browser.
2. Click **Edit Data**.
3. Paste your own roadmap JSON into the editor. See `Product-Roadmap.md` for the JSON schema.
4. Click **Save & Render**.
5. Click **Download JSON** to save a backup.

## JSON Schema

The roadmap is an array of product objects, each containing an array of deliverables.

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
        "start": "May",
        "end": "Jun",
        "desc": "Implement OAuth2 and JWT token management for all API endpoints."
      }
    ]
  }
]
```

Allowed statuses: `not-started`, `in-progress`, `at-risk`, `blocked`, `completed`.

See `Product-Roadmap.md` for the full schema documentation.

## Customization

- **Date range** — edit the `MONTHS` array at the top of the HTML (e.g., `['Jan','Feb','Mar','Apr','May','Jun']`).
- **Theme** — adjust the CSS variables in the `:root` block.

## Files

| File | Description |
|---|---|
| `Product-Roadmap.html` | The interactive roadmap artifact |
| `Product-Roadmap.md` | JSON schema documentation |

## License

See `LICENSE`.
