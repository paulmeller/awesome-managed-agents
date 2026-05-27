# Awesome Claude Managed Agents [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A fully managed, server-side agent runtime by Anthropic for building and deploying cloud-hosted AI agents at scale. Define an agent, an environment, and start a session &mdash; Anthropic handles the agent loop, sandboxed containers, tool execution, and event streaming.

## Contents

- [Official Resources](#official-resources)
- [SDKs](#sdks)
- [CLI](#cli)
- [Documentation](#documentation)
- [Tutorials and Guides](#tutorials-and-guides)
- [Community Projects](#community-projects)
- [Integrations](#integrations)
- [Articles and Press](#articles-and-press)
- [Videos and Talks](#videos-and-talks)
- [Related Products](#related-products)

## Official Resources

- [Product Announcement](https://claude.com/blog/claude-managed-agents) - Official blog post introducing Claude Managed Agents.
- [Engineering Deep-Dive](https://www.anthropic.com/engineering/managed-agents) - Architecture post on decoupling the brain from the hands.
- [Pricing](https://platform.claude.com/docs/en/about-claude/pricing) - Standard token rates plus $0.08 per session-hour metered to the millisecond.
- [Research Preview Access Form](https://claude.com/form/claude-managed-agents) - Request access to Outcomes, Multi-agent, and Memory features.

## SDKs

All SDKs expose Managed Agents under `client.beta.agents`, `client.beta.environments`, and `client.beta.sessions`.

- [Python SDK](https://pypi.org/project/anthropic/) - Install with `pip install anthropic`, requires version 0.92.0 or later.
- [TypeScript SDK](https://www.npmjs.com/package/@anthropic-ai/sdk) - Install with `npm install @anthropic-ai/sdk`, requires version 0.86.0 or later.
- [Go SDK](https://github.com/anthropics/anthropic-sdk-go) - Install with `go get github.com/anthropics/anthropic-sdk-go`, requires version 1.33.0 or later.
- [Java SDK](https://central.sonatype.com/artifact/com.anthropic/anthropic-java) - Available via Maven or Gradle with `com.anthropic:anthropic-java`.
- [C# SDK](https://www.nuget.org/packages/Anthropic) - Install with `dotnet add package Anthropic`.
- [Ruby SDK](https://rubygems.org/gems/anthropic) - Install with `bundle add anthropic`.
- [PHP SDK](https://packagist.org/packages/anthropic-ai/sdk) - Install with `composer require anthropic-ai/sdk`.

## CLI

- [Anthropic CLI](https://github.com/anthropics/anthropic-cli) - Go-based `ant` CLI for managing agents, environments, and sessions from the terminal.

## Documentation

- [Overview](https://platform.claude.com/docs/en/managed-agents/overview) - What Managed Agents are and when to use them.
- [Quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart) - Create an agent, environment, and session in minutes.
- [Agent Setup](https://platform.claude.com/docs/en/managed-agents/agent-setup) - Configure model, system prompt, tools, MCP servers, and skills.
- [Sessions](https://platform.claude.com/docs/en/managed-agents/sessions) - Session lifecycle and status management.
- [Environments](https://platform.claude.com/docs/en/managed-agents/environments) - Container configuration, packages, and networking modes.
- [Tools](https://platform.claude.com/docs/en/managed-agents/tools) - Built-in tools, custom tools, and MCP toolsets.
- [Events and Streaming](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) - SSE-based event protocol for real-time communication with sessions.
- [Cloud Containers](https://platform.claude.com/docs/en/managed-agents/cloud-containers) - Container specs including Ubuntu 22.04, 8 GB RAM, and 10 GB disk.
- [Skills](https://platform.claude.com/docs/en/managed-agents/skills) - Reusable filesystem-based expertise packages for domain-specific workflows.
- [MCP Connector](https://platform.claude.com/docs/en/managed-agents/mcp-connector) - Remote MCP server integration with vault-based authentication.
- [Permission Policies](https://platform.claude.com/docs/en/managed-agents/permission-policies) - Configure `always_allow` and `always_ask` tool execution policies.
- [Multi-agent](https://platform.claude.com/docs/en/managed-agents/multi-agent) - Coordinator agents delegating to callable agents in isolated threads (research preview).
- [Memory](https://platform.claude.com/docs/en/managed-agents/memory) - Persistent memory stores that survive across sessions (research preview).
- [Outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes) - Self-evaluation with rubrics and iterative improvement (research preview).
- [API Reference](https://platform.claude.com/docs/en/api/beta/sessions) - Full API specification for all endpoints.

## Tutorials and Guides

- [Verdent Developer Guide](https://www.verdent.ai/guides/what-is-claude-managed-agents) - Comprehensive walkthrough for developers getting started.
- [Honest Pros and Cons](https://medium.com/@unicodeveloper/claude-managed-agents-what-it-actually-offers-the-honest-pros-and-cons-and-how-to-run-agents-52369e5cff14) - Practical evaluation with setup instructions.
- [Features, Pricing and Early Adopters](https://www.thesys.dev/blogs/claude-managed-agents) - Overview of capabilities with early adopter case studies.
- [Which Should You Use?](https://avinashsangle.com/blog/claude-managed-agents) - Decision guide for choosing between Managed Agents and Agent SDK.
- [Managed Agents vs Agent SDK](https://docs.bswen.com/blog/2026-04-09-claude-managed-agents-vs-agent-sdk/) - Detailed comparison of both approaches.
- [Agent Platform Comparison](https://docs.bswen.com/blog/2026-04-09-agent-platform-comparison/) - Comparison of Claude Managed Agents, OpenAI, and self-hosted alternatives.
- [Build Your First Claude Agent in 15 Minutes](https://findskill.ai/blog/build-first-claude-agent-tutorial/) - Step-by-step tutorial with complete Python and TypeScript code walking through agent creation, environment setup, session launch, and event streaming.
- [Everything You Need to Know](https://www.lowcode.agency/blog/claude-managed-agents) - Comprehensive guide covering architecture, built-in tools, pricing, early adopter case studies, and when to use Managed Agents versus the Messages API or Agent SDK.
- [Deploy Your First Production Agent in 10 Minutes](https://medium.com/@roeyzalta/claude-managed-agents-deploy-your-first-production-agent-in-10-minutes-8af00f608209) - Hands-on walkthrough with practical code and production examples from Sentry, Rakuten, and Asana.
- [Claude Managed Agents + Azure: The Multi-Cloud AI Strategy](https://medium.com/@roeyzalta/claude-managed-agents-azure-the-multi-cloud-ai-strategy-nobodys-talking-about-76da68b16877) - Analysis of integrating Managed Agents into Azure-first enterprise stacks, covering multi-cloud architectural patterns from a Microsoft Azure engineering perspective.
- [Python Tutorial with Code and OpenAI Comparison](https://pasqualepillitteri.it/en/news/789/claude-managed-agents-python-tutorial-code-openai) - Complete Python walkthrough with four working examples covering ClaudeSDKClient, custom tools with the @tool decorator, OAuth credential vault for Slack, and a technical comparison with the OpenAI Responses API.
- [Trying Claude Managed Agents for Building Agents at Scale](https://azukiazusa.dev/en/blog/claude-managed-agents/) - Developer walkthrough of the Console UI from agent creation to session launch, including a practical GitHub pull request demo using GitHub MCP server authentication via Vault.
- [Build a Claude Managed Agent on Vercel](https://vercel.com/kb/guide/claude-managed-agent-vercel) - Official Vercel guide for building an internal knowledge agent with per-user credential vaults, durable SSE polling via Vercel Workflows, and a Next.js chat UI connecting GitHub, Notion, and Slack.
- [Claude Managed Agents vs Amazon Bedrock AgentCore](https://dev.to/aws-builders/agent-as-a-service-comparing-claude-managed-agents-and-amazon-bedrock-agentcore-22eb) - Side-by-side comparison of both agent-as-a-service platforms covering architecture philosophy, pricing model differences, and a clear decision framework for choosing between them.
- [I Built a Claude Managed Agent in 30 Minutes](https://aiblewmymind.substack.com/p/claude-managed-agents-explained-demo) - Practical build demo connecting a feedback agent to Notion and a live website, with five enterprise case studies covering Notion, Rakuten, Asana, Sentry, and Vibecode.
- [Build, Stream, Test: Your First Claude Managed Agent in 30 Minutes](https://medium.com/data-science-collective/build-stream-test-your-first-claude-managed-agent-in-30-minutes-d83fe01b7b45) - Hands-on Python tutorial building a retail competitive price monitor with real-time SSE streaming and output grading using the Outcomes API.
- [Deep Dive: How Claude Managed Agents Solve the AI Scaffolding Nightmare](https://medium.com/@jiten.p.oswal/deep-dive-how-anthropics-claude-managed-agents-solve-the-ai-scaffolding-nightmare-2e7289c22f06) - Technical analysis of the architecture covering credential isolation via dedicated MCP proxies, durable session context management, and the decoupled sandbox model.
- [Claude Managed Agents Deep Dive](https://dev.to/bean_bean/claude-managed-agents-deep-dive-anthropics-new-ai-agent-infrastructure-2026-3286) - Comprehensive coverage of architecture, real-world pricing calculations, a Managed Agents vs self-hosted comparison table, and a preview of upcoming features such as private networking and regional deployments.
- [Claude Managed Agents Pricing: Costs and Limits (2026)](https://www.verdent.ai/guides/claude-managed-agents-pricing) - Detailed pricing breakdown with worked cost calculations, prompt caching analysis, batch API limitations, and guidance on when Managed Agents is cost-effective versus self-hosted alternatives.
- [Building a Home Personal Assistant with Claude Managed Agents](https://dev.to/trknhr/building-a-home-personal-assistant-with-claude-managed-agents-5a8f) - Hands-on walkthrough building a Slack-connected household assistant using Managed Agents with Lambda, DynamoDB, and EventBridge Scheduler for async processing and custom memory tools.
- [From Building to Deploying: The Complete Guide to Anthropic's Claude Managed Agents](https://atalupadhyay.wordpress.com/2026/04/11/from-building-to-deploying-the-complete-guide-to-anthropics-claude-managed-agents/) - Complete guide covering the conceptual foundation, decoupled sandbox architecture, open-source trade-offs, and hands-on labs building two agents — a Slack support agent and a long-running deep research pipeline — with production hardening patterns.
- [Claude Managed Agents: The Complete Developer Guide (2026)](https://aiworkflows.tools/blog/claude-managed-agents-complete-guide-2026) - Complete developer guide covering architecture deep-dives, Python and TypeScript quickstarts, pricing tables with worked examples, a Claude Agent SDK comparison matrix, and an honest vendor lock-in assessment.
- [Claude Managed Agents: The Fourth Way to Build AI Agents With Claude](https://cobusgreyling.medium.com/claude-managed-agents-0f47df3caa6f) - Frames Managed Agents as the fourth paradigm for building with Claude alongside the Agent SDK, Markdown Definitions, and Agent Teams, with working Python code and a brain-vs-hands architecture breakdown.
- [Claude Managed Agents: The April 2026 Cloud Deployment Guide](https://www.aimagicx.com/blog/claude-managed-agents-cloud-deployment-guide-2026) - Engineering write-up from deploying three production workflows the week of launch, with detailed cost tables for each workload, observability trace structure, gVisor isolation model, and a decision matrix for Managed Agents versus self-hosted alternatives.
- [Claude Managed Agents in 2026: The Complete Developer's Guide](https://www.eesel.ai/blog/claude-managed-agents) - Complete developer guide with architectural analysis of the decoupled brain-from-hands model, including Anthropic's reported 60% p50 and 90% p95 time-to-first-token improvements from lazy sandbox provisioning, pricing breakdown, and real-world case studies.
- [Anthropic's New Agent Platform and What It Means for SMEs](https://medium.com/@ai_93276/claude-managed-agents-anthropics-new-agent-platform-and-what-it-means-for-smes-57586acfaa97) - SME-focused analysis covering the decoupled architecture, structural credential security model, build-vs-buy economic framework with concrete cost comparisons, and guidance on when the platform makes sense for smaller engineering teams.

## Community Projects

- [CelestoAI/agentor](https://github.com/CelestoAI/agentor) - Open-source alternative inspired by Claude Managed Agents.
- [rogeriochaves/open-managed-agents](https://github.com/rogeriochaves/open-managed-agents) - Self-hostable version with multi-LLM support.
- [linear/claude-managed-agents-demo](https://github.com/linear/claude-managed-agents-demo) - Integration example connecting Linear with Claude Managed Agents.
- [0xArx/claude-managed-agents-skill](https://github.com/0xArx/claude-managed-agents-skill) - Claude Code skill for building with the Managed Agents API.
- [Attilio81/MCP_CMA](https://github.com/Attilio81/MCP_CMA) - MCP server exposing Managed Agents docs to Claude Desktop and Claude Code.
- [contro1-hq/centcom-claude-managed-agents](https://github.com/contro1-hq/centcom-claude-managed-agents) - CENTCOM connector for Claude Managed Agents.
- [ucsandman/DashClaw](https://github.com/ucsandman/DashClaw) - AI agent observability and governance platform with a real-time dashboard, guard policies, audit trail, and an MCP server for integrating with Claude Managed Agents.
- [vercel-labs/claude-managed-agents-starter](https://github.com/vercel-labs/claude-managed-agents-starter) - Official Vercel Labs open-source starter template for an internal knowledge agent connecting GitHub, Notion, and Slack via MCP, built with Next.js 16, Better Auth, Neon Postgres, and Vercel Workflows.
- [stainlu/openclaw-managed-agents](https://github.com/stainlu/openclaw-managed-agents) - Self-hostable open alternative implementing the same four-primitive API shape as Claude Managed Agents using OpenClaw, supporting any model provider with pre-warmed container pools, durable sessions, subagent delegation, per-session quotas, and one-command deploy scripts for Hetzner, AWS, and GCP.
- [agentstep/gateway](https://github.com/agentstep/gateway) - Self-hosted, open-source Anthropic Managed Agents-compatible gateway supporting six agent engines (Claude, Codex, OpenCode, Gemini, Factory, Pi) and eleven sandbox providers. Includes a web UI, CLI, per-session cost tracking, and OpenTelemetry tracing.
- [openma](https://github.com/open-ma/open-managed-agents) - Self-hosted, open-source implementation of Anthropic's Managed Agents API. Wire-compatible with the official SDKs; runs on Cloudflare Workers + Durable Objects or Node. Includes an ACP bridge for routing sessions to locally-installed Claude Code/Codex/Gemini. Apache 2.0.

## Integrations

- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/agents/providers/anthropic) - Anthropic provider for the Microsoft agent framework.
- [Promptfoo](https://www.promptfoo.dev/docs/providers/claude-agent-sdk/) - Evaluation and testing provider for Claude agents.
- [Composio](https://composio.dev/content/claude-agents-sdk-vs-openai-agents-sdk-vs-google-adk) - Framework comparison and integration support across agent platforms.

## Articles and Press

- [SiliconANGLE](https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/) - Anthropic launches Claude Managed Agents to speed AI agent development.
- [The New Stack](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/) - Anthropic wants to run your AI agents for you.
- [InfoWorld](https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html) - Anthropic rolls out Claude Managed Agents.
- [9to5Mac](https://9to5mac.com/2026/04/09/anthropic-scales-up-with-enterprise-features-for-claude-cowork-and-managed-agents/) - Enterprise features for Claude Cowork and Managed Agents.
- [The Register](https://www.theregister.com/2026/04/09/anthropic_offers_to_host_ai/) - Anthropic offers to host AI.
- [TechRadar](https://www.techradar.com/pro/go-from-prototype-to-launch-in-days-rather-than-months-anthropic-reveals-claude-managed-agents-promises-to-make-agent-building-10x-faster) - Prototype to launch in days rather than months.
- [Help Net Security](https://www.helpnetsecurity.com/2026/04/09/claude-managed-agents-bring-execution-and-control-to-ai-agent-workflows/) - Execution and control for AI agent workflows.
- [Analytics Insight](https://www.analyticsinsight.net/news/anthropic-rolls-out-managed-agents-in-claude-to-simplify-enterprise-ai-deployment) - Simplifying enterprise AI deployment.
- [The Decoder](https://the-decoder.com/anthropic-launches-managed-infrastructure-for-autonomous-ai-agents/) - Managed infrastructure for autonomous AI agents.
- [Hacker News Discussion](https://news.ycombinator.com/item?id=47693047) - Community discussion thread from launch day.
- [WIRED](https://www.wired.com/story/anthropic-launches-claude-managed-agents/) - In-depth launch coverage including demos from Notion and quotes from Anthropic engineering leadership on the infrastructure challenge Managed Agents solves.
- [WinBuzzer](https://winbuzzer.com/2026/04/10/anthropic-launches-claude-managed-agents-enterprise-ai-xcxwbn/) - Enterprise-focused analysis covering the OpenClaw ecosystem context, competitive landscape against Amazon Bedrock and Azure AI, and strategic implications of Anthropic's infrastructure push.
- [Data Center Knowledge](https://www.datacenterknowledge.com/data-center-software/anthropic-targets-ai-data-center-bottleneck-with-claude-managed-agents) - Industry analysis of how Managed Agents shifts AI workload control to Anthropic's platform, with commentary from Moor Insights and Constellation Research analysts on enterprise lock-in and operational implications.
- [Mac Observer](https://www.macobserver.com/news/anthropic-expands-claude-cowork-and-launches-managed-agents-for-enterprise-use/) - Coverage of Anthropic's simultaneous Managed Agents public beta launch and Claude Cowork general availability, including new enterprise features such as role-based access controls and expanded OpenTelemetry support.

## Videos and Talks

- [Introducing Claude Managed Agents](https://www.youtube.com/watch?v=I1BvAHOsjBU) - Official product overview of the composable APIs including native MCP, tool integrations, memory, and multi-agent coordination features.
- [Claude Managed Agents Full Tutorial: How to Setup Your First AI Agent](https://www.youtube.com/watch?v=OU4gE2M45vY) - Hands-on walkthrough building and deploying Claude Managed Agents from scratch, covering sessions, environments, and real-world integrations.
- [Claude Managed Agents Full Tutorial & Honest Review](https://www.youtube.com/watch?v=Pve75_Zi8oE) - In-depth tutorial and honest review from a developer running 31 scheduled Claude agents, with production insights on costs, patterns, and limitations.
- [What is Managed Agents?](https://www.youtube.com/watch?v=NLWiIj47IdI) - Concise explainer of the Managed Agents API covering agents, environments, sessions, and how success criteria drive autonomous execution.
- [How Notion Built with Claude Managed Agents](https://www.youtube.com/watch?v=45hPRdfDEsI) - Notion product manager Eric Liu demonstrates delegating complex work to Claude inside a workspace, showing engineers shipping code and teams building websites and presentations using Managed Agents in production.
- [Anthropic drops Claude Managed Agents: here's an explanation and demo of what it actually is](https://www.youtube.com/watch?v=5z1EX77_3po) - Clear explanation and live demo from AI educator Edward Donner clarifying what Managed Agents is, who it is for, and showing a working build with a companion GitHub repository.
- [Claude Managed Agents Clearly Explained (and why it matters)](https://www.youtube.com/watch?v=nAOyErphp5M) - Interview-style breakdown of the four user personas for Managed Agents, real cost data from a live deployment, and a decision framework for when the platform ROI justifies the spend.
- [Claude Managed Agents Just Dropped, And It Kills n8n](https://www.youtube.com/watch?v=Ob5Vu-gD3mo) - Practical walkthrough building a transcript-to-ClickUp agent using credential vaults to connect MCP tools without API keys, with a full tour of sessions, the debugging timeline, environments, vaults, analytics, and cost tracking.
- [Claude Code's NEW Managed Agents Just Changed EVERYTHING](https://www.youtube.com/watch?v=SSPy3cCSLuc) - Live SaaS build demo showing how Harbor Build, an AI website builder that ships production Astro sites with Stripe checkout, was built on Managed Agents, with a full walkthrough of vault-scoped credentials, custom MCP tools, all 8 built-in tools, and a live universal scraper build.
- [Claude Managed Agents: Deploy AI Agents That Run for Hours](https://www.youtube.com/watch?v=DpfLbBuhHOg) - Tutorial building a complete Next.js app on Managed Agents covering all four core primitives, the Console, CLI, and SDK, plus how to assign skills, tools, and MCP servers to remote cloud agents.
- [Claude Managed Agents is AMAZING. Here's How to Build Any Agent in 16 Minutes](https://www.youtube.com/watch?v=n1je-98lvsQ) - Practical walkthrough demonstrating the four core concepts by building a YouTube content planner agent connected to Notion, targeting business users and knowledge workers new to agent development.

## Related Products

- [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) - Same engine as Managed Agents, exposed as a library you run on your own infrastructure.
- [Claude Code](https://claude.ai/code) - Agentic coding CLI by Anthropic, built on the same underlying technology.
- [Anthropic Skills](https://github.com/anthropics/skills) - Official Claude Code skills repository.

## Automated Updates

This list is itself maintained using Claude Managed Agents. A [weekly workflow](.github/workflows/update-list.yml) spins up a Managed Agents session with a [custom curator skill](skills/awesome-list-curator/SKILL.md) that searches the web for new resources, scores each candidate against quality criteria, and opens a PR with any additions. See [`scripts/`](scripts/) for the implementation.

## Contributing

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.
