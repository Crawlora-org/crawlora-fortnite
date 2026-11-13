# Fortnite API endpoint reference and client usage

This reference lists all 10 public Fortnite API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/fortnite`, `crawlora-fortnite`, and `crawlora-fortnite` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Fortnite locally; Crawlora is independent from and not endorsed by Fortnite or its owners.

The package tracks the public API contract revision `sha256:1c6f1621c65970474912953ca435726229f924e3037dbcbbe728bfb688c82d7f` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `fortnite`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `ecosystemMetric` | `ecosystem_metric` | `fortnite.ecosystem_metric` | `GET /fortnite/ecosystem-metric` | `interval` (query, required; values: `day`, `hour`, `minute`), `metric` (query, required; values: `in-client-peak-ccu`, `in-match-peak-ccu`), `from` (query, optional), `to` (query, optional) | Get one Fortnite ecosystem metric |
| `ecosystemMetrics` | `ecosystem_metrics` | `fortnite.ecosystem_metrics` | `GET /fortnite/ecosystem-metrics` | `interval` (query, required; values: `day`, `hour`, `minute`), `metrics` (query, optional; values: `inMatchPeakCCU`, `inClientPeakCCU`), `from` (query, optional), `to` (query, optional) | Get Fortnite ecosystem metrics |
| `enums` | `enums` | `fortnite.enums` | `GET /fortnite/enums` | — | List Fortnite metric enums |
| `genreRankings` | `genre_rankings` | `fortnite.genre_rankings` | `GET /fortnite/genre-rankings` | `slug` (query, required), `at` (query, optional), `after` (query, optional), `before` (query, optional), `size` (query, optional) | Get rankings for a Fortnite genre |
| `genres` | `genres` | `fortnite.genres` | `GET /fortnite/genres` | — | List Fortnite genres |
| `island` | `island` | `fortnite.island` | `GET /fortnite/island` | `code` (query, required) | Get a Fortnite island |
| `islandMetric` | `island_metric` | `fortnite.island_metric` | `GET /fortnite/island-metric` | `code` (query, required), `interval` (query, required; values: `day`, `hour`, `minute`), `metric` (query, required; values: `peak-ccu`, `favorites`, `minutes-played`, `average-minutes-per-player`, `recommendations`, `unique-players`, `plays`, `retention`), `from` (query, optional), `to` (query, optional) | Get one Fortnite island metric |
| `islandMetrics` | `island_metrics` | `fortnite.island_metrics` | `GET /fortnite/island-metrics` | `code` (query, required), `interval` (query, optional; values: `day`, `hour`, `minute`), `metrics` (query, optional; values: `averageMinutesPerPlayer`, `peakCCU`, `favorites`, `minutesPlayed`, `recommendations`, `plays`, `uniquePlayers`, `retention`), `from` (query, optional), `to` (query, optional) | Get Fortnite island metrics |
| `islandRankings` | `island_rankings` | `fortnite.island_rankings` | `GET /fortnite/island-rankings` | `code` (query, required), `from` (query, optional), `to` (query, optional) | Get Fortnite island rankings |
| `islands` | `islands` | `fortnite.islands` | `GET /fortnite/islands` | `after` (query, optional), `before` (query, optional), `size` (query, optional) | Discover Fortnite islands |

## Client forms

- JavaScript: import `FortniteClient` (also exported as `Client`) from `@crawlora-org/fortnite`; use `new FortniteClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `FortniteClient` (also exported as `Client`) from `crawlora_fortnite`; use `with FortniteClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncFortniteClient`, used with `async with` and `await`.
- Rust: add `crawlora-fortnite` with Cargo; import `Client` and the generated operation parameter struct, then call `client.fortnite.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-fortnite/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
