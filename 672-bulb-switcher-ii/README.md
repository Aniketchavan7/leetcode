# 672. Bulb Switcher II

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/bulb-switcher-ii)
[![Topic: Bit Manipulation & Depth-First Search & Breadth-First Search](https://img.shields.io/badge/Topic-Bit%20Manipulation%20&%20Depth-First%20Search%20&%20Breadth-First%20Search-blue)](https://leetcode.com/problems/bulb-switcher-ii)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Bit Manipulation strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `n = 1, presses = 1`  
**Expected Output**: `2`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `n = 1, presses = 1` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `2` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int flipLights(int n, int presses) {
        int[] ops = new int[] {0b111111, 0b010101, 0b101010, 0b100100};
        Set<Integer> vis = new HashSet<>();
        n = Math.min(n, 6);
        for (int mask = 0; mask < 1 << 4; ++mask) {
            int cnt = Integer.bitCount(mask);
            if (cnt <= presses && cnt % 2 == presses % 2) {
                int t = 0;
                for (int i = 0; i < 4; ++i) {
                    if (((mask >> i) & 1) == 1) {
                        t ^= ops[i];
                    }
                }
                t &= ((1 << 6) - 1);
                t >>= (6 - n);
                vis.add(t);
            }
        }
        return vis.size();
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        ops = (0b111111, 0b010101, 0b101010, 0b100100)
        n = min(n, 6)
        vis = set()
        for mask in range(1 << 4):
            cnt = mask.bit_count()
            if cnt <= presses and cnt % 2 == presses % 2:
                t = 0
                for i, op in enumerate(ops):
                    if (mask >> i) & 1:
                        t ^= op
                t &= (1 << 6) - 1
                t >>= 6 - n
                vis.add(t)
        return len(vis)
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
