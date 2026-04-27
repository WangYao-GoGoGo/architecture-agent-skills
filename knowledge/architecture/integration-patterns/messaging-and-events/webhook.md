# Webhook

## Project Fit

Webhooks fit external event delivery between systems where the receiver exposes an HTTP endpoint.

## Use When

- A system needs to notify external consumers about events.
- Polling would be inefficient or delayed.
- Consumers can verify, deduplicate, and retry safely.

## Avoid When

- The receiver cannot provide stable, secure endpoints.
- Delivery ordering and retries are critical but unsupported.
- Payload schemas are not versioned.

## Core Idea

A provider sends HTTP callbacks to registered consumer endpoints when events occur.

## Fits Best With

- SaaS integrations, payment events, CI/CD callbacks, external notifications.

## Verification

- Signatures or authentication protect delivery.
- Receivers handle duplicate and delayed events.
- Retry, timeout, and dead-letter behavior are documented.
