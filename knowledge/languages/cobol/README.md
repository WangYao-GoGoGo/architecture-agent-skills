# COBOL Architecture Idioms

## Use When

- Reviewing COBOL program structure, file handling, batch processing, or mainframe application architecture.

## Heuristics

- Use the standard COBOL division structure: IDENTIFICATION, ENVIRONMENT, DATA, PROCEDURE.
- Use `COPY` for shared data structures and `CALL` for modular program decomposition.
- Use `FILE SECTION` with proper `FD` (File Description) entries for file I/O.
- Use `INITIALIZE` for clearing data structures instead of individual `MOVE` statements.
- Use `EVALUATE` for multi-way branching instead of nested `IF` statements.
- Use `PERFORM VARYING` for structured loops.
- Use `DECLARATIVES` for file error handling.
- Use `LINKAGE SECTION` for parameter passing between programs.

## Common Risks

- `GO TO` usage creating spaghetti code — prefer structured `PERFORM` and `EVALUATE`.
- Hard-coded file paths and dataset names.
- Missing `FILE STATUS` checking after I/O operations.
- Year 2000 legacy issues in date handling code.
- Mixing `DISPLAY` and `ACCEPT` for user interaction in batch programs.
