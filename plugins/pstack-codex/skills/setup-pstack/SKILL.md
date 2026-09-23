---
name: setup-pstack
description: Check the local pstack for Codex installation, optional Bun scripts, and model override settings. Use when the user asks to set up pstack or a bundled script fails.
---

Codex runtime: Read `../../references/codex-runtime.md` before following tool or agent steps. Host and user instructions take precedence.

# Set up pstack for Codex

1. Confirm that a configured marketplace exposes `pstack-codex` and that the plugin is enabled in the current host. The public Git marketplace and the personal marketplace are both supported. A new Codex task may be needed after installation for skill discovery.
2. Check `bun --version` only if the requested workflow calls `poteto-mode/scripts/`. Do not install Bun silently. The other skill instructions need no Bun setup.
3. Default to the host's current model. Do not write global `AGENTS.md` or model configuration just to use pstack. If the user explicitly wants per-role overrides, inspect the models supported by this host, then write only `~/.codex/pstack-models.md` with the requested role names and supported model values. A role with no entry inherits the current model. Validate the file before using it.
4. Do not enable any Slack integration or automation. The Benny pack is excluded.

If a script fails, run only its targeted test and report the exact failure. Do not run the full suite merely for setup.
