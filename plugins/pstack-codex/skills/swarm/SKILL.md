---
name: swarm
description: "Use only when explicitly invoked or routed by another pstack skill. Fan out N parallel workers, drain them, and return one report. Use for /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration."
---

Codex runtime: Read `../../references/codex-runtime.md` before following tool or agent steps. Host and user instructions take precedence.

# Swarm

Fan out bounded independent workers when Codex permits subagents. They may cover separate slices, race the same brief, or mix both. The parent waits, aggregates, and returns one report.

## Start

Open a todolist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Set N from the user or derive it from the shape. N is total workers, not the cloud concurrency limit.
4. Use the current host model by default. For an explicitly requested model race, verify each model is accepted by the chosen Codex execution mode before spawning.
5. Give each worker its own writable output when it writes. Use a verified worktree or a distinct directory under the host's temporary workspace; a branch name alone does not isolate files.
6. Choose a mode from `../../references/codex-runtime.md`: same-task child for ordinary parallel coverage, independent local CLI when a sandbox policy is required, or separate Codex Cloud tasks when remote execution is authorized and configured. State the selected isolation level in the report.

## Phase B: Fan out

Execute the chosen mode using its actual Codex tool or CLI parameters. Same-task children use the host's spawn tool up to its slot limit and share the filesystem; give writers separate worktrees or paths. An independent local CLI reviewer can use `-s read-only`; a local writer uses a verified worktree and a working `-s workspace-write` sandbox. A Cloud worker needs a configured environment ID and pushed starting branch. If the required isolation mode is unavailable, report the blocker instead of silently weakening it.

When the shared runtime reference cannot be read from a CLI sandbox, the supported command shapes are `codex exec -C <checkout> -s read-only <brief>` for a local reviewer and `codex cloud exec --env <environment-id> --branch <pushed-branch> <brief>` for an authorized remote task. Check this installed CLI's help and sandbox startup before launching. Neither command is a parameter to `spawn_agent`.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence.

If a worker drops out, proceed with N-1 and note it.

## Phase C: Aggregate

Read the terminal results. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

Keep a compact result table, one-line evidenced issues, and explicit gaps or dropouts.

## Phase D: Report

Return one consolidated in-chat report with the table, issue one-liners, gaps or dropouts, and the race rule when used.
