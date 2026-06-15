# HRD Research Skills

Codex skill pack for Human Resource Development research work.

This repository is designed as an expandable HRD research skill pack. It currently includes one installable skill, `hrd-research`, plus shared APA 7 and HRD domain references. The skill helps Codex revise, draft, restructure, and review HRD manuscript text while preserving the author's meaning, citations, constructs, empirical claims, and APA 7 social science style.

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

- HRD manuscript drafting, revision, restructuring, and review
- APA 7 social science style polishing
- Literature review synthesis
- Theory framing and conceptual contribution
- Research questions and hypotheses
- Abstracts, introductions, methods, discussions, conclusions, and reviewer-facing text
- HRD practice implications
- Journal fit for HRDQ, HRDR, ADHR, and HRDI
- Cautious social science claims for correlational, qualitative, cross-sectional, or exploratory designs

## How The Skill Works

`hrd-research` uses a router-style structure inspired by Nature-style skill packs:

1. `SKILL.md` routes the request.
2. `manifest.yaml` detects the task, genre, section, and journal.
3. The skill loads only the relevant files from `static/`.
4. Shared APA 7 and HRD domain guidance stays in `skills/_shared/`.

The current router axes are:

- `task`: polish, draft, restructure, review
- `genre`: empirical, conceptual, review, methods, generic
- `section`: abstract, introduction, literature-review, theory, methods, rq-hypotheses, discussion, implications, conclusion, reviewer-facing
- `journal`: generic, HRDQ, HRDR, ADHR, HRDI

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
