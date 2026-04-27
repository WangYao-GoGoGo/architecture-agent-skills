# Example Evaluation Checklist

Use this checklist when adding before/after examples.

## Before Example

- Shows a real architecture pressure.
- Is small enough to understand quickly.
- Has enough behavior to verify after refactoring.
- Avoids artificial complexity.

## After Example

- Preserves behavior.
- Makes ownership clearer.
- Reduces duplication, coupling, or state confusion.
- Uses a pattern only when the problem justifies it.
- Includes verification notes.

## Review Questions

- Could the agent learn a repeatable move from this example?
- Would the same refactor still make sense in a real codebase?
- Is there a simpler design that would be better?
- Are limitations or tradeoffs named?
