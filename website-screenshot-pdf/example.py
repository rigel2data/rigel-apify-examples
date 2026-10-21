"""Minimal example: run the Apify Actor rigel/website-screenshot-pdf and print the first results.

    pip install -r ../requirements.txt
    export APIFY_TOKEN=...   # Apify Console > Settings > API & Integrations
    python example.py [input.json]

Each run is billed to your Apify account (pay per event). MAX_TOTAL_CHARGE_USD caps it.
"""
import json
import os
import sys
from decimal import Decimal
from pathlib import Path

from apify_client import ApifyClient

ACTOR_ID = "rigel/website-screenshot-pdf"
MAX_TOTAL_CHARGE_USD = Decimal("0.05")  # the run stops when it reaches this amount


def main() -> None:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set the APIFY_TOKEN environment variable first.")

    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("input.json")
    run_input = json.loads(input_path.read_text(encoding="utf-8"))

    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input, max_total_charge_usd=MAX_TOTAL_CHARGE_USD)
    if run is None:
        sys.exit("The run did not start.")
    print(f"Run {run.id}: {run.status}", file=sys.stderr)

    for item in client.dataset(run.default_dataset_id).iterate_items(limit=5):
        print(json.dumps(item, ensure_ascii=False)[:500])


if __name__ == "__main__":
    main()
