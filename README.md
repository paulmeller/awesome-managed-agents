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

## Community Projects

- [CelestoAI/agentor](https://github.com/CelestoAI/agentor) - Open-source alternative inspired by Claude Managed Agents.
- [rogeriochaves/open-managed-agents](https://github.com/rogeriochaves/open-managed-agents) - Self-hostable version with multi-LLM support.
- [linear/claude-managed-agents-demo](https://github.com/linear/claude-managed-agents-demo) - Integration example connecting Linear with Claude Managed Agents.
- [0xArx/claude-managed-agents-skill](https://github.com/0xArx/claude-managed-agents-skill) - Claude Code skill for building with the Managed Agents API.
- [Attilio81/MCP_CMA](https://github.com/Attilio81/MCP_CMA) - MCP server exposing Managed Agents docs to Claude Desktop and Claude Code.
- [contro1-hq/centcom-claude-managed-agents](https://github.com/contro1-hq/centcom-claude-managed-agents) - CENTCOM connector for Claude Managed Agents.

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

## Videos and Talks

*Know of a video or talk about Claude Managed Agents? [Open a PR!](CONTRIBUTING.md)*

## Related Products

- [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) - Same engine as Managed Agents, exposed as a library you run on your own infrastructure.
- [Claude Code](https://claude.ai/code) - Agentic coding CLI by Anthropic, built on the same underlying technology.
- [Anthropic Skills](https://github.com/anthropics/skills) - Official Claude Code skills repository.

## Automated Updates

This list is itself maintained using Claude Managed Agents. A [weekly workflow](.github/workflows/update.yml) spins up a Managed Agents session with a [custom curator skill](skills/awesome-list-curator/SKILL.md) that searches the web for new resources, scores each candidate against quality criteria, and opens a PR with any additions. See [`scripts/`](scripts/) for the implementation.

## Contributing

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.
