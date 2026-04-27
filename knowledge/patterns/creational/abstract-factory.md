# Abstract Factory

## Use When

- Families of related objects must be created together consistently.
- The product family varies by platform, tenant, provider, or environment.

## Avoid When

- Only one product varies.
- A simple factory or configuration map is enough.

## Core Idea

Provide an interface for creating related objects without exposing concrete classes.
