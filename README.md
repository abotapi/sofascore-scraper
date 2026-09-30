# SofaScore Scraper

**Get live scores, fixtures, match statistics, lineups, players and odds from SofaScore as JSON or CSV, with no browser and no parsing.**

![Sports](https://img.shields.io/badge/sports-20%2B-blue?style=flat-square)
![Output](https://img.shields.io/badge/output-JSON%20%7C%20CSV%20%7C%20Excel-green?style=flat-square)
![License](https://img.shields.io/badge/examples-MIT-lightgrey?style=flat-square)

SofaScore is one of the richest free sources of sports data: football, basketball, tennis, ice hockey, cricket, esports and more,
with minute-by-minute incidents, advanced stats and player ratings. It has no official public API, and the site
changes often, so scraping it yourself means a lot of maintenance.

This repo shows how to pull that data with the
**[SofaScore Scraper on Apify](https://apify.com/abotapi/sofascore-scraper?utm_source=github&utm_medium=sofascore-scraper&utm_campaign=showcase)**,
a hosted scraper you can run from the web UI or call from code. Every example here was run against the live site before being published.

## Table of Contents

- [What you can get](#what-you-can-get)
- [Quick start](#quick-start)
- [Examples](#examples)
- [Input options](#input-options)
- [Sample output](#sample-output)
- [Use cases](#use-cases)
- [FAQ](#faq)

## What you can get

| Entity | Fields (highlights) |
| --- | --- |
| **Matches** | teams, scores (full-time, half-time, aggregate), status, start time, tournament, season, round, venue, referee, attendance, winner |
| **Match details** | statistics (possession, shots, xG, passes, ...), lineups with formations, incidents (goals, cards, substitutions), odds, fan votes, head-to-head |
| **Teams** | country, league, manager, stadium and capacity, colors, logo, recent form, squad |
| **Players** | position, jersey number, height, preferred foot, nationality, date of birth, market value, contract end, team |
| **Tournaments** | standings tables, seasons |

Five ways in:

- **`search`** - look up teams, players, tournaments or matches by name ("Real Madrid", "Lionel Messi")
- **`url`** - paste any SofaScore team, player, match or tournament URL
- **`live`** - every match in progress right now, filtered by sport
- **`scheduled`** - all fixtures and results for a date (plus extra days ahead)
- **incremental mode** - on a schedule, only emit what changed since the last run

## Quick start

**No code:** open the [scraper page](https://apify.com/abotapi/sofascore-scraper?utm_source=github&utm_medium=sofascore-scraper&utm_campaign=showcase),
type a team name, click **Start**, and download the results as JSON, CSV or Excel.

**From code:** get a free [Apify API token](https://console.apify.com/settings/integrations?utm_source=github&utm_medium=sofascore-scraper&utm_campaign=showcase), then:

```bash
git clone https://github.com/abotapi/sofascore-scraper && cd sofascore-scraper
export APIFY_TOKEN=<your token>
```

## Examples

### Python: search and save to CSV

[`examples/python/main.py`](examples/python/main.py)

```bash
pip install "apify-client>=3"
python examples/python/main.py "Real Madrid" "Lionel Messi"
```

```text
Saved 20 rows to sofascore.csv
- [team] Riverside FC (football, Exampleland)
- [player] Luca Brandt (football, Exampleland)
- [player] Sam Keller (football, Exampleland)
```

### Node.js: live scores across sports

[`examples/node/index.mjs`](examples/node/index.mjs)

```bash
cd examples/node && npm install && node index.mjs
```

```text
football | Northgate United 1 - 1 Lakeside Rovers | 2nd half
basketball | Harbor City Hawks 58 - 61 Riverside Rays | 3rd quarter
tennis | A. Moreno 1 - 0 N. Lind | 2nd set
```

### cURL: today's fixtures in one HTTP call

[`examples/curl.sh`](examples/curl.sh) uses the `run-sync-get-dataset-items` endpoint, which starts the run, waits, and returns the items:

```bash
./examples/curl.sh > matches.json
```

## Input options

| Option | What it does |
| --- | --- |
| `mode` | `search`, `url`, `live` or `scheduled` |
| `searchQueries` / `searchType` | Names to look up; optionally restrict to team, player, tournament or match |
| `urls` | SofaScore page URLs to scrape directly |
| `sports` | Sports to include in live/scheduled mode, e.g. `football`, `basketball`, `tennis` |
| `date` / `daysAhead` | Which day's fixtures to fetch in scheduled mode, and how many extra days |
| `includeStatistics`, `includeLineups`, `includeIncidents`, `includeOdds`, `includeVotes`, `includeH2H`, `includeStandings`, `includeSquad` | Toggle the detail blocks you need; fewer blocks means faster runs |
| `maxItems` | Stop after this many results |
| `incrementalMode` | For scheduled runs: only output new or changed items |

See the [scraper page](https://apify.com/abotapi/sofascore-scraper?utm_source=github&utm_medium=sofascore-scraper&utm_campaign=showcase) for the full list.

## Sample output

Mock data with the same fields and types as real output (the values are made up): [`sample-output/sample.json`](sample-output/sample.json) · [`sample-output/sample.csv`](sample-output/sample.csv)

```json
{
  "type": "match",
  "sport": "football",
  "name": "Riverside FC - Harbor City",
  "homeTeam": "Riverside FC",
  "awayTeam": "Harbor City",
  "homeScore": 2,
  "awayScore": 1,
  "homeScoreHalftime": 1,
  "statusDescription": "Ended",
  "tournament": "Example Premier League",
  "venue": "Riverside Arena",
  "statistics": [{ "period": "ALL", "groups": [{ "groupName": "Match overview", "statisticsItems": [{ "name": "Ball possession", "home": "58%", "away": "42%" }] }] }],
  "url": "https://www.sofascore.com/..."
}
```

## Use cases

- **Sports analytics and betting models:** historical results, xG and odds for backtesting
- **Live score widgets and bots:** poll `live` mode for a Discord, Telegram or Slack bot
- **Fantasy sports:** player form, ratings, lineups and injuries before the deadline
- **Media and newsrooms:** automated match reports from incidents and statistics
- **AI agents:** feed structured match data to an LLM instead of scraping HTML

## FAQ

**How much does it cost?** You pay per result on Apify, and new accounts get free monthly credit that covers small projects. See the scraper page for current pricing.

**Is scraping SofaScore allowed?** The scraper only collects publicly visible data. Check SofaScore's terms and your local laws for your use case, especially for commercial redistribution.

**Can I run it on a schedule?** Yes. Create a schedule in Apify (e.g. every 5 minutes for live scores) and turn on `incrementalMode` to receive only changes.

**Can I get the data somewhere other than JSON?** Download CSV, Excel, XML or HTML from the run, or push it to Google Sheets, webhooks, Zapier, Make or n8n through Apify integrations.

## Related

- [Awesome Web Scrapers](https://github.com/abotapi/abotapi): a curated list of 360+ ready-to-run scrapers
- [Sportsbook Odds Scraper](https://apify.com/abotapi/sportsbook-odds-scraper?utm_source=github&utm_medium=sofascore-scraper&utm_campaign=showcase): odds from 1xBet, Melbet and more

---

<sub>The scraper is maintained by [abotapi](https://abotapi.com/?utm_source=github&utm_medium=sofascore-scraper&utm_campaign=showcase). Examples in this repo are MIT licensed. Not affiliated with SofaScore.</sub>
