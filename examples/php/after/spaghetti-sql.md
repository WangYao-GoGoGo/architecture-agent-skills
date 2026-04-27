# Spaghetti SQL → Repository Pattern

Refactored from inline SQL in controllers to a clean repository layer with dependency injection.

## Design Pressure

- SQL queries were scattered across controllers — duplicated and untestable.
- Database connection was created inline, not injected.
- Business logic (display name, status mapping) was mixed with data access.
- No way to mock the database in tests.

## Applied Pattern

**Repository pattern + DI** — extract all data access into a `UserRepository`. Inject it into the controller.

## After Code

### `UserRepository.php`

```php
<?php

namespace App\Repository;

use PDO;

class UserRepository
{
    public function __construct(private PDO $pdo) {}

    public function findById(int $id): ?array
    {
        $stmt = $this->pdo->prepare('SELECT * FROM users WHERE id = ?');
        $stmt->execute([$id]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);
        return $user ?: null;
    }

    public function getOrderCount(int $userId): int
    {
        $stmt = $this->pdo->prepare('SELECT COUNT(*) FROM orders WHERE user_id = ?');
        $stmt->execute([$userId]);
        return (int) $stmt->fetchColumn();
    }
}
```

### `UserService.php`

```php
<?php

namespace App\Service;

use App\Repository\UserRepository;

class UserService
{
    public function __construct(private UserRepository $repository) {}

    public function getProfile(int $id): ?array
    {
        $user = $this->repository->findById($id);
        if (!$user) {
            return null;
        }

        $user['display_name'] = $user['first_name'] . ' ' . $user['last_name'];
        $user['is_active'] = $user['status'] === 'active';
        $user['order_count'] = $this->repository->getOrderCount($id);

        return $user;
    }
}
```

### `UserController.php`

```php
<?php

namespace App\Controller;

use App\Service\UserService;

class UserController
{
    public function __construct(private UserService $userService) {}

    public function show(int $id): array
    {
        $profile = $this->userService->getProfile($id);
        if (!$profile) {
            http_response_code(404);
            return ['error' => 'User not found'];
        }
        return $profile;
    }
}
```

## Verification

- `UserRepository` can be mocked in tests — no database required.
- `UserService` is testable with a fake repository.
- `UserController` only handles HTTP concerns.
- Adding a new query requires no changes to the controller or service.
- Database connection is configured in one place (DI container).
