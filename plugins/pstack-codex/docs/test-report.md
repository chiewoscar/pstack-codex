# Validation record

## 0.2.0 refresh, 2026-11-21

| Check | Observed result | Scope and limits |
| --- | --- | --- |
| Package and skills | 57 skills, 24 principles and 23 playbooks; manifests, licenses, marketplace and public documentation links pass. All 57 skills pass the skill-creator validator; imported Markdown links resolve. | Structure and links do not prove agent judgment. |
| Watcher regression before fix | Three five-second timeout cases slept 60 seconds and failed. | Single PR, queued stack and query retry paths. |
| Native Windows watcher | 53 tests pass, one POSIX fixture test skips; strict typecheck passes. | Invoke the CLI through Bun in PowerShell. |
| WSL watcher and orchestration | All 68 tests pass, including the POSIX gh fixture; no skips or failures. | The pre-existing orchestration suite has Unix-only fixtures and is not claimed to pass natively on Windows. |
| Statechart core | 70 tests pass on Windows and 70 on WSL. | Chart, message and pipeline tests. Imported fixture line endings follow package LF conventions. |
| Statechart TLC corpus in WSL | All 50 tests pass with real TLC; no skips or failures. | Passing/failing models, bounds, counterexamples, SANY errors and cleanup. |
| Real TLC smoke | `python scripts/check_statechart.py --jar <verified-jar>` passes on Windows and WSL. Login exits 0 with holding rules; CounterDeadlock exits 1 and reports NotThree and NoDeadlock violations. Both write Mermaid charts and reports. | Node 24.22.1, Java 21, TLC 1.7.4 with its pinned SHA-256. Full upstream POSIX-launcher integration fixtures are not claimed to run on native Windows. |
| CI | Package, watcher, strict typecheck, statechart core and real TLC smoke run on Windows and Ubuntu; orchestration additionally runs on Ubuntu. | See the workflow result for the release commit. |

New skill prose, the worker contract and the revised shipping playbook have not had full end-to-end Codex agent/PR trials. Historical trials below remain separate evidence. Reproduce the real-model checks with `python scripts/check_statechart.py`; it downloads and verifies TLC when no `--jar` is supplied and requires Java and Node on PATH.

## Earlier port trials

Port candidate checked on Codex desktop and CLI on Windows, September 2026. This is a record of tests run for this port, not a compatibility guarantee for future hosts.

| Scope | Result | Limit |
| --- | --- | --- |
| Skill structure | The original 45 `SKILL.md` files passed targeted skill validation. The two principles added in this refresh passed the same structural check. | Structural checks do not prove behavior. |
| Plugin metadata | Portable and Codex manifests passed the Codex plugin validator. | Installation still depends on the host's current plugin support. |
| Skill activation | The original 45 installed skills were read and exercised on a small TypeScript fixture or safe hypothetical. | The two newly added principles have structural validation only; the earlier checks were bounded, not full end-to-end workflows. |
| Subagents | Real Codex children ran role prompts, returned asynchronously, and reported separate review results. | Children in the same task shared tools and filesystem access. |
| Worktrees | Two writers used separate Git worktrees and branches; a worker could also read another worktree. | Branch separation is not a security boundary. |
| PR workflow | Two draft PR trials exercised review and verification skill workflows. Targeted tests and PR checks passed in the trial repository. | Drafts were left unmerged; optional Graphite and Cloud routes were not covered. |
| Local sandbox | `codex exec -s read-only` rejected a file write. A separate `workspace-write` Windows trial failed at sandbox startup with an ACL error. | Do not claim all local sandbox modes work on this host. |
| Cloud route | Verified CLI `exec`, `status`, and `diff` option shapes. | No configured Cloud environment ID was available for an end-to-end task. |

The earlier workflow trials used the pre-refresh 45-skill candidate. The two added principles and subsequent text edits have targeted structure checks, not new end-to-end PR trials. Run `python scripts/check_package.py` in the repository to verify package structure and metadata on your checkout. This release check is intentionally narrower than a full workflow suite.
