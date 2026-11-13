from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelFortniteResponse = TypedDict('ModelFortniteResponse', {
    'data': NotRequired[dict[str, Any]],
    'source_url': NotRequired[str],
}, total=False)

ModelFortniteEnumsResponse = TypedDict('ModelFortniteEnumsResponse', {
    'ecosystem_metric_paths': NotRequired[list[str]],
    'ecosystem_metrics': NotRequired[list[str]],
    'intervals': NotRequired[list[str]],
    'island_metric_paths': NotRequired[list[str]],
    'island_metrics': NotRequired[list[str]],
}, total=False)

FortniteEcosystemMetricResponse = Any
FortniteEcosystemMetricParams = TypedDict('FortniteEcosystemMetricParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'interval': Required[Literal['day', 'hour', 'minute']],
    'metric': Required[Literal['in-client-peak-ccu', 'in-match-peak-ccu']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteEcosystemMetricsResponse = Any
FortniteEcosystemMetricsParams = TypedDict('FortniteEcosystemMetricsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'interval': Required[Literal['day', 'hour', 'minute']],
    'metrics': NotRequired[list[Literal['inMatchPeakCCU', 'inClientPeakCCU']]],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteEnumsResponse = Any
FortniteEnumsParams = TypedDict('FortniteEnumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FortniteGenreRankingsResponse = Any
FortniteGenreRankingsParams = TypedDict('FortniteGenreRankingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'at': NotRequired[str],
    'after': NotRequired[str],
    'before': NotRequired[str],
    'size': NotRequired[int],
}, total=False)

FortniteGenresResponse = Any
FortniteGenresParams = TypedDict('FortniteGenresParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FortniteIslandResponse = Any
FortniteIslandParams = TypedDict('FortniteIslandParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'code': Required[str],
}, total=False)

FortniteIslandMetricResponse = Any
FortniteIslandMetricParams = TypedDict('FortniteIslandMetricParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'code': Required[str],
    'interval': Required[Literal['day', 'hour', 'minute']],
    'metric': Required[Literal['peak-ccu', 'favorites', 'minutes-played', 'average-minutes-per-player', 'recommendations', 'unique-players', 'plays', 'retention']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteIslandMetricsResponse = Any
FortniteIslandMetricsParams = TypedDict('FortniteIslandMetricsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'code': Required[str],
    'interval': NotRequired[Literal['day', 'hour', 'minute']],
    'metrics': NotRequired[list[Literal['averageMinutesPerPlayer', 'peakCCU', 'favorites', 'minutesPlayed', 'recommendations', 'plays', 'uniquePlayers', 'retention']]],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteIslandRankingsResponse = Any
FortniteIslandRankingsParams = TypedDict('FortniteIslandRankingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'code': Required[str],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteIslandsResponse = Any
FortniteIslandsParams = TypedDict('FortniteIslandsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'after': NotRequired[str],
    'before': NotRequired[str],
    'size': NotRequired[int],
}, total=False)

class FortniteGroup:
    @overload
    def ecosystem_metric(self, **params: Unpack[FortniteEcosystemMetricStreamParams]) -> BinaryIO: ...
    @overload
    def ecosystem_metric(self, **params: Unpack[FortniteEcosystemMetricTextResponseParams]) -> str: ...
    @overload
    def ecosystem_metric(self, **params: Unpack[FortniteEcosystemMetricDefaultParams]) -> FortniteEcosystemMetricResponse: ...
    @overload
    def ecosystem_metrics(self, **params: Unpack[FortniteEcosystemMetricsStreamParams]) -> BinaryIO: ...
    @overload
    def ecosystem_metrics(self, **params: Unpack[FortniteEcosystemMetricsTextResponseParams]) -> str: ...
    @overload
    def ecosystem_metrics(self, **params: Unpack[FortniteEcosystemMetricsDefaultParams]) -> FortniteEcosystemMetricsResponse: ...
    @overload
    def enums(self, **params: Unpack[FortniteEnumsStreamParams]) -> BinaryIO: ...
    @overload
    def enums(self, **params: Unpack[FortniteEnumsTextResponseParams]) -> str: ...
    @overload
    def enums(self, **params: Unpack[FortniteEnumsDefaultParams]) -> FortniteEnumsResponse: ...
    @overload
    def genre_rankings(self, **params: Unpack[FortniteGenreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def genre_rankings(self, **params: Unpack[FortniteGenreRankingsTextResponseParams]) -> str: ...
    @overload
    def genre_rankings(self, **params: Unpack[FortniteGenreRankingsDefaultParams]) -> FortniteGenreRankingsResponse: ...
    @overload
    def genres(self, **params: Unpack[FortniteGenresStreamParams]) -> BinaryIO: ...
    @overload
    def genres(self, **params: Unpack[FortniteGenresTextResponseParams]) -> str: ...
    @overload
    def genres(self, **params: Unpack[FortniteGenresDefaultParams]) -> FortniteGenresResponse: ...
    @overload
    def island(self, **params: Unpack[FortniteIslandStreamParams]) -> BinaryIO: ...
    @overload
    def island(self, **params: Unpack[FortniteIslandTextResponseParams]) -> str: ...
    @overload
    def island(self, **params: Unpack[FortniteIslandDefaultParams]) -> FortniteIslandResponse: ...
    @overload
    def island_metric(self, **params: Unpack[FortniteIslandMetricStreamParams]) -> BinaryIO: ...
    @overload
    def island_metric(self, **params: Unpack[FortniteIslandMetricTextResponseParams]) -> str: ...
    @overload
    def island_metric(self, **params: Unpack[FortniteIslandMetricDefaultParams]) -> FortniteIslandMetricResponse: ...
    @overload
    def island_metrics(self, **params: Unpack[FortniteIslandMetricsStreamParams]) -> BinaryIO: ...
    @overload
    def island_metrics(self, **params: Unpack[FortniteIslandMetricsTextResponseParams]) -> str: ...
    @overload
    def island_metrics(self, **params: Unpack[FortniteIslandMetricsDefaultParams]) -> FortniteIslandMetricsResponse: ...
    @overload
    def island_rankings(self, **params: Unpack[FortniteIslandRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def island_rankings(self, **params: Unpack[FortniteIslandRankingsTextResponseParams]) -> str: ...
    @overload
    def island_rankings(self, **params: Unpack[FortniteIslandRankingsDefaultParams]) -> FortniteIslandRankingsResponse: ...
    @overload
    def islands(self, **params: Unpack[FortniteIslandsStreamParams]) -> BinaryIO: ...
    @overload
    def islands(self, **params: Unpack[FortniteIslandsTextResponseParams]) -> str: ...
    @overload
    def islands(self, **params: Unpack[FortniteIslandsDefaultParams]) -> FortniteIslandsResponse: ...

OperationId = Literal[
    'fortnite-ecosystem-metric',
    'fortnite-ecosystem-metrics',
    'fortnite-enums',
    'fortnite-genre-rankings',
    'fortnite-genres',
    'fortnite-island',
    'fortnite-island-metric',
    'fortnite-island-metrics',
    'fortnite-island-rankings',
    'fortnite-islands',
]

class CrawloraClient:
    fortnite: FortniteGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fortnite-ecosystem-metric'],
        params: FortniteEcosystemMetricParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteEcosystemMetricResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fortnite-ecosystem-metrics'],
        params: FortniteEcosystemMetricsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteEcosystemMetricsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fortnite-enums'],
        params: FortniteEnumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteEnumsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fortnite-genre-rankings'],
        params: FortniteGenreRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteGenreRankingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fortnite-genres'],
        params: FortniteGenresParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteGenresResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fortnite-island'],
        params: FortniteIslandParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteIslandResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fortnite-island-metric'],
        params: FortniteIslandMetricParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteIslandMetricResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fortnite-island-metrics'],
        params: FortniteIslandMetricsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteIslandMetricsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fortnite-island-rankings'],
        params: FortniteIslandRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteIslandRankingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['fortnite-islands'],
        params: FortniteIslandsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteIslandsResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['fortnite-ecosystem-metric'],
        params: FortniteEcosystemMetricParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteEcosystemMetricResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fortnite-ecosystem-metrics'],
        params: FortniteEcosystemMetricsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteEcosystemMetricsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fortnite-enums'],
        params: FortniteEnumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteEnumsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fortnite-genre-rankings'],
        params: FortniteGenreRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteGenreRankingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fortnite-genres'],
        params: FortniteGenresParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteGenresResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fortnite-island'],
        params: FortniteIslandParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteIslandResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fortnite-island-metric'],
        params: FortniteIslandMetricParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteIslandMetricResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fortnite-island-metrics'],
        params: FortniteIslandMetricsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteIslandMetricsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fortnite-island-rankings'],
        params: FortniteIslandRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteIslandRankingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['fortnite-islands'],
        params: FortniteIslandsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FortniteIslandsResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class FortniteClient(CrawloraClient):
    def __enter__(self) -> FortniteClient: ...
    @overload
    def ecosystem_metric(self, **params: Unpack[FortniteEcosystemMetricStreamParams]) -> BinaryIO: ...
    @overload
    def ecosystem_metric(self, **params: Unpack[FortniteEcosystemMetricTextResponseParams]) -> str: ...
    @overload
    def ecosystem_metric(self, **params: Unpack[FortniteEcosystemMetricDefaultParams]) -> FortniteEcosystemMetricResponse: ...
    @overload
    def ecosystem_metrics(self, **params: Unpack[FortniteEcosystemMetricsStreamParams]) -> BinaryIO: ...
    @overload
    def ecosystem_metrics(self, **params: Unpack[FortniteEcosystemMetricsTextResponseParams]) -> str: ...
    @overload
    def ecosystem_metrics(self, **params: Unpack[FortniteEcosystemMetricsDefaultParams]) -> FortniteEcosystemMetricsResponse: ...
    @overload
    def enums(self, **params: Unpack[FortniteEnumsStreamParams]) -> BinaryIO: ...
    @overload
    def enums(self, **params: Unpack[FortniteEnumsTextResponseParams]) -> str: ...
    @overload
    def enums(self, **params: Unpack[FortniteEnumsDefaultParams]) -> FortniteEnumsResponse: ...
    @overload
    def genre_rankings(self, **params: Unpack[FortniteGenreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def genre_rankings(self, **params: Unpack[FortniteGenreRankingsTextResponseParams]) -> str: ...
    @overload
    def genre_rankings(self, **params: Unpack[FortniteGenreRankingsDefaultParams]) -> FortniteGenreRankingsResponse: ...
    @overload
    def genres(self, **params: Unpack[FortniteGenresStreamParams]) -> BinaryIO: ...
    @overload
    def genres(self, **params: Unpack[FortniteGenresTextResponseParams]) -> str: ...
    @overload
    def genres(self, **params: Unpack[FortniteGenresDefaultParams]) -> FortniteGenresResponse: ...
    @overload
    def island(self, **params: Unpack[FortniteIslandStreamParams]) -> BinaryIO: ...
    @overload
    def island(self, **params: Unpack[FortniteIslandTextResponseParams]) -> str: ...
    @overload
    def island(self, **params: Unpack[FortniteIslandDefaultParams]) -> FortniteIslandResponse: ...
    @overload
    def island_metric(self, **params: Unpack[FortniteIslandMetricStreamParams]) -> BinaryIO: ...
    @overload
    def island_metric(self, **params: Unpack[FortniteIslandMetricTextResponseParams]) -> str: ...
    @overload
    def island_metric(self, **params: Unpack[FortniteIslandMetricDefaultParams]) -> FortniteIslandMetricResponse: ...
    @overload
    def island_metrics(self, **params: Unpack[FortniteIslandMetricsStreamParams]) -> BinaryIO: ...
    @overload
    def island_metrics(self, **params: Unpack[FortniteIslandMetricsTextResponseParams]) -> str: ...
    @overload
    def island_metrics(self, **params: Unpack[FortniteIslandMetricsDefaultParams]) -> FortniteIslandMetricsResponse: ...
    @overload
    def island_rankings(self, **params: Unpack[FortniteIslandRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def island_rankings(self, **params: Unpack[FortniteIslandRankingsTextResponseParams]) -> str: ...
    @overload
    def island_rankings(self, **params: Unpack[FortniteIslandRankingsDefaultParams]) -> FortniteIslandRankingsResponse: ...
    @overload
    def islands(self, **params: Unpack[FortniteIslandsStreamParams]) -> BinaryIO: ...
    @overload
    def islands(self, **params: Unpack[FortniteIslandsTextResponseParams]) -> str: ...
    @overload
    def islands(self, **params: Unpack[FortniteIslandsDefaultParams]) -> FortniteIslandsResponse: ...

class AsyncFortniteClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncFortniteClient: ...
    fortnite: _AsyncFortniteGroup
    @overload
    async def ecosystem_metric(self, **params: Unpack[FortniteEcosystemMetricStreamParams]) -> BinaryIO: ...
    @overload
    async def ecosystem_metric(self, **params: Unpack[FortniteEcosystemMetricTextResponseParams]) -> str: ...
    @overload
    async def ecosystem_metric(self, **params: Unpack[FortniteEcosystemMetricDefaultParams]) -> FortniteEcosystemMetricResponse: ...
    @overload
    async def ecosystem_metrics(self, **params: Unpack[FortniteEcosystemMetricsStreamParams]) -> BinaryIO: ...
    @overload
    async def ecosystem_metrics(self, **params: Unpack[FortniteEcosystemMetricsTextResponseParams]) -> str: ...
    @overload
    async def ecosystem_metrics(self, **params: Unpack[FortniteEcosystemMetricsDefaultParams]) -> FortniteEcosystemMetricsResponse: ...
    @overload
    async def enums(self, **params: Unpack[FortniteEnumsStreamParams]) -> BinaryIO: ...
    @overload
    async def enums(self, **params: Unpack[FortniteEnumsTextResponseParams]) -> str: ...
    @overload
    async def enums(self, **params: Unpack[FortniteEnumsDefaultParams]) -> FortniteEnumsResponse: ...
    @overload
    async def genre_rankings(self, **params: Unpack[FortniteGenreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def genre_rankings(self, **params: Unpack[FortniteGenreRankingsTextResponseParams]) -> str: ...
    @overload
    async def genre_rankings(self, **params: Unpack[FortniteGenreRankingsDefaultParams]) -> FortniteGenreRankingsResponse: ...
    @overload
    async def genres(self, **params: Unpack[FortniteGenresStreamParams]) -> BinaryIO: ...
    @overload
    async def genres(self, **params: Unpack[FortniteGenresTextResponseParams]) -> str: ...
    @overload
    async def genres(self, **params: Unpack[FortniteGenresDefaultParams]) -> FortniteGenresResponse: ...
    @overload
    async def island(self, **params: Unpack[FortniteIslandStreamParams]) -> BinaryIO: ...
    @overload
    async def island(self, **params: Unpack[FortniteIslandTextResponseParams]) -> str: ...
    @overload
    async def island(self, **params: Unpack[FortniteIslandDefaultParams]) -> FortniteIslandResponse: ...
    @overload
    async def island_metric(self, **params: Unpack[FortniteIslandMetricStreamParams]) -> BinaryIO: ...
    @overload
    async def island_metric(self, **params: Unpack[FortniteIslandMetricTextResponseParams]) -> str: ...
    @overload
    async def island_metric(self, **params: Unpack[FortniteIslandMetricDefaultParams]) -> FortniteIslandMetricResponse: ...
    @overload
    async def island_metrics(self, **params: Unpack[FortniteIslandMetricsStreamParams]) -> BinaryIO: ...
    @overload
    async def island_metrics(self, **params: Unpack[FortniteIslandMetricsTextResponseParams]) -> str: ...
    @overload
    async def island_metrics(self, **params: Unpack[FortniteIslandMetricsDefaultParams]) -> FortniteIslandMetricsResponse: ...
    @overload
    async def island_rankings(self, **params: Unpack[FortniteIslandRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def island_rankings(self, **params: Unpack[FortniteIslandRankingsTextResponseParams]) -> str: ...
    @overload
    async def island_rankings(self, **params: Unpack[FortniteIslandRankingsDefaultParams]) -> FortniteIslandRankingsResponse: ...
    @overload
    async def islands(self, **params: Unpack[FortniteIslandsStreamParams]) -> BinaryIO: ...
    @overload
    async def islands(self, **params: Unpack[FortniteIslandsTextResponseParams]) -> str: ...
    @overload
    async def islands(self, **params: Unpack[FortniteIslandsDefaultParams]) -> FortniteIslandsResponse: ...

class _AsyncFortniteGroup:
    @overload
    async def ecosystem_metric(self, **params: Unpack[FortniteEcosystemMetricStreamParams]) -> BinaryIO: ...
    @overload
    async def ecosystem_metric(self, **params: Unpack[FortniteEcosystemMetricTextResponseParams]) -> str: ...
    @overload
    async def ecosystem_metric(self, **params: Unpack[FortniteEcosystemMetricDefaultParams]) -> FortniteEcosystemMetricResponse: ...
    @overload
    async def ecosystem_metrics(self, **params: Unpack[FortniteEcosystemMetricsStreamParams]) -> BinaryIO: ...
    @overload
    async def ecosystem_metrics(self, **params: Unpack[FortniteEcosystemMetricsTextResponseParams]) -> str: ...
    @overload
    async def ecosystem_metrics(self, **params: Unpack[FortniteEcosystemMetricsDefaultParams]) -> FortniteEcosystemMetricsResponse: ...
    @overload
    async def enums(self, **params: Unpack[FortniteEnumsStreamParams]) -> BinaryIO: ...
    @overload
    async def enums(self, **params: Unpack[FortniteEnumsTextResponseParams]) -> str: ...
    @overload
    async def enums(self, **params: Unpack[FortniteEnumsDefaultParams]) -> FortniteEnumsResponse: ...
    @overload
    async def genre_rankings(self, **params: Unpack[FortniteGenreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def genre_rankings(self, **params: Unpack[FortniteGenreRankingsTextResponseParams]) -> str: ...
    @overload
    async def genre_rankings(self, **params: Unpack[FortniteGenreRankingsDefaultParams]) -> FortniteGenreRankingsResponse: ...
    @overload
    async def genres(self, **params: Unpack[FortniteGenresStreamParams]) -> BinaryIO: ...
    @overload
    async def genres(self, **params: Unpack[FortniteGenresTextResponseParams]) -> str: ...
    @overload
    async def genres(self, **params: Unpack[FortniteGenresDefaultParams]) -> FortniteGenresResponse: ...
    @overload
    async def island(self, **params: Unpack[FortniteIslandStreamParams]) -> BinaryIO: ...
    @overload
    async def island(self, **params: Unpack[FortniteIslandTextResponseParams]) -> str: ...
    @overload
    async def island(self, **params: Unpack[FortniteIslandDefaultParams]) -> FortniteIslandResponse: ...
    @overload
    async def island_metric(self, **params: Unpack[FortniteIslandMetricStreamParams]) -> BinaryIO: ...
    @overload
    async def island_metric(self, **params: Unpack[FortniteIslandMetricTextResponseParams]) -> str: ...
    @overload
    async def island_metric(self, **params: Unpack[FortniteIslandMetricDefaultParams]) -> FortniteIslandMetricResponse: ...
    @overload
    async def island_metrics(self, **params: Unpack[FortniteIslandMetricsStreamParams]) -> BinaryIO: ...
    @overload
    async def island_metrics(self, **params: Unpack[FortniteIslandMetricsTextResponseParams]) -> str: ...
    @overload
    async def island_metrics(self, **params: Unpack[FortniteIslandMetricsDefaultParams]) -> FortniteIslandMetricsResponse: ...
    @overload
    async def island_rankings(self, **params: Unpack[FortniteIslandRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def island_rankings(self, **params: Unpack[FortniteIslandRankingsTextResponseParams]) -> str: ...
    @overload
    async def island_rankings(self, **params: Unpack[FortniteIslandRankingsDefaultParams]) -> FortniteIslandRankingsResponse: ...
    @overload
    async def islands(self, **params: Unpack[FortniteIslandsStreamParams]) -> BinaryIO: ...
    @overload
    async def islands(self, **params: Unpack[FortniteIslandsTextResponseParams]) -> str: ...
    @overload
    async def islands(self, **params: Unpack[FortniteIslandsDefaultParams]) -> FortniteIslandsResponse: ...

FortniteEcosystemMetricDefaultParams = TypedDict('FortniteEcosystemMetricDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'interval': Required[Literal['day', 'hour', 'minute']],
    'metric': Required[Literal['in-client-peak-ccu', 'in-match-peak-ccu']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteEcosystemMetricTextResponseParams = TypedDict('FortniteEcosystemMetricTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'interval': Required[Literal['day', 'hour', 'minute']],
    'metric': Required[Literal['in-client-peak-ccu', 'in-match-peak-ccu']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteEcosystemMetricStreamParams = TypedDict('FortniteEcosystemMetricStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'interval': Required[Literal['day', 'hour', 'minute']],
    'metric': Required[Literal['in-client-peak-ccu', 'in-match-peak-ccu']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteEcosystemMetricsDefaultParams = TypedDict('FortniteEcosystemMetricsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'interval': Required[Literal['day', 'hour', 'minute']],
    'metrics': NotRequired[list[Literal['inMatchPeakCCU', 'inClientPeakCCU']]],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteEcosystemMetricsTextResponseParams = TypedDict('FortniteEcosystemMetricsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'interval': Required[Literal['day', 'hour', 'minute']],
    'metrics': NotRequired[list[Literal['inMatchPeakCCU', 'inClientPeakCCU']]],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteEcosystemMetricsStreamParams = TypedDict('FortniteEcosystemMetricsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'interval': Required[Literal['day', 'hour', 'minute']],
    'metrics': NotRequired[list[Literal['inMatchPeakCCU', 'inClientPeakCCU']]],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteEnumsDefaultParams = TypedDict('FortniteEnumsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FortniteEnumsTextResponseParams = TypedDict('FortniteEnumsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FortniteEnumsStreamParams = TypedDict('FortniteEnumsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FortniteGenreRankingsDefaultParams = TypedDict('FortniteGenreRankingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
    'at': NotRequired[str],
    'after': NotRequired[str],
    'before': NotRequired[str],
    'size': NotRequired[int],
}, total=False)

FortniteGenreRankingsTextResponseParams = TypedDict('FortniteGenreRankingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
    'at': NotRequired[str],
    'after': NotRequired[str],
    'before': NotRequired[str],
    'size': NotRequired[int],
}, total=False)

FortniteGenreRankingsStreamParams = TypedDict('FortniteGenreRankingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
    'at': NotRequired[str],
    'after': NotRequired[str],
    'before': NotRequired[str],
    'size': NotRequired[int],
}, total=False)

FortniteGenresDefaultParams = TypedDict('FortniteGenresDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FortniteGenresTextResponseParams = TypedDict('FortniteGenresTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FortniteGenresStreamParams = TypedDict('FortniteGenresStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FortniteIslandDefaultParams = TypedDict('FortniteIslandDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'code': Required[str],
}, total=False)

FortniteIslandTextResponseParams = TypedDict('FortniteIslandTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'code': Required[str],
}, total=False)

FortniteIslandStreamParams = TypedDict('FortniteIslandStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'code': Required[str],
}, total=False)

FortniteIslandMetricDefaultParams = TypedDict('FortniteIslandMetricDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'code': Required[str],
    'interval': Required[Literal['day', 'hour', 'minute']],
    'metric': Required[Literal['peak-ccu', 'favorites', 'minutes-played', 'average-minutes-per-player', 'recommendations', 'unique-players', 'plays', 'retention']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteIslandMetricTextResponseParams = TypedDict('FortniteIslandMetricTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'code': Required[str],
    'interval': Required[Literal['day', 'hour', 'minute']],
    'metric': Required[Literal['peak-ccu', 'favorites', 'minutes-played', 'average-minutes-per-player', 'recommendations', 'unique-players', 'plays', 'retention']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteIslandMetricStreamParams = TypedDict('FortniteIslandMetricStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'code': Required[str],
    'interval': Required[Literal['day', 'hour', 'minute']],
    'metric': Required[Literal['peak-ccu', 'favorites', 'minutes-played', 'average-minutes-per-player', 'recommendations', 'unique-players', 'plays', 'retention']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteIslandMetricsDefaultParams = TypedDict('FortniteIslandMetricsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'code': Required[str],
    'interval': NotRequired[Literal['day', 'hour', 'minute']],
    'metrics': NotRequired[list[Literal['averageMinutesPerPlayer', 'peakCCU', 'favorites', 'minutesPlayed', 'recommendations', 'plays', 'uniquePlayers', 'retention']]],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteIslandMetricsTextResponseParams = TypedDict('FortniteIslandMetricsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'code': Required[str],
    'interval': NotRequired[Literal['day', 'hour', 'minute']],
    'metrics': NotRequired[list[Literal['averageMinutesPerPlayer', 'peakCCU', 'favorites', 'minutesPlayed', 'recommendations', 'plays', 'uniquePlayers', 'retention']]],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteIslandMetricsStreamParams = TypedDict('FortniteIslandMetricsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'code': Required[str],
    'interval': NotRequired[Literal['day', 'hour', 'minute']],
    'metrics': NotRequired[list[Literal['averageMinutesPerPlayer', 'peakCCU', 'favorites', 'minutesPlayed', 'recommendations', 'plays', 'uniquePlayers', 'retention']]],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteIslandRankingsDefaultParams = TypedDict('FortniteIslandRankingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'code': Required[str],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteIslandRankingsTextResponseParams = TypedDict('FortniteIslandRankingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'code': Required[str],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteIslandRankingsStreamParams = TypedDict('FortniteIslandRankingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'code': Required[str],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

FortniteIslandsDefaultParams = TypedDict('FortniteIslandsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'after': NotRequired[str],
    'before': NotRequired[str],
    'size': NotRequired[int],
}, total=False)

FortniteIslandsTextResponseParams = TypedDict('FortniteIslandsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'after': NotRequired[str],
    'before': NotRequired[str],
    'size': NotRequired[int],
}, total=False)

FortniteIslandsStreamParams = TypedDict('FortniteIslandsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'after': NotRequired[str],
    'before': NotRequired[str],
    'size': NotRequired[int],
}, total=False)
