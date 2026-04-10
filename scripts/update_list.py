"""Use Claude Managed Agents with the awesome-list-curator skill to find and assess new resources."""

import json
import os
import sys

from anthropic import Anthropic

SCRIPTS_DIR = os.path.dirname(__file__)
README_PATH = os.path.join(SCRIPTS_DIR, "..", "README.md")
SKILL_ID_FILE = os.path.join(SCRIPTS_DIR, "..", ".skill-id")


def get_skill_id():
    """Read the skill ID from the .skill-id file, or from CURATOR_SKILL_ID env var."""
    skill_id = os.environ.get("CURATOR_SKILL_ID")
    if skill_id:
        return skill_id
    if os.path.exists(SKILL_ID_FILE):
        with open(SKILL_ID_FILE) as f:
            return f.read().strip()
    print("No skill ID found. Run setup_skill.py first or set CURATOR_SKILL_ID.", file=sys.stderr)
    sys.exit(1)


def run():
    client = Anthropic()
    skill_id = get_skill_id()

    with open(README_PATH) as f:
        current_readme = f.read()

    agent = client.beta.agents.create(
        name="Awesome List Updater",
        model="claude-sonnet-4-6",
        system=(
            "You are a research agent that maintains an awesome-list for Claude Managed Agents. "
            "Use the awesome-list-curator skill to guide your search strategy, assessment criteria, "
            "and output format. Follow the skill instructions exactly."
        ),
        tools=[{"type": "agent_toolset_20260401"}],
        skills=[{"type": "custom", "skill_id": skill_id, "version": "latest"}],
    )

    environment = client.beta.environments.create(
        name="updater-env",
        config={"type": "cloud", "networking": {"type": "unrestricted"}},
    )

    session = client.beta.sessions.create(
        agent=agent.id,
        environment_id=environment.id,
        title="Weekly awesome-list update",
    )

    print(f"Session created: {session.id}")
    print(f"Using skill: {skill_id}")

    with client.beta.sessions.events.stream(session.id) as stream:
        client.beta.sessions.events.send(
            session.id,
            events=[
                {
                    "type": "user.message",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Here is the current README.md for the awesome-managed-agents repo.\n\n"
                                "Use the awesome-list-curator skill to:\n"
                                "1. Search for new resources using the search strategy defined in the skill.\n"
                                "2. Assess each candidate against the skill's criteria and score them.\n"
                                "3. Write the assessment to /mnt/session/outputs/assessment.json.\n"
                                "4. Write the updated README.md to /mnt/session/outputs/README.md.\n\n"
                                "Only add resources rated A or B.\n\n"
                                "---\n\n"
                                f"{current_readme}"
                            ),
                        }
                    ],
                }
            ],
        )

        for event in stream:
            match event.type:
                case "agent.tool_use":
                    print(f"  [tool: {event.name}]")
                case "agent.message":
                    for block in event.content:
                        if hasattr(block, "text"):
                            print(f"  {block.text[:200]}")
                case "session.status_idle":
                    print("Agent finished.")
                    break
                case "session.status_terminated":
                    print("Agent terminated unexpectedly.", file=sys.stderr)
                    sys.exit(1)

    # Download outputs from the session
    files = client.beta.files.list(scope_id=session.id)

    readme_file = None
    assessment_file = None
    for f in files.data:
        if f.filename == "README.md":
            readme_file = f
        elif f.filename == "assessment.json":
            assessment_file = f

    # Print assessment summary if available
    if assessment_file:
        content = client.beta.files.content(assessment_file.id)
        assessment = json.loads(content.text)
        print(f"\nAssessment: {assessment['candidates_found']} found, {assessment['candidates_accepted']} accepted")
        for c in assessment.get("candidates", []):
            status = "+" if c["rating"] in ("A", "B") else "-"
            print(f"  [{status}] [{c['rating']}] {c['title']} -> {c['section']}")

    if readme_file is None:
        print("No README.md found in session outputs. No changes.", file=sys.stderr)
        sys.exit(0)

    content = client.beta.files.content(readme_file.id)
    updated_readme = content.text

    if updated_readme.strip() == current_readme.strip():
        print("No new resources found.")
        sys.exit(0)

    with open(README_PATH, "w") as f:
        f.write(updated_readme)

    print("README.md updated with new resources.")


if __name__ == "__main__":
    run()
