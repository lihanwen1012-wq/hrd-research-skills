# Literature Search

Use this fragment when the user wants to find, identify, map, or screen scholarly articles.

Before querying, follow `../../../references/api-setup.md`: privately check configured sources and offer setup once for missing keys. Respect the user's choice to skip setup and disclose the sources actually searched.

Web of Science Starter is also available through `../../../references/wos-search.md` and `scripts/search_wos.py` (relative to the skill root) when `WOS_API_KEY` is set. Include it when the user requests WoS or when broader discovery merits another configured database. Apply the same evidence and deduplication rules below to all three sources; retain WoS UID and label source-specific counts.

1. Translate the research question into concepts, synonyms, and explicit inclusion boundaries.
2. Read `../../../references/scopus-search.md` and `../../../references/semantic-scholar-search.md`. Use Scopus, Semantic Scholar, or both when their API-key environment variables are available. For broader discovery, searching both can improve coverage; report each database separately.
3. Match the query syntax to the database: use reproducible fielded Scopus searches such as `TITLE-ABS-KEY(...)`, but use plain-language concepts for Semantic Scholar relevance search. Preserve each exact query, filters, search date, total results, and pagination used.
4. Return article metadata with stable identifiers (especially DOI and Scopus EID) and distinguish database metadata from claims verified in an abstract or full text.
5. Deduplicate by DOI first, then by normalized title and publication year.
6. Do not cite an article as support for a substantive claim based only on its title, keywords, citation count, or search-result metadata.

When the user needs a comprehensive or systematic search, treat Scopus and Semantic Scholar as named databases rather than implying that either exhausts the literature. Report database coverage and access limitations.
