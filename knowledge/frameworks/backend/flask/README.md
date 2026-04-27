# Flask Knowledge

## Heuristics

- Keep routes thin and organize larger apps with blueprints or feature modules.
- Separate app factory, configuration, extensions, and use-case logic.
- Make request globals and extension state explicit at boundaries.
- Avoid turning one `app.py` into the whole architecture.

## Common Risks

- Global mutable app state.
- Hidden coupling through Flask globals.
- Route handlers owning validation, persistence, and domain rules.

