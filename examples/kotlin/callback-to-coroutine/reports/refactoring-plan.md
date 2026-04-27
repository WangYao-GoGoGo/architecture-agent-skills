# Callback → Coroutine + Flow

Refactored from callback-based threading to structured concurrency with coroutines and Flow.

## Design Pressure

- Manual `Thread` creation — no cancellation, no error handling.
- Callback nesting made control flow hard to follow.
- No way to cancel an in-flight request.
- UI updates from background threads risked crashes.

## Applied Pattern

**Coroutines + Flow** — use `suspend` functions for single-shot requests, `Flow` for streaming data. Structured concurrency ensures cancellation.

## After Code

```kotlin
class UserRepository {
    suspend fun fetchUser(id: String): User {
        delay(500) // Simulate network (non-blocking)
        return User(id, "John Doe", "john@example.com")
    }

    suspend fun fetchOrders(userId: String): List<Order> {
        delay(300)
        return listOf(Order("ORD-1", 99.99))
    }
}

class UserProfileViewModel(
    private val repository: UserRepository,
    private val scope: CoroutineScope = viewModelScope
) {
    private val _uiState = MutableStateFlow<UserProfileState>(UserProfileState.Loading)
    val uiState: StateFlow<UserProfileState> = _uiState.asStateFlow()

    fun loadProfile(userId: String) {
        scope.launch {
            _uiState.value = UserProfileState.Loading
            try {
                val user = repository.fetchUser(userId)
                val orders = repository.fetchOrders(userId)
                _uiState.value = UserProfileState.Success(user, orders)
            } catch (e: Exception) {
                _uiState.value = UserProfileState.Error(e.message ?: "Unknown error")
            }
        }
    }
}

sealed class UserProfileState {
    object Loading : UserProfileState()
    data class Success(val user: User, val orders: List<Order>) : UserProfileState()
    data class Error(val message: String) : UserProfileState()
}
```

## Key Changes

| Before | After |
|--------|-------|
| Manual `Thread` creation | `scope.launch` — structured concurrency |
| Nested callbacks | Sequential `suspend` calls |
| No cancellation | Automatic cancellation via coroutine scope |
| No error handling | `try/catch` in coroutine |
| Implicit threading | Explicit dispatcher control |
| Mutable state scattered | Single `StateFlow` — predictable state |

## Verification

- Same data is loaded and displayed.
- Cancelling the scope cancels all in-flight requests.
- Errors are caught and propagated to the UI state.
- No thread creation overhead — coroutines are lightweight.
- UI state is predictable — one `StateFlow`, one sealed class.
