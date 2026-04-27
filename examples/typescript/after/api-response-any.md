# Any Types → Discriminated Union

Refactored from `any`-typed API responses to a type-safe discriminated union.

## Design Pressure

- `any` types defeat the purpose of TypeScript — no autocomplete, no compile-time checks.
- Callers had to guess the shape of `data` and `error`.
- Refactoring the API shape would not produce type errors anywhere.

## Applied Pattern

**Discriminated union + generics** — model success and error as distinct types. Use a generic `ApiResponse<T>` to preserve type information.

## After Code

```typescript
// Success and error are distinct, type-safe variants
type ApiResponse<T> =
  | { ok: true; status: number; data: T }
  | { ok: false; status: number; error: { message: string } };

interface User {
  firstName: string;
  lastName: string;
}

function handleResponse(response: ApiResponse<User>): string {
  if (!response.ok) {
    return `Error: ${response.error.message}`;
  }

  // TypeScript knows `response.data` is `User` here
  return `Hello, ${response.data.firstName} ${response.data.lastName}!`;
}

// TypeScript enforces the correct shape
const resp: ApiResponse<User> = {
  ok: true,
  status: 200,
  data: { firstName: "John", lastName: "Doe" },
};
console.log(handleResponse(resp));
```

## Key Changes

| Before | After |
|--------|-------|
| `data: any` | `data: T` — generic, type-safe |
| `error?: any` | `error: { message: string }` — explicit shape |
| Runtime guessing of shape | Compile-time type checking |
| No autocomplete | Full IDE support for `response.data` |
| Refactoring is risky | Refactoring produces type errors everywhere |

## Verification

- Accessing `response.data.lastName` is type-checked at compile time.
- Accessing `response.error.message` on a success response is a compile error.
- Adding a new field to `User` requires updating all consumers.
- The `ok` discriminant ensures exhaustive checking in switch/match.
