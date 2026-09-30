// Live scores right now, across sports.
// npm i apify-client
// APIFY_TOKEN=<your token> node index.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('abotapi/sofascore-scraper').call({
    mode: 'live',
    sports: ['football', 'basketball', 'tennis'],
    includeIncidents: true,
    maxItems: 20,
}, { log: null }); // don't stream the run log to your console

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const m of items) {
    console.log(`${m.sport} | ${m.homeTeam ?? m.name} ${m.homeScore ?? ''} - ${m.awayScore ?? ''} ${m.awayTeam ?? ''} | ${m.statusDescription ?? ''}`);
}
