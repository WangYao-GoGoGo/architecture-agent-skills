---
name: wechat-pay-integration
description: Use when reviewing or designing WeChat Pay integration, including JSAPI, Native, App, H5, Mini Program payment, refunds, notifications, certificate management, and merchant platform contracts.
---

# WeChat Pay Integration

## Knowledge To Use

- `knowledge/platform-ecosystems/wechat/`
- `knowledge/api/`
- `knowledge/platform/`

## Workflow

1. Identify payment scenarios: JSAPI, Native, App, H5, Mini Program, and partner/merchant platform flows.
2. Map WeChat Pay contracts: prepay order, payment notification, refund, query, close order, and certificate rotation.
3. Check whether payment logic, signature generation, XML/JSON parsing, notification handling, or refund workflows are mixed with domain order logic.
4. Review security: APIv2 vs APIv3 differences, certificate management, signature verification, notification idempotency, and merchant key storage.
5. Recommend payment adapter, order-payment mapping, notification handler, and refund service boundaries.
6. Verify with WeChat Pay sandbox, duplicate notification scenarios, timeout and retry, and refund idempotency tests.

## Output Format

```markdown
WeChat Pay integration:
- Payment scenarios:
- SDK coupling:
- Security concerns:
- Proposed boundaries:
- Verification:
```
