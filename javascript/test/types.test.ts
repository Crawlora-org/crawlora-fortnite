import { FortniteClient } from "../src/index.js";

const client = new FortniteClient({ apiKey: "test-key" });
void client.ecosystemMetric({"interval": "day", "metric": "in-client-peak-ccu"});
void client.request("fortnite-ecosystem-metric", {"interval": "day", "metric": "in-client-peak-ccu"});
const streamResponse: Promise<Response> = client.request("fortnite-ecosystem-metric", {"interval": "day", "metric": "in-client-peak-ccu"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("fortnite-ecosystem-metric", {"interval": "day", "metric": "in-client-peak-ccu"}, { responseType: "stream" });
const directStream: Promise<Response> = client.ecosystemMetric({"interval": "day", "metric": "in-client-peak-ccu"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("fortnite-ecosystem-metric", {"interval": "day", "metric": "in-client-peak-ccu", "from": "sample", "to": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("fortnite-ecosystem-metric", {"interval": "day", "metric": "in-client-peak-ccu"}, { responseType: "text" });
void rawText;


void client.enums();
void client.request("fortnite-enums");
// @ts-expect-error The selected operation requires its documented params.
void client.ecosystemMetric();
