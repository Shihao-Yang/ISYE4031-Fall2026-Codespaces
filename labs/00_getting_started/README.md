# Lab 00: Baseline, agent, audit

This short lab confirms that your environment works and establishes the course workflow. The data are synthetic, so the correct data-generating process is known.

## 1. Baseline

Run the supplied analysis and tests:

```bash
python labs/00_getting_started/analysis.py
pytest -q
```

Before using an agent, answer these questions in your notes:

1. Why is the train/test split chronological rather than random?
2. What does the naive forecast assume?
3. What information is available to each model when it predicts the test period?
4. Which metric is reported, and what units does it have?

## 2. Agent

Start `agy` or `codex` in the repository root. Ask the agent to inspect the supplied analysis and propose one meaningful improvement. A useful first prompt is:

> Inspect Lab 00 and explain the two baselines. Propose one additional diagnostic or model that preserves the chronological split. Do not edit files yet. Identify any leakage risk and say how we should test the change.

Review the plan. If it is statistically defensible, ask Codex to implement it and add a test.

## 3. Audit

Run all tests again, inspect the changed code, and write a short audit:

- What did the agent change?
- What evidence suggests the change is correct?
- Did it improve test-period RMSE, and is that comparison fair?
- What limitation remains?
- What did you reject or revise?

## AI Usage Statement

Include the tool, purpose, representative prompt, verification steps, and any revision or rejection. Do not paste login information or private data.
