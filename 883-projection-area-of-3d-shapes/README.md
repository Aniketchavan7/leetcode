# 883. Projection Area of 3D Shapes

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/projection-area-of-3d-shapes)
[![Topic: Geometry & Array & Math](https://img.shields.io/badge/Topic-Geometry%20&%20Array%20&%20Math-blue)](https://leetcode.com/problems/projection-area-of-3d-shapes)

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
**Expected Output**: `17`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `grid = [[1,2],[3,4]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `17` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int projectionArea(int[][] grid) {
        int xy = 0, yz = 0, zx = 0;
        for (int i = 0, n = grid.length; i < n; ++i) {
            int maxYz = 0;
            int maxZx = 0;
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] > 0) {
                    ++xy;
                }
                maxYz = Math.max(maxYz, grid[i][j]);
                maxZx = Math.max(maxZx, grid[j][i]);
            }
            yz += maxYz;
            zx += maxZx;
        }
        return xy + yz + zx;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        xy = sum(v > 0 for row in grid for v in row)
        yz = sum(max(row) for row in grid)
        zx = sum(max(col) for col in zip(*grid))
        return xy + yz + zx
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
