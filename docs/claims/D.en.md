# D — Asynchronous Delegation & Deferred Delivery

[简体中文（GitHub Issue）](https://github.com/Ir1svanquish/IntentAware-Agent/issues/4) | **English**

## Scope
Handle confirmed side questions as background jobs, retrieve up to two public sources, check evidence, and deliver results immediately (I) or at a user checkpoint (D).

## Implementation guide
1. Transform question, approved excerpt and optional note into an editable request; allow no more than one clarification.
2. Define durable draft, confirmed, queued, running, ready, delivered, failed and cancelled states.
3. Execute retrieval in a separate worker and record sources, latency and errors; never depend on a permanently running browser extension service worker.
4. Produce a short answer with traceable source links and unresolved points. Validate answer support against retrieved material.
5. Implement immediate display for I and checkpoint delivery for D, including view early, draft edits and cancellation.
6. Test timeout, retry, restart and failure behavior.

## Deliverables
Delegation and delivery backend modules, worker, API contracts, mock retriever, tests and usage guide.

## Acceptance checklist
- [ ] A request can be created, confirmed, run and viewed end-to-end.
- [ ] No more than two public sources are used, and citations map to retrieved content.
- [ ] I/D share model, source budget and answer format, changing delivery timing only.
- [ ] Early viewing works in D and cancelled jobs do not unexpectedly deliver later.
- [ ] Timeouts, worker errors and restart cases have observable status and documented handling.

**Dependencies:** F contract/job model and A controls. **Branch:** `feature/delegation-agent`.
