# Rasa Knowledge

## Heuristics

- Separate NLU pipeline, dialogue policies, custom actions, stories/rules, and evaluation.
- Keep training data versioned and tested.
- Treat action server boundaries and slot management as architecture.
- Add conversation-driven testing for important paths.

## Common Risks

- Stories that don't cover real user behavior.
- Custom actions with hidden side effects.
- NLU model drift without evaluation.
