# pstack for Codex

[简体中文](README.zh-CN.md) · [Runtime mapping](plugins/pstack-codex/references/codex-runtime.md) · [Credits and licenses](NOTICE.md)

An **unofficial** Codex adaptation of Lauren Tan's [pstack](https://github.com/cursor/plugins/tree/main/pstack), built from the [cstack](https://github.com/irg1008/cstack) Claude Code port. It packages 57 engineering skills, 23 `poteto-mode` playbooks, and the original pstack icon. It excludes the separate `cstack-benny` Slack automation plugin.

The portable `plugin.json` makes the package discoverable by hosts supporting the Agent Plugins format. The instructions and tool calls target **Codex**; other AI agents need a separate runtime adapter. This is not an official Cursor, Claude Code, or OpenAI release.

## Install

You need a current Codex CLI or desktop app. Bun is needed for the bundled `poteto-mode` scripts. The optional `statechart` workflow needs a TypeScript-capable Node runtime, Java 11 or later and TLC. It can use preinstalled Java/TLC or install pinned tools with mise. See the statechart skill for setup. GitHub CLI and Graphite are optional and only matter for workflows that call them.

**Codex desktop:** Open the Plugins Directory, choose **Add Marketplace → Add from a repository**, enter `https://github.com/chiewoscar/pstack-codex`, then install **pstack for Codex**.

**CLI:** Run these as two separate commands:

```sh
codex plugin marketplace add chiewoscar/pstack-codex
codex plugin add pstack-codex@pstack-codex
```

You can also [download the source ZIP from GitHub](https://github.com/chiewoscar/pstack-codex/archive/refs/heads/main.zip). After extracting it, run `codex plugin marketplace add .` from the extracted repository root, then `codex plugin add pstack-codex@pstack-codex`. Downloading alone does not activate a Codex plugin.

Start a new Codex task after installation so its skills are discovered. If the marketplace is not visible in the desktop app, restart it. To update a CLI installation after a release, run `codex plugin marketplace upgrade pstack-codex` and install again.

## First use

In a Codex task, invoke a skill by name:

```text
$pstack-codex:setup-pstack
$pstack-codex:how Explain the payment flow in this repository.
$pstack-codex:interrogate Review my current diff.
$pstack-codex:poteto-mode Fix this bug, prove the behavior, and prepare a reviewable PR.
```

`setup-pstack` checks installation and optional tools; it does not change global instructions or install Bun. Most skills work on their own. `poteto-mode` routes larger tasks through its playbooks. Repository instructions and user approvals still govern pushing, merging, deploying, and cloud work.

| Need | Skill |
| --- | --- |
| Understand a subsystem or its history | `how`, `why`, `teach`, `recall` |
| Design or parallelize a change | `architect`, `arena`, `swarm`, `poteto-mode` |
| Challenge a diff and clean code or prose | `interrogate`, `blast-radius`, `deslop`, `no-comments`, `unslop` |
| Prove app behavior and record decisions | `create-verification-skill`, `maintain-verification-skill`, `show-me-your-work` |

## Added in 0.2.0

- `benchmark-checklist`, `principle-explain-the-number`, `correct`, `sharpen`, `ketchup`, `poteto-help`, and `in-your-own-words`.
- `create-formal-verification-skill`, `maintain-formal-verification-skill`, and `statechart`.
- Watcher pagination, approval-gate classification, fork-aware stack discovery and deadline fixes; executable review evidence; shared Codex worker instructions; GitHub shipping without a Graphite requirement.
- `ketchup-video` and `make-bot-ui` are excluded. The bundled `deslop`, Codex model defaults, runtime mapping and existing orchestration playbook remain.

Windows and WSL maintain separate plugin installations. Run the marketplace upgrade and plugin add commands in each environment, then start a new chat.

## What this port adds and keeps

- **From pstack:** the engineering workflow, role lenses, 24 principles, 23 playbooks, and original icon. Version 0.2.0 selectively ports ten more skills and watcher fixes from upstream v0.15.46.
- **From cstack:** expanded review and orchestration wording, vendored `deslop`, verification skill workflows, decision logs, and supporting scripts. The upstream authors remain credited.
- **For Codex:** a portable manifest plus Codex presentation metadata, namespaced skill calls, a shared [runtime mapping](plugins/pstack-codex/references/codex-runtime.md), host-aware subagent instructions, and explicit local CLI/worktree/Cloud routes where their preconditions hold.
- **Excluded:** `cstack-benny` and its Slack triggers, scheduled issue triage, and reproduction automation. The upstream `make-bot-ui` skill depends on Cursor's Grok Bot routine and secret-request APIs, so it is not packaged as a working Codex skill. Investigation skills may still use chat history as an optional evidence source; they do not install Slack.

## Differences from original agent behavior

| Original intent or parameter | Codex route | Limit |
| --- | --- | --- |
| `subagent_type` such as `poteto-agent`, `Explore`, or `comment-sicko` | Put role instructions in a brief to the current host's child-agent tool. | These are prompt roles, not registered Codex agent types or enforced permissions. |
| `run_in_background` | Spawn, keep working, then wait on the returned handle; independent CLI or Cloud tasks have their own IDs. | No equivalent field on the tested Codex child-agent schema; no automatic overnight scheduler. |
| `readonly` / `Explore` | An independent `codex exec -s read-only` session, where supported. | A same-task child is not read-only by parameter. External MCP writes need separate controls. A Windows CLI write-mode trial hit an ACL startup error. |
| `isolation`, `environment: "cloud"`, `cloud_base_branch` | A separately configured `codex cloud exec --env ... --branch ...` task with a pushed ref. | This is a separate task, not a child-agent option. Cloud creation was not tested end to end for the trial repository because no environment ID was available. |
| Git worktree isolation | A separate checkout for each writer, or supported `codex exec --worktree`. | A worktree separates Git state, but workers can still read sibling paths and may share credentials. |
| Cross-vendor model panel | Distinct reviewer prompts and, if supported, Codex model overrides. | It does not recreate pstack's independent model vendors. |

The package preserves **workflow intent**, not parameter-by-parameter equivalence or a security boundary between same-task children. It cannot promise the original pstack environment behavior on every Codex host. If strict read or execution isolation is required, verify a sandbox or separately provisioned Cloud environment first.

## Validation and status

Version 0.2.0 adds watcher regression tests, Windows/WSL script checks, and real TLC chart generation. All 57 skills receive package structure checks. New skill prose and the revised shipping workflow have not had full end-to-end agent/PR trials. Earlier subagent and draft-PR trials remain historical evidence. See the [test report](plugins/pstack-codex/docs/test-report.md) and [execution parity report](plugins/pstack-codex/docs/execution-parity.md) for evidence and limits.

## Source and license

The cstack source snapshot used for this port is `b7e1933fa7485bb9bf937922862a7fc1fa43b738`. We reviewed original pstack through `aaeb0ea3a0584995aa8f55ce44c6c5259414b896` (v0.15.46) and selectively ported applicable guidance. This is not a byte-for-byte or complete upstream sync; see the [upstream adaptation record](plugins/pstack-codex/docs/upstream.md). [backnotprop/pstack](https://github.com/backnotprop/pstack) is a separate cross-agent mirror; this package focuses on Codex-native plugin installation and tested runtime mapping. pstack and cstack carry Lauren Tan's MIT notice; the included `deslop` material comes from Cursor Team Kit and retains Cursor's MIT notice. See [NOTICE.md](NOTICE.md) and the bundled license files. This adaptation is independent of those projects.
