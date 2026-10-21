// Minimal example: run the Apify Actor rigel/fr-supplier-check and print the first results.
//
//   npm install            (in the repository root)
//   export APIFY_TOKEN=... # Apify Console > Settings > API & Integrations
//   node example.mjs [input.json]
//
// Each run is billed to your Apify account (pay per event). MAX_TOTAL_CHARGE_USD caps it.
import { readFile } from 'node:fs/promises';
import { ApifyClient } from 'apify-client';

const ACTOR_ID = 'rigel/fr-supplier-check';
const MAX_TOTAL_CHARGE_USD = 0.05; // the run stops when it reaches this amount

const token = process.env.APIFY_TOKEN;
if (!token) {
    console.error('Set the APIFY_TOKEN environment variable first.');
    process.exit(1);
}

const inputPath = process.argv[2] ?? new URL('./input.json', import.meta.url);
const input = JSON.parse(await readFile(inputPath, 'utf8'));

const client = new ApifyClient({ token });
const run = await client.actor(ACTOR_ID).call(input, { maxTotalChargeUsd: MAX_TOTAL_CHARGE_USD });
console.error(`Run ${run.id}: ${run.status}`);

const { items } = await client.dataset(run.defaultDatasetId).listItems({ limit: 5 });
for (const item of items) console.log(JSON.stringify(item).slice(0, 500));
