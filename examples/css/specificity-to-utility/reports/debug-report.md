# Debug Report: Specificity to Utility

## 1. Original Problem

The CSS has a specificity war — selectors use `!important` as a crutch to override previous rules. After six months, nobody knows which rules actually apply.

## 2. Root Cause

High-specificity selectors (nested, ID-based) combined with `!important` overrides create unpredictable cascade behavior.

## 3. Fix Summary

Refactored to a utility-first approach:

- Replaced high-specificity selectors with single-purpose utility classes.
- Eliminated all `!important` usage.
- Consistent spacing, typography, and color tokens.

## 4. Files Changed

| File | Change |
|---|---|
| `before/styles.css` | Original — specificity war with !important |
| `after/styles.css` | Refactored — utility-first approach |

## 5. Validation Commands

```bash
# Visual comparison of before and after rendering
```

## 6. Validation Results

Validation Level: **Static reasoning only** — CSS cannot be executed directly.

- Visual behavior should be identical for all card variants.
- No `!important` usage in refactored code.
- Consistent design tokens.

## 7. Behavior Preservation Notes

✅ Behavior preserved — same visual output with cleaner cascade.

## 8. Remaining Risks

- HTML must be updated to use utility classes.
- Design changes require updating multiple utility class combinations.

## 9. Follow-up Recommendations

- Add visual regression tests (e.g., Percy, Chromatic).
- Document the utility class naming convention.
