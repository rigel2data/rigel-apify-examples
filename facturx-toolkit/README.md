# facturx-toolkit

Validate Factur-X / ZUGFeRD invoices (XSD, profile schematrons, French BR-FR rules, PDF/A-3 container), extract them to JSON, generate Factur-X PDFs, or convert a plain PDF invoice. The Actor page states: "Not an approved platform (PA)."

- Actor page: https://apify.com/rigel/facturx-toolkit
- Actor ID: `rigel/facturx-toolkit`
- Pricing (pay per event, as listed on 21 October 2026): $0.015 per validated document, $0.008 per extraction, $0.04 per generated invoice, plus $0.00005 per GB of run memory at start. The Actor page is the reference for current prices.

## Files

| File | Content |
|---|---|
| `input.json` | default input |
| `example.py` | Python (`apify-client`) |
| `example.mjs` | Node.js (`apify-client`) |

The sample is the FNFE `Facture_FR_BASICWL.pdf` from the public [ZUGFeRD corpus](https://github.com/ZUGFeRD/corpus). Other modes: `extract`, `validate-and-extract`, `generate` (uses `invoices`), `from-pdf`. The French BR-FR rules are the ones bundled with the factur-x 7.7 Python library.

## Run

From this folder:

```bash
export APIFY_TOKEN=...          # your own token, never commit it
python example.py               # or: python example.py my-input.json
node example.mjs                # or: node example.mjs my-input.json
```

Each example caps the run at $0.05 with `maxTotalChargeUsd` and prints the first 5 dataset items. All input fields are documented in the Input tab of the Actor page.
