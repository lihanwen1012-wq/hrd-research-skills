# HRD Research Skills

Codex skill pack for Human Resource Development research work.

This repository is designed as an expandable HRD research skill pack. It currently includes one installable skill, `hrd-research`, plus shared APA 7 and HRD domain references. The first skill helps Codex revise and draft HRD manuscript text while preserving the author's meaning, citations, constructs, empirical claims, and APA 7 social science style.

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
```

## What `hrd-research` Supports

- HRD manuscript drafting and revision
- APA 7 style polishing
- Literature review synthesis
- Theory framing
- Research questions and hypotheses
- Discussion sections
- HRD practice implications
- Journal fit for HRDQ, HRDR, ADHR, and HRDI
- Cautious social science claims for correlational, qualitative, cross-sectional, or exploratory designs

## Install For Codex

From the repository root:

```bash
mkdir -p ~/.codex/skills
cp -R skills/_shared ~/.codex/skills/
cp -R skills/hrd-research ~/.codex/skills/
```

Start a fresh Codex session after copying.

## Verify

Ask Codex for an HRD research writing task:

```text
Revise this HRD literature review paragraph in APA 7 style.
```

Codex should use the HRD research workflow, preserve citations and meaning, and avoid generic academic polishing.

## Full Installation Guide

See [install.md](install.md) for Codex, Claude Code, other-agent, update, and troubleshooting instructions.
