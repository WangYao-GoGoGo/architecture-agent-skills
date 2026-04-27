# Before: GenServer state leak — process state is manipulated directly,
# breaking OTP encapsulation.

defmodule Counter do
  use GenServer

  # Public API
  def start_link(initial_value) do
    GenServer.start_link(__MODULE__, initial_value, name: __MODULE__)
  end

  def increment do
    # BAD: Directly calling cast with state manipulation
    GenServer.cast(__MODULE__, {:increment})
  end

  def get do
    GenServer.call(__MODULE__, {:get})
  end

  # BAD: resetting state by sending a raw message
  def reset do
    send(__MODULE__, {:reset, 0})
  end

  # Callbacks
  def init(initial_value) do
    {:ok, initial_value}
  end

  def handle_cast({:increment}, state) do
    {:noreply, state + 1}
  end

  def handle_call({:get}, _from, state) do
    {:reply, state, state}
  end

  # BAD: handle_info for a message that should be a cast
  def handle_info({:reset, value}, _state) do
    {:noreply, value}
  end
end
