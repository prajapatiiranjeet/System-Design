# Content improvement progress

Review source: `content-original-en.json` contains the English course text extracted from the original runtime. The archive contributes first-stage snapshots only. This checklist is per lesson; a lesson remains in progress until its summary, goals, every stage title/body/callout/change note, and visible explanatory copy have been checked. Diagram labels, stage order, scene data, and interaction code are preserved.

Inventory: 40 unique lessons, 445 stages. The archive contains 41 HTML captures because the first lesson was captured twice.

| # | Lesson | Stages | Review | Content update | Unresolved issues |
|---:|---|---:|---|---|---|
| 1 | How a Request Travels | 10 | Complete | Complete | None |
| 2 | Latency & Throughput | 10 | Complete | Complete | None |
| 3 | Napkin Math | 9 | Complete | Complete | None |
| 4 | Vertical vs Horizontal Scaling | 11 | Complete | Complete | None |
| 5 | Load Balancing | 12 | Complete | Complete | None |
| 6 | Stateless Services | 10 | Complete | Complete | None |
| 7 | Caching | 13 | Complete | Complete | None |
| 8 | Content Delivery | 10 | Complete | Complete | None |
| 9 | SQL vs NoSQL | 10 | Complete | Complete | None |
| 10 | Indexes | 11 | Complete | Complete | None |
| 11 | Storage Engines | 13 | Complete | Complete | None |
| 12 | Replication | 11 | Complete | Complete | None |
| 13 | Sharding | 9 | Complete | Complete | None |
| 14 | Consistent Hashing | 10 | Complete | Complete | None |
| 15 | Unique IDs at Scale | 12 | Complete | Complete | None |
| 16 | CAP & Consistency | 11 | Complete | Complete | None |
| 17 | Consensus & Leader Election | 12 | Complete | Complete | None |
| 18 | Transactions & Isolation | 13 | Complete | Complete | None |
| 19 | Files & Media | 13 | Complete | Complete | None |
| 20 | REST, RPC & GraphQL | 10 | Complete | Complete | None |
| 21 | Message Queues | 11 | Complete | Complete | None |
| 22 | Pub/Sub & Events | 10 | Complete | Complete | None |
| 23 | Real-time Updates | 10 | Complete | Complete | None |
| 24 | Redundancy & Failover | 12 | Complete | Complete | None |
| 25 | Rate Limiting | 9 | Complete | Complete | None |
| 26 | Timeouts & Retries | 11 | Complete | Complete | None |
| 27 | Observability | 9 | Complete | Complete | None |
| 28 | Monolith vs Microservices | 12 | Complete | Complete | None |
| 29 | Service Discovery & Gateways | 13 | Complete | Complete | None |
| 30 | Sagas & Distributed Transactions | 11 | Complete | Complete | None |
| 31 | Batch & Stream Processing | 14 | Complete | Complete | None |
| 32 | Authentication | 12 | Complete | Complete | None |
| 33 | Authorization | 13 | Complete | Complete | None |
| 34 | Encryption & Secrets | 12 | Complete | Complete | None |
| 35 | Testing | 11 | Complete | Complete | None |
| 36 | CI/CD & Deployments | 11 | Complete | Complete | None |
| 37 | HLD & LLD | 8 | Complete | Complete | None |
| 38 | Design a URL Shortener | 12 | Complete | Complete | None |
| 39 | Design a News Feed | 12 | Complete | Complete | None |
| 40 | Design a Chat System | 12 | Complete | Complete | None |

## Writing and preservation rules

- Use short, direct sentences and define advanced terms when they first matter.
- Add familiar examples only when they explain a concept already in the lesson.
- Preserve the technical names, numbers, assumptions, limitations, and trade-offs.
- Preserve diagrams, labels, step order, UI, CSS, animation, and application behavior.
- Final verification: compare each rewrite against the extracted original and cross-check difficult distributed-systems claims against the user-provided GitHub reference.

## Accuracy notes

- The course resource index was consulted as a supporting map of System Design concepts: [awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources).
- UUID v7 wording clarifies that IDs sort roughly by time; strict ordering within one millisecond depends on the generator. Cross-checked against [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562.html).

- Password-storage, session-cookie, and phishing-resistance wording was checked against current [OWASP password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html), [OWASP session management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), and [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html) guidance.
- Encryption, key handling, TLS, and secret-management language was checked against current [OWASP cryptographic storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html), [OWASP secrets management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html), and [OWASP TLS](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html) guidance.
