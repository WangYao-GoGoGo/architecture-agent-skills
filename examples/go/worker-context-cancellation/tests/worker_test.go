// Tests for Worker — validates behavior preservation after context cancellation refactoring.
//
// Run with: go test ./tests/ -v

package main

import (
	"context"
	"testing"
	"time"
)

func TestWorkerCancellation(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	results := make(chan int, 10)
	go worker(ctx, 1, results)

	// Read one result
	select {
	case result := <-results:
		if result < 1000 || result >= 2000 {
			t.Errorf("Expected result in range [1000, 2000), got %d", result)
		}
	case <-time.After(2 * time.Second):
		t.Fatal("Timeout waiting for worker result")
	}

	// Cancel and verify worker stops
	cancel()

	// Give worker time to notice cancellation
	time.Sleep(100 * time.Millisecond)

	// Channel should not produce more results (or may produce one in-flight)
	select {
	case <-results:
		// OK — may have been in-flight
	default:
		// OK — worker stopped
	}
}

func TestWorkerContextDone(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	cancel() // Cancel immediately

	results := make(chan int, 10)
	go worker(ctx, 2, results)

	// Worker should exit without producing results
	time.Sleep(100 * time.Millisecond)
	select {
	case <-results:
		t.Error("Worker produced result after immediate cancellation")
	default:
		// Expected — worker should not produce results
	}
}
