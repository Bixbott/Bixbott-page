# ORGANIZATION

Landing page and organization overview for **Bixbott**, a modular AI Agent IDE ecosystem.

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

This repository includes a polished static landing page and organization hub:

- `index.html` — main landing page structure and Vietnamese product content.
- `styles.css` — responsive copper/glass UI, animated background, cards, layout, and 404 styles.
- `script.js` — scroll-reveal animation behavior.
- `_config.yml` — GitHub Pages/Jekyll metadata for the organization hub.
- `.nojekyll` — tells GitHub Pages to publish files as plain static assets.
- `site.webmanifest`, `robots.txt`, `sitemap.xml`, `404.html` — deployment and discoverability support files.
- `docs/architecture.md` and `docs/getting-started.md` — implementation blueprint and local setup notes.
- `CONTRIBUTING.md` — contribution principles for keeping this hub aligned with Bixbott.

## Run locally

Open `index.html` directly in a browser or serve the folder with any static file server:

```bash
python3 -m http.server 4173
```

Then open `http://127.0.0.1:4173/`.

## Organization profile links

This landing page is connected to the official Bixbott organization repository:

- Organization repository: https://github.com/Bixbott/.github
- Profile README: https://github.com/Bixbott/.github/tree/main/profile
- Documentation hub: https://github.com/Bixbott/.github/tree/main/docs

Use the `.github` repository as the source of truth for Bixbott's public profile, shared documentation, and GitHub-native workflow direction.

## Deployment notes

The site is prepared for GitHub Pages-style static hosting. `_config.yml` stores the page metadata, `.nojekyll` keeps GitHub Pages from transforming static assets unexpectedly, and the manifest/robots/sitemap files support browser install metadata and search discovery.

## Merge conflict policy

If this README conflicts with another branch, keep the complete file list, local run instructions, organization profile links, and deployment notes above. Do not keep any Git conflict marker lines in committed files.
