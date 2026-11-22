# Senior SWE System Design Rubric

## Assessment Dimensions
1. **Scope & Functional Requirements (15%)**: Clear boundary definition, edge cases, read/write ratios.
2. **Back-of-Envelope Calculations (15%)**: QPS estimation, storage footprint across 5 years, network bandwidth.
3. **High-Level Architecture (30%)**: Component decoupling, load balancing, caching tiers, data storage choice.
4. **Deep Dive & Bottlenecks (30%)**: Replication lag, partition strategies, consensus protocols (Raft/Paxos).
5. **Operational Excellence (10%)**: Telemetry, canary deployments, graceful degradation under stress.
