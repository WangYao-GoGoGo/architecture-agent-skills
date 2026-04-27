---
name: flask-app-architecture-review
description: Use when reviewing Flask application architecture, blueprint organization, app factory pattern, extension management, and request lifecycle.
---

# Flask App Architecture Review

## When To Use

- The main decision is about Flask project structure, blueprint boundaries, extension setup, or request lifecycle management.
- Reviewing app factory pattern, configuration management, or Flask global state usage.

## Workflow

1. Identify project structure — is there an app factory, blueprints, or a single monolithic `app.py`?
2. Review blueprint boundaries — do they follow domain or technical concerns?
3. Check extension initialization and configuration — are extensions properly scoped?
4. Review Flask global usage (`g`, `current_app`, `request`) — are they used appropriately or creating hidden coupling?
5. Check error handling and request lifecycle hooks (`before_request`, `teardown_request`).
6. Review configuration management across environments.
7. Recommend the smallest change that introduces structure without over-engineering.

## Output Format

```markdown
Flask architecture review:
- Project structure:
- Blueprint boundaries:
- Extension setup:
- Flask global usage:
- Error handling:
- Configuration:
- Recommended change:
- Verification:
```
