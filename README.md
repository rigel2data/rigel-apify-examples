# Rigel Apify Actor examples

Minimal Python and Node.js examples for the public [Apify](https://apify.com) Actors published by Rigel ([apify.com/rigel](https://apify.com/rigel)).

Each folder contains an `input.json` that matches the Actor's input schema, an `example.py` and an `example.mjs`. Both use the official `apify-client` library, read your token from the `APIFY_TOKEN` environment variable, start one run, and print the first dataset items.

| Folder | What the Actor does | Actor page |
|---|---|---|
| [`fr-marches-publics-intel`](fr-marches-publics-intel/) | New French public tender notices (BOAMP) filtered by keyword and department, or awarded contracts (DECP) by CPV code with the winners' SIRENE data. | [apify.com/rigel/fr-marches-publics-intel](https://apify.com/rigel/fr-marches-publics-intel) |
| [`fr-supplier-check`](fr-supplier-check/) | One card per French company (SIREN/SIRET): legal status from SIRENE, BODACC notices (insolvency, strike-off), public contracts won (DECP) and a green/orange/red risk level. | [apify.com/rigel/fr-supplier-check](https://apify.com/rigel/fr-supplier-check) |
| [`fr-siren-enricher`](fr-siren-enricher/) | Official SIRENE data for a list of SIREN or SIRET numbers: name, NAF/APE code, legal form, size, headcount band, active or closed, head office, VAT number. | [apify.com/rigel/fr-siren-enricher](https://apify.com/rigel/fr-siren-enricher) |
| [`facturx-toolkit`](facturx-toolkit/) | Validate Factur-X / ZUGFeRD invoices (XSD, profile schematrons, French BR-FR rules, PDF/A-3 container), extract them to JSON, generate Factur-X PDFs, or convert a plain PDF invoice. | [apify.com/rigel/facturx-toolkit](https://apify.com/rigel/facturx-toolkit) |
| [`doc-to-markdown`](doc-to-markdown/) | Convert PDF (native or scanned), DOCX, XLSX, PPTX, HTML and images, by URL or upload, to Markdown, JSON, plain text or RAG chunks with page numbers. | [apify.com/rigel/doc-to-markdown](https://apify.com/rigel/doc-to-markdown) |
| [`website-screenshot-pdf`](website-screenshot-pdf/) | Full-page PNG, JPEG, WebP screenshots and A4/Letter PDFs of web pages, from a URL list, a sitemap, a dataset or raw HTML. | [apify.com/rigel/website-screenshot-pdf](https://apify.com/rigel/website-screenshot-pdf) |

## Before you run anything

- You need an Apify account and an API token (Apify Console > Settings > API & Integrations). See [apify.com/pricing](https://apify.com/pricing) for plans.
- These Actors are **paid per event**: each run is billed to your Apify account. Prices are listed in each folder's README and on each Actor page, which is the reference.
- Every example passes `maxTotalChargeUsd` (a few cents) so a test run stops when it reaches that cap.
- Keep your token in the environment. Never commit it: `.env` is in `.gitignore`.

## Python

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export APIFY_TOKEN=...
python fr-siren-enricher/example.py
```

## Node.js (18 or later)

```bash
npm install
export APIFY_TOKEN=...
node fr-siren-enricher/example.mjs
```

## curl

Synchronous run (the run must finish within 300 seconds):

```bash
curl -s -X POST \
  "https://api.apify.com/v2/acts/rigel~fr-siren-enricher/run-sync-get-dataset-items?maxTotalChargeUsd=0.05" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @fr-siren-enricher/input.json
```

## Notes

- `facturx-toolkit` is a technical conformance tool. Its Actor page states that it is not an approved e-invoicing platform (PA), and it is not tax or legal advice.
- The French company and public-procurement Actors use official open data (SIRENE, BODACC, BOAMP, DECP) published under Licence Ouverte 2.0. Sources and limits are described on each Actor page.
- Questions or problems with an Actor: use the Issues tab of its Apify page.

## License

The example code in this repository is released under the [MIT License](LICENSE). The Actors themselves are hosted services on Apify and are not covered by this license.
