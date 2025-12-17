from crewai import Agent
from dotenv import load_dotenv
import os

load_dotenv()

print("ANTHROPIC_API_KEY loaded:", bool(os.getenv("ANTHROPIC_API_KEY")))
MODEL = "anthropic/claude-3-haiku-20240307"


def diagnosis_agent():
    return Agent(
        role="Vehicle Diagnosis Agent",
        goal="Detect and explain potential vehicle component failures using telemetry data",
        backstory=(
            "You are an expert automotive diagnostic engineer. "
            "You analyze vehicle sensor data to identify early signs of failure."
        ),
        llm=MODEL,
        verbose=True,
    )


def engagement_agent():
    return Agent(
        role="Customer Engagement Agent",
        goal="Explain vehicle issues clearly and recommend next steps to the vehicle owner",
        backstory=(
            "You are a customer-facing service advisor. "
            "You translate technical faults into clear, calm guidance."
        ),
        llm=MODEL,
        verbose=True,
    )


def insights_agent():
    return Agent(
        role="Manufacturing Insights Agent",
        goal="Identify patterns and insights useful for OEM quality teams",
        backstory=(
            "You are a quality engineer at an OEM. "
            "You detect patterns across failures to improve manufacturing."
        ),
        llm=MODEL,
        verbose=True,
    )
