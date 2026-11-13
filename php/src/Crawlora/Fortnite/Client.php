<?php

declare(strict_types=1);

namespace Crawlora\Fortnite;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'fortnite';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 10;
    public const OPERATION_IDS = ["fortnite-ecosystem-metric", "fortnite-ecosystem-metrics", "fortnite-enums", "fortnite-genre-rankings", "fortnite-genres", "fortnite-island", "fortnite-island-metric", "fortnite-island-metrics", "fortnite-island-rankings", "fortnite-islands"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"fortnite-ecosystem-metric": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-ecosystem-metric", "method": "GET", "params": [{"description": "Bucket size", "enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "required": true, "type": "string", "x-example": "day"}, {"description": "Native metric path variant", "enum": ["in-client-peak-ccu", "in-match-peak-ccu"], "in": "query", "name": "metric", "required": true, "type": "string", "x-example": "in-client-peak-ccu"}, {"description": "Inclusive ISO-8601 start time, within seven days", "in": "query", "name": "from", "type": "string"}, {"description": "Exclusive ISO-8601 end time", "in": "query", "name": "to", "type": "string"}], "path": "/fortnite/ecosystem-metric", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "required": true, "type": "string"}, {"enum": ["in-client-peak-ccu", "in-match-peak-ccu"], "in": "query", "name": "metric", "required": true, "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "fortnite-ecosystem-metrics": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-ecosystem-metrics", "method": "GET", "params": [{"description": "Bucket size", "enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "required": true, "type": "string", "x-example": "day"}, {"collectionFormat": "csv", "description": "Optional repeatable metric filter", "in": "query", "items": {"enum": ["inMatchPeakCCU", "inClientPeakCCU"], "type": "string"}, "name": "metrics", "type": "array"}, {"description": "Inclusive ISO-8601 start time, within seven days", "in": "query", "name": "from", "type": "string"}, {"description": "Exclusive ISO-8601 end time", "in": "query", "name": "to", "type": "string"}], "path": "/fortnite/ecosystem-metrics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "required": true, "type": "string"}, {"collectionFormat": "csv", "enum": ["inMatchPeakCCU", "inClientPeakCCU"], "in": "query", "name": "metrics", "type": "array"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "fortnite-enums": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-enums", "method": "GET", "params": [], "path": "/fortnite/enums", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "fortnite-genre-rankings": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-genre-rankings", "method": "GET", "params": [{"description": "Genre slug from fortnite_genres", "in": "query", "name": "slug", "required": true, "type": "string"}, {"description": "Hourly point-in-time snapshot, at most seven days old", "in": "query", "name": "at", "type": "string"}, {"description": "Return results after this upstream cursor", "in": "query", "name": "after", "type": "string"}, {"description": "Return results before this upstream cursor", "in": "query", "name": "before", "type": "string"}, {"description": "Upstream page size, 1 through 1000", "in": "query", "name": "size", "type": "integer"}], "path": "/fortnite/genre-rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"in": "query", "name": "at", "type": "string"}, {"in": "query", "name": "after", "type": "string"}, {"in": "query", "name": "before", "type": "string"}, {"in": "query", "name": "size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fortnite-genres": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-genres", "method": "GET", "params": [], "path": "/fortnite/genres", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "fortnite-island": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-island", "method": "GET", "params": [{"description": "Island code or first-party display name", "in": "query", "name": "code", "required": true, "type": "string"}], "path": "/fortnite/island", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "code", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fortnite-island-metric": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-island-metric", "method": "GET", "params": [{"description": "Island code or first-party display name", "in": "query", "name": "code", "required": true, "type": "string"}, {"description": "Bucket size", "enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "required": true, "type": "string", "x-example": "day"}, {"description": "Native metric path variant", "enum": ["peak-ccu", "favorites", "minutes-played", "average-minutes-per-player", "recommendations", "unique-players", "plays", "retention"], "in": "query", "name": "metric", "required": true, "type": "string", "x-example": "peak-ccu"}, {"description": "Inclusive ISO-8601 start time, within seven days", "in": "query", "name": "from", "type": "string"}, {"description": "Exclusive ISO-8601 end time", "in": "query", "name": "to", "type": "string"}], "path": "/fortnite/island-metric", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "code", "required": true, "type": "string"}, {"enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "required": true, "type": "string"}, {"enum": ["peak-ccu", "favorites", "minutes-played", "average-minutes-per-player", "recommendations", "unique-players", "plays", "retention"], "in": "query", "name": "metric", "required": true, "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "fortnite-island-metrics": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-island-metrics", "method": "GET", "params": [{"description": "Island code or first-party display name", "in": "query", "name": "code", "required": true, "type": "string"}, {"description": "Optional bucket size", "enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "type": "string"}, {"collectionFormat": "csv", "description": "Optional repeatable metric filter", "in": "query", "items": {"enum": ["averageMinutesPerPlayer", "peakCCU", "favorites", "minutesPlayed", "recommendations", "plays", "uniquePlayers", "retention"], "type": "string"}, "name": "metrics", "type": "array"}, {"description": "Inclusive ISO-8601 start time, within seven days", "in": "query", "name": "from", "type": "string"}, {"description": "Exclusive ISO-8601 end time", "in": "query", "name": "to", "type": "string"}], "path": "/fortnite/island-metrics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "code", "required": true, "type": "string"}, {"enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "type": "string"}, {"collectionFormat": "csv", "enum": ["averageMinutesPerPlayer", "peakCCU", "favorites", "minutesPlayed", "recommendations", "plays", "uniquePlayers", "retention"], "in": "query", "name": "metrics", "type": "array"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "fortnite-island-rankings": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-island-rankings", "method": "GET", "params": [{"description": "Island code or first-party display name", "in": "query", "name": "code", "required": true, "type": "string"}, {"description": "Inclusive ISO-8601 start time, within seven days", "in": "query", "name": "from", "type": "string"}, {"description": "Exclusive ISO-8601 end time", "in": "query", "name": "to", "type": "string"}], "path": "/fortnite/island-rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "code", "required": true, "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "fortnite-islands": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-islands", "method": "GET", "params": [{"description": "Return islands after this upstream cursor", "in": "query", "name": "after", "type": "string"}, {"description": "Return islands before this upstream cursor", "in": "query", "name": "before", "type": "string"}, {"description": "Upstream page size, 1 through 1000", "in": "query", "name": "size", "type": "integer"}], "path": "/fortnite/islands", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "after", "type": "string"}, {"in": "query", "name": "before", "type": "string"}, {"in": "query", "name": "size", "type": "integer"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-fortnite-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function ecosystem_metric(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fortnite-ecosystem-metric", $params, $responseType);
    }
    public function ecosystem_metrics(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fortnite-ecosystem-metrics", $params, $responseType);
    }
    public function enums(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fortnite-enums", $params, $responseType);
    }
    public function genre_rankings(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fortnite-genre-rankings", $params, $responseType);
    }
    public function genres(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fortnite-genres", $params, $responseType);
    }
    public function island(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fortnite-island", $params, $responseType);
    }
    public function island_metric(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fortnite-island-metric", $params, $responseType);
    }
    public function island_metrics(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fortnite-island-metrics", $params, $responseType);
    }
    public function island_rankings(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fortnite-island-rankings", $params, $responseType);
    }
    public function islands(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("fortnite-islands", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
