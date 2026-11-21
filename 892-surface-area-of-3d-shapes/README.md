# 892. Surface Area of 3D Shapes

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/surface-area-of-3d-shapes)
[![Topic: Geometry & Array & Math](https://img.shields.io/badge/Topic-Geometry%20&%20Array%20&%20Math-blue)](https://leetcode.com/problems/surface-area-of-3d-shapes)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Geometry strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `grid = [[1,2],[3,4]]`  
**Expected Output**: `34`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `grid = [[1,2],[3,4]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `34` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int surfaceArea(int[][] grid) {
        int n = grid.length;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] > 0) {
                    ans += 2 + grid[i][j] * 4;
                    if (i > 0) {
                        ans -= Math.min(grid[i][j], grid[i - 1][j]) * 2;
                    }
                    if (j > 0) {
                        ans -= Math.min(grid[i][j], grid[i][j - 1]) * 2;
                    }
                }
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        ans = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    ans += 2 + v * 4
                    if i:
                        ans -= min(v, grid[i - 1][j]) * 2
                    if j:
                        ans -= min(v, grid[i][j - 1]) * 2
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
