# website-screenshot-pdf

Full-page PNG, JPEG, WebP screenshots and A4/Letter PDFs of web pages, from a URL list, a sitemap, a dataset or raw HTML.

- Actor page: https://apify.com/rigel/website-screenshot-pdf
- Actor ID: `rigel/website-screenshot-pdf`
- Pricing (pay per event, as listed on 21 October 2026): $0.002 per file, $0.001 per visual diff, plus $0.0005 per GB of run memory at start. The Actor page is the reference for current prices.

## Files

| File | Content |
|---|---|
| `input.json` | default input |
| `example.py` | Python (`apify-client`) |
| `example.mjs` | Node.js (`apify-client`) |

PNG + PDF of the same page counts as 2 files. Each dataset row lists its `files` with a signed download `url`.

## Run

From this folder:

```bash
export APIFY_TOKEN=...          # your own token, never commit it
python example.py               # or: python example.py my-input.json
node example.mjs                # or: node example.mjs my-input.json
```

Each example caps the run at $0.05 with `maxTotalChargeUsd` and prints the first 5 dataset items. All input fields are documented in the Input tab of the Actor page.
