# 749. Contain Virus

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/contain-virus)
[![Topic: Depth-First Search & Breadth-First Search & Array](https://img.shields.io/badge/Topic-Depth-First%20Search%20&%20Breadth-First%20Search%20&%20Array-blue)](https://leetcode.com/problems/contain-virus)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Depth-First Search strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]`  
**Expected Output**: `10`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `10` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private static final int[] DIRS = {-1, 0, 1, 0, -1};
    private List<Integer> c = new ArrayList<>();
    private List<List<Integer>> areas = new ArrayList<>();
    private List<Set<Integer>> boundaries = new ArrayList<>();
    private int[][] infected;
    private boolean[][] vis;
    private int m;
    private int n;

    public int containVirus(int[][] isInfected) {
        infected = isInfected;
        m = infected.length;
        n = infected[0].length;
        vis = new boolean[m][n];
        int ans = 0;
        while (true) {
            for (boolean[] row : vis) {
                Arrays.fill(row, false);
            }
            c.clear();
            areas.clear();
            boundaries.clear();
            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (infected[i][j] == 1 && !vis[i][j]) {
                        c.add(0);
                        areas.add(new ArrayList<>());
                        boundaries.add(new HashSet<>());
                        dfs(i, j);
                    }
                }
            }
            if (areas.isEmpty()) {
                break;
            }
            int idx = max(boundaries);
            ans += c.get(idx);
            for (int t = 0; t < areas.size(); ++t) {
                if (t == idx) {
                    for (int v : areas.get(t)) {
                        int i = v / n, j = v % n;
                        infected[i][j] = -1;
                    }
                } else {
                    for (int v : areas.get(t)) {
                        int i = v / n, j = v % n;
                        for (int k = 0; k < 4; ++k) {
                            int x = i + DIRS[k], y = j + DIRS[k + 1];
                            if (x >= 0 && x < m && y >= 0 && y < n && infected[x][y] == 0) {
                                infected[x][y] = 1;
                            }
                        }
                    }
                }
            }
        }
        return ans;
    }

    private int max(List<Set<Integer>> boundaries) {
        int idx = 0;
        int mx = boundaries.get(0).size();
        for (int i = 1; i < boundaries.size(); ++i) {
            int t = boundaries.get(i).size();
            if (mx < t) {
                mx = t;
                idx = i;
            }
        }
        return idx;
    }

    private void dfs(int i, int j) {
        vis[i][j] = true;
        int idx = areas.size() - 1;
        areas.get(idx).add(i * n + j);
        for (int k = 0; k < 4; ++k) {
            int x = i + DIRS[k], y = j + DIRS[k + 1];
            if (x >= 0 && x < m && y >= 0 && y < n) {
                if (infected[x][y] == 1 && !vis[x][y]) {
                    dfs(x, y);
                } else if (infected[x][y] == 0) {
                    c.set(idx, c.get(idx) + 1);
                    boundaries.get(idx).add(x * n + y);
                }
            }
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def containVirus(self, isInfected: list[list[int]]) -> int:
        def dfs(i, j):
            vis[i][j] = True
            areas[-1].append((i, j))
            for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n:
                    if isInfected[x][y] == 1 and not vis[x][y]:
                        dfs(x, y)
                    elif isInfected[x][y] == 0:
                        c[-1] += 1
                        boundaries[-1].add((x, y))

        m, n = len(isInfected), len(isInfected[0])
        ans = 0
        while 1:
            vis = [[False] * n for _ in range(m)]
            areas = []
            c = []
            boundaries = []
            for i, row in enumerate(isInfected):
                for j, v in enumerate(row):
                    if v == 1 and not vis[i][j]:
                        areas.append([])
                        boundaries.append(set())
                        c.append(0)
                        dfs(i, j)
            if not areas:
                break
            idx = boundaries.index(max(boundaries, key=len))
            ans += c[idx]
            for k, area in enumerate(areas):
                if k == idx:
                    for i, j in area:
                        isInfected[i][j] = -1
                else:
                    for i, j in area:
                        for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                            x, y = i + a, j + b
                            if 0 <= x < m and 0 <= y < n and isInfected[x][y] == 0:
                                isInfected[x][y] = 1
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
