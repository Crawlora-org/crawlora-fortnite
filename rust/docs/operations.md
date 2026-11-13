# Crawlora Fortnite Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `10`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fortnite | `fortnite.ecosystem_metric` | `fortnite-ecosystem-metric` | `GET /fortnite/ecosystem-metric` | `interval` (query String enum{day, hour, minute} required)<br>`metric` (query String enum{in-client-peak-ccu, in-match-peak-ccu} required)<br>`from` (query String)<br>`to` (query String) | `ApiKeyAuth` | `FortniteEcosystemMetricResponse` |  |
| fortnite | `fortnite.ecosystem_metrics` | `fortnite-ecosystem-metrics` | `GET /fortnite/ecosystem-metrics` | `interval` (query String enum{day, hour, minute} required)<br>`metrics` (query Vec<String> enum{inMatchPeakCCU, inClientPeakCCU})<br>`from` (query String)<br>`to` (query String) | `ApiKeyAuth` | `FortniteEcosystemMetricsResponse` |  |
| fortnite | `fortnite.enums` | `fortnite-enums` | `GET /fortnite/enums` | none | `ApiKeyAuth` | `FortniteEnumsResponse` |  |
| fortnite | `fortnite.genre_rankings` | `fortnite-genre-rankings` | `GET /fortnite/genre-rankings` | `slug` (query String required)<br>`at` (query String)<br>`after` (query String)<br>`before` (query String)<br>`size` (query i64) | `ApiKeyAuth` | `FortniteGenreRankingsResponse` |  |
| fortnite | `fortnite.genres` | `fortnite-genres` | `GET /fortnite/genres` | none | `ApiKeyAuth` | `FortniteGenresResponse` |  |
| fortnite | `fortnite.island` | `fortnite-island` | `GET /fortnite/island` | `code` (query String required) | `ApiKeyAuth` | `FortniteIslandResponse` |  |
| fortnite | `fortnite.island_metric` | `fortnite-island-metric` | `GET /fortnite/island-metric` | `code` (query String required)<br>`interval` (query String enum{day, hour, minute} required)<br>`metric` (query String enum{peak-ccu, favorites, minutes-played, average-minutes-per-player, recommendations, unique-players, plays, retention} required)<br>`from` (query String)<br>`to` (query String) | `ApiKeyAuth` | `FortniteIslandMetricResponse` |  |
| fortnite | `fortnite.island_metrics` | `fortnite-island-metrics` | `GET /fortnite/island-metrics` | `code` (query String required)<br>`interval` (query String enum{day, hour, minute})<br>`metrics` (query Vec<String> enum{averageMinutesPerPlayer, peakCCU, favorites, minutesPlayed, recommendations, plays, uniquePlayers, retention})<br>`from` (query String)<br>`to` (query String) | `ApiKeyAuth` | `FortniteIslandMetricsResponse` |  |
| fortnite | `fortnite.island_rankings` | `fortnite-island-rankings` | `GET /fortnite/island-rankings` | `code` (query String required)<br>`from` (query String)<br>`to` (query String) | `ApiKeyAuth` | `FortniteIslandRankingsResponse` |  |
| fortnite | `fortnite.islands` | `fortnite-islands` | `GET /fortnite/islands` | `after` (query String)<br>`before` (query String)<br>`size` (query i64) | `ApiKeyAuth` | `FortniteIslandsResponse` |  |
