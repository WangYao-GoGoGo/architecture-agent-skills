// Before: Synchronous blocking — thread pool starvation and poor scalability.

using System;
using System.Net.Http;
using System.Threading;

class UserService
{
    private readonly HttpClient _httpClient;

    public UserService()
    {
        _httpClient = new HttpClient();
    }

    public string FetchUserData(string userId)
    {
        // Blocking call — ties up a thread while waiting for I/O
        var response = _httpClient
            .GetStringAsync($"https://api.example.com/users/{userId}")
            .Result;  // BAD: blocks the calling thread

        Thread.Sleep(200); // Simulate processing

        return response;
    }
}

class Program
{
    static void Main(string[] args)
    {
        var service = new UserService();

        // Under load, this causes thread pool starvation
        for (int i = 0; i < 10; i++)
        {
            var result = service.FetchUserData($"user-{i}");
            Console.WriteLine($"Got data for user-{i}: {result.Length} chars");
        }
    }
}
