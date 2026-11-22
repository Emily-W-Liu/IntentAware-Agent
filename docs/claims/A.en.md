# A — Browser Extension & UX

[简体中文（GitHub Issue）](https://github.com/Ir1svanquish/IntentAware-Agent/issues/1) | **English**

## Scope
Build a React + TypeScript Chrome Manifest V3 sidebar to show the user goal, context-aware activity prompts, detour capture, resumption suggestions, and delegation controls. The extension is a frontend client; NLP inference belongs to module B.

## Implementation guide
1. Bootstrap a buildable extension with a manifest and side panel entry point; document how to load it in Chrome.
2. Add goal confirmation, progress view, classification explanation, detour save/edit, and resumption controls.
3. Add editable delegation confirmation, status, early-view, cancel, and checkpoint interactions.
4. Capture minimal page context (title/URL); obtain user permission before sending excerpts. Support pause/dismiss controls.
5. Follow the F API contract. Use mocked request/response fixtures until backend endpoints are available.

## Deliverables
Source in `apps/extension/`, setup instructions, UI walkthrough/screenshots, tests, and a list of required API endpoints.

## Acceptance checklist
- [ ] A fresh developer can build, load, and open the extension using the README.
- [ ] With mock responses, demonstrate goal → activity prompt → detour capture → resumption.
- [ ] Loading, empty, failure, and success UI states are handled without silent errors.
- [ ] No page excerpt is sent without consent, and pause/dismiss works.
- [ ] The same UI can support G/P/I/D feature settings, without separate applications.

**Dependencies:** F contracts; B, C and D response schemas. **Branch:** `feature/extension-sidebar`.
