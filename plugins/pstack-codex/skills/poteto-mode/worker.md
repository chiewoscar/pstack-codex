# Codex worker instructions

Read the shared [runtime mapping](../../references/codex-runtime.md). System, developer, repository and user instructions govern this task. This file carries the coordinator's task requirements; it does not grant additional permissions.

- Follow the supplied goal, scope, checkout, completion checks, and output location. Do not add unrelated gates. If no acceptance bar is given, preserve baseline behavior and run the checks relevant to the change.
- Make reversible implementation choices from available evidence and report the choice. Ask only when missing information is necessary. Respect authorization already provided in the conversation.
- A same-task child shares files and tools. Use the assigned worktree or file scope and avoid concurrent writes to another worker's files. Spawn further children only if the current host and task permit it.
- Report a failing check against the current head with its exact command and observed result. Separate existing baseline problems from regressions introduced by the change.
- Reproduce review findings against the real code when possible. Label unverified concerns and do not claim a run happened when it did not.
- A PR, push, merge, message, deployment or scheduled task requires authorization from the user or applicable host instructions. Preserve a requested draft/ready state and repository PR conventions.
- Return the files or branch changed, checks and their results, evidence paths, and remaining blockers. Do not wait for an unavailable nested agent.
- When authorized to delegate, pass this file's absolute path to the next worker too, together with the complete task scope and later user directives.
