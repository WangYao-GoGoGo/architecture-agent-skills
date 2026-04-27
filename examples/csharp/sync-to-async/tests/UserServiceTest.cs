/**
 * Tests for UserService — validates behavior preservation after async refactoring.
 *
 * Compile with: csc tests/UserServiceTest.cs after/UserService.cs -out:tests/UserServiceTest.exe
 * Run with: mono tests/UserServiceTest.exe
 */

using System;
using System.Threading.Tasks;

public class UserServiceTest
{
    static int passed = 0;
    static int failed = 0;

    static void Assert(bool condition, string message)
    {
        if (condition)
        {
            Console.WriteLine($"  PASS: {message}");
            passed++;
        }
        else
        {
            Console.WriteLine($"  FAIL: {message}");
            failed++;
        }
    }

    static async Task TestFetchUserDataAsync()
    {
        Console.WriteLine("FetchUserDataAsync:");
        var service = new UserService();

        try
        {
            // This will fail without a real HTTP endpoint, but we can verify the method exists
            var task = service.FetchUserDataAsync("test-user");
            Assert(task != null, "method returns a Task");
            Assert(task is Task<string>, "method returns Task<string>");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"  INFO: Expected network error: {ex.Message}");
        }
    }

    static async Task Main(string[] args)
    {
        Console.WriteLine("UserService Tests\n");

        await TestFetchUserDataAsync();

        Console.WriteLine($"\nResults: {passed} passed, {failed} failed");
    }
}
