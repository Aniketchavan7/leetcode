# 200. Number of Islands

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/number-of-islands/)
[![Topic: Graph / BFS/DFS](https://img.shields.io/badge/Topic-Graph%20/%20BFS/DFS-blue)](https://leetcode.com/problems/number-of-islands/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Given an M x N 2D binary grid, an island is formed by connected 1s (land). We iterate through each cell. When we find a '1', we increment our island count and launch a DFS/BFS to sink the entire island by marking all reachable 1s to '0' (water). Sinking the island prevents double-counting."

---

### 💡 Intuition & Core Insight
- **Connected Components**: Each island is a connected component. Flood-fill sinking labels the entire component in O(size) without extra visited memory.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**:
`1 1 0`
`1 1 0`
`0 0 1`
- At (0,0)='1': count=1. Sinks (0,0), (0,1), (1,0), (1,1) all to '0'.
- Continues scanning... meets '0's until (2,2)='1': count=2. Sinks (2,2).
Total islands = 2.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        int m = grid.length, n = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    sink(grid, i, j);
                }
            }
        }
        return count;
    }

    private void sink(char[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != '1') return;
        grid[r][c] = '0'; // Sink to water
        sink(grid, r + 1, c);
        sink(grid, r - 1, c);
        sink(grid, r, c + 1);
        sink(grid, r, c - 1);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0

        def sink(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            sink(r + 1, c)
            sink(r - 1, c)
            sink(r, c + 1)
            sink(r, c - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    sink(i, j)

        return count
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(M \cdot N)$ — Every cell is visited at most a constant number of times.
- **Space Complexity**: $\mathcal{O}(M \cdot N)$ — Worst-case recursion call stack if the entire grid is one huge island.

---

### ⚠️ Edge Cases & Interview Traps
1. All '0's: returns 0.
2. All '1's: returns 1.

---

### 💬 Follow-Up Questions You Might Get
- *What if the grid cannot be modified?* Use a boolean visited[][] matrix or Disjoint Set Union (Union-Find).
