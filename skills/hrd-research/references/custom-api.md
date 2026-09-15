# Connect an institutional or other research API

You can extend HRD Research with your university's research repository, researcher directory, library discovery service, or another scholarly API. An additional source needs its own adapter and instructions; adding an API key alone does not connect it. Choose a source whose coverage fits your question.

## 1. Identify the service and access requirements

Find the provider's official API documentation or ask your library's research/data services team for it. Confirm:

- What can be searched: publications, researchers, datasets, catalog records, or full text?
- Which HTTPS endpoint, query syntax, filters, and pagination does the API use?
- Is public access available, or does it require an API key, OAuth, institutional network, or separate approval?
- What are its request limits and conditions for storing or sharing returned data?

Library website access does not establish API access or permission to download full text. A researcher directory may contain only institution-associated publications. Do not assume a library login or a key for one product works with another.

## 2. Choose where the extension lives

For a personal extension, work in the **installed skill folder**, outside the Git checkout. Add, for example:

```text
hrd-research/
  references/my-institution.md
  scripts/search_my_institution.py
```

Add a short route in the installed `SKILL.md` telling the agent when to read the new reference. Keep a private backup of these files and that route outside the repository: reinstalling the public skill can overwrite local edits. Mark them as local-only so future maintenance does not copy them into a public commit.

For an extension you intend to share, use the repository's corresponding `skills/hrd-research/` paths and include only provider documentation, code, and placeholder configuration. Confirm that provider terms allow sharing the adapter and any examples. Never bundle credentials, internal endpoints, or restricted records.

## 3. Configure authentication privately

Public APIs may need no credentials. For a key-based service, choose a dedicated environment variable such as `MY_INSTITUTION_API_KEY` and follow [private API setup](api-setup.md). Read it at runtime and use the authentication method documented by that provider. Do not reuse another service's key. OAuth requires the provider's approved sign-in flow and token handling; a static API-key helper is not sufficient.

Tell the agent the documentation URL, desired source, and variable **name**. Enter the actual credential only in local environment or secret settings. Missing credentials should disable only that source.

## 4. Build a small adapter and route it

Use the existing `scripts/search_wos.py`, `scripts/search_scopus.py`, or `scripts/search_semantic_scholar.py` as structural examples, not as interchangeable clients. Adapt the endpoint, authentication, parameter names, pagination, and response parsing to the chosen API. Use URL encoding, bounded pages, timeouts, and clear error messages without exposing credentials. Avoid automatic bulk retrieval or unbounded retries.

The new reference should describe coverage, configuration, query examples, page handling, evidence limitations, and official documentation. In `SKILL.md`, add a route such as:

```text
For institution-specific researcher or publication searches, read
references/my-institution.md and use scripts/search_my_institution.py.
```

Add an entry under the existing `references.on_demand` list in `manifest.yaml`:

```yaml
    - condition: searching the institution's publications or researchers
      path: references/my-institution.md
```

Extend the API setup instructions to check the new variable privately only when this source needs credentials. Do not make an optional institutional service mandatory for every user or every search.

Preserve source name, exact query, retrieval date, stable record IDs/URLs, DOI when available, and pagination. Keep missing fields unknown; do not invent authors or publication details. When combining sources, deduplicate by DOI, then title/year, retain provenance, and label citation counts by database. Verify article claims against the original source.

## 5. Verify before relying on it

Run one small search for a known record and inspect its title, identifier, source link, and relevance. Check an empty result, a second page if supported, and missing-key/error handling. Do not claim live access when only simulated tests have run. Record access limits and any untested behavior. Before publishing, inspect the complete commit for credentials, private URLs, and restricted sample data.

## Copyable request for your agent

```text
Extend my installed HRD Research skill with my institution's research API.
Official API documentation: [URL]
Search purpose: [publications / researchers / datasets / other]
Authentication: [public / API key / OAuth / unknown]
Environment variable name, if applicable: MY_INSTITUTION_API_KEY
Keep this extension local; do not change or push the public GitHub repository.
Read the provider's documentation, add a bounded search adapter and routing
instructions, and test one small search if access is available. Do not ask
me to paste credentials into chat. Preserve existing research sources.
```
