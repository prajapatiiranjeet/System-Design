# Lesson verification

This checklist distinguishes static archive inspection from live local-app verification. A checked item means it was exercised in the local browser; do not infer success from the source files alone.

## Archive inventory

- Supplied archive: 41 HTML captures.
- Unique course lessons: 40.
- Duplicate: `How a Request Travels` appears twice; both files are preserved in `source-captures/`.
- Lesson order, module, title, and the saved timeline labels/tooltips are recorded in `lesson-registry.json`.

## Per-lesson browser checklist

For each of the 40 rows below, verify: opens; correct title and module; diagram renders; all local assets load; Next and Previous work; Play/Pause and Replay work; final stage is reachable; switching away and returning restores the lesson; no console errors.

| # | Lesson | Stages | Open, title & initial stage | Diagram and local assets | Next / Previous | Play / Pause | Replay / final stage | Switch / return | Runtime errors |
|---:|---|---:|---|---|---|---|---|---|---|
| 1 | How a Request Travels | 10 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 2 | Latency & Throughput | 10 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 3 | Napkin Math | 9 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 4 | Vertical vs Horizontal Scaling | 11 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 5 | Load Balancing | 12 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 6 | Stateless Services | 10 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 7 | Caching | 13 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 8 | Content Delivery | 10 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 9 | SQL vs NoSQL | 10 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 10 | Indexes | 11 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 11 | Storage Engines | 13 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 12 | Replication | 11 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 13 | Sharding | 9 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 14 | Consistent Hashing | 10 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 15 | Unique IDs at Scale | 12 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 16 | CAP & Consistency | 11 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 17 | Consensus & Leader Election | 12 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 18 | Transactions & Isolation | 13 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 19 | Files & Media | 13 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 20 | REST, RPC & GraphQL | 10 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 21 | Message Queues | 11 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 22 | Pub/Sub & Events | 10 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 23 | Real-time Updates | 10 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 24 | Redundancy & Failover | 12 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 25 | Rate Limiting | 9 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 26 | Timeouts & Retries | 11 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 27 | Observability | 9 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 28 | Monolith vs Microservices | 12 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 29 | Service Discovery & Gateways | 13 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 30 | Sagas & Distributed Transactions | 11 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 31 | Batch & Stream Processing | 14 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 32 | Authentication | 12 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 33 | Authorization | 13 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 34 | Encryption & Secrets | 12 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 35 | Testing | 11 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 36 | CI/CD & Deployments | 11 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 37 | HLD & LLD | 8 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 38 | Design a URL Shortener | 12 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 39 | Design a News Feed | 12 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| 40 | Design a Chat System | 12 | [x] | [x] | [x] | [x] | [x] | [x] | [x] |

## Browser verification

- [x] All 40 lessons opened in a local browser with the expected lesson title, a rendered SVG diagram, and a non-empty stage timeline.
- [x] For every lesson, Next reached stage 2, Back returned to stage 1, and the final timeline stage was reachable.
- [x] For every lesson, the original traffic Pause/Play control toggled its label, Replay returned to stage 1, and switching to another lesson and back reopened the expected lesson.
- [x] All 820 dynamically imported language chunks and 11 font files load from the local project. A clean local session switched to Spanish without console errors.
- [x] A clean lesson refresh resumed the saved stage (Caching, stage 2).
- [x] Search returned Caching and related topics; selecting the result opened Caching. Light/dark theme toggled and was restored.
- [x] The progress panel showed 40/40 after all lessons reached their final stage. Reset progress cleared the saved completion state and returned the panel to 0/40.
- [x] Added lesson autoplay advanced to stage 2, paused without advancing, resumed to stage 3, and Replay lesson returned to stage 1.
- [x] A 1280×720 browser view showed the responsive course shell and full lesson diagram. The original stylesheet includes breakpoint rules for smaller screens.
- [x] The checks ran on a separate local test origin (`127.0.0.1:5174`) so they did not populate the app’s normal progress storage.

