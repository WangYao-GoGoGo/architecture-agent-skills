# Goroutine Leak → Context Cancellation

Refactored from leaking goroutines to clean shutdown via `context.Context`.

## Design Pressure

- Worker goroutines ran forever — no mechanism to signal shutdown.
- If `main()` returned early (e.g., on error), workers leaked.
- No way to propagate cancellation from caller to callee.

## Applied Pattern

**Context-based cancellation** — pass `context.Context` to workers. Use `select` to listen for both work and cancellation.

## After Code

```go
package main

import (
	"context"
	"fmt"
	"math/rand"
	"time"
)

func worker(ctx context.Context, id int, results chan<- int) {
	for {
		select {
		case <-ctx.Done():
			fmt.Printf("Worker %d shutting down: %v\n", id, ctx.Err())
			return
		default:
			n := rand.Intn(100)
			time.Sleep(time.Duration(n) * time.Millisecond)
			results <- id * 1000 + n
		}
	}
}

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	results := make(chan int)

	// Start 5 workers with cancellable context
	for i := 0; i < 5; i++ {
		go worker(ctx, i, results)
	}

	// Read 3 results, then cancel all workers
	for i := 0; i < 3; i++ {
		result := <-results
		fmt.Printf("Got result: %d\n", result)
	}

	cancel() // Signal all workers to stop
	fmt.Println("Done — all workers cleaned up!")
}
```

## Key Changes

| Before | After |
|--------|-------|
| Infinite loop in worker | `select` with `ctx.Done()` |
| No shutdown mechanism | `context.WithCancel` + `cancel()` |
| Goroutine leak on early return | `defer cancel()` ensures cleanup |
| Workers unaware of caller state | Workers respond to cancellation |

## Verification

- Workers exit promptly when `cancel()` is called.
- `defer cancel()` ensures cleanup even on panic or early return.
- No goroutine leaks — verified with `runtime.NumGoroutine()`.
- Adding timeout is trivial: `context.WithTimeout` instead of `WithCancel`.
