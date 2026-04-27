// Before: Goroutine leak — worker goroutines are never cleaned up
// when the main function returns early on error.

package main

import (
	"fmt"
	"math/rand"
	"time"
)

func worker(id int, results chan<- int) {
	for {
		// Simulate work
		n := rand.Intn(100)
		time.Sleep(time.Duration(n) * time.Millisecond)
		results <- id * 1000 + n
	}
}

func main() {
	results := make(chan int)

	// Start 5 workers — they run forever
	for i := 0; i < 5; i++ {
		go worker(i, results)
	}

	// Read 3 results, then stop
	for i := 0; i < 3; i++ {
		result := <-results
		fmt.Printf("Got result: %d\n", result)
	}

	// Main exits, but workers keep running in the background (leak)
	fmt.Println("Done — but workers are still running!")
}
