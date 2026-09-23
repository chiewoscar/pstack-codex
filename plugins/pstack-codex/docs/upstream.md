# Upstream adaptation record

This is an independent Codex adapter, not a mirror of every upstream file.

| Source | Revision inspected or used | Role |
| --- | --- | --- |
| [Lauren Tan's pstack](https://github.com/cursor/plugins/tree/main/pstack) | [`b0b9c7a0baf8b6aa1d00bf77d4101e577d4ba411`](https://github.com/cursor/plugins/commit/b0b9c7a0baf8b6aa1d00bf77d4101e577d4ba411), v0.15.4, 2026-09-23 | Original workflow and icon; source of the two principles added in this refresh. |
| [irg1008/cstack](https://github.com/irg1008/cstack) | `b7e1933fa7485bb9bf937922862a7fc1fa43b738` | Claude Code adaptation and enhanced review, verification, decision log, and orchestration material used for the initial port. |
| [backnotprop/pstack](https://github.com/backnotprop/pstack) | Inspected 2026-09-24 | Separate cross-agent mirror. It was not copied into this package. |

## What this refresh includes

- `principle-attack-the-premise` and `principle-test-behavior-not-implementation` from the original pstack snapshot. These are general instructions, with no Cursor-only tool calls.
- A Codex version of pstack's new setup budget choice: use supported per-role model and reasoning-effort values instead of Cursor's model slugs.
- Verification rounds in the autopilot playbooks: review each changed patch, tie the verdict to its head, and wait for CI on the final merge-prep head.
- The cstack enhancements and the existing Codex runtime mapping remain in place.

## What this refresh does not claim

- It does not apply all textual edits from pstack v0.15.4. Several upstream changes shorten wording or assume Cursor's `Task`, `/goal`, `/loop`, cloud agents, Origin, Grok Bot, model catalog, and approval tools. Those cannot be copied as executable Codex commands.
- Original pstack has a `make-bot-ui` skill that creates a Cursor Grok Bot webhook routine and requests a sender key through Cursor's secret-request card. Codex does not expose that same workflow in this package, so the skill is omitted. The port retains cstack's vendored `deslop` instead. This explains why both packages can list 47 skills while their sets differ.
- The independent `cstack-benny` Slack automation plugin remains excluded. Optional Slack evidence references in `why` do not install or trigger an automation.
- The two added principles have structural validation only. The older 45-skill activation and draft-PR evidence predates this refresh; see [validation record](test-report.md).

## Runtime boundary

Use the shared [Codex runtime mapping](../references/codex-runtime.md) for subagents, background execution, worktrees, read-only CLI runs, and optional Cloud tasks. `subagent_type`, `run_in_background`, and `isolation` are not Codex child-agent fields. Role prompts and worktrees do not enforce separate filesystem access. A separate Cloud task needs its own configured environment and authorized remote branch.
