---
name: hrd-research
description: Use for Human Resource Development research in APA 7 style, including Scopus- and Semantic Scholar-supported article discovery, developing papers from scratch, building manuscripts from ideas or materials, manuscript drafting, paragraph revision, de-AI polishing to avoid generic AI vocabulary/rhythm/flow, strict in-text citation integrity, reference-list checking, citation-reference matching, APA 7 reference formatting, theory framing, literature synthesis, research questions, hypotheses, discussion sections, implications for HRD practice, journal fit for HRDQ, HRDR, ADHR, HRDI, and HRD research charts, graphs, tables, figure captions, visualization choices, and interpretation for workforce learning, training, organization development, adult learning, career development, and performance improvement research.
---

# HRD Research Router

This skill is split into two layers:

- A router layer: this `SKILL.md` plus `manifest.yaml`.
- A reusable guidance layer: shared files, core files, and fragments under `static/`.

Do not try to apply the full workflow from memory. Route the request, read the matching files, then revise or draft.

## Routing Protocol

### 1. Load The Manifest And Core Layer

Read `manifest.yaml`.

Then read every file listed under `always_load`. These files contain the APA, HRD domain, citation integrity, de-AI style guardrails, stance, workflow, and output rules that apply to every request.

### 2. Detect Axis Values

Use `manifest.yaml` to detect:

- `task`: literature-search, build-paper, polish, draft, restructure, review, visualize, interpret-visual, or table.
- `genre`: empirical, conceptual, review, methods, or generic.
- `section`: abstract, introduction, literature-review, theory, methods, rq-hypotheses, discussion, implications, conclusion, or reviewer-facing.
- `journal`: generic, hrdq, hrdr, adhr, or hrdi.
- `citation`: in-text-integrity, reference-list-check, citation-reference-match, or apa-reference-format.
- `visualization`: chart-choice, apa-figure, apa-table, code-guidance, or narrative.
- `paper-development`: motivation, architecture, evidence-bank, section-blueprint, or drafting-plan.

Default to `generic` when the user does not specify enough information. Ask only when the missing value changes the work in a consequential way.

State the detected values in one short line before the substantive output when doing a substantial revision or draft.

### 3. Load Matching Fragments

For each detected axis value, read the mapped file in `manifest.yaml`.

Load only the fragments needed for the request. Do not read every file under `static/`.

### 4. Apply Guidance In Priority Order

Apply the loaded material in this order:

1. Shared APA 7 and HRD domain guidance.
2. Core citation integrity rules.
3. Core de-AI style guardrails, especially for polish, revision, and restructuring.
4. Citation and reference-list guidance when the request involves references, bibliography, cited works, DOI, APA reference entries, or citation/reference matching.
5. Core stance, workflow, and output format.
6. Genre-specific expectations.
7. Section-specific structure and failure modes.
8. Journal-specific fit guidance.
9. Paper-development guidance when the request involves building a paper from an idea, notes, data, or materials.
10. Visualization guidance when the request involves graphs, charts, tables, captions, or figure interpretation.
11. The user's stated preferences.

Preserve the author's claims, citations, constructs, variables, sample details, research design, hypotheses, findings, and limitations unless the user explicitly asks for substantive rewriting.

### 5. Reach For References Only When Needed

When the user wants to connect an institutional or other research API, read `references/custom-api.md` for adapter, authentication, local-only installation, and verification guidance. Adding a key alone does not implement a new source.

Before the first article search in a conversation, read `references/api-setup.md`. Check key availability privately and offer setup for missing sources once. Users may skip setup and continue with available sources; ordinary writing does not require keys.

Use `references/revision-checklist.md` when revising or evaluating prose quality.

Use deeper references only when the user asks for detailed review, a checklist, or explicit diagnosis. If a needed reference does not exist yet, say what would be useful to add instead of inventing source-specific rules.

For article discovery, use the configured sources: Scopus (`SCOPUS_API_KEY`), Semantic Scholar (`SEMANTIC_SCHOLAR_API_KEY`), and Web of Science Starter (`WOS_API_KEY`). Read the corresponding `references/scopus-search.md`, `references/semantic-scholar-search.md`, or `references/wos-search.md` before querying. Treat search metadata as discovery evidence rather than proof of substantive claims; disclose unavailable sources.

## Output Rules

- If the user asks for direct revision, put the revised text first.
- Keep notes concise unless the user asks for detailed explanation.
- For revision, polish, and restructuring, run a de-AI pass: remove generic AI vocabulary, overly symmetrical rhythm, inflated transitions, and formulaic flow while preserving the author's intended voice.
- Do not invent citations, findings, journal policies, or reference details.
- Preserve APA in-text citation style unless the user asks to convert formats.
- Treat every source-dependent claim as needing an adjacent citation. If a revision moves, merges, splits, generalizes, or strengthens a cited sentence, move or duplicate the citation as needed and flag uncertain support.
- Do not let a paragraph-final citation appear to support claims that precede it unless the original text clearly uses that citation for the full claim sequence.
- For reference-list tasks, check both directions: every in-text citation should have a reference entry, and every reference entry should be cited or marked as uncited.
- For build-from-scratch requests, separate user-provided evidence from proposed argument structure; mark missing evidence as needed rather than filling it in.
- For graphs, charts, or tables, preserve the user's data and statistical meaning; do not invent values, labels, or relationships.
- Flag missing evidence, unsupported causal language, ambiguous constructs, inconsistent terminology, and claims that exceed the design.
