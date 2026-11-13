import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class FortniteClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-fortnite-js/0.1.0" });
    this["ecosystemMetric"] = (...args) => this.request("fortnite-ecosystem-metric", ...args);
    this["ecosystemMetrics"] = (...args) => this.request("fortnite-ecosystem-metrics", ...args);
    this["enums"] = (...args) => this.request("fortnite-enums", ...args);
    this["genreRankings"] = (...args) => this.request("fortnite-genre-rankings", ...args);
    this["genres"] = (...args) => this.request("fortnite-genres", ...args);
    this["island"] = (...args) => this.request("fortnite-island", ...args);
    this["islandMetric"] = (...args) => this.request("fortnite-island-metric", ...args);
    this["islandMetrics"] = (...args) => this.request("fortnite-island-metrics", ...args);
    this["islandRankings"] = (...args) => this.request("fortnite-island-rankings", ...args);
    this["islands"] = (...args) => this.request("fortnite-islands", ...args);
  }
}

export { FortniteClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default FortniteClient;
