# Crawlora Fortnite JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `10`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fortnite | `fortnite.ecosystemMetric` | `fortnite-ecosystem-metric` | `GET /fortnite/ecosystem-metric` | `interval` (query "day" \| "hour" \| "minute" required)<br>`metric` (query "in-client-peak-ccu" \| "in-match-peak-ccu" required)<br>`from` (query string)<br>`to` (query string) | `ApiKeyAuth` | `FortniteEcosystemMetricResponse` |  |
| fortnite | `fortnite.ecosystemMetrics` | `fortnite-ecosystem-metrics` | `GET /fortnite/ecosystem-metrics` | `interval` (query "day" \| "hour" \| "minute" required)<br>`metrics` (query Array<"inMatchPeakCCU" \| "inClientPeakCCU">)<br>`from` (query string)<br>`to` (query string) | `ApiKeyAuth` | `FortniteEcosystemMetricsResponse` |  |
| fortnite | `fortnite.enums` | `fortnite-enums` | `GET /fortnite/enums` | none | `ApiKeyAuth` | `FortniteEnumsResponse` |  |
| fortnite | `fortnite.genreRankings` | `fortnite-genre-rankings` | `GET /fortnite/genre-rankings` | `slug` (query string required)<br>`at` (query string)<br>`after` (query string)<br>`before` (query string)<br>`size` (query number) | `ApiKeyAuth` | `FortniteGenreRankingsResponse` |  |
| fortnite | `fortnite.genres` | `fortnite-genres` | `GET /fortnite/genres` | none | `ApiKeyAuth` | `FortniteGenresResponse` |  |
| fortnite | `fortnite.island` | `fortnite-island` | `GET /fortnite/island` | `code` (query string required) | `ApiKeyAuth` | `FortniteIslandResponse` |  |
| fortnite | `fortnite.islandMetric` | `fortnite-island-metric` | `GET /fortnite/island-metric` | `code` (query string required)<br>`interval` (query "day" \| "hour" \| "minute" required)<br>`metric` (query "peak-ccu" \| "favorites" \| "minutes-played" \| "average-minutes-per-player" \| "recommendations" \| "unique-players" \| "plays" \| "retention" required)<br>`from` (query string)<br>`to` (query string) | `ApiKeyAuth` | `FortniteIslandMetricResponse` |  |
| fortnite | `fortnite.islandMetrics` | `fortnite-island-metrics` | `GET /fortnite/island-metrics` | `code` (query string required)<br>`interval` (query "day" \| "hour" \| "minute")<br>`metrics` (query Array<"averageMinutesPerPlayer" \| "peakCCU" \| "favorites" \| "minutesPlayed" \| "recommendations" \| "plays" \| "uniquePlayers" \| "retention">)<br>`from` (query string)<br>`to` (query string) | `ApiKeyAuth` | `FortniteIslandMetricsResponse` |  |
| fortnite | `fortnite.islandRankings` | `fortnite-island-rankings` | `GET /fortnite/island-rankings` | `code` (query string required)<br>`from` (query string)<br>`to` (query string) | `ApiKeyAuth` | `FortniteIslandRankingsResponse` |  |
| fortnite | `fortnite.islands` | `fortnite-islands` | `GET /fortnite/islands` | `after` (query string)<br>`before` (query string)<br>`size` (query number) | `ApiKeyAuth` | `FortniteIslandsResponse` |  |
