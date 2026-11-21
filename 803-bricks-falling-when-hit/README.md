# 803. Bricks Falling When Hit

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/bricks-falling-when-hit)
[![Topic: Union Find & Array & Matrix](https://img.shields.io/badge/Topic-Union%20Find%20&%20Array%20&%20Matrix-blue)](https://leetcode.com/problems/bricks-falling-when-hit)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Union Find strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]`  
**Expected Output**: `[2]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[2]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int[] p;
    private int[] size;

    public int[] hitBricks(int[][] grid, int[][] hits) {
        int m = grid.length;
        int n = grid[0].length;
        p = new int[m * n + 1];
        size = new int[m * n + 1];
        for (int i = 0; i < p.length; ++i) {
            p[i] = i;
            size[i] = 1;
        }
        int[][] g = new int[m][n];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                g[i][j] = grid[i][j];
            }
        }
        for (int[] h : hits) {
            g[h[0]][h[1]] = 0;
        }
        for (int j = 0; j < n; ++j) {
            if (g[0][j] == 1) {
                union(j, m * n);
            }
        }
        for (int i = 1; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (g[i][j] == 0) {
                    continue;
                }
                if (g[i - 1][j] == 1) {
                    union(i * n + j, (i - 1) * n + j);
                }
                if (j > 0 && g[i][j - 1] == 1) {
                    union(i * n + j, i * n + j - 1);
                }
            }
        }
        int[] ans = new int[hits.length];
        int[] dirs = {-1, 0, 1, 0, -1};
        for (int k = hits.length - 1; k >= 0; --k) {
            int i = hits[k][0];
            int j = hits[k][1];
            if (grid[i][j] == 0) {
                continue;
            }
            g[i][j] = 1;
            int prev = size[find(m * n)];
            if (i == 0) {
                union(j, m * n);
            }
            for (int l = 0; l < 4; ++l) {
                int x = i + dirs[l];
                int y = j + dirs[l + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && g[x][y] == 1) {
                    union(i * n + j, x * n + y);
                }
            }
            int curr = size[find(m * n)];
            ans[k] = Math.max(0, curr - prev - 1);
        }
        return ans;
    }

    private int find(int x) {
        if (p[x] != x) {
            p[x] = find(p[x]);
        }
        return p[x];
    }

    private void union(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        if (pa != pb) {
            size[pb] += size[pa];
            p[pa] = pb;
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                size[pb] += size[pa]
                p[pa] = pb

        m, n = len(grid), len(grid[0])
        p = list(range(m * n + 1))
        size = [1] * len(p)
        g = deepcopy(grid)
        for i, j in hits:
            g[i][j] = 0
        for j in range(n):
            if g[0][j] == 1:
                union(j, m * n)
        for i in range(1, m):
            for j in range(n):
                if g[i][j] == 0:
                    continue
                if g[i - 1][j] == 1:
                    union(i * n + j, (i - 1) * n + j)
                if j > 0 and g[i][j - 1] == 1:
                    union(i * n + j, i * n + j - 1)
        ans = []
        for i, j in hits[::-1]:
            if grid[i][j] == 0:
                ans.append(0)
                continue
            g[i][j] = 1
            prev = size[find(m * n)]
            if i == 0:
                union(j, m * n)
            for a, b in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and g[x][y] == 1:
                    union(i * n + j, x * n + y)
            curr = size[find(m * n)]
            ans.append(max(0, curr - prev - 1))
        return ans[::-1]
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
