# Model-View-Controller (MVC)

## Intent
Separate the user interface (View) from the data (Model) and the input handling (Controller), allowing each to be developed and tested independently.

## Use When
- You need multiple views of the same data.
- The user interface changes independently of the business logic.
- You want to test business logic without a UI.

## Structure
- Model manages data, business rules, and state. Notifies observers on changes.
- View renders the Model into a UI. Can be passive (Controller pushes data) or active (observes Model).
- Controller handles user input and updates the Model.

## Heuristics
1. **Keep Model pure**: The Model should have no reference to View or Controller.
2. **Thin controllers**: Controllers should only handle input and delegate to the Model.
3. **Passive View**: The View should not contain business logic. It only renders what it's told.
4. **Observer pattern**: Model notifies View of changes via Observer.

## Common Risks
1. **Fat controllers**: Business logic leaks into controllers, making them hard to test.
2. **Model-View coupling**: If the View directly accesses Model internals, changes to the Model break the View.
3. **Multiple MVC confusion**: In complex UIs, nested MVC hierarchies can be confusing.
4. **Framework lock-in**: Many web frameworks claim MVC but have different interpretations.

## Related Patterns
- **Observer**: Model uses Observer to notify Views.
- **Strategy**: Controller can use Strategy for different input handling.
- **Composite**: Views can be composed of sub-views.
