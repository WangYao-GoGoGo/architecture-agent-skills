# Scheduler

## Intent
Control the order in which tasks are executed, ensuring that resource constraints and timing requirements are met.

## Use When
- Tasks have different priorities or deadlines.
- Resources are limited and must be shared among tasks.
- You need to control the execution order of concurrent or asynchronous tasks.

## Structure
- Scheduler maintains a queue of tasks and decides execution order.
- Task represents a unit of work.
- Resource represents a limited resource that tasks need.

## Heuristics
1. **Choose the right scheduling algorithm**: FIFO, priority-based, round-robin, deadline-based. Match the algorithm to the requirements.
2. **Preemption**: Decide whether a higher-priority task can interrupt a running lower-priority task.
3. **Starvation prevention**: Ensure low-priority tasks eventually get executed.
4. **Monitor and adjust**: Track scheduling metrics and adjust parameters dynamically.

## Common Risks
1. **Priority inversion**: A high-priority task waiting for a resource held by a low-priority task.
2. **Starvation**: Low-priority tasks never get CPU time.
3. **Deadlock**: Tasks waiting for resources held by each other.
4. **Overhead**: The scheduler itself consumes CPU time.

## Related Patterns
- **Strategy**: Different scheduling algorithms can be Strategies.
- **Command**: Tasks are often Command objects.
- **Mediator**: Scheduler mediates between tasks and resources.
