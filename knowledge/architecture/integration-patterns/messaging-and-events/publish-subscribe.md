# Publish-Subscribe

## Project Fit

Publish-subscribe fits systems where one event should fan out to multiple independent subscribers.

## Use When

- Producers should not know subscriber identities.
- Multiple consumers independently react to the same event.
- Adding a subscriber should not require producer changes.

## Avoid When

- There is only one required next step and synchronous behavior is simpler.
- Ordering and delivery guarantees are not understood.
- Subscribers are actually tightly coupled steps in one workflow.

## Core Idea

A publisher emits messages to a topic or channel. Subscribers receive messages independently.

## Fits Best With

- Domain events, notifications, analytics, cache invalidation, indexing, integration events.

## Verification

- Subscriber failure does not break the publisher.
- Duplicate delivery is safe or handled.
- Topic ownership and schema evolution are clear.
