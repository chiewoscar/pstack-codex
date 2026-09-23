---
name: reflect
description: "Use only when explicitly invoked or routed by another pstack skill. Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect."
---

Codex runtime: Read `../../references/codex-runtime.md` before following tool or agent steps. Host and user instructions take precedence.

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits.

## When to invoke

- The user said "reflect" or "/reflect".
- A complex task (5+ tool calls) just landed cleanly and the recipe is worth keeping.
- The agent hit dead ends, found the working path, and the path generalizes.
- The user corrected the agent's approach mid-task.
- A non-trivial workflow emerged that isn't captured anywhere.

Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## Process

### 1. Locate the active transcript

Use the visible current conversation as the source. If a tool provides an export of this task, use that exact export. Do not search raw transcript directories. When no export is available, write a tight digest from the current conversation and pass that.

### 2. Spawn three reviewers in parallel

When delegation is permitted, spawn up to three read-only reviewers with the current host's subagent spawn tool, one per lens. Give each the digest or exact export and the relevant prompt template. Otherwise apply the lenses serially.

| Lens | `model` | Prompt template |
|---|---|---|
| Judgment | the current host model | `references/judgment-reviewer.md` |
| Tooling | the current host model | `references/tooling-reviewer.md` |
| Divergent | the current host model | `references/divergent-reviewer.md` |

Pass each template verbatim, substituting the transcript path or digest where marked. The spawn call returns a worker identifier before the findings. Wait for each reviewer to finish with the available collaboration wait/status tool, then read its final findings.

### 3. Synthesize

Synthesize the reviews in the current task, using `references/synthesizer.md` and spot-checking citations. Return a structured Accepted / Rejected / Backlog list.

### 4. Structural enforcement check

Sanity-check the synthesizer's Accepted list. For any item that would be enforced more reliably by a lint rule, script, metadata flag, or runtime check, move it from Accepted to Backlog. The synthesizer already applies this criterion; this is a final pass before edits land. See the **encode-lessons-in-structure** principle skill.

### 5. Apply

Before applying any Accepted edit, present the synthesizer's full Accepted/Rejected/Backlog output to the user and wait for explicit approval. The user picks which subset to apply and may redirect routings. Skill changes affect every future agent in the org; do not auto-apply.

Keep backlog items in the report. File them in a tracker only if the user authorizes that external write.

For each approved Accepted item, follow the Routing field exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): parent does directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): hand to Codex's `$skill-creator` skill and run its draft / test / iterate loop.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): hand to `skill-creator` and run its description-optimization loop.
- `new skill via skill-creator: <kebab-name>`: hand creation to `skill-creator`. Do not invent the shape ad hoc.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done. Skip this step if it doesn't.

### 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
