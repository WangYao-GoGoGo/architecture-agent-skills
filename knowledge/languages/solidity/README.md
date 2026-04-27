# Solidity Architecture Idioms

## Use When

- Reviewing Solidity smart contract design, gas optimization, access control, or upgradeability patterns.

## Heuristics

- Use `Checks-Effects-Interactions` pattern to prevent reentrancy.
- Prefer `OpenZeppelin` contracts for standard implementations (ERC20, ERC721, Ownable).
- Use `uint256` as the default integer type — avoid smaller types unless packing in structs.
- Use `immutable` and `constant` for values that don't change after deployment.
- Use `modifier` for access control — `onlyOwner` is the most common pattern.
- Emit events for all state-changing operations.
- Use `receive()` and `fallback()` functions carefully — they can receive ETH.
- Use `interface` for external contract interactions.

## Common Risks

- Reentrancy attacks from external calls before state updates.
- Integer overflow/underflow (though Solidity 0.8+ has built-in checks).
- Front-running from transaction ordering dependencies.
- Gas griefing from unbounded loops or dynamic array iteration.
- Upgradeability proxy pattern bugs (storage collision, function selector clashes).
