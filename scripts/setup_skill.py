"""Upload the awesome-list-curator skill to Anthropic. Run once, then store the skill ID."""

import json
import os

from anthropic import Anthropic
from anthropic.lib import files_from_dir

SKILL_DIR = os.path.join(os.path.dirname(__file__), "..", "skills", "awesome-list-curator")
SKILL_ID_FILE = os.path.join(os.path.dirname(__file__), "..", ".skill-id")


def run():
    client = Anthropic()

    # Check if skill already exists
    if os.path.exists(SKILL_ID_FILE):
        with open(SKILL_ID_FILE) as f:
            skill_id = f.read().strip()
        print(f"Skill already exists: {skill_id}")
        print("Creating new version...")
        client.beta.skills.versions.create(
            skill_id=skill_id,
            files=files_from_dir(SKILL_DIR),
            betas=["skills-2025-10-02"],
        )
        print("Skill version updated.")
        return

    skill = client.beta.skills.create(
        display_title="Awesome List Curator",
        files=files_from_dir(SKILL_DIR),
        betas=["skills-2025-10-02"],
    )

    with open(SKILL_ID_FILE, "w") as f:
        f.write(skill.id)

    print(f"Skill created: {skill.id}")
    print(f"Stored skill ID in .skill-id")


if __name__ == "__main__":
    run()
