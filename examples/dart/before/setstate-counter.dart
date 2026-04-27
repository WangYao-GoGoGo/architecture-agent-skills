// Before: setState scattered across widgets — state logic mixed with UI.

import 'package:flutter/material.dart';

class CounterPage extends StatefulWidget {
  @override
  State<CounterPage> createState() => _CounterPageState();
}

class _CounterPageState extends State<CounterPage> {
  int _count = 0;
  bool _isLoading = false;

  void _increment() {
    setState(() {
      _count++;
    });
  }

  void _fetchRemoteCount() async {
    setState(() => _isLoading = true);
    // Simulate network call
    await Future.delayed(Duration(seconds: 1));
    setState(() {
      _count = 42;
      _isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Counter')),
      body: Center(
        child: _isLoading
            ? CircularProgressIndicator()
            : Text('Count: $_count', style: TextStyle(fontSize: 24)),
      ),
      floatingActionButton: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          FloatingActionButton(
            onPressed: _increment,
            child: Icon(Icons.add),
          ),
          SizedBox(height: 8),
          FloatingActionButton(
            onPressed: _fetchRemoteCount,
            child: Icon(Icons.cloud_download),
          ),
        ],
      ),
    );
  }
}
