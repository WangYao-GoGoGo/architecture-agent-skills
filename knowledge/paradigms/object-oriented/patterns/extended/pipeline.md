# Pipeline

## Intent
Chain processing stages together, where the output of one stage is the input to the next. Each stage performs a specific transformation.

## Use When
- A processing task can be broken into sequential, independent steps.
- Steps should be reusable in different combinations.
- You want to add, remove, or reorder processing steps easily.

## Structure
- Pipeline manages the chain of stages.
- Stage defines the processing interface (input → output).
- ConcreteStage implements a specific transformation.
- Context carries data through the pipeline.

## Heuristics
1. **Single responsibility per stage**: Each stage should do exactly one transformation.
2. **Immutable context**: Pass immutable data between stages to prevent side effects.
3. **Error handling**: Decide whether a stage failure stops the pipeline or continues with a fallback.
4. **Parallel pipelines**: Consider fan-out (parallel stages) and fan-in (merge results).

## Common Risks
1. **Pipeline complexity**: Too many stages make the pipeline hard to understand.
2. **Error propagation**: Errors in the middle of a pipeline can leave the system in an inconsistent state.
3. **Performance**: Each stage adds overhead. Very fine-grained stages can be inefficient.
4. **Debugging difficulty**: Tracing data through many stages is harder than a single function.

## Related Patterns
- **Chain of Responsibility**: Similar chain structure. Pipeline transforms data; Chain of Responsibility finds a handler.
- **Decorator**: Can add behavior to pipeline stages.
- **Strategy**: Stages can use Strategy for different processing algorithms.
