### Opening a PR

Use after a change-producing playbook when the user requested or authorized a PR. Do not turn a read-only investigation, plan, or forensics result into an unsolicited PR.

**Worktree.** For parallel writers, create and verify one distinct Git worktree per worker before spawning; give each worker its exact path. A subagent spawn call does not necessarily create worktrees or restrict filesystem access. Preserve dirty or unrelated work; inspect status before switching, moving, or cleaning anything. Never reset a branch merely to imitate isolation.

**Commits.** Commit liberally; rebase into small, ordered commits before opening PRs. Each commit is a future PR: landable, ordered to tell the story. Amend when the fix belongs in a just-made commit; new commit when separable.

**PRs.** `$pstack-codex:deslop` the diff before commit; `$pstack-codex:no-comments` the diff before review; apply the **unslop** skill to the PR description and commit bodies. Small PRs, 5 narrow over 1 fat; stack follow-ups, branch off main only for genuinely independent work. For stacked PRs, use whatever stacking tool your team uses; the principle is small, ordered slices with the stack visible to reviewers. `gh pr view <number>` before referencing PR status. Rebase on `main` before substantial stack work. No `## Summary` / `## Test plan` boilerplate on small PRs; commit bodies don't restate the subject. After opening, verify the PR URL, head SHA, changed files, and current checks once. Use `playbooks/babysit.md` only when the user asks to watch, get green, or check on the PR; push back when feedback drifts from intent.

A subagent that opens a PR runs `interrogate`, `$pstack-codex:deslop`, and `$pstack-codex:no-comments`, returns the URL, and does NOT babysit. Return to the parent.
