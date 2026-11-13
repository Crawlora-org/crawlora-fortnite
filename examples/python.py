import os

from crawlora_fortnite import FortniteClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with FortniteClient(api_key=api_key) as client:
    genres = client.genres()
    print('genres', genres)
    islands = client.islands(size=5)
    print('islands', islands)
