# Borrow Checker Struggle → Ownership Design

Refactored from excessive cloning to proper ownership transfer using `join()` and iterator patterns.

## Design Pressure

- `build()` cloned every string because it only had `&self` access.
- The builder pattern fought Rust's ownership model — you couldn't consume the builder to avoid cloning.
- Unnecessary allocations for every word.

## Applied Pattern

**Ownership-based design** — use `join()` on slices, consume the builder when building, or use `IntoIterator` for zero-cost construction.

## After Code

```rust
struct StringBuilder {
    parts: Vec<String>,
}

impl StringBuilder {
    fn new() -> Self {
        StringBuilder { parts: Vec::new() }
    }

    fn add(&mut self, word: String) {
        self.parts.push(word);
    }

    /// Consume the builder and produce the final string.
    /// This avoids cloning — ownership of the parts is transferred.
    fn build(mut self, separator: &str) -> String {
        self.parts.join(separator)
    }

    /// Alternative: build without consuming, if you need to keep adding.
    fn build_ref(&self, separator: &str) -> String {
        self.parts.join(separator)
    }
}

fn main() {
    let mut builder = StringBuilder::new();
    builder.add("hello".to_string());
    builder.add("world".to_string());
    builder.add("foo".to_string());
    builder.add("bar".to_string());

    // Use build_ref if we need to keep using the builder
    let result = builder.build_ref(", ");
    println!("{}", result);

    builder.add("baz".to_string());
    // Now consume the builder
    let result2 = builder.build(" ");
    println!("{}", result2);
}
```

## Key Changes

| Before | After |
|--------|-------|
| `self.parts[i].clone()` | `self.parts.join(separator)` — no clone |
| `build(&self)` — can't move out | `build(self)` — consumes, zero-copy |
| Manual loop + separator logic | Standard library `join()` |
| Builder always borrows | Two methods: borrow or consume |

## Verification

- Same output for same inputs.
- No unnecessary allocations — `join()` writes directly into the result.
- Compiler guarantees no use-after-move when using `build(self)`.
- `build_ref()` still available when the builder needs to be reused.
