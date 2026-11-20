# Upstream adaptation record

This is an independent Codex adapter, not a mirror of every upstream file.

| Source | Revision | Use |
| --- | --- | --- |
| [pstack](https://github.com/cursor/plugins/tree/aaeb0ea3a0584995aa8f55ce44c6c5259414b896/pstack) | `aaeb0ea3a0584995aa8f55ce44c6c5259414b896`, v0.15.46 | Ten additional skills, statechart tooling and fixtures, watch-pr fixes, workflow guidance for 0.2.0. |
| pstack previous review | `b0b9c7a0baf8b6aa1d00bf77d4101e577d4ba411`, v0.15.4 | Principles and selectively adapted verification guidance in 0.1.2. |
| [cstack](https://github.com/irg1008/cstack) | `b7e1933fa7485bb9bf937922862a7fc1fa43b738` | Original port base, expanded review/orchestration, deslop and decision log material. |

## Included in 0.2.0

- `benchmark-checklist`, `correct`, `create-formal-verification-skill`, `in-your-own-words`, `ketchup`, `maintain-formal-verification-skill`, `poteto-help`, `principle-explain-the-number`, `sharpen`, and `statechart`.
- The watch-pr implementation and matching regression tests from this snapshot. The POSIX gh fixture test runs on Linux; native Windows covers the other watcher tests.
- A Codex worker contract, executable evidence for interrogate, benchmark/eval routing, and bottom-up GitHub shipping. These are selective adaptations, not complete copies of the new upstream workflows.
- Statechart tools and fixtures retain upstream behavior, with text resources normalized to the package's LF convention. Native Windows uses the documented direct Node entry point. Java/TLC may be preinstalled; mise is optional when those paths are supplied.

## Preserved and excluded

- Kept the Codex runtime mapping, namespaced skill calls, host model defaults, authorization boundaries, deslop and the existing orchestration playbook/scripts.
- Rewrote poteto-help for Codex instead of importing Cursor installation, Custom Modes, model rule files and built-in tools.
- Excluded ketchup-video and make-bot-ui at the user's request. Slack automation remains excluded.
- Did not copy upstream vendor model slugs, Cursor cloud-agent calls, arbitrary messaging grants or recurring `/loop` instructions as executable Codex behavior.
- Formal verification reports properties, assumptions, bounds and counterexamples. It does not claim that a model proves an entire production system.

The MIT notices remain in [NOTICE.md](../NOTICE.md). See [validation](test-report.md) for observed checks and limitations.
