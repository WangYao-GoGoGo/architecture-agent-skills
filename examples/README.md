# Examples

Examples show how skills should change agent behavior. Each example demonstrates a concrete **before → after** transformation driven by a skill's heuristics and workflow.

## Structure

Each language or domain has its own directory with:

```
examples/{lang}/
├── README.md              # Overview of examples for this language
├── before/                # Problematic code or architecture
│   └── {example-name}.{ext}
└── after/                 # Refactored code or design report
    └── {example-name}.md
```

## What Each Example Includes

- **Design pressure** — what forces the change (complexity, coupling, performance, etc.)
- **Before code** — the problematic implementation
- **After code or design report** — the refactored solution
- **Pattern or architecture style** — what was applied (if any)
- **Verification notes** — how to confirm behavior is preserved

## Language Examples

### Systems & Performance
| Language | Example | Skill Applied |
|----------|---------|---------------|
| C | Global state → explicit context | [`c-modular-architecture`](../skills/languages/c/c-modular-architecture/SKILL.md) |
| C++ | God class → separated concerns | [`cpp-class-design`](../skills/languages/cpp/cpp-class-design/SKILL.md) |
| Rust | Borrow checker struggle → ownership design | [`rust-ownership-architecture`](../skills/languages/rust/rust-ownership-architecture/SKILL.md) |
| Go | Goroutine leak → context cancellation | [`go-concurrency-architecture`](../skills/languages/go/go-concurrency-architecture/SKILL.md) |
| Zig | Manual allocator → arena pattern | — |
| Nim | Macro overuse → typed proc | — |

### Scripting & Dynamic
| Language | Example | Skill Applied |
|----------|---------|---------------|
| Python | Large conditional → Strategy pattern | [`python`](../skills/languages/python/) |
| JavaScript | Callback hell → async/await | [`javascript-module-architecture`](../skills/languages/javascript/javascript-module-architecture/SKILL.md) |
| TypeScript | Any types → discriminated union | [`typescript`](../skills/languages/typescript/) |
| Ruby | Mixin collision → module composition | [`ruby-module-architecture`](../skills/languages/ruby/ruby-module-architecture/SKILL.md) |
| PHP | Spaghetti SQL → repository pattern | [`php-namespace-architecture`](../skills/languages/php/php-namespace-architecture/SKILL.md) |
| Lua | Global table → local module | — |
| Perl | One-liner → structured script | — |
| Shell | Monolithic script → function decomposition | [`shell`](../skills/languages/shell/) |

### Web & Markup
| Language | Example | Skill Applied |
|----------|---------|---------------|
| HTML | Div soup → semantic landmarks | [`html-semantic-architecture`](../skills/languages/html/html-semantic-architecture/SKILL.md) |
| CSS | Specificity war → utility-first layout | [`css-layout-architecture`](../skills/languages/css/css-layout-architecture/SKILL.md) |

### Scientific & Numerical
| Language | Example | Skill Applied |
|----------|---------|---------------|
| R | Copy-on-modify → data.table reference | — |
| Julia | Type instability → stable function | — |
| MATLAB | Script → function decomposition | — |

### Functional & JVM
| Language | Example | Skill Applied |
|----------|---------|---------------|
| Java | God class → layered architecture | [`java-oo-refactor`](../skills/languages/java/java-oo-refactor/SKILL.md) |
| Kotlin | Null checks → nullable types + scope | [`kotlin-coroutine-architecture`](../skills/languages/kotlin/kotlin-coroutine-architecture/SKILL.md) |
| Scala | Implicit magic → given instances | [`scala-functional-architecture`](../skills/languages/scala/scala-functional-architecture/SKILL.md) |
| Clojure | Mutable atom → pure function | — |
| Haskell | IO monad abuse → pure core | — |
| Elixir | GenServer state leak → OTP design | [`elixir-otp-architecture`](../skills/languages/elixir/elixir-otp-architecture/SKILL.md) |
| Erlang | Process crash → supervision tree | — |
| OCaml | Variant → GADT refinement | — |
| Groovy | Dynamic type → @CompileStatic | — |

### Database & Query
| Language | Example | Skill Applied |
|----------|---------|---------------|
| SQL | Offset pagination → cursor pagination | [`sql-query-structure`](../skills/languages/sql/sql-query-structure/SKILL.md) |
| GraphQL | N+1 resolver → DataLoader batch | [`graphql-schema-design`](../skills/languages/graphql/graphql-schema-design/SKILL.md) |

### Mobile & UI
| Language | Example | Skill Applied |
|----------|---------|---------------|
| Swift | Massive VC → MVVM + coordinators | [`swift-protocol-architecture`](../skills/languages/swift/swift-protocol-architecture/SKILL.md) |
| Dart | setState → BLoC pattern | [`dart-flutter-architecture`](../skills/languages/dart/dart-flutter-architecture/SKILL.md) |
| Kotlin | Callback → coroutine + Flow | [`kotlin-coroutine-architecture`](../skills/languages/kotlin/kotlin-coroutine-architecture/SKILL.md) |

### Hardware & Embedded
| Language | Example | Skill Applied |
|----------|---------|---------------|
| Assembly | Hard-coded loop → macro parameterized | — |
| VHDL/Verilog | Flat RTL → hierarchical FSM | — |
| Ada | Unchecked access → protected type | — |

### Blockchain
| Language | Example | Skill Applied |
|----------|---------|---------------|
| Solidity | Reentrancy → checks-effects-interactions | — |

### WebAssembly
| Language | Example | Skill Applied |
|----------|---------|---------------|
| WASM | Linear memory → structured binding | — |

## Domain Examples

| Domain | Example | Skill Applied |
|--------|---------|---------------|
| Database | Cache invalidation for product detail | [`database`](../skills/domains/database/) |
| Backend | Service boundary extraction | [`service-boundary-review`](../skills/domains/backend/service-boundary-review/SKILL.md) |
| Frontend | Component decomposition | [`component-architecture-review`](../skills/domains/frontend/component-architecture-review/SKILL.md) |
