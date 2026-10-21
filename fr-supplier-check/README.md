# fr-supplier-check

One card per French company (SIREN/SIRET): legal status from SIRENE, BODACC notices (insolvency, strike-off), public contracts won (DECP) and a green/orange/red risk level.

- Actor page: https://apify.com/rigel/fr-supplier-check
- Actor ID: `rigel/fr-supplier-check`
- Pricing (pay per event, as listed on 21 October 2026): $0.01 per card ($0.006 without public contracts), plus $0.00005 per GB of run memory at start. The Actor page is the reference for current prices.

## Files

| File | Content |
|---|---|
| `input.json` | default input |
| `example.py` | Python (`apify-client`) |
| `example.mjs` | Node.js (`apify-client`) |

`ids` accepts SIREN (9 digits) or SIRET (14 digits). Set `includePublicContracts` to `false` for the cheaper card without DECP data.

## Run

From this folder:

```bash
export APIFY_TOKEN=...          # your own token, never commit it
python example.py               # or: python example.py my-input.json
node example.mjs                # or: node example.mjs my-input.json
```

Each example caps the run at $0.05 with `maxTotalChargeUsd` and prints the first 5 dataset items. All input fields are documented in the Input tab of the Actor page.
