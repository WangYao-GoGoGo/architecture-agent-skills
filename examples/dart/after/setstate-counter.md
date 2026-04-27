# setState → BLoC Pattern

Refactored from scattered `setState` calls to a clean BLoC (Business Logic Component) pattern.

## Design Pressure

- State logic (`_count`, `_isLoading`) was mixed with widget code.
- Adding a new state variable required more `setState` calls.
- Testing required widget integration tests — no way to unit test logic.
- Async operations (fetching remote count) were hard to manage.

## Applied Pattern

**BLoC (Business Logic Component)** — separate business logic from UI using `Stream`/`StreamBuilder`. The BLoC is pure Dart, testable without Flutter.

## After Code

### `counter_bloc.dart`

```dart
import 'dart:async';

class CounterBloc {
  int _count = 0;
  bool _isLoading = false;

  final _stateController = StreamController<CounterState>();
  Stream<CounterState> get state => _stateController.stream;

  void increment() {
    _count++;
    _stateController.add(CounterState(count: _count, isLoading: _isLoading));
  }

  Future<void> fetchRemoteCount() async {
    _isLoading = true;
    _stateController.add(CounterState(count: _count, isLoading: true));
    await Future.delayed(Duration(seconds: 1));
    _count = 42;
    _isLoading = false;
    _stateController.add(CounterState(count: _count, isLoading: false));
  }

  void dispose() => _stateController.close();
}

class CounterState {
  final int count;
  final bool isLoading;
  const CounterState({required this.count, required this.isLoading});
}
```

### `counter_page.dart`

```dart
import 'package:flutter/material.dart';

class CounterPage extends StatefulWidget {
  @override
  State<CounterPage> createState() => _CounterPageState();
}

class _CounterPageState extends State<CounterPage> {
  final _bloc = CounterBloc();

  @override
  void dispose() {
    _bloc.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Counter')),
      body: Center(
        child: StreamBuilder<CounterState>(
          stream: _bloc.state,
          initialData: CounterState(count: 0, isLoading: false),
          builder: (context, snapshot) {
            final state = snapshot.data!;
            return state.isLoading
                ? CircularProgressIndicator()
                : Text('Count: ${state.count}', style: TextStyle(fontSize: 24));
          },
        ),
      ),
      floatingActionButton: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          FloatingActionButton(
            onPressed: () => _bloc.increment(),
            child: Icon(Icons.add),
          ),
          SizedBox(height: 8),
          FloatingActionButton(
            onPressed: () => _bloc.fetchRemoteCount(),
            child: Icon(Icons.cloud_download),
          ),
        ],
      ),
    );
  }
}
```

## Verification

- `CounterBloc` is pure Dart — testable without Flutter widget tests.
- State changes are predictable — single stream of `CounterState` objects.
- Adding a new state variable requires no widget changes.
- The widget is a pure presentation layer — no business logic.
- Async operations are managed by the BLoC, not the widget lifecycle.
