# 684. Redundant Connection

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/redundant-connection)
[![Topic: Depth-First Search & Breadth-First Search & Union Find](https://img.shields.io/badge/Topic-Depth-First%20Search%20&%20Breadth-First%20Search%20&%20Union%20Find-blue)](https://leetcode.com/problems/redundant-connection)

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
**Sample Input**: `edges = [[1,2],[1,3],[2,3]]`  
**Expected Output**: `[2,3]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `edges = [[1,2],[1,3],[2,3]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[2,3]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int[] p;

    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        p = new int[n];
        for (int i = 0; i < n; ++i) {
            p[i] = i;
        }
        for (int i = 0;; ++i) {
            int pa = find(edges[i][0] - 1);
            int pb = find(edges[i][1] - 1);
            if (pa == pb) {
                return edges[i];
            }
            p[pa] = pb;
        }
    }

    private int find(int x) {
        if (p[x] != x) {
            p[x] = find(p[x]);
        }
        return p[x];
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        p = list(range(len(edges)))
        for a, b in edges:
            pa, pb = find(a - 1), find(b - 1)
            if pa == pb:
                return [a, b]
            p[pa] = pb
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
