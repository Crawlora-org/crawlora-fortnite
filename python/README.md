# crawlora-fortnite — Fortnite API client for Python

Python client for Crawlora's hosted Fortnite API. It exposes 10 API endpoints covering public island discovery, genres, rankings, and engagement metrics. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-python-homepage); the package does not run a browser or scrape
Fortnite locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Fortnite or its owners.

## Install

```sh
python -m pip install crawlora-fortnite
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_fortnite import FortniteClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with FortniteClient(api_key=api_key) as client:
    result_1 = client.genres()
    print(result_1)
    result_2 = client.islands(size=5)
    print(result_2)
```

The package also exports `Client` as an alias for `FortniteClient`. Operation
methods are available directly in snake_case and through the `fortnite`
group. The async package client is `AsyncFortniteClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-fortnite/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-fortnite/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_fortnite import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.genres()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-fortnite/blob/main/examples/python.py) for a complete usage example.

## Supported Fortnite API endpoints

This package exposes every route below through direct snake_case methods and the `fortnite` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-fortnite/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/fortnite/ecosystem-metric` | `fortnite-ecosystem-metric` | Get one Fortnite ecosystem metric |
| `GET` | `/fortnite/ecosystem-metrics` | `fortnite-ecosystem-metrics` | Get Fortnite ecosystem metrics |
| `GET` | `/fortnite/enums` | `fortnite-enums` | List Fortnite metric enums |
| `GET` | `/fortnite/genre-rankings` | `fortnite-genre-rankings` | Get rankings for a Fortnite genre |
| `GET` | `/fortnite/genres` | `fortnite-genres` | List Fortnite genres |
| `GET` | `/fortnite/island` | `fortnite-island` | Get a Fortnite island |
| `GET` | `/fortnite/island-metric` | `fortnite-island-metric` | Get one Fortnite island metric |
| `GET` | `/fortnite/island-metrics` | `fortnite-island-metrics` | Get Fortnite island metrics |
| `GET` | `/fortnite/island-rankings` | `fortnite-island-rankings` | Get Fortnite island rankings |
| `GET` | `/fortnite/islands` | `fortnite-islands` | Discover Fortnite islands |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
