# 822. Card Flipping Game

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/card-flipping-game)
[![Topic: Array & Hash Table](https://img.shields.io/badge/Topic-Array%20&%20Hash%20Table-blue)](https://leetcode.com/problems/card-flipping-game)

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
**Sample Input**: `fronts = [1,2,4,4,7], backs = [1,3,4,1,3]`  
**Expected Output**: `2`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `fronts = [1,2,4,4,7], backs = [1,3,4,1,3]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `2` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int flipgame(int[] fronts, int[] backs) {
        Set<Integer> s = new HashSet<>();
        int n = fronts.length;
        for (int i = 0; i < n; ++i) {
            if (fronts[i] == backs[i]) {
                s.add(fronts[i]);
            }
        }
        int ans = 9999;
        for (int v : fronts) {
            if (!s.contains(v)) {
                ans = Math.min(ans, v);
            }
        }
        for (int v : backs) {
            if (!s.contains(v)) {
                ans = Math.min(ans, v);
            }
        }
        return ans % 9999;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        s = {a for a, b in zip(fronts, backs) if a == b}
        return min((x for x in chain(fronts, backs) if x not in s), default=0)
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
