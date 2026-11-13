import test from "node:test";
import assert from "node:assert/strict";
import {
  FortniteClient, CrawloraClientError, CrawloraNetworkError,
  CrawloraServerError, groups, operations, operationCount
} from "../src/index.js";

const json = (data, status = 200, headers = {}) => new Response(JSON.stringify(data), {
  status, headers: { "content-type": "application/json", ...headers }
});

test("exports only this platform and exposes direct and grouped methods", async () => {
  const client = new FortniteClient({ apiKey: "test-key", fetch: async () => json({ ok: true }) });
  assert.equal(operationCount, Object.keys(operations).length);
  assert.deepEqual(Object.keys(groups), ["fortnite"]);
  assert.equal(typeof client["ecosystemMetric"], "function");
  assert.equal(typeof client["fortnite"]["ecosystemMetric"], "function");
});

test("serializes required query/path values, adds API key and platform User-Agent", async () => {
  let seen;
  const client = new FortniteClient({ apiKey: "secret", fetch: async (url, init) => {
    seen = { url: String(url), headers: init.headers };
    return json({ ok: true });
  } });
  await client.request("fortnite-ecosystem-metric", {"interval": "day", "metric": "in-client-peak-ccu"});
  assert.match(seen.url, /\/fortnite\/ecosystem\-metric/);
  assert.equal(seen.headers["x-api-key"], "secret");
  assert.equal(seen.headers["user-agent"], "crawlora-fortnite-js/0.1.0");
});

test("allows caller User-Agent override and response text mode", async () => {
  let seen;
  const client = new FortniteClient({ apiKey: "key", userAgent: "custom-agent", fetch: async (_url, init) => {
    seen = init.headers;
    return new Response("caption text", { headers: { "content-type": "text/plain" } });
  } });
  const result = await client.request("fortnite-ecosystem-metric", {"interval": "day", "metric": "in-client-peak-ccu"}, { responseType: "text" });
  assert.equal(seen["user-agent"], "custom-agent");
  assert.equal(result, "caption text");

  const rawFeed = "1~home|2~away\n";
  const autoClient = new FortniteClient({ fetch: async () => new Response(rawFeed, {
    headers: { "content-type": "text/plain" }
  }) });
  assert.equal(await autoClient.request("fortnite-ecosystem-metric", {"interval": "day", "metric": "in-client-peak-ccu"}), rawFeed);
});

test("maps API errors and retries server failures", async () => {
  let calls = 0;
  const client = new FortniteClient({ apiKey: "key", retries: 1, retryDelay: 0, fetch: async () => {
    calls++;
    return calls === 1 ? json({ msg: "try again" }, 503) : json({ ok: true });
  } });
  assert.deepEqual(await client.request("fortnite-ecosystem-metric", {"interval": "day", "metric": "in-client-peak-ccu"}), { ok: true });
  assert.equal(calls, 2);

  const bad = new FortniteClient({ fetch: async () => json({ msg: "bad input" }, 400) });
  await assert.rejects(bad.request("fortnite-ecosystem-metric", {"interval": "day", "metric": "in-client-peak-ccu"}), CrawloraClientError);
  const down = new FortniteClient({ fetch: async () => json({ msg: "down" }, 503) });
  await assert.rejects(down.request("fortnite-ecosystem-metric", {"interval": "day", "metric": "in-client-peak-ccu"}), CrawloraServerError);
});

test("reports timeout and caller cancellation as network errors", async () => {
  const hanging = (_url, { signal }) => new Promise((_resolve, reject) => {
    signal.addEventListener("abort", () => reject(new Error("aborted")), { once: true });
  });
  const timed = new FortniteClient({ timeout: 5, fetch: hanging });
  await assert.rejects(timed.request("fortnite-ecosystem-metric", {"interval": "day", "metric": "in-client-peak-ccu"}), CrawloraNetworkError);

  const controller = new AbortController();
  const aborted = new FortniteClient({ fetch: hanging });
  const pending = aborted.request("fortnite-ecosystem-metric", {"interval": "day", "metric": "in-client-peak-ccu"}, { signal: controller.signal });
  controller.abort();
  await assert.rejects(pending, CrawloraNetworkError);
});
