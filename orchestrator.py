from crewai import Crew, Process
from agents import diagnosis_agent, engagement_agent, insights_agent
from tasks import diagnosis_task, engagement_task, insights_task


def run_autosentinels_pipeline(telemetry_summary: str):
    # Create agents
    diag_agent = diagnosis_agent()
    engage_agent = engagement_agent()
    oem_agent = insights_agent()

    # Create tasks
    diag_task = diagnosis_task(diag_agent, telemetry_summary)
    engage_task = engagement_task(engage_agent, "{diagnosis_task}")
    oem_task = insights_task(oem_agent, "{diagnosis_task}")

    # Create crew
    crew = Crew(
        agents=[diag_agent, engage_agent, oem_agent],
        tasks=[diag_task, engage_task, oem_task],
        process=Process.sequential,
        verbose=True,
    )

    crew.kickoff()

    return {
        "diagnosis": diag_task.output,
        "customer_message": engage_task.output,
        "oem_insights": oem_task.output,
    }
