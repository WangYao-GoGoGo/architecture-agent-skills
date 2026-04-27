# Synchronous Blocking → Async/Await

Refactored from blocking `.Result` calls to proper async/await with `Task.WhenAll` for concurrency.

## Design Pressure

- `.Result` blocks the calling thread — causes thread pool starvation under load.
- `Thread.Sleep` blocks — should use `Task.Delay`.
- Sequential requests when they could be parallel.
- No cancellation support.

## Applied Pattern

**Async/await all the way** — make the entire call chain async. Use `Task.WhenAll` for independent requests.

## After Code

```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;

class UserService
{
    private readonly HttpClient _httpClient;

    public UserService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<string> FetchUserDataAsync(string userId)
    {
        var response = await _httpClient
            .GetStringAsync($"https://api.example.com/users/{userId}");

        await Task.Delay(200); // Non-blocking delay

        return response;
    }
}

class Program
{
    static async Task Main(string[] args)
    {
        var httpClient = new HttpClient();
        var service = new UserService(httpClient);

        // Parallel requests — no thread blocking
        var tasks = new Task<string>[10];
        for (int i = 0; i < 10; i++)
        {
            tasks[i] = service.FetchUserDataAsync($"user-{i}");
        }

        var results = await Task.WhenAll(tasks);

        for (int i = 0; i < results.Length; i++)
        {
            Console.WriteLine($"Got data for user-{i}: {results[i].Length} chars");
        }
    }
}
```

## Key Changes

| Before | After |
|--------|-------|
| `.Result` — blocks thread | `await` — non-blocking |
| `Thread.Sleep` — blocks | `Task.Delay` — non-blocking |
| Sequential requests | `Task.WhenAll` — parallel |
| No DI for HttpClient | `HttpClient` injected |
| `void Main` | `async Task Main` — async entry point |

## Verification

- Same data is returned for the same inputs.
- Under load, no thread pool starvation — I/O operations don't block threads.
- 10 parallel requests complete in ~the time of 1 request + 200ms, not 10x.
- Cancellation can be added by passing `CancellationToken`.
- `HttpClient` is injected — testable with mock handlers.
