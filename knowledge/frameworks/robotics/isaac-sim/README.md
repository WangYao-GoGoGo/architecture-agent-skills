# Isaac Sim Knowledge

## Heuristics

- Separate scene composition, robot models, sensor simulation, and reinforcement learning setup.
- Keep USD scene definitions versioned and composable.
- Treat sensor noise models and domain randomization as architecture.
- Add proper logging and visualization for debugging training runs.

## Common Risks

- Simulation assumptions not matching real hardware.
- Domain randomization not covering real-world variation.
- Training and evaluation environments diverging.
