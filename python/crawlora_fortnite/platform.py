"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class FortniteClient(CrawloraClient):
    """Synchronous Fortnite API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-fortnite-python/0.1.0')
        super().__init__(*args, **kwargs)

    def ecosystem_metric(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fortnite-ecosystem-metric', params, response_type=response_type, timeout=timeout, headers=headers)

    def ecosystem_metrics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fortnite-ecosystem-metrics', params, response_type=response_type, timeout=timeout, headers=headers)

    def enums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fortnite-enums', params, response_type=response_type, timeout=timeout, headers=headers)

    def genre_rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fortnite-genre-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    def genres(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fortnite-genres', params, response_type=response_type, timeout=timeout, headers=headers)

    def island(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fortnite-island', params, response_type=response_type, timeout=timeout, headers=headers)

    def island_metric(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fortnite-island-metric', params, response_type=response_type, timeout=timeout, headers=headers)

    def island_metrics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fortnite-island-metrics', params, response_type=response_type, timeout=timeout, headers=headers)

    def island_rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fortnite-island-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    def islands(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('fortnite-islands', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncFortniteClient(AsyncCrawloraClient):
    """Asynchronous Fortnite API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-fortnite-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def ecosystem_metric(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fortnite-ecosystem-metric', params, response_type=response_type, timeout=timeout, headers=headers)

    async def ecosystem_metrics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fortnite-ecosystem-metrics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def enums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fortnite-enums', params, response_type=response_type, timeout=timeout, headers=headers)

    async def genre_rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fortnite-genre-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def genres(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fortnite-genres', params, response_type=response_type, timeout=timeout, headers=headers)

    async def island(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fortnite-island', params, response_type=response_type, timeout=timeout, headers=headers)

    async def island_metric(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fortnite-island-metric', params, response_type=response_type, timeout=timeout, headers=headers)

    async def island_metrics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fortnite-island-metrics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def island_rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fortnite-island-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def islands(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('fortnite-islands', params, response_type=response_type, timeout=timeout, headers=headers)
