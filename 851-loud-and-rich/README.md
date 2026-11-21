# 851. Loud and Rich

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/loud-and-rich)
[![Topic: Depth-First Search & Graph & Topological Sort](https://img.shields.io/badge/Topic-Depth-First%20Search%20&%20Graph%20&%20Topological%20Sort-blue)](https://leetcode.com/problems/loud-and-rich)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We model the problem as a graph of vertices and edges. Using standard BFS/DFS or Topological Sort / Union-Find, we explore connectivity and paths systematically."

---

### 💡 Intuition & Core Insight
- **Visited State**: Maintaining a visited set prevents infinite cycles in directed/undirected graphs.
- **Topological Invariant**: In-degree tracking identifies dependency resolution order.
- **Connectivity**: Disjoint Set Union (DSU) provides near O(1) amortized path compression.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]`  
**Expected Output**: `[5,5,2,5,4,5,6,7]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[5,5,2,5,4,5,6,7]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private List<Integer>[] g;
    private int n;
    private int[] quiet;
    private int[] ans;

    public int[] loudAndRich(int[][] richer, int[] quiet) {
        n = quiet.length;
        this.quiet = quiet;
        g = new List[n];
        ans = new int[n];
        Arrays.fill(ans, -1);
        Arrays.setAll(g, k -> new ArrayList<>());
        for (var r : richer) {
            g[r[1]].add(r[0]);
        }
        for (int i = 0; i < n; ++i) {
            dfs(i);
        }
        return ans;
    }

    private void dfs(int i) {
        if (ans[i] != -1) {
            return;
        }
        ans[i] = i;
        for (int j : g[i]) {
            dfs(j);
            if (quiet[ans[j]] < quiet[ans[i]]) {
                ans[i] = ans[j];
            }
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        def dfs(i: int):
            if ans[i] != -1:
                return
            ans[i] = i
            for j in g[i]:
                dfs(j)
                if quiet[ans[j]] < quiet[ans[i]]:
                    ans[i] = ans[j]

        g = defaultdict(list)
        for a, b in richer:
            g[b].append(a)
        n = len(quiet)
        ans = [-1] * n
        for i in range(n):
            dfs(i)
        return ans
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(V + E)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(V)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Disconnected graph components.
2. Self-loops and multi-edges between the same vertex pair.
3. Cyclic dependencies causing deadlock.

---

### 💬 Follow-Up Questions You Might Get
*What if edges have arbitrary weights?* Use Dijkstra's algorithm for non-negative weights or Bellman-Ford / SPFA for negative edge weights.
