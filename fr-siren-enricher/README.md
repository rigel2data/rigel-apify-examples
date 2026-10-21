# fr-siren-enricher

Official SIRENE data for a list of SIREN or SIRET numbers: name, NAF/APE code, legal form, size, headcount band, active or closed, head office, VAT number.

- Actor page: https://apify.com/rigel/fr-siren-enricher
- Actor ID: `rigel/fr-siren-enricher`
- Pricing (pay per event, as listed on 21 October 2026): $0.003 per company found (invalid ids are not charged), plus $0.00005 per GB of run memory at start. The Actor page is the reference for current prices.

## Files

| File | Content |
|---|---|
| `input.json` | default input |
| `example.py` | Python (`apify-client`) |
| `example.mjs` | Node.js (`apify-client`) |

`ids` mixes SIREN and SIRET. `fields` is `standard` or `full`.

## Run

From this folder:

```bash
export APIFY_TOKEN=...          # your own token, never commit it
python example.py               # or: python example.py my-input.json
node example.mjs                # or: node example.mjs my-input.json
```

Each example caps the run at $0.05 with `maxTotalChargeUsd` and prints the first 5 dataset items. All input fields are documented in the Input tab of the Actor page.
