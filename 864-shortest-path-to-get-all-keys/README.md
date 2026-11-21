# 864. Shortest Path to Get All Keys

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/shortest-path-to-get-all-keys)
[![Topic: Bit Manipulation & Breadth-First Search & Array](https://img.shields.io/badge/Topic-Bit%20Manipulation%20&%20Breadth-First%20Search%20&%20Array-blue)](https://leetcode.com/problems/shortest-path-to-get-all-keys)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Bit Manipulation strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `grid = [&quot;@.a..&quot;,&quot;###.#&quot;,&quot;b.A.B&quot;]`  
**Expected Output**: `8`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `grid = [&quot;@.a..&quot;,&quot;###.#&quot;,&quot;b.A.B&quot;]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `8` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int[] dirs = {-1, 0, 1, 0, -1};

    public int shortestPathAllKeys(String[] grid) {
        int m = grid.length, n = grid[0].length();
        int k = 0;
        int si = 0, sj = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                char c = grid[i].charAt(j);
                if (Character.isLowerCase(c)) {
                    ++k;
                } else if (c == '@') {
                    si = i;
                    sj = j;
                }
            }
        }
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {si, sj, 0});
        boolean[][][] vis = new boolean[m][n][1 << k];
        vis[si][sj][0] = true;
        int ans = 0;
        while (!q.isEmpty()) {
            for (int t = q.size(); t > 0; --t) {
                var p = q.poll();
                int i = p[0], j = p[1], state = p[2];
                if (state == (1 << k) - 1) {
                    return ans;
                }
                for (int h = 0; h < 4; ++h) {
                    int x = i + dirs[h], y = j + dirs[h + 1];
                    if (x >= 0 && x < m && y >= 0 && y < n) {
                        char c = grid[x].charAt(y);
                        if (c == '#'
                            || (Character.isUpperCase(c) && ((state >> (c - 'A')) & 1) == 0)) {
                            continue;
                        }
                        int nxt = state;
                        if (Character.isLowerCase(c)) {
                            nxt |= 1 << (c - 'a');
                        }
                        if (!vis[x][y][nxt]) {
                            vis[x][y][nxt] = true;
                            q.offer(new int[] {x, y, nxt});
                        }
                    }
                }
            }
            ++ans;
        }
        return -1;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        si, sj = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == '@')
        k = sum(v.islower() for row in grid for v in row)
        dirs = (-1, 0, 1, 0, -1)
        q = deque([(si, sj, 0)])
        vis = {(si, sj, 0)}
        ans = 0
        while q:
            for _ in range(len(q)):
                i, j, state = q.popleft()
                if state == (1 << k) - 1:
                    return ans

                for a, b in pairwise(dirs):
                    x, y = i + a, j + b
                    nxt = state
                    if 0 <= x < m and 0 <= y < n:
                        c = grid[x][y]
                        if (
                            c == '#'
                            or c.isupper()
                            and (state & (1 << (ord(c) - ord('A')))) == 0
                        ):
                            continue
                        if c.islower():
                            nxt |= 1 << (ord(c) - ord('a'))
                        if (x, y, nxt) not in vis:
                            vis.add((x, y, nxt))
                            q.append((x, y, nxt))
            ans += 1
        return -1
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
