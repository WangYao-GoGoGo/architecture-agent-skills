# Kubeflow Knowledge

## Heuristics

- Separate pipeline components, ML training, serving, metadata tracking, and orchestration.
- Keep component contracts explicit with input/output specifications.
- Treat pipeline caching, artifact management, and experiment tracking as architecture.
- Add model validation and monitoring for production.

## Common Risks

- Pipeline components with implicit dependencies.
- Artifact paths not versioned or namespaced.
- Training and serving environments diverging.
