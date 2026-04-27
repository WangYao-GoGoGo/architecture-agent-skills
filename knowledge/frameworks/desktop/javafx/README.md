# JavaFX Knowledge

## Heuristics

- Separate scene graph, FXML views, controllers, model, and business logic.
- Keep UI updates on the JavaFX Application Thread.
- Treat property binding and observable collections as architecture.
- Add proper lifecycle management for stages, scenes, and controllers.

## Common Risks

- Business logic running on the JavaFX Application Thread.
- FXML controllers becoming god objects.
- Observable collections not properly synchronized.
