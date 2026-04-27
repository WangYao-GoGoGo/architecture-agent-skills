# Commands

## Run Original Code

```bash
# Run the Flutter app with setState approach
flutter run lib/main.dart
```

## Run Refactored Code

```bash
# Run the Flutter app with BLoC approach
flutter run lib/main_bloc.dart
```

## Run Tests

```bash
flutter test tests/
```

## Validate Behavior Preservation

The refactoring moves state management from `setState` in widgets to a BLoC (Business Logic Component) pattern. The UI behavior should remain identical.

Validation Level: **Static reasoning only** — requires Flutter SDK to run end-to-end.
