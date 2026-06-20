# Bixbott Architecture Blueprint

Bixbott is planned as a modular AI Agent IDE ecosystem. This repository is the public organization hub and should stay aligned with the canonical organization profile in [`Bixbott/.github`](https://github.com/Bixbott/.github).

## Modules

| Module | Responsibility |
| --- | --- |
| Bixbott-Core | Shared domain logic, policies, schemas, and execution contracts. |
| Bixbott-Agent | Task execution, tool calls, code generation, review, and automation loops. |
| Bixbott-Council | Multi-agent planning, evaluation, routing, and decision support. |
| Bixbott-Management | User/project configuration, permissions, state, logs, and operations. |
| Bixbott-CLI | Terminal-first workflows for developers and operators. |
| Bixbott-Dashboard | Web UI for monitoring, task orchestration, analytics, and system health. |
| Bixbott-Docs | Product docs, API reference, contribution guide, and examples. |

## Recommended implementation order

1. Define schemas and contracts in Core.
2. Build CLI commands that exercise Core locally.
3. Add Agent execution loops with logs and replayable state.
4. Introduce Council planning and routing.
5. Add Management APIs and Dashboard views.
6. Keep Docs synchronized with the `.github` organization profile.
