# Instructions for AI coding agents

This repository supports ISYE 4031 Regression and Forecasting. Python is the primary language.

## Analysis workflow

For each statistical task:

1. State the response, predictors, data structure, and intended estimand or forecast target.
2. Establish a transparent baseline before proposing a more complex method.
3. Use chronological splits for forecasting. Never use future observations to construct training features.
4. Check model assumptions, diagnostics, uncertainty, and out-of-sample performance as appropriate.
5. Run the relevant code and tests. Do not invent numerical results, data, citations, or successful test output.
6. Explain changes in language the student can defend orally.
7. Record material AI assistance in the assignment's AI Usage Statement.

## Repository boundaries

- Never request, expose, or commit credentials, tokens, student records, grades, private communications, or restricted course materials.
- Do not overwrite source data. Write derived artifacts to a clearly named output directory when an assignment requires them.
- Keep changes scoped to the current assignment and preserve instructor-provided tests.
- Ask before downloading data or adding a dependency that is not already in `requirements.txt`.
