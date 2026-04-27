# Interpreter

## Intent
Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.

## Use When
- The grammar is simple and stable.
- Efficiency is not a critical concern.
- You need to parse and evaluate expressions (math, search queries, configuration rules).

## Structure
- AbstractExpression declares an Interpret operation.
- TerminalExpression implements Interpret for terminal symbols.
- NonterminalExpression implements Interpret for non-terminal symbols (composed of sub-expressions).
- Context contains global information for the interpreter.

## Heuristics
1. **Keep grammars small**: Interpreter works well for small, simple grammars. For complex grammars, use a parser generator.
2. **Use the Composite pattern**: The abstract syntax tree is a Composite structure.
3. **Visitor for operations**: Use Visitor to define operations on the syntax tree without modifying the expression classes.
4. **Consider DSLs**: Interpreter is useful for domain-specific languages.

## Common Risks
1. **Complex grammars**: The pattern doesn't scale well for complex grammars — class count grows with grammar size.
2. **Performance**: Recursive interpretation can be slow for large expressions.
3. **Maintenance**: Grammar changes require changing many expression classes.
4. **Better alternatives**: For most parsing needs, parser generators (ANTLR, PEG) or existing expression evaluators are better.

## Related Patterns
- **Composite**: The abstract syntax tree is a Composite.
- **Flyweight**: Can share terminal symbols.
- **Visitor**: Can define operations on the syntax tree without modifying classes.
- **Iterator**: Can traverse the syntax tree.
