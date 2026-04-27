# Observer

## Use When

- Multiple independent consumers need to react to a state change or domain event.
- The publisher should not know concrete subscribers.

## Avoid When

- There is only one required next step in a synchronous workflow.
- Event ordering, retries, or consistency requirements are not understood.

## Core Idea

Publish an event or notification, and let subscribers react independently.

## Verification

- Subscribers can be added without changing the publisher.
- Failure behavior is defined for each subscriber.
- Event payloads are stable and minimal.
