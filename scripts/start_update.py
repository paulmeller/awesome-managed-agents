"""Kick off a Claude Managed Agents session with the awesome-list-curator skill.

This only creates the agent/environment/session and sends the initial message -
it does not wait for the agent to finish. The session runs on Anthropic's side;
scripts/check_update.py polls it separately so no GitHub Actions runner sits
idle for the duration of the search.
"""

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
                            "1. Search for new resources using the search strategy.\n"
                            "2. Assess each candidate against the criteria and score them.\n"
                            "3. Write the assessment JSON and updated README.md to /mnt/session/outputs/.\n"
                            "4. After writing the files, print the assessment JSON, then print the "
                            "exact marker line `===README_START===` followed by the complete updated "
                            "README.md content, followed by `===README_END===`.\n\n"
                            "Only add resources rated A or B.\n\n"
                            "---\n\n"
                            f"{current_readme}"
                        ),
                    }
                ],
            }
        ],
    )

    print(f"Session started: {session.id}")
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"session_id={session.id}\n")


if __name__ == "__main__":
    run()
