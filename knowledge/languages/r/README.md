# R Architecture Idioms

## Use When

- Reviewing R package structure, vectorized operations, functional pipelines, or data analysis workflows.

## Heuristics

- Prefer vectorized operations over explicit loops for performance.
- Use `purrr::map()` family for functional iteration over `lapply`/`sapply`.
- Use `dplyr` pipelines (`%>%`/`|>`) for data transformation — keep steps focused.
- Organize R packages with `R/` directory structure and `DESCRIPTION` metadata.
- Use `R6` classes for reference semantics when needed; prefer S3 for simple dispatch.
- Use `testthat` for unit tests — co-locate tests with package code.
- Document functions with `roxygen2` inline documentation.
- Use `renv` for reproducible environments in projects.

## Common Risks

- Growing environments with large objects that aren't cleaned up.
- Over-relying on global assignment (`<<-`) which breaks referential transparency.
- Loading entire packages with `library()` inside functions instead of using `::`.
- Silent type coercion in vectorized operations.
- Non-reproducible scripts due to missing seed setting or package version pinning.
