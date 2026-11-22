# System Design Blueprint: Distributed URL Shortener

## 1. Capacity Estimations
- Write QPS: 1,160 writes/sec
- Read QPS: 11,600 reads/sec (10:1 ratio)
- Storage (5 years): 15 TB

## 2. High-Availability Caching
Redis cluster caching top 20% hottest URLs (80-20 Pareto distribution).
