# 370. Range Addition

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/range-addition)
[![Topic: Array & Prefix Sum](https://img.shields.io/badge/Topic-Array%20&%20Prefix%20Sum-blue)](https://leetcode.com/problems/range-addition)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Array strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]`  
**Expected Output**: `[-2,0,3,5,3]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[-2,0,3,5,3]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] getModifiedArray(int length, int[][] updates) {
        int[] d = new int[length];
        for (var e : updates) {
            int l = e[0], r = e[1], c = e[2];
            d[l] += c;
            if (r + 1 < length) {
                d[r + 1] -= c;
            }
        }
        for (int i = 1; i < length; ++i) {
            d[i] += d[i - 1];
        }
        return d;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        d = [0] * length
        for l, r, c in updates:
            d[l] += c
            if r + 1 < length:
                d[r + 1] -= c
        return list(accumulate(d))
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Handling empty or single-element inputs.
2. Boundary index arithmetic and potential overflow.
3. Duplicate or negative values in input collections.

---

### 💬 Follow-Up Questions You Might Get
*How does this scale to distributed streams?* Hash partitioning across shards or MapReduce pipelines can process data in parallel.
