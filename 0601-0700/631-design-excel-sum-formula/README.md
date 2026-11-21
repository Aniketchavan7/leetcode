# 631. Design Excel Sum Formula

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/design-excel-sum-formula)
[![Topic: Graph & Design & Topological Sort](https://img.shields.io/badge/Topic-Graph%20&%20Design%20&%20Topological%20Sort-blue)](https://leetcode.com/problems/design-excel-sum-formula)

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
**Sample Input**: `Standard sample testcase`  
**Expected Output**: `Computed result`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `Input elements` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `Optimal Result` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
// Implementation provided in Solution.java
```

#### Python 3 Solution
```python
# Implementation provided in solution.py
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
