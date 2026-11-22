# F — Shared API Contracts & Integration

[简体中文（GitHub Issue）](https://github.com/Ir1svanquish/IntentAware-Agent/issues/6) | **English**

## Scope
Coordinate shared schemas, development setup and integration. A volunteer can lead, with all five team members reviewing. This is not a sixth compulsory team member.

## Implementation guide
1. Agree on repository boundaries, Python/Node versions, local startup, and basic CI checks.
2. Define Goal, ActivityContext, ActivityClassification, Detour, DelegationRequest, DelegationJob, Checkpoint and ExperimentEvent schemas.
3. Publish `openapi.yaml` or equivalent API documentation with input/output and error examples.
4. Supply mock JSON fixtures and an integration plan so module owners can work in parallel.
5. Document branch/PR review expectations and how shared contracts can change.
6. Integrate the goal → detour → resume MVP before delegation and experiments.

## Deliverables
Shared API specification, setup guide, request/response fixtures and minimum integration smoke tests.

## Acceptance checklist
- [ ] All modules use unambiguous contracts agreed by owners.
- [ ] Mock frontend calls can exercise the planned main endpoints.
- [ ] New collaborators can follow the setup guide, with unimplemented steps clearly marked.
- [ ] Success, invalid-input and error examples are available for core APIs.
- [ ] Contract changes are reviewed by dependent owners and smoke tests are reproducible.

**Dependencies:** Cross-team agreement before significant parallel implementation. **Branch:** `feature/shared-contracts`.
