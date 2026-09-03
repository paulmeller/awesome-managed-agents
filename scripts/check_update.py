"""Poll a Claude Managed Agents session started by start_update.py.

Does one cheap status check (no streaming, no waiting) and exits. Meant to be
run repeatedly on a short cron until the session goes idle, so no single
GitHub Actions job is ever blocked for the duration of the agent's search.
"""

import os
import sys

from anthropic import Anthropic

SCRIPTS_DIR = os.path.dirname(__file__)
README_PATH = os.path.join(SCRIPTS_DIR, "..", "README.md")

START_MARKER = "===README_START==="
END_MARKER = "===README_END==="


def set_output(**kwargs):
    github_output = os.environ.get("GITHUB_OUTPUT")
    if not github_output:
        return
    with open(github_output, "a") as f:
        for key, value in kwargs.items():
            f.write(f"{key}={value}\n")


def run():
    session_id = os.environ.get("SESSION_ID")
    if not session_id:
        print("No session in progress.")
        set_output(done="false")
        return

    client = Anthropic()
    session = client.beta.sessions.retrieve(session_id)

    if session.status in ("running", "rescheduling"):
        print(f"Session {session_id} still {session.status}.")
        set_output(done="false")
        return

    if session.status == "terminated":
        print(f"Session {session_id} terminated unexpectedly.", file=sys.stderr)
        set_output(done="true", failed="true", changed="false")
        return

    # status == "idle": the agent has finished, collect its output
    collected_text = []
    for event in client.beta.sessions.events.list(session_id, order="asc"):
        if event.type == "agent.message":
            for block in event.content:
                if hasattr(block, "text"):
                    collected_text.append(block.text)

    full_output = "\n".join(collected_text)

    if START_MARKER not in full_output:
        print("No README markers found in agent output. No changes.")
        set_output(done="true", changed="false")
        return

    start_idx = full_output.index(START_MARKER) + len(START_MARKER)
    end_idx = full_output.index(END_MARKER) if END_MARKER in full_output else len(full_output)
    updated_readme = full_output[start_idx:end_idx].strip()

    with open(README_PATH) as f:
        current_readme = f.read()

    if not updated_readme or updated_readme.strip() == current_readme.strip():
        print("No new resources found.")
        set_output(done="true", changed="false")
        return

    with open(README_PATH, "w") as f:
        f.write(updated_readme + "\n")

    print("README.md updated with new resources.")
    set_output(done="true", changed="true")


if __name__ == "__main__":
    run()
