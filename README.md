# FlowPilot AI Support Ticket Triage Agent

This is a beginner-friendly AI agent project that routes messy customer support messages into structured triage data for a fictional B2B SaaS product called FlowPilot.

The agent reads an inbound support ticket and returns:

```json
{
  "category": "account_access",
  "urgency": "high",
  "missing_information": ["account email"],
  "suggested_next_action": "Check password reset email delivery logs.",
  "confidence": 0.9
}
```

The project focuses on prompt design, schema validation, provider abstraction, and evaluation against golden fixtures.

## What It Demonstrates

- Structured AI output with Pydantic validation
- A reusable provider interface for multiple LLM providers
- DeepSeek and OpenAI implementations using the OpenAI SDK
- Prompt loading from a versioned system prompt file
- Golden fixture evaluation for category and urgency accuracy
- Side-by-side model comparison
- Unit tests for local project logic without live API calls

## Tech Stack

- Python 3.12
- Pydantic
- OpenAI Python SDK
- python-dotenv
- pytest
- DeepSeek API
- OpenAI API

## Output Schema

The runtime output is validated as a `TicketRoute`:

```json
{
  "category": "string",
  "urgency": "string",
  "missing_information": ["string"],
  "suggested_next_action": "string",
  "confidence": 0.0
}
```

Allowed categories:

- `account_access`
- `billing`
- `bug`
- `how_to`
- `feature_request`
- `other`

Allowed urgency levels:

- `low`
- `medium`
- `high`
- `critical`

## Project Structure

```text
fixtures/
  golden_v1.json              Golden evaluation fixtures
  test_valid.json             Small valid fixture test data
  test_invalid_urgency.json   Invalid fixture test data
  test_bad_shape.json         Invalid top-level shape test data

prompts/
  route_ticket_system.md      System prompt for ticket routing

src/
  schemas.py                  Pydantic models
  prompt_loader.py            Loads prompt files
  fixture_loader.py           Loads and validates fixtures
  evaluator.py                Compares provider output to expected labels
  providers/
    base.py                   Abstract provider contract
    deepseek.py               DeepSeek provider
    openai_provider.py        OpenAI provider

tests/
  test_evaluator.py
  test_fixtures.py
  test_prompt_loader.py
  test_provider_base.py

manual_deepseek_check.py      Manual DeepSeek smoke test
manual_openai_check.py        Manual OpenAI smoke test
run_deepseek_evaluation.py    DeepSeek golden fixture evaluation
run_openai_evaluation.py      OpenAI golden fixture evaluation
compare_provider_results.py   Side-by-side provider comparison
```

## Setup

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
DEEPSEEK_API_KEY=your_deepseek_key_here
OPENAI_API_KEY=your_openai_key_here
```

The `.env` file is ignored by Git and should not be committed.

## Running Tests

The unit tests do not call live LLM APIs. They test the local schema, fixture loading, prompt loading, provider interface, and evaluator behavior.

```powershell
python -m pytest
```

## Manual Provider Checks

Run one ticket through DeepSeek:

```powershell
python manual_deepseek_check.py
```

Run one ticket through OpenAI:

```powershell
python manual_openai_check.py
```

## Running Evaluations

Evaluate DeepSeek against the golden fixtures:

```powershell
python run_deepseek_evaluation.py
```

Evaluate OpenAI against the golden fixtures:

```powershell
python run_openai_evaluation.py
```

Compare both providers:

```powershell
python compare_provider_results.py
```

Example comparison output from a recent run:

```text
Provider comparison summary
Total fixtures: 30

DeepSeek V4
Category accuracy: 29/30 (96.7%)
Urgency accuracy: 23/30 (76.7%)

OpenAI - GPT 5 nano
Category accuracy: 26/30 (86.7%)
Urgency accuracy: 17/30 (56.7%)
```

LLM results can vary between runs, especially for models or settings that do not support deterministic temperature settings.

## Architecture

The core flow is:

```text
golden fixture
  -> provider.route_ticket(message)
  -> TicketRoute validation
  -> evaluator comparison
  -> accuracy report
```

`BaseTriageProvider` defines the shared provider contract:

```text
route_ticket(message: str) -> TicketRoute
```

This means the evaluator can work with either `DeepSeekProvider` or `OpenAIProvider` without changing its logic.

## Evaluation Approach

The golden fixture set contains 30 realistic support tickets with expected category and urgency labels.

The evaluator currently scores:

- category match
- urgency match

It does not automatically score `missing_information`, `suggested_next_action`, or `confidence` because those fields are more subjective and better suited to manual review at this stage.

## Current Findings

The strongest pattern from evaluation is that category classification is easier than urgency classification.

Urgency is more subjective because it depends on business impact, scope, deadline pressure, data-loss risk, security risk, and whether the issue affects one user or many users. This project treats over-escalation as an important behavior to measure.

## Future Improvements

- Save evaluation results to JSON or CSV
- Add more golden fixtures
- Improve failure reporting with fixture notes and original messages
- Tune the prompt to reduce urgency over-escalation
- Add tests for provider parsing with mocked API responses
- Add an `.env.example` file
- Refactor duplicated evaluation script logic into shared helpers

## Notes

This is intentionally a script-based AI agent project, not a full production helpdesk app. The goal is to demonstrate the core AI engineering loop: prompt, schema, provider abstraction, validation, evaluation, comparison, and iteration.
