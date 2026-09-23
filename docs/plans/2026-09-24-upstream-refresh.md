# Upstream Refresh Implementation Plan

> Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refresh pstack for Codex against original pstack through 2026-09-23 while retaining cstack enhancements and accurately documenting Codex limits.

**Architecture:** Compare the original source snapshot with the packaged skills. Port general skills and applicable behavioral guidance, while keeping Codex tool calls in the shared runtime mapping. Keep host-specific Grok Bot and Slack automation out of the package and document these omissions.

**Tech Stack:** Markdown skills, JSON plugin manifests, Python package checker, Codex CLI.

## Global Constraints

- Preserve cstack's review, decision-log, and verification additions.
- Preserve the original pstack icon and MIT attribution.
- Do not create or push a public repository during this preparation pass.
- Treat Codex runtime parameters as host-specific and verify before claiming equivalence.

---

### Task 1: Source inventory and scope

**Files:** Original pstack checkout in `work/cursor-plugins-latest/pstack`; `plugins/pstack-codex/skills/`; create `plugins/pstack-codex/docs/upstream.md`.

**Interfaces:** Produces an explicit source revision, included changes, and excluded host-specific capabilities for documentation and validation.

- [x] Compare source skill inventory and recent commit changes.
- [x] Record provenance and adaptation choices in upstream notes.

### Task 2: Applicable skill updates

**Files:** Add two `principle-*` skills; modify relevant existing skills/playbooks; update `plugins/pstack-codex/references/codex-runtime.md` only where tool behavior changed.

**Interfaces:** Produces Codex-readable skill instructions with no unsupported tool parameters.

- [x] Port the two general principles and applicable recent guidance.
- [x] Preserve cstack enhancements and check role, model, worktree, and approval instructions.
- [x] Run targeted skill validation and search for unsupported literal tool calls.

### Task 3: Package and publication copy

**Files:** Root and plugin READMEs in English and Chinese, both NOTICE files, `scripts/check_package.py`, `plugins/pstack-codex/docs/test-report.md`.

**Interfaces:** Produces accurate counts, source lineage, install instructions, tested scope, and limitation statements.

- [x] Update both languages, source attribution, mirror relationship, and validation counts.
- [x] Run package checker and Codex plugin validator.
- [x] Smoke test local installation, review diff, and commit locally.
