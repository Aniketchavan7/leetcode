# 210. Course Schedule II

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/course-schedule-ii)
[![Topic: Depth-First Search & Breadth-First Search & Graph](https://img.shields.io/badge/Topic-Depth-First%20Search%20&%20Breadth-First%20Search%20&%20Graph-blue)](https://leetcode.com/problems/course-schedule-ii)

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
**Sample Input**: `numCourses = 2, prerequisites = [[1,0]]`  
**Expected Output**: `[0,1]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `numCourses = 2, prerequisites = [[1,0]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[0,1]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<Integer>[] g = new List[numCourses];
        Arrays.setAll(g, k -> new ArrayList<>());
        int[] indeg = new int[numCourses];
        for (var p : prerequisites) {
            int a = p[0], b = p[1];
            g[b].add(a);
            ++indeg[a];
        }
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) {
                q.offer(i);
            }
        }
        int[] ans = new int[numCourses];
        int cnt = 0;
        while (!q.isEmpty()) {
            int i = q.poll();
            ans[cnt++] = i;
            for (int j : g[i]) {
                if (--indeg[j] == 0) {
                    q.offer(j);
                }
            }
        }
        return cnt == numCourses ? ans : new int[0];
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        g = defaultdict(list)
        indeg = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            indeg[a] += 1
        ans = []
        q = deque(i for i, x in enumerate(indeg) if x == 0)
        while q:
            i = q.popleft()
            ans.append(i)
            for j in g[i]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        return ans if len(ans) == numCourses else []
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
