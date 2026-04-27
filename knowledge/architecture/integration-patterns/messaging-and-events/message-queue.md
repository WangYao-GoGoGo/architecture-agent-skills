# Message Queue

## Project Fit

Message queues fit workloads that need buffering, retry, backpressure, or asynchronous processing by workers.

## Use When

- Work can happen after the request completes.
- Producers and consumers run at different rates.
- Retry and dead-letter handling are needed.

## Avoid When

- Immediate response and strong consistency are required.
- Queue ordering, visibility timeout, and retry behavior are not understood.
- The queue is used to hide slow synchronous work without user experience design.

## Core Idea

A producer enqueues work. One or more consumers process messages asynchronously.

## Fits Best With

- Background jobs, email sending, media processing, imports, indexing, webhook delivery.

## Verification

- Consumers are idempotent.
- Dead-letter and retry behavior is defined.
- Queue lag and failures are observable.
