# HRD Research Skills Installation Guide

This file explains how to install the HRD research skills in this repository so they are usable in Codex and other coding agents.

The most important point is simple:

- `hrd-research-skills` is not a Python package or npm package.
- Each `skills/hrd-*` folder is one reusable skill unit.
- In most cases, copy or reference the entire skill folder, not only `SKILL.md`.
- `skills/_shared/` contains shared support content used by HRD research skills.

Why that matters:

- HRD research skills can depend on `references/`.
- Some skills read shared APA or HRD domain guidance from `../_shared`.
- Copying only `SKILL.md` can silently break the workflow.

---

## 1. What Gets Installed

Each installable skill lives under `skills/` and is centered on `SKILL.md`.

Current structure:

```text
skills/
├── _shared/
│   ├── apa-7.md
│   └── hrd-domain.md
└── hrd-writing/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        └── revision-checklist.md
```

If you want one skill, install one folder plus `skills/_shared`. If you want the full collection, install `skills/_shared` plus all `skills/hrd-*` folders.

---

## 2. Quick Choice

Choose the path that matches your agent:

- Codex local skills: best if you want direct folder copying.
- Claude Code wrappers: best if you prefer terminal-based agent workflows pinned to a local clone path.
- Other agents: use the whole skill folder as a reusable prompt bundle.

---

## 3. Install For Codex

Codex can use local skill folders directly.

### 3.1 Manual Local-Skill Installation

Clone or download this repository, then enter it:

```bash
git clone <this-repository-url>
cd hrd-research-skills
```

If you already have this folder locally, just run the install commands from the repository root.

### 3.2 Install One Skill

Example: install `hrd-writing`.

```bash
mkdir -p ~/.codex/skills
cp -R skills/_shared ~/.codex/skills/
cp -R skills/hrd-writing ~/.codex/skills/
```

Copying `_shared` is intentional. It preserves shared APA 7 and HRD domain references used by the skill.

### 3.3 Install All Current Skills

```bash
mkdir -p ~/.codex/skills
cp -R skills/_shared ~/.codex/skills/
for d in skills/hrd-*; do cp -R "$d" ~/.codex/skills/; done
```

### 3.4 Verify

Start a fresh Codex session and ask for a task that clearly matches the skill, for example:

```text
Revise this HRD literature review paragraph in APA 7 style.
```

or:

```text
Strengthen these HRD practice implications without overclaiming from correlational findings.
```

If the skill is discovered correctly, Codex should use the HRD writing workflow, preserve citations and meaning, apply APA 7 social science style, and avoid generic academic polishing.

### 3.5 Update Later

When this repository changes:

```bash
cd /path/to/hrd-research-skills
git pull
cp -R skills/_shared ~/.codex/skills/
cp -R skills/hrd-writing ~/.codex/skills/
```

If you installed all skills, re-copy `skills/_shared` and all `skills/hrd-*` folders after pulling:

```bash
cp -R skills/_shared ~/.codex/skills/
for d in skills/hrd-*; do cp -R "$d" ~/.codex/skills/; done
```

### 3.6 Common Codex Mistake

Do not do this:

```bash
cp skills/hrd-writing/SKILL.md ~/.codex/skills/
```

That copies only one file and drops the rest of the skill bundle.

Use this instead:

```bash
cp -R skills/_shared ~/.codex/skills/
cp -R skills/hrd-writing ~/.codex/skills/
```

---

## 4. Install For Claude Code

Claude Code can use this repository through a thin wrapper that points to a stable local clone path.

### 4.1 Install Claude Code First

If you have not installed Claude Code yet:

```bash
npm install -g @anthropic-ai/claude-code
claude
```

### 4.2 Clone This Repository To A Stable Local Path

Example:

```bash
mkdir -p ~/ai-skills
cd ~/ai-skills
git clone <this-repository-url> hrd-research-skills
```

In the examples below, the repository path is:

```text
~/ai-skills/hrd-research-skills
```

If you use a different path, replace it consistently.

### 4.3 Recommended Wrapper Method: Create A Subagent

Create a user-level subagent:

```bash
mkdir -p ~/.claude/agents
cat > ~/.claude/agents/hrd-writing.md <<'EOF'
---
name: hrd-writing
description: Use proactively for Human Resource Development academic writing, APA 7 manuscript revision, HRD theory framing, literature synthesis, research questions, hypotheses, discussion sections, and implications for HRD practice.
---

When invoked, first read `~/ai-skills/hrd-research-skills/skills/hrd-writing/SKILL.md`. Treat that file as the governing workflow.

If the skill references supporting files, read only the specific files you need from `~/ai-skills/hrd-research-skills/skills/hrd-writing/` and `~/ai-skills/hrd-research-skills/skills/_shared/`. Do not replace the skill with generic academic polishing.
EOF
```

Then start a new Claude Code session and ask:

```text
Use the hrd-writing subagent to revise this HRD discussion section.
```

### 4.4 Alternative Wrapper Method: Create A Slash Command

If you prefer a command instead of a subagent:

```bash
mkdir -p ~/.claude/commands
cat > ~/.claude/commands/hrd-writing.md <<'EOF'
Read `~/ai-skills/hrd-research-skills/skills/hrd-writing/SKILL.md` first and follow it strictly. Read any directly needed supporting files from `~/ai-skills/hrd-research-skills/skills/hrd-writing/` and `~/ai-skills/hrd-research-skills/skills/_shared/`.

$ARGUMENTS
EOF
```

Then inside Claude Code:

```text
/hrd-writing Revise this HRD literature review paragraph in APA 7 style.
```

### 4.5 Why Wrappers Are Better Than Copying Only `SKILL.md`

This repository is designed as a folder-based skill pack. If you only copy `SKILL.md` into `~/.claude/agents/` and leave the rest behind:

- relative supporting material is no longer colocated
- shared APA 7 and HRD domain references are missing
- future updates are harder to reuse
- the skill becomes incomplete in practice

Keeping the repository cloned and pointing Claude Code at the real folder is more robust.

### 4.6 Update Later

```bash
cd ~/ai-skills/hrd-research-skills
git pull
```

If your wrapper points to this stable clone path, no further reinstall step is needed.

---

## 5. Install For Other Agents

If your agent supports reusable prompt folders, profile files, or custom system prompts, use the real skill directory under `skills/` as the portable unit:

```text
skills/
├── _shared/
└── hrd-writing/
    ├── SKILL.md
    ├── agents/
    └── references/
```

Recommended rule:

1. Copy the full skill directory.
2. Preserve `SKILL.md`, `agents/`, `references/`, scripts, assets, and any needed `skills/_shared/` files together.
3. Adapt only the outer wrapper format required by the target agent.

---

## 6. Which Method Should You Use?

Use Codex if:

- you want to copy folders into `~/.codex/skills/` and use them directly
- you want Codex to auto-discover the skill in fresh sessions

Use Claude Code if:

- you already work in Claude Code
- you are comfortable using subagents or slash commands as wrappers

Use manual folder reuse if:

- your agent has no native skill system
- you still want the HRD writing rules, references, and workflow as a reusable bundle

---

## 7. Troubleshooting

### Problem: The Agent Gives A Generic Answer Instead Of Using The Skill

Check:

- Did you install the full `skills/hrd-writing` folder rather than only `SKILL.md`?
- Did you also install `skills/_shared`?
- Did you start a fresh session after installation?
- Are you asking for a task that clearly matches HRD writing, APA 7 manuscript revision, or HRD practice implications?

### Problem: Claude Code Wrapper Exists But Results Are Weak

Check:

- Does the wrapper point to the correct local clone path?
- Does that path still exist?
- Did you explicitly tell Claude Code to use the subagent or slash command?
- Does the wrapper tell Claude Code to read the real `SKILL.md` first?

### Problem: Updates Are Not Reflected Locally

Run:

```bash
git pull
```

Then:

- for Codex local skills, copy `skills/_shared` and the updated folder again
- for Claude Code wrappers, no reinstall is needed if the wrapper still points to the same clone path

---

## 8. Minimal Examples

### Codex: One-Skill Install

```bash
git clone <this-repository-url> hrd-research-skills
cd hrd-research-skills
mkdir -p ~/.codex/skills
cp -R skills/_shared ~/.codex/skills/
cp -R skills/hrd-writing ~/.codex/skills/
```

### Codex: Full Install

```bash
git clone <this-repository-url> hrd-research-skills
cd hrd-research-skills
mkdir -p ~/.codex/skills
cp -R skills/_shared ~/.codex/skills/
for d in skills/hrd-*; do cp -R "$d" ~/.codex/skills/; done
```

### Claude Code: One Subagent Wrapper

```bash
npm install -g @anthropic-ai/claude-code
mkdir -p ~/ai-skills
cd ~/ai-skills
git clone <this-repository-url> hrd-research-skills
mkdir -p ~/.claude/agents
cat > ~/.claude/agents/hrd-writing.md <<'EOF'
---
name: hrd-writing
description: Use proactively for Human Resource Development academic writing, APA 7 manuscript revision, HRD theory framing, literature synthesis, and implications for HRD practice.
---

When invoked, first read `~/ai-skills/hrd-research-skills/skills/hrd-writing/SKILL.md`. Treat that file as the governing workflow.

If the skill references supporting files, read only the specific files you need from `~/ai-skills/hrd-research-skills/skills/hrd-writing/` and `~/ai-skills/hrd-research-skills/skills/_shared/`.
EOF
```

---

## 9. Final Recommendation

If you only want the simplest path, use Codex local skills:

```bash
mkdir -p ~/.codex/skills
cp -R skills/_shared ~/.codex/skills/
cp -R skills/hrd-writing ~/.codex/skills/
```

Then start a fresh Codex session and ask for an HRD writing task.
