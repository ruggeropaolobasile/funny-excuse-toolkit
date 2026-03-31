# Human-in-the-loop flow

## Goal

Add an explicit human approval step before finalizing generated output.

## Stages

1. **Generate**
   - create multiple candidate excuses
2. **Review**
   - write candidates and metadata to a JSON review artifact
3. **Human decision**
   - choose a candidate index
   - optionally edit the text
4. **Approve**
   - confirm approval explicitly
5. **Publish**
   - save final approved text to a final artifact

## Why this matters

Even for a playful toolkit, this mirrors production-grade patterns:
- no blind auto-publish
- clear checkpoints
- traceable review artifacts
- recoverable history
