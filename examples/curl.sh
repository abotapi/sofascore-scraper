#!/usr/bin/env bash
# Today's scheduled football matches as JSON, in one HTTP call (waits for the run to finish).
# APIFY_TOKEN=<your token> ./curl.sh > matches.json
curl -s -X POST \
  "https://api.apify.com/v2/acts/abotapi~sofascore-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H 'Content-Type: application/json' \
  -d '{
    "mode": "scheduled",
    "sports": ["football"],
    "includeOdds": false,
    "maxItems": 50
  }'
