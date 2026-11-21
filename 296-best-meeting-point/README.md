# 296. Best Meeting Point

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/best-meeting-point)
[![Topic: Array & Math & Matrix](https://img.shields.io/badge/Topic-Array%20&%20Math%20&%20Matrix-blue)](https://leetcode.com/problems/best-meeting-point)

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
**Sample Input**: `grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]`  
**Expected Output**: `6`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `6` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int minTotalDistance(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        List<Integer> rows = new ArrayList<>();
        List<Integer> cols = new ArrayList<>();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    rows.add(i);
                    cols.add(j);
                }
            }
        }
        Collections.sort(cols);
        int i = rows.get(rows.size() >> 1);
        int j = cols.get(cols.size() >> 1);
        return f(rows, i) + f(cols, j);
    }

    private int f(List<Integer> arr, int x) {
        int s = 0;
        for (int v : arr) {
            s += Math.abs(v - x);
        }
        return s;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def minTotalDistance(self, grid: list[list[int]]) -> int:
        def f(arr, x):
            return sum(abs(v - x) for v in arr)

        rows, cols = [], []
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    rows.append(i)
                    cols.append(j)
        cols.sort()
        i = rows[len(rows) >> 1]
        j = cols[len(cols) >> 1]
        return f(rows, i) + f(cols, j)
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
