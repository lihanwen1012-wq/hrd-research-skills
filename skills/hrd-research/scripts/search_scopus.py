#!/usr/bin/env python3
"""Search Scopus and emit compact, citation-safe JSON metadata."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


ENDPOINT = "https://api.elsevier.com/content/search/scopus"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Scopus Boolean query, ideally fielded with TITLE-ABS-KEY")
    parser.add_argument("--count", type=int, default=20, choices=range(1, 26), metavar="1-25")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument(
        "--sort",
        default="relevancy",
        choices=("relevancy", "citedby-count", "coverDate", "pubyear"),
    )
    parser.add_argument("--date", help="Optional year or range, for example 2020-2026")
    parser.add_argument("--subject", help="Optional Scopus subject code, for example BUSI, PSYC, or SOCI")
    parser.add_argument("--raw", action="store_true", help="Print the complete API response")
    args = parser.parse_args()
    if args.start < 0:
        parser.error("--start must be zero or greater")
    return args


def request_json(args: argparse.Namespace) -> dict:
    api_key = os.environ.get("SCOPUS_API_KEY")
    if not api_key:
        raise RuntimeError("SCOPUS_API_KEY is not set")

    params = {
        "query": args.query,
        "count": str(args.count),
        "start": str(args.start),
        "sort": args.sort,
        "view": "STANDARD",
        "suppressNavLinks": "true",
    }
    if args.date:
        params["date"] = args.date
    if args.subject:
        params["subj"] = args.subject

    headers = {
        "Accept": "application/json",
        "X-ELS-APIKey": api_key,
        "User-Agent": "hrd-research-skill/2.6",
    }
    insttoken = os.environ.get("SCOPUS_INSTTOKEN")
    if insttoken:
        headers["X-ELS-Insttoken"] = insttoken

    request = urllib.request.Request(
        f"{ENDPOINT}?{urllib.parse.urlencode(params)}", headers=headers
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        detail = exc.read(1000).decode("utf-8", errors="replace").strip()
        messages = {
            401: "Scopus authentication failed; check the API key.",
            403: "Scopus access was denied; the key or current network may lack entitlement.",
            429: "Scopus quota was exceeded; stop and try after the quota resets.",
        }
        message = messages.get(exc.code, f"Scopus returned HTTP {exc.code}.")
        if detail:
            message = f"{message} Response: {detail}"
        raise RuntimeError(message) from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach Scopus: {exc.reason}") from exc


def compact(payload: dict, query: str) -> dict:
    results = payload.get("search-results", {})
    entries = results.get("entry", [])
    if isinstance(entries, dict):
        entries = [entries]

    articles = []
    for entry in entries:
        if entry.get("error"):
            continue
        articles.append(
            {
                "title": entry.get("dc:title"),
                "authors": entry.get("dc:creator"),
                "year": (entry.get("prism:coverDate") or "")[:4] or None,
                "publication": entry.get("prism:publicationName"),
                "doi": entry.get("prism:doi"),
                "eid": entry.get("eid"),
                "document_type": entry.get("subtypeDescription"),
                "cited_by": entry.get("citedby-count"),
                "open_access": entry.get("openaccessFlag"),
            }
        )

    return {
        "query": query,
        "total_results": results.get("opensearch:totalResults"),
        "start_index": results.get("opensearch:startIndex"),
        "items_per_page": results.get("opensearch:itemsPerPage"),
        "articles": articles,
    }


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = parse_args()
    try:
        payload = request_json(args)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    output = payload if args.raw else compact(payload, args.query)
    json.dump(output, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
