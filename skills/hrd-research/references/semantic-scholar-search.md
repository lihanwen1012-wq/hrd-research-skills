# Semantic Scholar Article Search

Use the Semantic Scholar Academic Graph API for scholarly discovery when `SEMANTIC_SCHOLAR_API_KEY` is available.

## Access And Secret Handling

- Read the key only from the `SEMANTIC_SCHOLAR_API_KEY` environment variable.
- Send it only in the case-sensitive `x-api-key` header. Never place it in a URL, prompt, output, source file, citation, log, or tracked configuration.
- Do not reveal the credential while diagnosing failures.
- If access returns 401 or 403, stop and explain that the API key was rejected or lacks access.
- If access returns 429, stop and report the rate limit. Do not retry rapidly; introductory authenticated access is normally limited to one request per second.

## Search Method

The bundled helper uses the relevance-search endpoint:

```text
python scripts/search_semantic_scholar.py "workplace learning training transfer" --limit 20 --year 2020-2026
```

Semantic Scholar relevance search accepts a plain-text query and does not support special Boolean query syntax. Use concise construct names and synonyms in natural language. Hyphenated search terms may fail to match, so replace hyphens with spaces when appropriate.

Use `--year`, `--fields-of-study`, and `--open-access` only when they reflect the research question. For additional pages, pass the response's `next` value as `--offset`. Record the exact query, filters, search date, total results, and pages retrieved.

Request only fields needed for screening. The helper returns stable paper and corpus identifiers, DOI when available, bibliographic metadata, citation counts, abstract, and open-access PDF metadata.

## Combining With Scopus

- Use one database when the request is narrow and the selected source is adequate; use both when broader recall, cross-checking, or transparent multi-database discovery matters.
- Keep source-specific queries and result counts separate because Scopus and Semantic Scholar have different coverage, ranking, and query behavior.
- Merge results by DOI first, then by normalized title and publication year. Preserve database-specific identifiers.
- Do not add citation counts from the two databases; label which database supplied each count.

## Evidence Boundaries

Semantic Scholar results and abstracts support discovery and screening, not automatic citation of substantive claims.

- Inspect the original abstract or full text before describing findings, theory, methods, samples, or limitations.
- Verify bibliographic details against the DOI record or publisher page when accuracy matters.
- Treat AI-generated or database-provided summaries as leads rather than authoritative evidence.
- Label inaccessible full text and avoid inferring results from titles, abstracts, citation counts, or snippets.
- For comprehensive work, name all databases searched and avoid claiming exhaustive coverage unless the protocol supports it.

Official documentation:

- Semantic Scholar API overview: https://www.semanticscholar.org/product/api
- Academic Graph API: https://api.semanticscholar.org/api-docs/graph
- API tutorial and rate-limit guidance: https://www.semanticscholar.org/product/api/tutorial
