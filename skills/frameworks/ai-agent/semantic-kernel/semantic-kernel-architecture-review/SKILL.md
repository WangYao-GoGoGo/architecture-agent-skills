---
name: semantic-kernel-architecture-review
description: Use when reviewing Semantic Kernel architecture, plugin/skill design, planner configuration, memory, connectors, and AI orchestration.
---

# Semantic Kernel Architecture Review

## When To Use

- The main decision is about Semantic Kernel plugin/skill boundaries, planner configuration, memory integration, or connector design.
- Reviewing prompt engineering, function calling, or orchestration patterns.

## Workflow

1. Identify the plugin/skill structure and function boundaries.
2. Review planner configuration — which planner, prompt, and step limits.
3. Check memory integration — semantic memory, text memory, and vector store connectors.
4. Review connector boundaries — OpenAI, Azure, Hugging Face, or custom.
5. Check prompt template design for injection risks and output structure.
6. Review evaluation and telemetry setup.
7. Recommend the smallest structural change that improves orchestration clarity or safety.

## Output Format

```markdown
Semantic Kernel architecture review:
- Plugin/skill structure:
- Planner configuration:
- Memory integration:
- Connector boundaries:
- Prompt design:
- Evaluation & telemetry:
- Recommended change:
- Verification:
```
