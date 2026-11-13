# @crawlora-org/fortnite — Fortnite API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Fortnite API.
It exposes 10 API endpoints for public island discovery, genres, rankings, and engagement metrics through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-javascript-homepage). It does not run a browser or scrape Fortnite locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Fortnite or its owners.

## Install

```sh
npm install @crawlora-org/fortnite
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { FortniteClient } from "@crawlora-org/fortnite";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new FortniteClient({ apiKey });
const result1 = await client.genres({});
console.log(result1);
const result2 = await client.islands({ size: 5 });
console.log(result2);
```

The client also exports `Client` as an alias for `FortniteClient`. Operation
methods are available directly in camelCase and through the `fortnite`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-fortnite/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-fortnite/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Fortnite API endpoints

This package exposes each route below as a direct method and through the `fortnite` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-fortnite/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/fortnite/ecosystem-metric` | `fortnite-ecosystem-metric` | Get one Fortnite ecosystem metric |
| `GET` | `/fortnite/ecosystem-metrics` | `fortnite-ecosystem-metrics` | Get Fortnite ecosystem metrics |
| `GET` | `/fortnite/enums` | `fortnite-enums` | List Fortnite metric enums |
| `GET` | `/fortnite/genre-rankings` | `fortnite-genre-rankings` | Get rankings for a Fortnite genre |
| `GET` | `/fortnite/genres` | `fortnite-genres` | List Fortnite genres |
| `GET` | `/fortnite/island` | `fortnite-island` | Get a Fortnite island |
| `GET` | `/fortnite/island-metric` | `fortnite-island-metric` | Get one Fortnite island metric |
| `GET` | `/fortnite/island-metrics` | `fortnite-island-metrics` | Get Fortnite island metrics |
| `GET` | `/fortnite/island-rankings` | `fortnite-island-rankings` | Get Fortnite island rankings |
| `GET` | `/fortnite/islands` | `fortnite-islands` | Discover Fortnite islands |

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
