# Crawlora Fortnite API client for Ruby (`crawlora-fortnite`)

This Ruby gem calls Crawlora's hosted Fortnite API at `https://api.crawlora.net/api/v1`. It exposes 10 endpoints covering public island discovery, genres, rankings, and engagement metrics; it does not call or scrape Fortnite directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-fortnite"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/fortnite"

client = Crawlora::Fortnite::Client.new
result = client.request("fortnite-ecosystem-metric", JSON.parse("{\"interval\": \"day\", \"metric\": \"in-client-peak-ccu\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 10 API operations.

```ruby
client = Crawlora::Fortnite::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Fortnite API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-fortnite/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-fortnite) for account setup, the API operation reference, and release history.
