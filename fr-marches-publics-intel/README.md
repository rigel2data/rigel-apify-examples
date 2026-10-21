# fr-marches-publics-intel

New French public tender notices (BOAMP) filtered by keyword and department, or awarded contracts (DECP) by CPV code with the winners' SIRENE data.

- Actor page: https://apify.com/rigel/fr-marches-publics-intel
- Actor ID: `rigel/fr-marches-publics-intel`
- Pricing (pay per event, as listed on 21 October 2026): $0.003 per tender notice, $0.005 per awarded contract, $0.005 per winner profile, plus $0.00005 per GB of run memory at start. The Actor page is the reference for current prices.

## Files

| File | Content |
|---|---|
| `input.json` | default input |
| `input-awards.json` | alternative input |
| `example.py` | Python (`apify-client`) |
| `example.mjs` | Node.js (`apify-client`) |

`input.json` asks for open tender notices (`mode: tenders`); `input-awards.json` asks for awarded contracts (`mode: awards`). `maxItems` (20) and `topWinners` (5) keep a test run small. Data: BOAMP and DECP open data (Licence Ouverte 2.0).

## Run

From this folder:

```bash
export APIFY_TOKEN=...          # your own token, never commit it
python example.py               # or: python example.py input-awards.json
node example.mjs                # or: node example.mjs input-awards.json
```

Each example caps the run at $0.10 with `maxTotalChargeUsd` and prints the first 5 dataset items. All input fields are documented in the Input tab of the Actor page.
