#!/usr/bin/env python3
"""Search Semantic Scholar and emit compact, citation-safe JSON metadata."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


ENDPOINT = "https://api.semanticscholar.org/graph/v1/paper/search"
FIELDS = (
    "paperId,corpusId,title,authors,year,publicationDate,venue,journal,"
    "externalIds,abstract,citationCount,referenceCount,influentialCitationCount,"
    "publicationTypes,openAccessPdf,url"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Plain-text Semantic Scholar relevance query")
    parser.add_argument("--limit", type=int, default=20, choices=range(1, 101), metavar="1-100")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--year", help="Optional year or range, for example 2020-2026")
    parser.add_argument(
        "--fields-of-study",
        help="Optional comma-separated fields, for example Business,Psychology",
    )
    parser.add_argument("--open-access", action="store_true", help="Require an open-access PDF")
    parser.add_argument("--raw", action="store_true", help="Print the complete API response")
    args = parser.parse_args()
    if args.offset < 0:
        parser.error("--offset must be zero or greater")
    return args


def request_json(args: argparse.Namespace) -> dict:
    api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
    if not api_key:
        raise RuntimeError("SEMANTIC_SCHOLAR_API_KEY is not set")

    params = {
        "query": args.query,
        "limit": str(args.limit),
        "offset": str(args.offset),
        "fields": FIELDS,
    }
    if args.year:
        params["year"] = args.year
    if args.fields_of_study:
        params["fieldsOfStudy"] = args.fields_of_study
    if args.open_access:
        params["openAccessPdf"] = ""

    request = urllib.request.Request(
        f"{ENDPOINT}?{urllib.parse.urlencode(params)}",
        headers={
            "Accept": "application/json",
            "x-api-key": api_key,
            "User-Agent": "hrd-research-skill/2.7",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        detail = exc.read(1000).decode("utf-8", errors="replace").strip()
        messages = {
            401: "Semantic Scholar authentication failed; check the API key.",
            403: "Semantic Scholar access was denied; the key may lack access.",
            429: "Semantic Scholar rate limit was exceeded; stop and retry later.",
        }
        message = messages.get(exc.code, f"Semantic Scholar returned HTTP {exc.code}.")
        if detail:
            message = f"{message} Response: {detail}"
        raise RuntimeError(message) from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach Semantic Scholar: {exc.reason}") from exc


def compact(payload: dict, query: str) -> dict:
    papers = []
    for paper in payload.get("data", []):
        external_ids = paper.get("externalIds") or {}
        journal = paper.get("journal") or {}
        authors = [author.get("name") for author in paper.get("authors") or [] if author.get("name")]
        papers.append(
            {
                "title": paper.get("title"),
                "authors": authors,
                "year": paper.get("year"),
                "publication_date": paper.get("publicationDate"),
                "venue": paper.get("venue"),
                "journal": journal.get("name"),
                "doi": external_ids.get("DOI"),
                "paper_id": paper.get("paperId"),
                "corpus_id": paper.get("corpusId"),
                "publication_types": paper.get("publicationTypes"),
                "citation_count": paper.get("citationCount"),
                "influential_citation_count": paper.get("influentialCitationCount"),
                "reference_count": paper.get("referenceCount"),
                "abstract": paper.get("abstract"),
                "open_access_pdf": paper.get("openAccessPdf"),
                "url": paper.get("url"),
            }
        )

    return {
        "query": query,
        "total_results": payload.get("total"),
        "offset": payload.get("offset"),
        "next_offset": payload.get("next"),
        "papers": papers,
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
