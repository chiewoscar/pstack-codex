---
name: arena
description: "Use only when explicitly invoked or routed by another pstack skill. Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape."
---

Codex runtime: Read `../../references/codex-runtime.md` before following tool or agent steps. Host and user instructions take precedence.

# Arena

Fan out N parallel attempts at the same task. Read every candidate end to end. Pick the strongest as the base. Graft the best ideas from the others into it. Verify the synthesized result.

## Start

Open a todolist with one entry per phase before launching anything. The arena runs autonomously and the list keeps phases from silently disappearing.

1. Frame
2. Fan out
3. Cross-judge
4. Pick
5. Graft
6. Verify

## Phase A: Frame

The N candidates will receive the same prompt, so the prompt is the contract. Get it right before spawning anything.

1. State the artifact each candidate is producing.
2. Derive the rubric. State what success looks like for *this* task, then turn it into 3-6 concrete gradeable criteria. Concrete: `Adds a --dry-run flag that skips writes`. Vague: `code is correct`. The rubric is the picker's tool in Phase D; candidates only see the task.
3. Pick two or three candidates for distinct design directions. Use the current host model unless the user or host explicitly configured valid model overrides.
4. Assign output paths. Each candidate writes to its own location (a Git worktree where possible, otherwise a distinct directory under the host's temporary workspace). N candidates writing to the same path is shared mutable state and fails the **separate-before-serializing-shared-state** principle skill test.
5. Choose the execution mode in `../../references/codex-runtime.md`. Use same-task children for ordinary local candidates, independent Codex CLI sessions for a verified sandbox policy, or separate Cloud tasks when authorized and configured. Record whether isolation is a worktree convention or a separate execution environment.

## Phase B: Fan out

Run candidates through the chosen Codex mode, respecting its concurrency limit. Give each the same task and a separate worktree or output path. A same-task child can still read sibling worktrees. If the task requires stronger isolation and that mode is unavailable, report the blocker; otherwise, run candidates serially when parallel writers cannot be kept in distinct paths.

If a CLI sandbox cannot read the shared runtime reference, use only the verified Codex command shapes: `codex exec -C <candidate-worktree> -s workspace-write <brief>` for an independent local writer, or `codex cloud exec --env <environment-id> --branch <pushed-branch> <brief>` for an authorized remote task. Verify sandbox startup or Cloud configuration before fan-out; do not downgrade failed isolation to `danger-full-access`.

The rationale is mandatory. Without it, the parent cannot tell whether a candidate's structure is principled or accidental, which makes Phase E grafting unreliable. Each rationale names the alternatives the candidate considered and what it rejected.

If a candidate fails to produce output, proceed with N-1 and note the dropout in the synthesis record.

## Phase C: Cross-judge

After candidates finish, ask an authorized read-only judge subagent to score them against the rubric, or perform the scoring locally when delegation is unavailable. The judge sees complete candidates, never partial files. Review all candidates yourself before choosing.

## Phase D: Pick a base

Read every candidate end to end before picking. Skimming N candidates surfaces only the candidate whose surface looks most familiar.

Score each candidate against the rubric criterion by criterion, not on holistic feel. Compare against the cross-judge. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base on which candidate a future maintainer can extend most easily without breaking invariants. Prefer the cleaner boundary or smaller surface area when two feel tied, per the Laziness Protocol.

Record the pick and the reason in a short synthesis note alongside the base artifact, including the cross-judge's verdict.

## Phase E: Graft

Walk each losing candidate once more and identify what is worth porting into the base. The signal is usually one or two things per candidate, not most of it.

Fold each graft in by hand, per the **redesign-from-first-principles** principle skill. Don't paste mechanically. The result has to remain coherent under one mental model.

Record what was grafted, from which candidate, and what was rejected and why. The rejection notes are the highest-signal part of the record. Future readers learn from what you considered and dropped, not just what you kept.

When N candidates converge on the same shape, that is a strong agreement signal. Note the convergence in the record and ship the consensus shape. No graft is needed. When N candidates wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

The synthesized artifact has to hold up under the same scrutiny as any other output, per the **prove-it-works** principle skill. The arena does not earn you a pass.

If verification surfaces a problem the arena did not catch, either Phase A was wrong (re-frame and re-run) or one candidate caught it and you missed the graft (go back to Phase E). Don't paper over.

## Outputs

One synthesized artifact. One short synthesis note alongside, naming the base, the grafts (with source candidate), the rejections, the dropouts if any, and the verification result.
