# Pipe And Filter

## Project Fit

Pipe and filter is language-neutral. It fits projects where work naturally flows through ordered transformation or processing stages.

## Use When

- A workflow is a sequence of transformations.
- Each step can be understood, tested, reused, or reordered independently.
- Data moves through validation, enrichment, transformation, routing, or output phases.

## Avoid When

- Steps require heavy shared mutable state.
- The workflow is mostly interactive state management rather than transformation.
- Error handling and partial failure cannot be made clear between steps.

## Core Idea

Pipe and filter architecture passes data through a sequence of processing steps. Each filter transforms or enriches the data and passes it onward.

## Fits Best With

- ETL, data pipelines, compilers, text/media processing, request middleware, import/export workflows, and shell pipelines.
- Backend request processing where middleware stages are clear.
- Frontend build tools or data transformation flows.

## Heuristics

- Keep filters focused and side-effect boundaries explicit.
- Define data contracts between steps.
- Make error handling and partial failure behavior clear.
- Use for compilers, ETL, text processing, media processing, and request pipelines when the flow is natural.

## Adaptation Notes

- Backend: middleware or handler chains can use this style.
- Frontend: build steps and data preparation pipelines can use this style.
- Shell: command pipelines are a concrete form, but error handling must be explicit.
- Data systems: make schema and quality checks visible between stages.

## Risks

- Debugging becomes hard without tracing.
- Shared mutable context couples filters.
- Error handling is inconsistent across steps.

## Verification

- Each filter can be tested independently.
- Data contracts between filters are named.
- Failure at any step has defined behavior.
