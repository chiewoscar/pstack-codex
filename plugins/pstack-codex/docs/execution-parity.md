# Execution mapping and parity limits

The detailed normative mapping for skills is in [`references/codex-runtime.md`](../references/codex-runtime.md). This page summarizes what was actually observed.

## Working Codex routes

- A same-task child agent can receive a bounded role brief and finish asynchronously. The tool name differs by host; the tested desktop exposed `collaboration.spawn_agent`, while a CLI run exposed `multi_agent_v1.spawn_agent`.
- Multiple writers can be assigned separate Git worktrees. A supported Codex CLI option also created a managed worktree in a bounded trial.
- An independent `codex exec -s read-only` run rejected a file write attempt. Sandbox success must be checked on the host before relying on it.
- `codex cloud exec --env <id> --branch <pushed-ref>` is a separately configured task route, and the CLI supports status and diff inspection. An end-to-end Cloud task was not run for this port.

## Differences that remain

`subagent_type`, `run_in_background`, `isolation`, `environment`, and `cloud_base_branch` are not fields on the tested Codex same-task child-agent tool. `poteto-agent`, `Explore`, and `comment-sicko` are role prompts in this package. They do not create registered agent types or grant permissions. The plugin maps the **requested effect** to available Codex operations rather than forwarding Claude Code or Cursor parameters.

Same-task children can access the same filesystem and tools. A worktree gives each writer a separate checkout and branch, but we observed one worker reading another worktree. It is not a file or credential isolation mechanism. A read-only prompt is not an enforced sandbox. File sandboxes also do not automatically prevent a connected MCP tool from changing an external service.

A separate Codex Cloud task may offer a distinct configured environment, but requires an environment ID, a pushed branch, authorization, and its own verification. It is not a child agent of the current conversation; local uncommitted files and desktop-only integrations do not appear automatically. Per-role Codex model selection does not reproduce the original pstack panel's cross-vendor diversity.

In one Windows CLI trial, `workspace-write` failed before agent work began with an `apply deny-read ACLs` error. The runtime instructions require reporting such a failure and never silently relaxing to unrestricted access.
