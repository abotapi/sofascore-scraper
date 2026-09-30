"""Search SofaScore and save the results to CSV.

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python main.py "Real Madrid" "Lionel Messi"
"""
import csv
import os
import sys

from apify_client import ApifyClient

queries = sys.argv[1:] or ["Real Madrid"]
client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/sofascore-scraper").call(run_input={
    "mode": "search",
    "searchQueries": queries,
    "searchType": "all",      # or "team", "player", "tournament", "match"
    "includeStatistics": True,
    "includeStandings": True,
    "maxItems": 20,
}, logger=None)  # logger=None: don't stream the run log to your console

items = list(client.dataset(run.default_dataset_id).iterate_items())
fields = sorted({k for it in items for k, v in it.items() if not isinstance(v, (dict, list))})
with open("sofascore.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(items)

print(f"Saved {len(items)} rows to sofascore.csv")
for it in items[:5]:
    print(f"- [{it.get('type')}] {it.get('name')} ({it.get('sport')}, {it.get('country') or it.get('tournament') or ''})")
