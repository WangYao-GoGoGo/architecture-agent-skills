<?php
// Before: SQL mixed into controller logic — no separation of concerns.

class UserController
{
    public function show(int $id): array
    {
        $pdo = new PDO('mysql:host=localhost;dbname=app', 'root', '');
        
        // SQL mixed with presentation logic
        $stmt = $pdo->prepare('SELECT * FROM users WHERE id = ?');
        $stmt->execute([$id]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);
        
        if (!$user) {
            http_response_code(404);
            return ['error' => 'User not found'];
        }
        
        // Business logic mixed in
        $user['display_name'] = $user['first_name'] . ' ' . $user['last_name'];
        $user['is_active'] = $user['status'] === 'active';
        
        // Another query inline
        $stmt = $pdo->prepare('SELECT COUNT(*) FROM orders WHERE user_id = ?');
        $stmt->execute([$id]);
        $user['order_count'] = (int) $stmt->fetchColumn();
        
        return $user;
    }
}
