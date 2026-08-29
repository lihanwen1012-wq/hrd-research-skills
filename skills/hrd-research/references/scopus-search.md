# Scopus Article Search

Use Scopus for scholarly article discovery when `SCOPUS_API_KEY` is available.

## Access And Secret Handling

- Read the API key only from the `SCOPUS_API_KEY` environment variable.
- Optionally read an institutional token from `SCOPUS_INSTTOKEN`.
- Send credentials in the `X-ELS-APIKey` and `X-ELS-Insttoken` headers. Never place them in a URL, prompt, output, source file, citation, log, or tracked configuration.
- Do not reveal credential values while diagnosing failures.
- If access returns 401 or 403, explain that the key, institutional entitlement, or network context may be insufficient. Do not repeatedly retry.
- If access returns 429, stop and report that the quota was exceeded.

## Search Method

The bundled helper is `scripts/search_scopus.py`:

```text
python scripts/search_scopus.py "TITLE-ABS-KEY(\"training transfer\" AND workplace)" --count 20 --sort relevancy
```

Build a query from the user's constructs and plausible synonyms. Prefer fielded clauses such as `TITLE-ABS-KEY(...)`, combine synonyms with `OR`, combine concepts with `AND`, and use `AND NOT` only when an exclusion is defensible. Use Scopus date, subject, or open-access filters only when they reflect the research question.

For multi-page searches, increment `--start` by the returned page size. Record the exact query, filters, search date, total result count, and pages retrieved so the search can be reproduced.

## Evidence Boundaries

Scopus search results are metadata for discovery and screening. A title, keyword list, abstract snippet, citation count, or database index entry does not establish that a paper supports a substantive claim.

- Verify bibliographic details against the DOI record or publisher page when accuracy matters.
- Inspect the abstract or full text before summarizing findings, theory, methods, sample, or limitations.
- Label inaccessible full text and avoid inferring results from metadata.
- Deduplicate by DOI, then by normalized title and year.
- For systematic or comprehensive work, report Scopus as one searched database and avoid claiming exhaustive coverage unless the protocol supports that claim.

Official documentation:

- Scopus Search API: https://dev.elsevier.com/documentation/SCOPUSSearchAPI.wadl
- Scopus search syntax: https://dev.elsevier.com/sc_search_tips.html
- Elsevier API authentication: https://dev.elsevier.com/tecdoc_api_authentication.html
