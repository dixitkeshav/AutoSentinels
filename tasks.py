from crewai import Task


def diagnosis_task(agent, telemetry_summary: str):
    return Task(
        description=(
            "Analyze the following vehicle telemetry and identify potential component failures.\n\n"
            f"Telemetry Data:\n{telemetry_summary}\n\n"
            "Clearly state:\n"
            "- Which component is likely failing\n"
            "- Why it is failing\n"
            "- Severity level (low / medium / high)\n"
        ),
        expected_output="A concise technical diagnosis with severity.",
        agent=agent,
    )


def engagement_task(agent, diagnosis_output: str):
    return Task(
        description=(
            "Explain the vehicle issue to the owner in simple language.\n\n"
            f"Diagnosis:\n{diagnosis_output}\n\n"
            "- What is wrong\n"
            "- Is it safe to drive\n"
            "- What to do next\n"
        ),
        expected_output="A calm, user-friendly explanation.",
        agent=agent,
    )


def insights_task(agent, diagnosis_output: str):
    return Task(
        description=(
            "Extract OEM-level insights from the diagnosis.\n\n"
            f"Diagnosis Summary:\n{diagnosis_output}\n\n"
            "- Potential design or quality issues\n"
            "- Whether this could be recurring\n"
            "- Recommended investigation\n"
        ),
        expected_output="Actionable manufacturing insights.",
        agent=agent,
    )
