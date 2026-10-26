---
applyTo: "tests/**"
---

- Keep unit tests isolated: call services directly with mocked repositories; do not use the database or HTTP client.
- Use integration tests for HTTP contracts and persistence; they use `TestClient` with a real PostgreSQL test database.
- Integration fixtures create and drop tables per test. Do not run `make test-integration` while the app is running.
- For state-transition failures, assert both the error response and that persisted order state remains unchanged.
- When testing cross-module payment behavior, verify both invoice and order state.
