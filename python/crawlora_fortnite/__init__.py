"""Typed Fortnite client for the Crawlora hosted API."""

from .platform import FortniteClient, AsyncFortniteClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = FortniteClient
AsyncClient = AsyncFortniteClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Fortnite'
PLATFORM = 'fortnite'
CONTRACT_REVISION = 'sha256:1c6f1621c65970474912953ca435726229f924e3037dbcbbe728bfb688c82d7f'

__all__ = [
    "FortniteClient", "AsyncFortniteClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
