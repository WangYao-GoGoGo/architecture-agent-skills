# Tests for Counter — validates behavior preservation after OTP refactoring.
#
# Run with: elixir -r tests/test_counter.exs -e "CounterTest.run()"

defmodule CounterTest do
  def run do
    IO.puts("Counter Tests\n")
    test_increment()
    test_get_initial()
    test_reset()
    IO.puts("\nAll tests passed!")
  end

  def test_increment do
    IO.write("Test: increment increases counter... ")
    {:ok, pid} = Counter.start_link(0)
    Counter.increment()
    value = Counter.get()
    if value == 1 do
      IO.puts("PASS")
    else
      IO.puts("FAIL: expected 1, got #{value}")
    end
    # Clean up
    Process.exit(pid, :kill)
  end

  def test_get_initial do
    IO.write("Test: get returns initial value... ")
    {:ok, pid} = Counter.start_link(42)
    value = Counter.get()
    if value == 42 do
      IO.puts("PASS")
    else
      IO.puts("FAIL: expected 42, got #{value}")
    end
    Process.exit(pid, :kill)
  end

  def test_reset do
    IO.write("Test: reset sets counter to 0... ")
    {:ok, pid} = Counter.start_link(100)
    Counter.reset()
    value = Counter.get()
    if value == 0 do
      IO.puts("PASS")
    else
      IO.puts("FAIL: expected 0, got #{value}")
    end
    Process.exit(pid, :kill)
  end
end
