# ORGANIZATION

Landing page and organization overview for **Bixbott**, a modular AI agent ecosystem.

## Bixbott ecosystem

```text
Bixbott
├── Bixbott-Management
├── Bixbott-Agent
├── Bixbott-Council
├── Bixbott-Core
├── Bixbott-CLI
├── Bixbott-Dashboard
└── Bixbott-Docs
```

## Current website

This repository now includes a polished static landing page:

- `index.html` — page structure and content.
- `styles.css` — responsive modern UI, copper animated background, glass cards, and layout system.
- `script.js` — scroll-reveal animation behavior.
- `_config.yml` — GitHub Pages/Jekyll metadata for the organization hub.
- `site.webmanifest`, `robots.txt`, `sitemap.xml`, `404.html` — deployment and discoverability support files.
- `docs/architecture.md` and `docs/getting-started.md` — implementation blueprint and local setup notes.

Open `index.html` directly in a browser or serve the folder with any static file server.


## Organization profile links

This landing page is connected to the official Bixbott organization repository:

- Organization repository: https://github.com/Bixbott/.github
- Profile README: https://github.com/Bixbott/.github/tree/main/profile
- Documentation hub: https://github.com/Bixbott/.github/tree/main/docs

Use the `.github` repository as the source of truth for Bixbott's public profile, shared documentation, and GitHub-native workflow direction.


## Local development

```bash
python3 -m http.server 4173
```

Then open `http://127.0.0.1:4173/`.

## Deployment notes

The site is prepared for GitHub Pages-style static hosting. `_config.yml` stores the page metadata, `.nojekyll` keeps GitHub Pages from transforming static assets unexpectedly, and the manifest/robots/sitemap files support browser install metadata and search discovery.
