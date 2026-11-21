# 755. Pour Water

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/pour-water)
[![Topic: Array & Simulation](https://img.shields.io/badge/Topic-Array%20&%20Simulation-blue)](https://leetcode.com/problems/pour-water)

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
**Sample Input**: `heights = [2,1,1,2,1,2,2], volume = 4, k = 3`  
**Expected Output**: `[2,2,2,3,2,2,2]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `heights = [2,1,1,2,1,2,2], volume = 4, k = 3` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[2,2,2,3,2,2,2]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] pourWater(int[] heights, int volume, int k) {
        while (volume-- > 0) {
            boolean find = false;
            for (int d = -1; d < 2 && !find; d += 2) {
                int i = k, j = k;
                while (i + d >= 0 && i + d < heights.length && heights[i + d] <= heights[i]) {
                    if (heights[i + d] < heights[i]) {
                        j = i + d;
                    }
                    i += d;
                }
                if (j != k) {
                    find = true;
                    ++heights[j];
                }
            }
            if (!find) {
                ++heights[k];
            }
        }
        return heights;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def pourWater(self, heights: list[int], volume: int, k: int) -> list[int]:
        for _ in range(volume):
            for d in (-1, 1):
                i = j = k
                while 0 <= i + d < len(heights) and heights[i + d] <= heights[i]:
                    if heights[i + d] < heights[i]:
                        j = i + d
                    i += d
                if j != k:
                    heights[j] += 1
                    break
            else:
                heights[k] += 1
        return heights
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
