# 317. Shortest Distance from All Buildings

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/shortest-distance-from-all-buildings)
[![Topic: Breadth-First Search & Array & Matrix](https://img.shields.io/badge/Topic-Breadth-First%20Search%20&%20Array%20&%20Matrix-blue)](https://leetcode.com/problems/shortest-distance-from-all-buildings)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Breadth-First Search strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]`  
**Expected Output**: `7`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `7` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int shortestDistance(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        Deque<int[]> q = new LinkedList<>();
        int total = 0;
        int[][] cnt = new int[m][n];
        int[][] dist = new int[m][n];
        int[] dirs = {-1, 0, 1, 0, -1};
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    ++total;
                    q.offer(new int[] {i, j});
                    int d = 0;
                    boolean[][] vis = new boolean[m][n];
                    while (!q.isEmpty()) {
                        ++d;
                        for (int k = q.size(); k > 0; --k) {
                            int[] p = q.poll();
                            for (int l = 0; l < 4; ++l) {
                                int x = p[0] + dirs[l];
                                int y = p[1] + dirs[l + 1];
                                if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 0
                                    && !vis[x][y]) {
                                    ++cnt[x][y];
                                    dist[x][y] += d;
                                    q.offer(new int[] {x, y});
                                    vis[x][y] = true;
                                }
                            }
                        }
                    }
                }
            }
        }
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 0 && cnt[i][j] == total) {
                    ans = Math.min(ans, dist[i][j]);
                }
            }
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def shortestDistance(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        total = 0
        cnt = [[0] * n for _ in range(m)]
        dist = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total += 1
                    q.append((i, j))
                    d = 0
                    vis = set()
                    while q:
                        d += 1
                        for _ in range(len(q)):
                            r, c = q.popleft()
                            for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                                x, y = r + a, c + b
                                if (
                                    0 <= x < m
                                    and 0 <= y < n
                                    and grid[x][y] == 0
                                    and (x, y) not in vis
                                ):
                                    cnt[x][y] += 1
                                    dist[x][y] += d
                                    q.append((x, y))
                                    vis.add((x, y))
        ans = inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and cnt[i][j] == total:
                    ans = min(ans, dist[i][j])
        return -1 if ans == inf else ans
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
