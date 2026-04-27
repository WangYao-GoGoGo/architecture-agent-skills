// Before: Callback-based networking — nested callbacks, manual thread management.

class UserRepository {
    fun fetchUser(id: String, onResult: (User?) -> Unit) {
        Thread {
            Thread.sleep(500) // Simulate network
            val user = User(id, "John Doe", "john@example.com")
            onResult(user)
        }.start()
    }

    fun fetchOrders(userId: String, onResult: (List<Order>) -> Unit) {
        Thread {
            Thread.sleep(300)
            val orders = listOf(Order("ORD-1", 99.99))
            onResult(orders)
        }.start()
    }
}

class UserProfileViewModel(private val repository: UserRepository) {
    private var user: User? = null
    private var orders: List<Order> = emptyList()

    fun loadProfile(userId: String) {
        repository.fetchUser(userId) { user ->
            this.user = user
            repository.fetchOrders(userId) { orders ->
                this.orders = orders
                // Update UI (but we're on a background thread!)
                displayProfile()
            }
        }
    }

    private fun displayProfile() {
        // This runs on a background thread — potential UI thread violation
        println("User: ${user?.name}, Orders: ${orders.size}")
    }
}
