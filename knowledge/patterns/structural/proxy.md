# Proxy

## Use When

- Access to another object or service needs control, lazy loading, caching, authorization, or remote access handling.

## Avoid When

- A direct dependency is simpler and there is no access policy.

## Core Idea

Stand in for another object while controlling access to it.

## Risks

- Hidden network or cache behavior can surprise callers.
- Keep latency, failure, and consistency visible in naming or documentation.
