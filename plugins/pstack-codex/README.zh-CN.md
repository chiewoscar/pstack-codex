# pstack for Codex

[English](README.md) · [Codex 运行方式](references/codex-runtime.md) · [来源与许可证](NOTICE.md)

这是 Lauren Tan 的 [pstack](https://github.com/cursor/plugins/tree/main/pstack) 的**非官方 Codex 适配版**，以 Claude Code 移植项目 [cstack](https://github.com/irg1008/cstack) 为基础。它包含 47 个工程技能、23 个 `poteto-mode` 工作流程，以及原版 pstack 图标。独立的 `cstack-benny` Slack 自动化插件没有打包。

根目录的 `plugin.json` 使用可移植的 Agent Plugins 格式，但技能中的工具调用是按 **Codex** 编写的；其他 AI agent 需要另做运行时适配。这不是 Cursor、Claude Code 或 OpenAI 的官方版本。

## 安装

需要较新的 Codex CLI 或桌面版。只有运行 `poteto-mode` 附带的 TypeScript 脚本时才需要 Bun。GitHub CLI 和 Graphite 分别只对依赖它们的 PR 或分支堆栈流程有用。

```sh
codex plugin marketplace add chiewoscar/pstack-codex
codex plugin add pstack-codex@pstack-codex
```

第一条命令只注册 marketplace，不会安装插件。如果桌面版还看不到它，重启应用，然后在 Plugins Directory 选择 **pstack for Codex**。安装后请新建 Codex 任务，让新技能被加载。发布新版本后，可运行 `codex plugin marketplace upgrade pstack-codex`，再安装一次。

## 开始使用

在 Codex 任务中按名称调用：

```text
$pstack-codex:setup-pstack
$pstack-codex:how 解释这个仓库的支付流程。
$pstack-codex:interrogate 审查当前 diff。
$pstack-codex:poteto-mode 修复这个问题，验证真实行为，并准备可审查的 PR。
```

`setup-pstack` 会检查安装和可选工具，不会改写全局指令或偷偷安装 Bun。多数技能可以单独使用；较大的任务可由 `poteto-mode` 选择相应流程。推送、合并、部署、创建 Cloud 任务等操作仍受仓库规则和你的授权约束。

| 需求 | 技能 |
| --- | --- |
| 理解代码和历史原因 | `how`、`why`、`teach`、`recall` |
| 设计或并行处理改动 | `architect`、`arena`、`swarm`、`poteto-mode` |
| 审查改动、清理代码或文字 | `interrogate`、`blast-radius`、`deslop`、`no-comments`、`unslop` |
| 验证真实行为、记录决策 | `create-verification-skill`、`maintain-verification-skill`、`show-me-your-work` |

## 保留和新增的能力

- **来自 pstack：** 工程流程、评审角色、23 条原则、23 个 playbook 和原版图标。另有两条原则取自本次核对的 2026-09-23 上游快照。
- **来自 cstack：** 扩展的评审与编排说明、打包进来的 `deslop`、验证技能流程、决策记录和辅助脚本；这些内容继续归功于上游作者。
- **Codex 适配新增：** 可移植清单与 Codex 展示信息、带命名空间的技能调用、统一的[运行时参数映射](references/codex-runtime.md)、按当前宿主工具决定的子 agent 调用，以及满足前置条件时可用的本地 CLI、worktree 和 Cloud 路线。
- **未打包：** `cstack-benny`、Slack 触发器、定时 issue 分流及自动复现。上游 `make-bot-ui` 依赖 Cursor 的 Grok Bot routine 和密钥卡片 API，因此未冒充为可用的 Codex 技能。调查技能仍可把聊天记录作为可选证据来源，但不会安装 Slack。

## 与原版 agent 行为的差异

| 原版意图或参数 | Codex 做法 | 不能等价的部分 |
| --- | --- | --- |
| `subagent_type`，如 `poteto-agent`、`Explore`、`comment-sicko` | 将角色指引写入当前宿主的子 agent 任务说明。 | 这些只是提示词角色，不是 Codex 注册的 agent 类型，也不会强制权限。 |
| `run_in_background` | 启动子 agent 后继续工作，再等待返回的 handle；独立 CLI/Cloud 任务有各自 ID。 | 已测 Codex 子 agent 的 schema 没有同名字段；也不会自动创建过夜定时任务。 |
| `readonly` / `Explore` | 在支持时使用独立的 `codex exec -s read-only`。 | 同任务子 agent 没有强制只读参数；外部 MCP 写操作需要另行控制。本机 Windows CLI 的一次写入模式测试遇到 ACL 启动错误。 |
| `isolation`、`environment: "cloud"`、`cloud_base_branch` | 配好环境后，以已推送分支创建独立的 `codex cloud exec --env ... --branch ...` 任务。 | 这不是子 agent 参数。测试仓库没有可用的环境 ID，因此未做 Cloud 端到端创建测试。 |
| Git worktree 隔离 | 每个写入者使用独立 checkout，或使用受支持的 `codex exec --worktree`。 | worktree 只隔开 Git 状态，仍可读取其他可访问路径，也可能共享凭据。 |
| 跨厂商模型评审组 | 用不同评审提示词，并在宿主支持时选择 Codex 模型。 | 无法重现 pstack 的跨厂商模型独立性。 |

本插件尽量保留**流程效果**，但不保证参数逐项等价，也不保证同任务子 agent 之间有安全隔离。若任务要求严格只读或独立执行环境，应先验证沙箱或单独配置的 Cloud 环境；提示词角色和 worktree 都不能代替强制隔离。

## 验证现状

原有 45 个技能通过定向校验及受限场景的激活检查。新加的两条原则通过结构校验，尚未分别做端到端测试。真实 Codex 子 agent、异步完成、worktree 分支分离及两个草稿 PR 流程均在旧候选版测试过；本次改过的 playbook 文字没有重新完成整套 PR 测试。具体证据和限制见[技能测试报告](docs/test-report.md)及[执行能力报告](docs/execution-parity.md)。

## 来源与许可证

此次移植使用的 cstack 源码快照为 `b7e1933fa7485bb9bf937922862a7fc1fa43b738`。我们核对了原版 pstack 至 `b0b9c7a0baf8b6aa1d00bf77d4101e577d4ba411`（v0.15.4），并选择性移植可用的内容；这不是完整的逐文件同步，详情见[上游适配记录](docs/upstream.md)。[backnotprop/pstack](https://github.com/backnotprop/pstack) 是另一个跨 agent 镜像；本包主要提供 Codex 原生插件安装与经过实测的运行时映射。pstack 和 cstack 保留 Lauren Tan 的 MIT 声明；随包提供的 `deslop` 来自 Cursor Team Kit，并保留 Cursor 的 MIT 声明。详情见 [NOTICE.md](NOTICE.md) 与许可证文件。本适配版独立于上述项目。
