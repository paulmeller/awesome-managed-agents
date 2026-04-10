---
name: awesome-list-curator
description: Finds, assesses, and curates new resources for an awesome-list about Claude Managed Agents. Use when searching for and evaluating blog posts, GitHub repos, tutorials, videos, and press coverage to add to a curated list.
---

# Awesome List Curator

A skill for discovering and evaluating new resources to add to an awesome-list.

## Search Strategy

Run multiple searches to cover different resource types. Use `web_search` for each:

1. **Blog posts and tutorials** — Search for recent posts teaching people how to use Claude Managed Agents. Try queries like:
   - `"Claude Managed Agents" tutorial`
   - `"Claude Managed Agents" guide`
   - `"Managed Agents" Anthropic blog`
   - `site:medium.com "Claude Managed Agents"`
   - `site:dev.to "Claude Managed Agents"`

2. **GitHub repositories** — Search for community projects and tools. Try:
   - `"Claude Managed Agents" site:github.com`
   - `"managed-agents" anthropic site:github.com`
   - `claude managed agents sdk site:github.com`

3. **Press and news** — Search for coverage from tech publications:
   - `"Claude Managed Agents" news`
   - `Anthropic "Managed Agents" launch`

4. **Videos and talks** — Search for demos and conference talks:
   - `"Claude Managed Agents" site:youtube.com`
   - `"Claude Managed Agents" talk OR demo OR walkthrough`

5. **Integrations** — Search for framework and platform integrations:
   - `"Claude Managed Agents" integration`
   - `"Claude Managed Agents" plugin OR connector OR provider`

## Assessment Criteria

For each candidate resource, evaluate against these criteria. A resource must pass ALL required criteria and score well on quality signals.

### Required (must pass all)

- **Exists** — The URL is accessible. Use `web_fetch` to verify.
- **Relevant** — Directly about Claude Managed Agents, not just Claude in general.
- **Not a duplicate** — Not already in the list (check URLs AND content — same article on different domains counts as duplicate).
- **Not spam** — Not a low-effort SEO article, affiliate link farm, or auto-generated content.

### Quality Signals (aim for 3+ out of 5)

- **Substantive** — Contains original insight, working code, or meaningful analysis (not just a product summary).
- **Accurate** — Technical claims are correct based on what you know about Managed Agents.
- **Maintained** — For repos: has recent commits, a README, and isn't archived. For articles: published within the last 6 months.
- **Useful** — Would help a developer building with Managed Agents.
- **Credible** — From a known publication, established developer, or official source.

### Scoring

Rate each resource:

- **A** — High quality, clearly belongs in the list. Add it.
- **B** — Decent quality, adds value. Add it.
- **C** — Borderline. Skip unless the section is sparse.
- **D** — Low quality or barely relevant. Skip.

Only add resources rated A or B.

## Output Format

Write your assessment to `/mnt/session/outputs/assessment.json` as:

```json
{
  "searched_at": "2026-04-11T12:00:00Z",
  "queries_run": ["query1", "query2"],
  "candidates_found": 12,
  "candidates_accepted": 3,
  "candidates": [
    {
      "title": "Resource Name",
      "url": "https://example.com/resource",
      "section": "Tutorials and Guides",
      "description": "Description starting uppercase, ending with period.",
      "rating": "A",
      "rationale": "Why this resource was accepted or rejected."
    }
  ]
}
```

Then write the complete updated README.md to `/mnt/session/outputs/README.md`.

## Awesome List Formatting Rules

Every list item must follow this exact format:

```
- [Name](URL) - Description starting with uppercase, ending with period.
```

Additional rules:
- Add new items at the BOTTOM of the appropriate section.
- Never remove existing items.
- No License section in the README.
- Top description describes the subject, not the list.
- Table of contents section must be named "Contents".
- Contributing and Footnotes must not appear in Contents.
- Use ` - ` (space-dash-space) between link and description.
- Descriptions must not repeat the link text.
