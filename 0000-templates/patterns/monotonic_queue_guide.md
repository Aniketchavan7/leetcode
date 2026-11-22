# Algorithmic Pattern: Monotonic Queue

## 1. Overview
A Monotonic Queue maintains elements in strictly ascending or descending order, supporting amortized $O(1)$ push, pop, and max/min queries.

## 2. Canonical Implementation (Python)
```python
from collections import deque

class MonotonicQueue:
    def __init__(self):
        self.q = deque()

    def push(self, val: int) -> None:
        while self.q and self.q[-1] < val:
            self.q.pop()
        self.q.append(val)

    def pop(self, val: int) -> None:
        if self.q and self.q[0] == val:
            self.q.popleft()

    def max(self) -> int:
        return self.q[0]
```

## 3. Top Interview Problems
- **LeetCode 239**: Sliding Window Maximum ($O(N)$ time)
- **LeetCode 862**: Shortest Subarray with Sum at Least K
- **LeetCode 1425**: Constrained Subsequence Sum
