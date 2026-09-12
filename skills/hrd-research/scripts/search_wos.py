#!/usr/bin/env python3
"""Retrieve one page from the Web of Science Starter API."""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

ENDPOINT = "https://api.clarivate.com/apis/wos-starter/v1/documents"


def search(query, limit=10, page=1):
    key = os.environ.get("WOS_API_KEY", "").strip()
    if not key:
        raise RuntimeError("Set WOS_API_KEY to a Web of Science Starter API key before searching.")
    if not query.strip() or not 1 <= limit <= 50 or page < 1:
        raise ValueError("Supply a query, limit 1-50, and page >= 1.")
    params = {"q": query, "db": "WOS", "limit": limit, "page": page}
    request = urllib.request.Request(
        ENDPOINT + "?" + urllib.parse.urlencode(params),
        headers={"X-ApiKey": key, "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as exc:
        messages = {
            400: "Web of Science rejected the query or parameters.",
            401: "Web of Science rejected the API key.",
            403: "Web of Science Starter access requires an approved subscription.",
            429: "Web of Science rate or quota limit reached; stop and retry later.",
        }
        raise RuntimeError(messages.get(exc.code, f"Web of Science returned HTTP {exc.code}.")) from None
    except urllib.error.URLError:
        raise RuntimeError("Could not reach Web of Science; check network access.") from None
    except (ValueError, TimeoutError):
        raise RuntimeError("Web of Science returned invalid JSON or timed out.") from None
    if not isinstance(payload, dict) or not isinstance(payload.get("hits"), list):
        raise RuntimeError("Unexpected Web of Science response; expected a hits list.")
    return {
        "database": "Web of Science Core Collection (Starter API)",
        "searched_at": datetime.now(timezone.utc).isoformat(),
        "query": query,
        "requested_page": page,
        "requested_limit": limit,
        "metadata": payload.get("metadata", {}),
        "hits": payload["hits"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help='WoS query, e.g. TI=("workplace learning")')
    parser.add_argument("--limit", type=int, default=10, choices=range(1, 51), metavar="1-50")
    parser.add_argument("--page", type=int, default=1)
    args = parser.parse_args()
    if args.page < 1 or not args.query.strip():
        parser.error("Query must be nonempty and page must be >= 1.")
    try:
        result = search(args.query, args.limit, args.page)
    except (RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    # ASCII JSON escapes preserve Unicode across Windows console encodings.
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
