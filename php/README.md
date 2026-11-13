# Crawlora Fortnite API client for PHP (`crawlora/fortnite`)

This PHP package calls Crawlora's hosted Fortnite API at `https://api.crawlora.net/api/v1`. It exposes 10 endpoints covering public island discovery, genres, rankings, and engagement metrics. It does not call or scrape Fortnite directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/fortnite
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Fortnite\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("fortnite-ecosystem-metric", ['interval' => 'day', 'metric' => 'in-client-peak-ccu']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 10 API operations.

## Supported Fortnite API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-fortnite/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-fortnite). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-fortnite/blob/main/docs/usage.md).
