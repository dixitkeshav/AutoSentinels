HEAD
# AutoSentinels
EY Techathon Project Submission

AutoSentinels

Quick start
-----------

- To run the Streamlit UI (recommended when you have dependencies installed):

  pip install -r requirements.txt
  streamlit run autosentinels/app.py

- If `streamlit` or `crewai` are not available the project provides **local stubs** for
  development and the app can be run from the CLI:

  python3 autosentinels/app.py
  # or
  python3 -m autosentinels.orchestrator

What I changed for local development
------------------------------------

- Added `local_stubs.py` which provides small Agent/Task/Crew stubs that run a
  deterministic, telemetry-aware local pipeline. This allows running and testing
  the pipeline without network access or expensive LLM calls.

- Made imports in `agents.py`, `tasks.py`, and `orchestrator.py` robust to missing
  `crewai` by falling back to `local_stubs`.

- Made `app.py` tolerant to missing `streamlit` by adding a CLI fallback.

Notes
-----

- This local stub is intended for development and testing; to get real LLM
  behaviour you will need to install and configure `crewai` and the appropriate
  LLM provider as documented in your provider's setup docs.
  28f2a30 (Add AutoSentinels agentic AI system)
