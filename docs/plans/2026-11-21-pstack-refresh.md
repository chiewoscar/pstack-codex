# pstack 0.2.0 implementation plan

> Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Release the upstream watcher fixes and ten requested skills, preserve Codex behavior, push to GitHub, and update Windows and Ubuntu WSL installations.

**Architecture:** Keep the existing Codex port and its runtime mapping. Import the pinned upstream watcher implementation and tests together. Adapt new skill instructions and routing rather than replacing the port wholesale.

**Tech Stack:** Python package checks, Bun watcher tests, Node TypeScript statechart tooling, GitHub Actions, Codex plugin CLI.

## Global constraints

- Upstream snapshot: aaeb0ea3a0584995aa8f55ce44c6c5259414b896, pstack v0.15.46.
- Include create-formal-verification-skill, maintain-formal-verification-skill, and statechart.
- Exclude ketchup-video and make-bot-ui. Retain deslop and existing supported playbooks.
- Preserve host instructions, existing authorization, namespaced skill calls, model defaults, and Windows/WSL support.

## Task 1: PR watcher

- [x] Import upstream polling regression tests and demonstrate the existing timeout defect with `bun test watch-pr/policy.test.ts -t 'polling deadline sleeps'`.
- [x] Port watch-pr implementation and companion tests, then run `bun test orch watch-pr` and `bun run typecheck`.

## Task 2: Skills and workflows

- [x] Add ten upstream skills with Codex runtime preambles and namespaced cross-references.
- [x] Adapt shipping and interrogate, add worker.md, and connect new skills to mode/help/performance routing.
- [x] Keep Codex authorization, discovery, history, runtime and model rules. Remove links to the two excluded skills from imported help.
- [x] Run statechart tests and an actual TLC chart generation on Windows and WSL.

## Task 3: Release and installations

- [x] Update both manifests to 0.2.0, package checks, CI, English/Chinese READMEs, changelog, provenance and validation record.
- [x] Run `python scripts/check_package.py`, inspect diff and validate references.
- [ ] Commit and push main, wait for GitHub Actions.
- [ ] Upgrade marketplace and reinstall pstack-codex with the native Codex CLI in Windows and Ubuntu WSL.
- [ ] Confirm version, enabled status, skill count and matching installed contents on both systems.
