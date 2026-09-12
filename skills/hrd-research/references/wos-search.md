# Web of Science Starter Search

Use `scripts/search_wos.py` when `WOS_API_KEY` is available. This helper supports Starter only; Expanded uses a different API and subscription. If no key is configured, report that WoS is unavailable and continue with the other configured databases.

Request Starter access by registering an application at https://developer.clarivate.com/apis/wos-starter. Store the approved key locally as `WOS_API_KEY`; never commit, print, or put it in a request URL. Authentication uses the `X-ApiKey` header over HTTPS. A website subscription alone does not establish API access.

Example (from the skill directory):

```text
python scripts/search_wos.py 'TI=("workplace learning")' --limit 10 --page 1
```

Use WoS field tags: TI for title, TS for topic, DO for DOI, and PY for year; translate the research concepts into WoS syntax. Keep title-only searches labeled as such. The helper targets the Core Collection (`db=WOS`), returns one page, and preserves the provider's `hits` and `metadata` along with the query and UTC search time. Page numbering starts at 1; limit is 1-50. Use metadata.total, page, limit and returned hits to determine whether another page is needed. Retrieve only the scope required by the task; do not imply a first-page search is exhaustive.

Stop on authentication, entitlement, or quota errors. Do not automatically retry or evade limits. Space repeated requests according to the approved plan. The free plan may omit citation counts; absent counts are unknown, not zero. Starter bibliographic results do not guarantee abstracts or full text. Inspect source content before making substantive claims.

When combining databases, keep queries, counts, and identifiers separate. Deduplicate by DOI first, then title/year; retain WoS UID. Label citation counts by source and never add counts across databases. Report the databases actually queried and any access gaps.

Official references:
- https://developer.clarivate.com/apis/wos-starter
- https://github.com/clarivate/wosstarter_python_client/blob/master/docs/DocumentsApi.md
