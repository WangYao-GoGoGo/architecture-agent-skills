# Mixin Collision → Module Composition

Refactored from fragile `super` chain to explicit composition with named collaborators.

## Design Pressure

- `include` order determines execution order — a silent behavior dependency.
- Adding a new concern requires understanding the entire `super` chain.
- Testing a concern in isolation is impossible — it depends on `super`.
- The `save` method's behavior is implicit, not explicit.

## Applied Pattern

**Composition over inheritance** — extract concerns into separate objects, compose them explicitly in the class.

## After Code

```ruby
class Validator
  def validate(record)
    puts "[Validator] Validating..."
    true
  end
end

class Logger
  def log(record)
    puts "[Logger] Saving..."
  end
end

class Record
  def initialize(validator: Validator.new, logger: Logger.new)
    @validator = validator
    @logger = logger
  end

  def save
    @logger.log(self)
    @validator.validate(self)
    puts "[Record] Saving to database"
  end
end

record = Record.new
record.save
# Output:
# [Logger] Saving...
# [Validator] Validating...
# [Record] Saving to database
```

## Key Changes

| Before | After |
|--------|-------|
| Implicit `super` chain | Explicit method calls in order |
| Include-order dependency | Constructor injection |
| Concerns coupled via inheritance | Concerns are independent objects |
| Cannot test concerns in isolation | Each concern is independently testable |
| Adding a concern risks collision | Adding a concern is adding a collaborator |

## Verification

- Same output for the same inputs.
- `Validator` and `Logger` can be tested independently.
- Changing the order of operations is a one-line change in `save`.
- Adding a new concern (e.g., `Notifier`) requires no changes to existing concerns.
