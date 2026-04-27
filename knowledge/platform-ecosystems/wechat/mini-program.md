# WeChat Mini Program Architecture

## Heuristics

- Keep pages responsible for route-level composition and user interaction.
- Keep reusable UI in components and reusable workflow/data logic in services or model modules.
- Keep `wx.*` platform API calls behind adapters when the behavior matters to tests, portability, or error handling.
- Keep backend contracts explicit instead of coupling UI directly to cloud function or request details.
- Treat login, session refresh, permissions, subscription messages, uploads, and storage as architecture concerns.

## Common Risks

- Page files owning UI, state, network requests, authorization, and business policy together.
- Platform API calls scattered across components.
- Backend trust decisions placed in mini program client code.
- Package size, subpackage loading, and review constraints handled too late.

## Verification

- Representative pages can be tested or reasoned about without invoking real WeChat APIs.
- Platform adapters have clear fallback/error behavior.
- Sensitive operations are delegated to trusted backend endpoints.
