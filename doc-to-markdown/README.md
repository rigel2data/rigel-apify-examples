# doc-to-markdown

Convert PDF (native or scanned), DOCX, XLSX, PPTX, HTML and images, by URL or upload, to Markdown, JSON, plain text or RAG chunks with page numbers.

- Actor page: https://apify.com/rigel/doc-to-markdown
- Actor ID: `rigel/doc-to-markdown`
- Pricing (pay per event, as listed on 21 October 2026): $0.002 per document + $0.0003 per text page ($0.004 per OCR page). The Actor page is the reference for current prices.

## Files

| File | Content |
|---|---|
| `input.json` | default input |
| `example.py` | Python (`apify-client`) |
| `example.mjs` | Node.js (`apify-client`) |

Set `output` to `chunks` for one dataset row per chunk (`chunkSize`, `chunkOverlap`). `pages` limits the PDF page range.

## Run

From this folder:

```bash
export APIFY_TOKEN=...          # your own token, never commit it
python example.py               # or: python example.py my-input.json
node example.mjs                # or: node example.mjs my-input.json
```

Each example caps the run at $0.05 with `maxTotalChargeUsd` and prints the first 5 dataset items. All input fields are documented in the Input tab of the Actor page.
