# Funny Excuse Toolkit

A tiny example toolkit that generates funny excuses in different tones.

## What it does

Given:
- a problem key such as `ritardo`, `task_non_fatto`, or `pc_rotto`
- a tone such as `short`, `corporate`, or `epic`

it generates a formatted excuse.

## Human-in-the-loop flow

The evolved version adds a review workflow:

1. the system generates one or more excuse candidates
2. the candidates are saved in a review file
3. a human selects the preferred candidate and can edit it
4. the human approves the final text
5. the approved output is published to a final file

This demonstrates a reusable pattern for serious toolkits:
- draft automatically
- review explicitly
- approve intentionally
- only then publish

## Usage

### Basic generation

```bash
python scripts/generate_excuse.py ritardo corporate
```

### Human-in-the-loop review flow

```bash
python scripts/hitl_excuse_flow.py ritardo corporate
```

This will create:
- `output/review/review_*.json`
- `output/final/final_*.txt`

## Optional local Git hooks

To enable the provided pre-commit hook:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
```
