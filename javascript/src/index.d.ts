import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class FortniteClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  ecosystemMetric(params: OperationParamsMap["fortnite-ecosystem-metric"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  ecosystemMetrics(params: OperationParamsMap["fortnite-ecosystem-metrics"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  enums(params?: OperationParamsMap["fortnite-enums"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  genreRankings(params: OperationParamsMap["fortnite-genre-rankings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  genres(params?: OperationParamsMap["fortnite-genres"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  island(params: OperationParamsMap["fortnite-island"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  islandMetric(params: OperationParamsMap["fortnite-island-metric"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  islandMetrics(params: OperationParamsMap["fortnite-island-metrics"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  islandRankings(params: OperationParamsMap["fortnite-island-rankings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  islands(params?: OperationParamsMap["fortnite-islands"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  ecosystemMetric(params: OperationParamsMap["fortnite-ecosystem-metric"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  ecosystemMetrics(params: OperationParamsMap["fortnite-ecosystem-metrics"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  enums(params?: OperationParamsMap["fortnite-enums"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  genreRankings(params: OperationParamsMap["fortnite-genre-rankings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  genres(params?: OperationParamsMap["fortnite-genres"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  island(params: OperationParamsMap["fortnite-island"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  islandMetric(params: OperationParamsMap["fortnite-island-metric"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  islandMetrics(params: OperationParamsMap["fortnite-island-metrics"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  islandRankings(params: OperationParamsMap["fortnite-island-rankings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  islands(params?: OperationParamsMap["fortnite-islands"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  ecosystemMetric(...args: OperationRequestArgs<"fortnite-ecosystem-metric">): Promise<OperationResponseMap["fortnite-ecosystem-metric"]>;
  ecosystemMetrics(...args: OperationRequestArgs<"fortnite-ecosystem-metrics">): Promise<OperationResponseMap["fortnite-ecosystem-metrics"]>;
  enums(...args: OperationRequestArgs<"fortnite-enums">): Promise<OperationResponseMap["fortnite-enums"]>;
  genreRankings(...args: OperationRequestArgs<"fortnite-genre-rankings">): Promise<OperationResponseMap["fortnite-genre-rankings"]>;
  genres(...args: OperationRequestArgs<"fortnite-genres">): Promise<OperationResponseMap["fortnite-genres"]>;
  island(...args: OperationRequestArgs<"fortnite-island">): Promise<OperationResponseMap["fortnite-island"]>;
  islandMetric(...args: OperationRequestArgs<"fortnite-island-metric">): Promise<OperationResponseMap["fortnite-island-metric"]>;
  islandMetrics(...args: OperationRequestArgs<"fortnite-island-metrics">): Promise<OperationResponseMap["fortnite-island-metrics"]>;
  islandRankings(...args: OperationRequestArgs<"fortnite-island-rankings">): Promise<OperationResponseMap["fortnite-island-rankings"]>;
  islands(...args: OperationRequestArgs<"fortnite-islands">): Promise<OperationResponseMap["fortnite-islands"]>;
}
export { FortniteClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default FortniteClient;
