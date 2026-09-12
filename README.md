# HRD Research Skills

Codex skill pack for Human Resource Development research work.

This repository is designed as an expandable HRD research skill pack. It currently includes one installable skill, `hrd-research`, plus shared APA 7 and HRD domain references. The skill helps Codex develop papers from scratch, revise, draft, restructure, review, visualize, and interpret HRD research materials while preserving the author's meaning, citations, constructs, empirical claims, data integrity, and APA 7 social science style.

## Included Skill

```text
skills/
├── _shared/
│   ├── apa-7.md
│   └── hrd-domain.md
└── hrd-research/
    ├── SKILL.md
    ├── manifest.yaml
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   └── revision-checklist.md
    └── static/
        ├── core/
        └── fragments/
            ├── genre/
            ├── journal/
            ├── section/
            └── task/
```

## What `hrd-research` Supports

- Web of Science Starter article searches using a local `WOS_API_KEY`; request access at https://developer.clarivate.com/apis/wos-starter. API access must be approved before live searches can run.

- HRD manuscript drafting, revision, restructuring, and review
- Scopus- and Semantic Scholar-supported scholarly article discovery and metadata retrieval
- Paper development from ideas, notes, data, findings, or rough materials
- Motivation, paper architecture, evidence-bank, section-blueprint, and drafting-plan support
- De-AI polishing to reduce generic AI vocabulary, rhythm, and flow
- Strict in-text citation integrity and claim-to-citation checking
- Reference-list checking, APA 7 reference formatting, and citation-reference matching
- APA 7 social science style polishing
- Literature review synthesis
- Theory framing and conceptual contribution
- Research questions and hypotheses
- Abstracts, introductions, methods, discussions, conclusions, and reviewer-facing text
- HRD practice implications
- Journal fit for HRDQ, HRDR, ADHR, and HRDI
- HRD research graphs, charts, tables, figure captions, and visual interpretation
- Cautious social science claims for correlational, qualitative, cross-sectional, or exploratory designs

## How The Skill Works

`hrd-research` uses a router-style structure inspired by Nature-style skill packs:

1. `SKILL.md` routes the request.
2. `manifest.yaml` detects the task, genre, section, and journal.
3. The skill loads only the relevant files from `static/`.
4. Shared APA 7 and HRD domain guidance stays in `skills/_shared/`.

The current router axes are:

- `task`: literature-search, build-paper, polish, draft, restructure, review, visualize, interpret-visual, table
- `genre`: empirical, conceptual, review, methods, generic
- `section`: abstract, introduction, literature-review, theory, methods, rq-hypotheses, discussion, implications, conclusion, reviewer-facing
- `journal`: generic, HRDQ, HRDR, ADHR, HRDI
- `citation`: in-text-integrity, reference-list-check, citation-reference-match, apa-reference-format
- `visualization`: chart-choice, apa-figure, apa-table, code-guidance, narrative
- `paper-development`: motivation, architecture, evidence-bank, section-blueprint, drafting-plan

## Install For Codex

Clone the repository, then copy the full skill folder and shared references:

```bash
git clone https://github.com/lihanwen1012-wq/hrd-research-skills.git
cd hrd-research-skills

mkdir -p ~/.codex/skills
cp -R skills/_shared ~/.codex/skills/
cp -R skills/hrd-research ~/.codex/skills/
```

Start a fresh Codex session after copying.

On the first article-search request in a conversation, the skill checks which API keys are configured and offers setup instructions for missing sources. Users can skip setup and continue with available sources or public web search. Downloading the repository itself does not launch a setup prompt.

Each user supplies their own keys through `SCOPUS_API_KEY`, `SEMANTIC_SCHOLAR_API_KEY`, and/or `WOS_API_KEY`. Keys are optional for ordinary writing and are never bundled in GitHub downloads. See [private API setup](skills/hrd-research/references/api-setup.md) for provider links and configuration instructions. Never paste keys into chat or tracked files.

## Use In Codex

Invoke the skill explicitly with `$hrd-research`:

```text
Use $hrd-research to revise this HRD literature review paragraph for APA 7 style and HRDI fit:
[paste paragraph]
```

More examples:

```text
Use $hrd-research to draft an abstract for an empirical HRD study targeting HRDQ.
```

```text
Use $hrd-research to restructure this literature review so it synthesizes instead of listing studies.
```

```text
Use $hrd-research to review this conceptual manuscript introduction for HRDR fit.
```

```text
Use $hrd-research to strengthen these HRD practice implications without overclaiming from correlational findings.
```

```text
Use $hrd-research to help me develop an HRD paper from scratch. I have a topic, rough findings, and a possible target journal.
```

```text
Use $hrd-research to create a motivation statement, paper architecture, and section blueprint for a conceptual HRD paper.
```

```text
Use $hrd-research to check whether my in-text citations match my reference list and flag APA 7 reference issues.
```

```text
Use $hrd-research to revise this paragraph with a de-AI pass while preserving my meaning and citations.
```

```text
Use $hrd-research to recommend the best chart for these training transfer results and write an APA-style figure note.
```

```text
Use $hrd-research to interpret this interaction plot for an HRDQ discussion section.
```

## Update Local Codex Install

After pulling repository updates:

```bash
git pull
cp -R skills/_shared ~/.codex/skills/
cp -R skills/hrd-research ~/.codex/skills/
```

Start a fresh Codex session so the updated skill is discovered.

## Full Installation Guide

See [install.md](install.md) for Codex, Claude Code, other-agent, update, and troubleshooting instructions.
