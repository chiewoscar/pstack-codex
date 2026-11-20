---
name: poteto-help
description: Help users set up pstack for Codex and choose a skill, playbook, or principle. Use for pstack help and skill selection questions.
---

Codex runtime: Read `../../references/codex-runtime.md` before following tool or agent steps. Host and user instructions take precedence.

# Poteto help

Answer a help question without starting the workflow it asks about. If the user asks for work, invoke the relevant skill and do the work. Read the linked skill before explaining its behavior. The installed port owns the answer when upstream differs.

## Setup and use

Install this port with `codex plugin marketplace add chiewoscar/pstack-codex`, then `codex plugin add pstack-codex@pstack-codex`. To update, run `codex plugin marketplace upgrade pstack-codex`, then install again. Windows and WSL have separate Codex homes; update each with its native CLI. Start a new chat to discover the new skills.

Use `$pstack-codex:setup-pstack` to check prerequisites and supported model choices. No setup is required for a simple standalone skill. Model overrides are optional and must be supported by the current host; otherwise inherit its configured model. Do not describe Cursor Custom Modes, model rule files, or `/loop` as Codex features.

For a substantial task, use `$pstack-codex:poteto-mode` with the goal and an observable completion condition. Playbooks live inside that skill and are not separate slash commands. A request to babysit a PR stops at merge-ready; a request to ship authorizes the shipping workflow within the user's stated scope. A plan request produces a plan and does not authorize its execution.

## Pick a skill

| Skill | When it helps |
| --- | --- |
| [`$pstack-codex:architect`](../architect/SKILL.md) | Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. Use for /architect, 'architect this', 'design this', or non-trivial work where jumping to code would lock in the wrong shape. |
| [`$pstack-codex:arena`](../arena/SKILL.md) | Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape. |
| [`$pstack-codex:automate-me`](../automate-me/SKILL.md) | Use for \"automate me\", \"create/update/refresh my -mode skill\", \"turn/capture my preferences or working style into a skill\", or wanting agents to follow how the user works. Drafts or revises a personal -mode skill via skill-creator + unslop, optionally pulling fresh evidence from recent transcripts. |
| [`$pstack-codex:benchmark-checklist`](../benchmark-checklist/SKILL.md) | Vet a perf measurement (limiter, tuning, limits, errors, repeatability, relevance, and whether the work happened) before you report or act on it. Use when you run a benchmark or report a speedup or regression you measured. |
| [`$pstack-codex:blast-radius`](../blast-radius/SKILL.md) | Find what a change could break somewhere else before it ships, beyond the diff, and prove the one fact it's safe because of by running real code instead of writing it up. Use for 'blast radius of X', 'what could this break', or reviewing a small diff you don't trust. |
| [`$pstack-codex:bro`](../bro/SKILL.md) | Restate the last message in plain human language, with no jargon. |
| [`$pstack-codex:correct`](../correct/SKILL.md) | Find the mistakes agents keep repeating in this repo and make each one impossible. Try architecture first, then types, then a lint whose error names the fix, then a test, and write docs last. Prove each check fails on a real past mistake. Repeat this each time the operator corrects you. Use for /correct. |
| [`$pstack-codex:create-formal-verification-skill`](../create-formal-verification-skill/SKILL.md) | Generate a project-local skill that formally verifies the code where a bug costs the most and tests reach the least, in any language, with whichever verification tool fits. Use for $pstack-codex:create-formal-verification-skill, \"model-check this race\", \"prove this invariant\", or when concurrency, retries, state machines, parsers, or unsafe code need more than tests. |
| [`$pstack-codex:create-verification-skill`](../create-verification-skill/SKILL.md) | Generate a project-local verification skill that drives your app the way a user does — any language, framework, or platform. Use for /create-verification-skill, \"make a control skill for this repo\", or when a project has no scripted way to prove UI/CLI/service behavior. |
| [`$pstack-codex:deslop`](../deslop/SKILL.md) | Remove AI-generated code slop from a branch or diff. Use when the user says "deslop", "remove AI slop", "clean up the AI code", or asks to strip over-commenting, unnecessary defensive try/catch, `as any` casts, deep nesting, or styling that doesn't match the surrounding file. Run before opening a PR or committing agent-written code. |
| [`$pstack-codex:figure-it-out`](../figure-it-out/SKILL.md) | Design an auditable playbook when no narrower one fits: a large migration, an ambitious multi-part change, or work a human reviews after stepping away. Scales rigor to the task, runs a hypothesis loop, and logs decisions via show-me-your-work. Use for /figure-it-out, 'figure it out', a large migration, or when no narrower playbook applies. |
| [`$pstack-codex:how`](../how/SKILL.md) | Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, onboarding mental models. Can critique architecture. Use why for motivation. |
| [`$pstack-codex:in-your-own-words`](../in-your-own-words/SKILL.md) | Restate in your own words what you think the user's goals are and what problem they're trying to solve. Use for /in-your-own-words. |
| [`$pstack-codex:interrogate`](../interrogate/SKILL.md) | Use for \"interrogate\", \"adversarial review\", \"multi-model review\", \"challenge this\", \"stress test this code\", \"find blind spots\", or \"tear this apart\". Multiple LLM reviewers challenge changes from independent angles. |
| [`$pstack-codex:ketchup`](../ketchup/SKILL.md) | Catch the user up on what changed in this chat since their last message, in plain words and small visuals. List every item waiting on them with what they need to decide it from the reply alone. Use for /ketchup. |
| [`$pstack-codex:maintain-formal-verification-skill`](../maintain-formal-verification-skill/SKILL.md) | Bring a project's formal verification back in line with the code after the code changes: find the commits that touched verified code, update the model, harness, or properties to describe the code as it is now, rerun, and say whether each failure is drift in the verification or a bug in the code. Use for $pstack-codex:maintain-formal-verification-skill, \"is the model still true to the code\", or after merges and refactors that touched verified code without rechecking it. |
| [`$pstack-codex:maintain-verification-skill`](../maintain-verification-skill/SKILL.md) | Periodic pass that keeps a project's verification skill and feature map honest: parallel source readers per feature, one live session driving every feature, at most one PR of proven corrections. Use for /maintain-verification-skill or \"audit the verify skill\". |
| [`$pstack-codex:no-comments`](../no-comments/SKILL.md) | Spawn Comment Sicko, fix accepted findings, and offer encodings for claimed constraints. |
| [`$pstack-codex:poteto-help`](../poteto-help/SKILL.md) | Guides users through pstack setup, $pstack-codex:poteto-mode, and picking the skill, playbook, or principle for a task. Type $pstack-codex:poteto-help with a question. |
| [`$pstack-codex:poteto-mode`](../poteto-mode/SKILL.md) | poteto's agent style for concise, detailed responses, deliberate subagents, unslopped prose, simple code, and verified work. Use for poteto, /poteto-mode, or requests to work in this style. |
| [`$pstack-codex:principle-attack-the-premise`](../principle-attack-the-premise/SKILL.md) | Apply when two or more fixes that share one premise have failed the same gate. Take a census of which actors hold the imbalance before the next fix, then question the premise instead of writing another fix that assumes it. |
| [`$pstack-codex:principle-boundary-discipline`](../principle-boundary-discipline/SKILL.md) | Explicit pstack principle: boundary discipline. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-build-the-lever`](../principle-build-the-lever/SKILL.md) | Explicit pstack principle: build the lever. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-encode-lessons-in-structure`](../principle-encode-lessons-in-structure/SKILL.md) | Explicit pstack principle: encode lessons in structure. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-exhaust-the-design-space`](../principle-exhaust-the-design-space/SKILL.md) | Explicit pstack principle: exhaust the design space. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-experience-first`](../principle-experience-first/SKILL.md) | Explicit pstack principle: experience first. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-explain-the-number`](../principle-explain-the-number/SKILL.md) | Apply before you measure, and before you trust, report, or act on a number you measured: a speedup, a regression, a throughput, a latency, or an eval result. Find what limits it, and rule out that it measured something other than the work you think. |
| [`$pstack-codex:principle-fix-root-causes`](../principle-fix-root-causes/SKILL.md) | Explicit pstack principle: fix root causes. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-foundational-thinking`](../principle-foundational-thinking/SKILL.md) | Explicit pstack principle: foundational thinking. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-guard-the-context-window`](../principle-guard-the-context-window/SKILL.md) | Explicit pstack principle: guard the context window. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-laziness-protocol`](../principle-laziness-protocol/SKILL.md) | Explicit pstack principle: laziness protocol. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-make-operations-idempotent`](../principle-make-operations-idempotent/SKILL.md) | Explicit pstack principle: make operations idempotent. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-migrate-callers-then-delete-legacy-apis`](../principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | Explicit pstack principle: migrate callers then delete legacy apis. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-minimize-reader-load`](../principle-minimize-reader-load/SKILL.md) | Explicit pstack principle: minimize reader load. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-model-the-domain`](../principle-model-the-domain/SKILL.md) | Explicit pstack principle: model the domain. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-never-block-on-the-human`](../principle-never-block-on-the-human/SKILL.md) | Explicit pstack principle: never block on the human. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-outcome-oriented-execution`](../principle-outcome-oriented-execution/SKILL.md) | Explicit pstack principle: outcome oriented execution. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-prove-it-works`](../principle-prove-it-works/SKILL.md) | Explicit pstack principle: prove it works. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-redesign-from-first-principles`](../principle-redesign-from-first-principles/SKILL.md) | Explicit pstack principle: redesign from first principles. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-separate-before-serializing-shared-state`](../principle-separate-before-serializing-shared-state/SKILL.md) | Explicit pstack principle: separate before serializing shared state. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-sequence-verifiable-units`](../principle-sequence-verifiable-units/SKILL.md) | Explicit pstack principle: sequence verifiable units. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-subtract-before-you-add`](../principle-subtract-before-you-add/SKILL.md) | Explicit pstack principle: subtract before you add. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:principle-test-behavior-not-implementation`](../principle-test-behavior-not-implementation/SKILL.md) | Apply when you write, change, or keep a test. Call the code the way its users do and assert the result they observe against a literal expected value. If the test would still pass when every imported function returns undefined, rewrite the assertion or delete the test. |
| [`$pstack-codex:principle-type-system-discipline`](../principle-type-system-discipline/SKILL.md) | Explicit pstack principle: type system discipline. Use when the user names it or poteto-mode routes to it. |
| [`$pstack-codex:recall`](../recall/SKILL.md) | Reconstruct your recent working context from your own chat history, live state, and the shared record (user reports, prior fixes, incidents), then hand back a tight current-state brief. Use for 'recall my work on X', 'catch me up', 'what have I been working on', 'where did I leave off', before starting or resuming work. |
| [`$pstack-codex:reflect`](../reflect/SKILL.md) | Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect. |
| [`$pstack-codex:setup-pstack`](../setup-pstack/SKILL.md) | Check the local pstack for Codex installation, optional Bun scripts, and supported model and reasoning effort overrides. Use when the user asks to set up pstack, choose a budget, or a bundled script fails. |
| [`$pstack-codex:sharpen`](../sharpen/SKILL.md) | Make a task deeper, not bigger, then rewrite the prompt. Use for /sharpen. |
| [`$pstack-codex:show-me-your-work`](../show-me-your-work/SKILL.md) | Keep a reviewable decision trail for long-running or unattended work: a TSV log with one row per decision (what, why, evidence, result). Local by default; commit it when a reviewer needs the trail to trust the result. Use for /show-me-your-work, autonomous or multi-phase runs, or work a human reviews after stepping away. |
| [`$pstack-codex:statechart`](../statechart/SKILL.md) | Check a TLA+ model of a system that moves between states, such as a product flow, a protocol, or a service, and draw it as a Mermaid statechart. The report gives the shortest path to each state that breaks a rule. Use for $pstack-codex:statechart, or to show a bug as a path through states. |
| [`$pstack-codex:swarm`](../swarm/SKILL.md) | Fan out N parallel workers, drain them, and return one report. Use for /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration. |
| [`$pstack-codex:tdd`](../tdd/SKILL.md) | Use only when the user explicitly asks for TDD, a failing test, or a regression test, OR when the bug has an obvious cheap local test target. Skip when the test path is unclear, expensive, integration-heavy, or not requested. |
| [`$pstack-codex:teach`](../teach/SKILL.md) | Explain a body of work plainly so a person actually understands it. Runs the `how` and `why` skills and weaves what they find into one clear explanation. Use for 'teach me this', 'help me really understand X', 'explain this change or subsystem to me'. |
| [`$pstack-codex:technical-writing`](../technical-writing/SKILL.md) | Layered technical-writing standard: Diátaxis structure, Google developer style sentences, STE instruction rules, Global English syntax. Use for /technical-writing or when writing or reviewing docs, RFCs, readmes, PR descriptions, or commit messages. |
| [`$pstack-codex:typescript-best-practices`](../typescript-best-practices/SKILL.md) | TypeScript best practices. Use when reading or editing any .ts or .tsx file. |
| [`$pstack-codex:unslop`](../unslop/SKILL.md) | Cut AI tells from any writing. Must always apply. |
| [`$pstack-codex:why`](../why/SKILL.md) | Use for 'why does X work this way', 'why we picked Y', design rationale, regressions, postmortems, or data-backed thresholds. Discovers available MCPs and queries each evidence category (source control, issue tracker, long-form docs, real-time chat, infrastructure observability, error tracking, product analytics warehouse) in parallel, then returns a cited read on decisions and tradeoffs. Use how for runtime behavior. |

## Close choices

- `how` explains behavior; `why` explains rationale; `teach` combines the explanation for a reader.
- `recall` reconstructs recent chats; `ketchup` catches up only this chat since the user's previous message.
- `arena` compares attempts at one task; `swarm` divides independent work; `interrogate` tries to demonstrate failures.
- App verification drives real behavior. Formal verification checks stated properties under explicit assumptions and bounds. Keep both tied to the code.
- `correct` prevents repeated mistakes through architecture, types, checks, and then documentation. `reflect` proposes improvements to agent guidance.

This port includes its own `deslop`. It excludes `ketchup-video`, `make-bot-ui`, and Slack automation. Read [the runtime mapping](../../references/codex-runtime.md) for tool and execution differences. Public links should point to `https://github.com/chiewoscar/pstack-codex/blob/main/plugins/pstack-codex/` followed by the package-relative path.

Reply with the direct answer and at most one example prompt unless the user asked for a complete map.
