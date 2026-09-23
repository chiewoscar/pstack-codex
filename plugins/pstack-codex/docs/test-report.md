# Validation record

Port candidate checked on Codex desktop and CLI on Windows, September 2026. This is a record of tests run for this port, not a compatibility guarantee for future hosts.

| Scope | Result | Limit |
| --- | --- | --- |
| Skill structure | 45/45 `SKILL.md` files passed targeted skill validation. | Structural checks do not prove behavior. |
| Plugin metadata | Portable and Codex manifests passed the Codex plugin validator. | Installation still depends on the host's current plugin support. |
| Skill activation | All 45 installed skills were read and exercised on a small TypeScript fixture or safe hypothetical. | Bounded read-only checks; not 45 full end-to-end workflows. |
| Subagents | Real Codex children ran role prompts, returned asynchronously, and reported separate review results. | Children in the same task shared tools and filesystem access. |
| Worktrees | Two writers used separate Git worktrees and branches; a worker could also read another worktree. | Branch separation is not a security boundary. |
| PR workflow | Two draft PR trials exercised review and verification skill workflows. Targeted tests and PR checks passed in the trial repository. | Drafts were left unmerged; optional Graphite and Cloud routes were not covered. |
| Local sandbox | `codex exec -s read-only` rejected a file write. A separate `workspace-write` Windows trial failed at sandbox startup with an ACL error. | Do not claim all local sandbox modes work on this host. |
| Cloud route | Verified CLI `exec`, `status`, and `diff` option shapes. | No configured Cloud environment ID was available for an end-to-end task. |

The checks above used the workflow source represented by this release candidate. Run `python scripts/check_package.py` in the public repository to verify package structure and metadata on your checkout. This release check is intentionally narrower than a full workflow suite.
