# 573. Squirrel Simulation

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/squirrel-simulation)
[![Topic: Array & Math](https://img.shields.io/badge/Topic-Array%20&%20Math-blue)](https://leetcode.com/problems/squirrel-simulation)

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
**Sample Input**: `height = 5, width = 7, tree = [2,2], squirrel = [4,4], nuts = [[3,0], [2,5]]`  
**Expected Output**: `12`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `height = 5, width = 7, tree = [2,2], squirrel = [4,4], nuts = [[3,0], [2,5]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `12` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
import static java.lang.Math.*;

class Solution {
    public int minDistance(int height, int width, int[] tree, int[] squirrel, int[][] nuts) {
        int tr = tree[0], tc = tree[1];
        int sr = squirrel[0], sc = squirrel[1];
        int s = 0;
        for (var e : nuts) {
            s += abs(e[0] - tr) + abs(e[1] - tc);
        }
        s <<= 1;
        int ans = Integer.MAX_VALUE;
        for (var e : nuts) {
            int a = abs(e[0] - tr) + abs(e[1] - tc);
            int b = abs(e[0] - sr) + abs(e[1] - sc);
            ans = min(ans, s - a + b);
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def minDistance(
        self,
        height: int,
        width: int,
        tree: list[int],
        squirrel: list[int],
        nuts: list[list[int]],
    ) -> int:
        tr, tc = tree
        sr, sc = squirrel
        s = sum(abs(r - tr) + abs(c - tc) for r, c in nuts) * 2
        ans = inf
        for r, c in nuts:
            a = abs(r - tr) + abs(c - tc)
            b = abs(r - sr) + abs(c - sc)
            ans = min(ans, s - a + b)
        return ans
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
