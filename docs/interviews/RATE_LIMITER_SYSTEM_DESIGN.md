# System Design Blueprint: Distributed Rate Limiter

## 1. Sliding Window Counter via Redis Sorted Sets
Uses `ZREMRANGEBYSCORE` and `ZCARD` executed atomically via Lua scripts to prevent race conditions.
