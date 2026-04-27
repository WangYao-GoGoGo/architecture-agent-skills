---
name: elixir-otp-architecture
description: Use when reviewing Elixir OTP supervision trees, GenServer design, Phoenix contexts, and fault-tolerant architecture.
---

# Elixir OTP Architecture

## When To Use
- The main decision is about supervision tree design, GenServer state management, or Phoenix context boundaries.
- Reviewing process lifecycle, restart strategies, or PubSub patterns.

## Workflow
1. Identify supervision tree structure — are processes organized with clear restart strategies?
2. Review GenServer design — is state minimal and focused on a single responsibility?
3. Check Phoenix context boundaries — are contexts independent with clear APIs?
4. Review process communication — is `GenServer.call`/`cast` used appropriately vs `PubSub`?
5. Check error handling — are supervisors configured with appropriate intensity/period?
6. Review `with` and pipe usage — are data transformation pipelines readable?
7. Recommend the simplest OTP design.

## Output Format
```markdown
Elixir OTP review:
- Supervision tree:
- GenServer design:
- Context boundaries:
- Process communication:
- Error handling:
- Pipeline readability:
- Recommended change:
- Verification:
```
