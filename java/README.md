# Crawlora Fortnite API client for Java

The official Java client for Crawlora's hosted Fortnite API. It exposes 10 endpoints covering public island discovery, genres, rankings, and engagement metrics. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-fortnite</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-java-console) to get an API key.

```java
import net.crawlora.fortnite.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.genres(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Fortnite API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-fortnite/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-fortnite)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-java-api-docs)
