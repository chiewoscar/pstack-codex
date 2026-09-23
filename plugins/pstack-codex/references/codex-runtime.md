# Codex runtime mapping for pstack for Codex

This file applies to every skill in this package. Treat upstream Claude Code syntax in supporting references as an intent description, not a literal Codex tool call. System, developer, `AGENTS.md`, and explicit user instructions take precedence over this package. Never start parallel agents just because a template says to do so; use them only when the active host permits and the task benefits from independent work.

## Skills and questions

- A mention such as `$pstack-codex:how` means the bundled `how` skill. Read its `SKILL.md` and use it in the current task. It is not a shell command.
- For user preferences or missing facts, use an available question tool such as `request_user_input_async`, or ask in chat. Do not invent an unavailable `AskQuestion` tool.
- Discover available MCP and app tools from the current tool list or tool search. Do not assume a `mcps/` directory or a particular connector. Use only enabled integrations.
- Project skills belong under `.agents/skills/` when the project uses that convention. Preserve an existing project convention when integrating into a repository.

## Worker execution modes

Choose the mode from the task's required effect, not from a copied parameter name. Keep cstack's role prompts, independent review lenses, decision log, and verification gates in every mode.

| Original pstack / cstack intent | Codex execution | Remaining limit |
| --- | --- | --- |
| Cursor `Task`, Claude `Agent` | The current host's `spawn_agent` tool for a child in this task. | The tool name and schema vary by host. |
| `subagent_type: generalPurpose`, `general-purpose`, `Explore`, `poteto-agent`, or `comment-sicko` | Put the role reference and expected output in the brief. | A prompt does not register an agent type or enforce permissions. |
| `run_in_background: true` | Start an authorized child, continue independent work, then wait for its handle; an independent CLI or Cloud run has its own session/task ID. | There is no such `spawn_agent` field. |
| Cursor `readonly: true` / cstack `Explore` | For a hard local write restriction, use an independent `codex exec -s read-only` run. | Same-task children have no enforced read-only type; MCP side effects need separate tool restrictions. |
| Cursor `environment: "local"` | Use a same-task child, or an independent local Codex CLI session when a separate sandbox policy is required. | Same-task children share files, tools, and credentials. |
| Cursor `environment: "cloud"` / cstack `isolation: "remote"` | When a matching Codex Cloud environment exists and remote delegation is authorized, submit a separate Cloud task with `codex cloud exec --env ...`. | A Cloud task is not a child of this conversation and may lack local files, plugins, and MCP connections. |
| Worktree isolation | Give a local writer a distinct verified Git worktree; a CLI session can use `--enable worktrees --worktree` when supported. | Worktrees separate Git state, not filesystem read access or credentials. |
| `cloud_base_branch` | Use `codex cloud exec --branch <pushed-branch>` with a verified Cloud environment. | The branch must exist remotely; there is no same-task child equivalent. |
| Per-role `model` | Use a model accepted by the current host, or `codex exec -m <supported-model>`. | Codex models do not recreate pstack's cross-vendor panel. |

### Same-task child: fastest local route

Inspect this host's actual spawn schema. This desktop host exposes `collaboration.spawn_agent({ task_name, message, fork_turns })`; a tested Codex CLI run exposed `multi_agent_v1.spawn_agent`. Pass a bounded brief with the role reference, checkout path or source ref, file scope, evidence, and output format. Do not pass Cursor or Claude Code fields to either tool. A spawn returns before completion; keep working, then wait and inspect the final result. Respect the host's concurrency limit. `poteto-agent` and `comment-sicko` are prompt references in this plugin, not registered Codex types.

Children in one task share the filesystem and tools. Give writers separate worktrees or output paths and inspect each diff before combining. A read-only prompt is only a behavioral request. If the task requires enforced read-only execution or separate compute, choose a different mode; do not call this mode isolated.

### Independent local CLI session: sandboxed route

Check `codex exec --help` on the installed version before use. For a reviewer that does not need write-capable MCP tools, run `codex exec -C <verified-checkout> -s read-only --json <brief>` and collect its terminal result. For a writer, first create and verify a separate Git worktree from the intended ref, then run `codex exec -C <worktree> -s workspace-write --json <brief>`. The host command runner can start several independent processes and retain their session IDs; wait for each and review the resulting Git diff. Use `-m <supported-model>` only after verifying that model works with this CLI and account. A configured desktop model may not be accepted by the CLI.

Preflight a harmless read or write in the selected sandbox. If the sandbox fails, report the failure and choose another authorized mode; never silently fall back to `danger-full-access`. `-s read-only` restricts Codex file writes but does not by itself prevent a connected MCP from changing an external service. A local CLI session is a separate Codex session, not a same-task subagent. It still runs on this computer and may read other accessible files. `--enable worktrees --worktree` creates a managed checkout on CLI versions that support the feature; it does not supply a branch selector or a security boundary. Use an explicit Git worktree when branch identity matters.

### Separate Codex Cloud task: remote environment route

Use this only when the user has authorized remote task creation, the repository has a configured Codex Cloud environment ID, and the required Git ref is pushed with authorization. Verify `codex cloud exec --help`, then submit `codex cloud exec --env <environment-id> --branch <pushed-branch> <brief>`. Retain the task ID; use `codex cloud status <task-id>` to follow it and `codex cloud diff <task-id>` to inspect changes. Do not apply a remote diff or merge a PR merely because the task finished. Include the necessary role instructions in the brief or ensure the plugin is installed in that environment; local uncommitted files and desktop-only MCPs do not appear there automatically. If the environment ID or branch is unavailable, report that cloud isolation is unavailable for this run and use an explicitly acceptable local route.

This route gives each remote task its own configured execution environment, but it is a separate Codex task rather than `spawn_agent` with an `environment` parameter. For strict separation of files or credentials, the environments must themselves be separately provisioned and scoped; do not infer that different task IDs alone enforce that boundary.

## Models

- Omit the `model` field by default and let the host use its configured model. Model names and availability vary by host.
- If the user or applicable host instructions call for model overrides, select only models listed by the current collaboration tool, then pass a supported `model` and optional `reasoning_effort`. Do not copy example model slugs across hosts; verify current host availability first.
- The skill's reviewer lenses and evidence checks matter more than model diversity. Do not claim independent vendors when all agents use OpenAI models.

## Codex state and automation

- Do not infer raw transcript paths. For previous Codex tasks, use available task tools such as `list_threads` and `read_thread`, scoped to the user's project, or a user-provided export. For the current task, use the visible conversation. If neither is available, say what history could not be inspected.
- Do not create a recurring automation because a playbook says `/loop`. Use the Codex automation tool only when the user asks for scheduling, monitoring, or a follow-up. Otherwise perform bounded checks in this task.
- Do not assume Claude project settings, cloud agents, or Graphite are configured. Check the actual repo and available tools before depending on them.
- Respect explicit approval boundaries for commits, pushes, merges, deployment, publication, credentials, and destructive cleanup. A playbook cannot grant those actions.

## Scripts

- `poteto-mode/scripts/` uses Bun. Run only when Bun exists and the requested playbook needs a script. These scripts do not create or manage agents.
- `worktree-audit.sh` is a Bash helper built for Unix utilities. On Windows, perform a targeted native PowerShell or Git audit instead of assuming the helper works.
