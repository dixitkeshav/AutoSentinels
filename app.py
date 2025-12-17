import streamlit as st
from orchestrator import run_autosentinels_pipeline

st.set_page_config(
    page_title="AutoSentinels | Agentic AI",
    layout="wide",
)

st.title("🚗 AutoSentinels — Agentic Vehicle Intelligence")

st.markdown(
    """
    **AutoSentinels** uses multiple AI agents to analyze vehicle telemetry,
    explain issues to drivers, and surface insights for OEM teams.
    """
)

st.subheader("📡 Vehicle Telemetry Input")

default_telemetry = """
VIN: FAULTVIN9999999999
Coolant Temperature: 125°C
Coolant Pressure: 3.0 bar
Engine RPM: 3500
Vibration Level: High
Battery Voltage: 11.8V
Ambient Temperature: 32°C
"""

telemetry_input = st.text_area(
    "Paste or modify vehicle telemetry data:",
    value=default_telemetry,
    height=180,
)

if st.button("🚨 Run AutoSentinels Agents"):
    with st.spinner("Agents are analyzing telemetry..."):
        result = run_autosentinels_pipeline(telemetry_input)

    st.success("Analysis complete")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🧠 Diagnosis Agent")
        st.write(result["diagnosis"])

    with col2:
        st.subheader("💬 Customer Engagement Agent")
        st.write(result["customer_message"])

    with col3:
        st.subheader("🏭 OEM Insights Agent")
        st.write(result["oem_insights"])
