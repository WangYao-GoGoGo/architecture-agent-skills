# Specification

## Intent
Encapsulate a business rule that determines whether an object satisfies some criteria. Allows combining rules with logical operators.

## Use When
- Business rules for selection should be reusable across different contexts.
- You need to combine rules with AND, OR, NOT.
- You want to keep domain logic out of repository queries.

## Structure
- Specification declares IsSatisfiedBy and And/Or/Not combinators.
- CompositeSpecification implements logical combinators.
- ConcreteSpecification implements specific business rules.

## Heuristics
1. **Composable**: Specifications should support AND, OR, NOT composition.
2. **Reusable**: A specification should be usable in-memory and for query generation.
3. **Naming**: Name specifications after business concepts (GoldCustomerSpec, OverdueInvoiceSpec).
4. **Query translation**: Specifications can be translated to SQL, LINQ, or other query languages.

## Common Risks
1. **Performance**: In-memory evaluation of specifications can be slow for large collections.
2. **Query generation complexity**: Translating specifications to efficient database queries is hard.
3. **Over-engineering**: Simple filter methods are often sufficient.
4. **Specification explosion**: Too many fine-grained specifications become hard to manage.

## Related Patterns
- **Repository**: Specifications are often passed to Repository methods.
- **Strategy**: Specification is a specialized Strategy for selection.
- **Composite**: Specification composition uses the Composite pattern.
