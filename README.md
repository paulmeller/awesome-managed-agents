# Awesome Claude Managed Agents [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of resources, tools, demos, and community projects for [Claude Managed Agents](https://claude.com/blog/claude-managed-agents) by Anthropic.

Claude Managed Agents is a fully managed, server-side agent runtime. Anthropic hosts the agent loop, sandboxed cloud containers, built-in tools, and SSE-based event streaming &mdash; you define an agent, an environment, and start a session. No need to build your own orchestration, tool execution, or container infrastructure.

Launched in public beta on April 8, 2026. Available exclusively through the Anthropic API (not via AWS Bedrock or Google Vertex AI).

## Contents

- [Official Resources](#official-resources)
- [SDKs & CLI](#sdks--cli)
- [Documentation](#documentation)
- [API Surface](#api-surface)
- [Built-in Tools](#built-in-tools)
- [Research Preview Features](#research-preview-features)
- [Tutorials & Guides](#tutorials--guides)
- [Community Projects](#community-projects)
- [Integrations](#integrations)
- [Launch Partners](#launch-partners)
- [Articles & Press](#articles--press)
- [Videos & Talks](#videos--talks)
- [Managed Agents vs Agent SDK](#managed-agents-vs-agent-sdk)
- [Related Products](#related-products)

## Official Resources

- [Product Announcement](https://claude.com/blog/claude-managed-agents) - Official blog post: "Get to production 10x faster."
- [Engineering Deep-Dive](https://www.anthropic.com/engineering/managed-agents) - "Scaling Managed Agents: Decoupling the brain from the hands."
- [Pricing](https://platform.claude.com/docs/en/about-claude/pricing) - Standard token rates + $0.08/session-hour (metered to the millisecond) + $10/1K web searches.
- [Research Preview Access](https://claude.com/form/claude-managed-agents) - Request access to Outcomes, Multi-agent, and Memory features.

## SDKs & CLI

All SDKs expose Managed Agents under `client.beta.*` (agents, environments, sessions). Beta header: `managed-agents-2026-04-01`.

- [Python SDK](https://pypi.org/project/anthropic/) - `pip install anthropic`
- [TypeScript SDK](https://www.npmjs.com/package/@anthropic-ai/sdk) - `npm install @anthropic-ai/sdk`
- [Go SDK](https://github.com/anthropics/anthropic-sdk-go) - `go get github.com/anthropics/anthropic-sdk-go`
- [Java SDK](https://central.sonatype.com/artifact/com.anthropic/anthropic-java) - `implementation("com.anthropic:anthropic-java:2.20.0")`
- [C# SDK](https://www.nuget.org/packages/Anthropic) - `dotnet add package Anthropic`
- [Ruby SDK](https://rubygems.org/gems/anthropic) - `bundle add anthropic`
- [PHP SDK](https://packagist.org/packages/anthropic-ai/sdk) - `composer require anthropic-ai/sdk`
- [Anthropic CLI (`ant`)](https://github.com/anthropics/anthropic-cli) - Go-based CLI. `brew install anthropics/tap/ant` (macOS). Supports `ant beta:agents`, `ant beta:sessions`, `ant beta:environments`, etc.

## Documentation

- [Overview](https://platform.claude.com/docs/en/managed-agents/overview) - What Managed Agents are and when to use them.
- [Quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart) - Create an agent, environment, and session in minutes.
- [Agent Setup](https://platform.claude.com/docs/en/managed-agents/agent-setup) - Configure model, system prompt, tools, MCP servers, and skills.
- [Sessions](https://platform.claude.com/docs/en/managed-agents/sessions) - Session lifecycle and status management.
- [Environments](https://platform.claude.com/docs/en/managed-agents/environments) - Container configuration, packages, and networking modes.
- [Tools](https://platform.claude.com/docs/en/managed-agents/tools) - Built-in tools, custom tools, and MCP toolsets.
- [Events & Streaming](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) - SSE-based event protocol and event types.
- [Cloud Containers](https://platform.claude.com/docs/en/managed-agents/cloud-containers) - Container specs (Ubuntu 22.04, x86_64, 8 GB RAM, 10 GB disk).
- [Skills](https://platform.claude.com/docs/en/managed-agents/skills) - Reusable, filesystem-based expertise packages (up to 20 per session).
- [MCP Connector](https://platform.claude.com/docs/en/managed-agents/mcp-connector) - Remote MCP server integration with vault-based auth.
- [Permission Policies](https://platform.claude.com/docs/en/managed-agents/permission-policies) - `always_allow` and `always_ask` tool policies.
- [API Reference](https://platform.claude.com/docs/en/api/beta/sessions) - Full API specification for all endpoints.

## API Surface

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Agent** | Reusable, versioned config: model + system prompt + tools + MCP servers + skills. Created once via `POST /v1/agents`. |
| **Environment** | Container template: packages, networking rules, file mounts. Created via `POST /v1/environments`. |
| **Session** | A running agent instance within an environment. Maintains conversation history. Created via `POST /v1/sessions`. |
| **Events** | Messages exchanged via SSE. User events go in; agent/session/span events come back. |

### Endpoints

**Agents:** `POST /v1/agents` | `GET /v1/agents/:id` | `POST /v1/agents/:id` (update/version) | `POST /v1/agents/:id/archive`

**Environments:** `POST /v1/environments` | `GET /v1/environments` | `GET /v1/environments/:id` | `DELETE /v1/environments/:id`

**Sessions:** `POST /v1/sessions` | `GET /v1/sessions` | `GET /v1/sessions/:id` | `POST /v1/sessions/:id/archive`

**Events:** `POST /v1/sessions/:id/events` (send) | `GET /v1/sessions/:id/stream` (SSE) | `GET /v1/sessions/:id/events` (list)

**Files:** `POST /v1/files` (upload) | `GET /v1/files?scope_id=:session_id` (list) | `GET /v1/files/:id/content` (download)

**Threads (multi-agent):** `GET /v1/sessions/:id/threads` | `GET /v1/sessions/:id/threads/:tid/stream`

**Memory Stores:** `POST /v1/memory_stores` | `POST /v1/memory_stores/:id/memories` | `GET /v1/memory_stores/:id/memories` | `PATCH /v1/memory_stores/:id/memories/:mid`

### Event Types

**You send:** `user.message` | `user.interrupt` | `user.custom_tool_result` | `user.tool_confirmation` | `user.define_outcome`

**You receive:** `agent.message` | `agent.thinking` | `agent.tool_use` | `agent.tool_result` | `agent.custom_tool_use` | `agent.mcp_tool_use` | `agent.mcp_tool_result`

**Session lifecycle:** `session.status_running` | `session.status_idle` | `session.status_rescheduled` | `session.status_terminated` | `session.error`

**Observability:** `span.model_request_start` | `span.model_request_end` | `span.outcome_evaluation_start` | `span.outcome_evaluation_end`

### Quickstart Example (Python)

```python
from anthropic import Anthropic

client = Anthropic()

agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-sonnet-4-6",
    system="You are a helpful coding assistant.",
    tools=[{"type": "agent_toolset_20260401"}],
)

environment = client.beta.environments.create(
    name="quickstart-env",
    config={"type": "cloud", "networking": {"type": "unrestricted"}},
)

session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="Quickstart session",
)

with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(
        session.id,
        events=[{
            "type": "user.message",
            "content": [{"type": "text", "text": "Create a Python script that generates the first 20 Fibonacci numbers"}],
        }],
    )

    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    print(block.text, end="")
            case "agent.tool_use":
                print(f"\n[Using tool: {event.name}]")
            case "session.status_idle":
                print("\n\nAgent finished.")
                break
```

## Built-in Tools

Enabled via `agent_toolset_20260401`. All enabled by default; individually configurable.

| Tool | Description |
|------|-------------|
| `bash` | Execute bash commands in a persistent shell session. |
| `read` | Read a file from the container filesystem. |
| `write` | Write a file to the container filesystem. |
| `edit` | Perform string replacement in a file. |
| `glob` | Fast file pattern matching using glob patterns. |
| `grep` | Text search using regex patterns. |
| `web_fetch` | Fetch content from a URL. |
| `web_search` | Search the web for information ($10/1K searches). |

Additional tool types: **Custom tools** (you define schema, your app executes), **MCP toolsets** (remote MCP servers), **Memory tools** (auto-added when memory stores attached).

## Research Preview Features

Require [access request](https://claude.com/form/claude-managed-agents).

- **[Outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes)** - Define success criteria with rubrics. A separate grader model evaluates and provides feedback. The agent iterates until the outcome is satisfied (configurable, up to 20 iterations).
- **[Multi-agent](https://platform.claude.com/docs/en/managed-agents/multi-agent)** - A coordinator agent delegates to `callable_agents`, each running in its own thread with isolated context but shared filesystem. One level of delegation (no recursion).
- **[Memory](https://platform.claude.com/docs/en/managed-agents/memory)** - Persistent memory stores that survive across sessions. Workspace-scoped text documents with version history, audit trail, and redaction support. Up to 8 stores per session, 100KB per memory.

## Tutorials & Guides

- [Verdent Guides - Developer Guide](https://www.verdent.ai/guides/what-is-claude-managed-agents) - Comprehensive walkthrough for developers.
- [Medium - Honest Pros and Cons](https://medium.com/@unicodeveloper/claude-managed-agents-what-it-actually-offers-the-honest-pros-and-cons-and-how-to-run-agents-52369e5cff14) - Practical evaluation with setup instructions.
- [Thesys - Features, Pricing & Early Adopters](https://www.thesys.dev/blogs/claude-managed-agents) - Overview with early adopter case studies.
- [Avinash Sangle - Which Should You Use?](https://avinashsangle.com/blog/claude-managed-agents) - Managed Agents vs Agent SDK decision guide.
- [BSWEN - Managed Agents vs Agent SDK](https://docs.bswen.com/blog/2026-04-09-claude-managed-agents-vs-agent-sdk/) - Detailed comparison of both approaches.
- [BSWEN - Agent Platform Comparison](https://docs.bswen.com/blog/2026-04-09-agent-platform-comparison/) - Claude Managed Agents vs OpenAI vs self-hosted.

## Community Projects

- [CelestoAI/agentor](https://github.com/CelestoAI/agentor) - Open-source alternative inspired by Claude Managed Agents.
- [rogeriochaves/open-managed-agents](https://github.com/rogeriochaves/open-managed-agents) - Self-hostable, open-source version with multi-LLM support.
- [linear/claude-managed-agents-demo](https://github.com/linear/claude-managed-agents-demo) - Linear + Claude Managed Agents integration example.
- [0xArx/claude-managed-agents-skill](https://github.com/0xArx/claude-managed-agents-skill) - Claude Code skill for building with the CMA API.
- [Attilio81/MCP_CMA](https://github.com/Attilio81/MCP_CMA) - MCP server exposing CMA docs to Claude Desktop/Code.
- [contro1-hq/centcom-claude-managed-agents](https://github.com/contro1-hq/centcom-claude-managed-agents) - CENTCOM connector for Claude Managed Agents.

## Integrations

- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/agents/providers/anthropic) - Anthropic provider for Microsoft's agent framework.
- [Promptfoo](https://www.promptfoo.dev/docs/providers/claude-agent-sdk/) - Claude Agent SDK provider for evaluation and testing.
- [Composio](https://composio.dev/content/claude-agents-sdk-vs-openai-agents-sdk-vs-google-adk) - Framework comparison and integration support.

## Launch Partners

- **Notion** - Teams delegate coding, slides, and spreadsheet tasks to Claude in parallel.
- **Rakuten** - Specialist agents across product, sales, marketing, finance, and HR, each live in under a week.
- **Asana** - AI Teammates working alongside humans.
- **Vibecode** - Customers deploy AI-native apps ~10x faster.
- **Sentry** - Paired with debugging agent to write patches and open PRs.

## Articles & Press

- [SiliconANGLE](https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/) - "Anthropic launches Claude Managed Agents to speed AI agent development."
- [The New Stack](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/) - "Anthropic wants to run your AI agents for you."
- [InfoWorld](https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html) - "Anthropic rolls out Claude Managed Agents."
- [9to5Mac](https://9to5mac.com/2026/04/09/anthropic-scales-up-with-enterprise-features-for-claude-cowork-and-managed-agents/) - Enterprise features for Claude Cowork and Managed Agents.
- [The Register](https://www.theregister.com/2026/04/09/anthropic_offers_to_host_ai/) - "Anthropic offers to host AI."
- [TechRadar](https://www.techradar.com/pro/go-from-prototype-to-launch-in-days-rather-than-months-anthropic-reveals-claude-managed-agents-promises-to-make-agent-building-10x-faster) - "Prototype to launch in days, not months."
- [Help Net Security](https://www.helpnetsecurity.com/2026/04/09/claude-managed-agents-bring-execution-and-control-to-ai-agent-workflows/) - "Execution and control for AI agent workflows."
- [Analytics Insight](https://www.analyticsinsight.net/news/anthropic-rolls-out-managed-agents-in-claude-to-simplify-enterprise-ai-deployment) - "Simplifying enterprise AI deployment."
- [The Decoder](https://the-decoder.com/anthropic-launches-managed-infrastructure-for-autonomous-ai-agents/) - "Managed infrastructure for autonomous AI agents."
- [Hacker News Discussion](https://news.ycombinator.com/item?id=47693047) - Community discussion thread.

## Videos & Talks

*Know of a video or talk about Claude Managed Agents? [Open a PR!](CONTRIBUTING.md)*

## Managed Agents vs Agent SDK

| Dimension | Managed Agents | Agent SDK |
|---|---|---|
| **Where it runs** | Anthropic's cloud | Your infrastructure (laptop, VPS, K8s) |
| **Agent loop** | Managed by Anthropic | You build and run it |
| **Containers** | Managed cloud sandboxes (Ubuntu 22.04, 8 GB RAM) | Your own environment |
| **Best for** | Long-running async tasks, production workloads | Full runtime control, private network access, compliance (HIPAA, FedRAMP) |
| **Setup effort** | Minimal &mdash; define agent + environment, start session | More setup &mdash; you manage the runtime |
| **Pricing** | Token rates + $0.08/session-hour | Token rates only |

## Related Products

- [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) - The same engine that powers Managed Agents, exposed as a library you run anywhere.
- [Claude Code](https://claude.ai/code) - Anthropic's agentic coding CLI, built on the same underlying technology.
- [Claude Cowork](https://claude.com/blog/claude-managed-agents) - Enterprise collaboration features launched alongside Managed Agents.
- [Anthropic Skills](https://github.com/anthropics/skills) - Official Claude Code skills repository.

## Architecture

From the [engineering blog](https://www.anthropic.com/engineering/managed-agents), the system decouples three components:

1. **Brain** &mdash; Claude model + harness (orchestration loop)
2. **Hands** &mdash; Sandboxed containers with a uniform `execute(name, input) -> string` interface
3. **Session** &mdash; Append-only, durable event log (context engineering applied at runtime)

Key results: p50 time-to-first-token reduced ~60%, p95 reduced >90%. Credentials are structurally isolated from sandboxed code via vault-based tokens.

## Contributing

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the authors have waived all copyright and related or neighboring rights to this work.
