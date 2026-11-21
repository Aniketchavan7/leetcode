# 885. Spiral Matrix III

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/spiral-matrix-iii)
[![Topic: Array & Matrix & Simulation](https://img.shields.io/badge/Topic-Array%20&%20Matrix%20&%20Simulation-blue)](https://leetcode.com/problems/spiral-matrix-iii)

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
**Sample Input**: `rows = 1, cols = 4, rStart = 0, cStart = 0`  
**Expected Output**: `[[0,0],[0,1],[0,2],[0,3]]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `rows = 1, cols = 4, rStart = 0, cStart = 0` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[[0,0],[0,1],[0,2],[0,3]]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[][] spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        int cnt = rows * cols;
        int[][] ans = new int[cnt][2];
        ans[0] = new int[] {rStart, cStart};
        if (cnt == 1) {
            return ans;
        }
        for (int k = 1, idx = 1;; k += 2) {
            int[][] dirs = new int[][] {{0, 1, k}, {1, 0, k}, {0, -1, k + 1}, {-1, 0, k + 1}};
            for (int[] dir : dirs) {
                int r = dir[0], c = dir[1], dk = dir[2];
                while (dk-- > 0) {
                    rStart += r;
                    cStart += c;
                    if (rStart >= 0 && rStart < rows && cStart >= 0 && cStart < cols) {
                        ans[idx++] = new int[] {rStart, cStart};
                        if (idx == cnt) {
                            return ans;
                        }
                    }
                }
            }
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> list[list[int]]:
        ans = [[rStart, cStart]]
        if rows * cols == 1:
            return ans
        k = 1
        while True:
            for dr, dc, dk in [[0, 1, k], [1, 0, k], [0, -1, k + 1], [-1, 0, k + 1]]:
                for _ in range(dk):
                    rStart += dr
                    cStart += dc
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        ans.append([rStart, cStart])
                        if len(ans) == rows * cols:
                            return ans
            k += 2
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
