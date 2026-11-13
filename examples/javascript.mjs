import { FortniteClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new FortniteClient({ apiKey });

  const genres = await client.genres({  });
  console.log("genres", genres);
  const islands = await client.islands({ size: 5 });
  console.log("islands", islands);
