# 582. Kill Process

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/kill-process)
[![Topic: Tree & Depth-First Search & Breadth-First Search](https://img.shields.io/badge/Topic-Tree%20&%20Depth-First%20Search%20&%20Breadth-First%20Search-blue)](https://leetcode.com/problems/kill-process)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "For tree structures, we leverage recursive DFS or iterative BFS to traverse nodes. In **Kill Process**, processing each node once while maintaining tree invariants allows linear-time resolution."

---

### 💡 Intuition & Core Insight
- **Recursive Invariant**: At each subtree, we compute left and right subtree properties and aggregate the result.
- **Traversal Choice**: Pre-order / In-order / Post-order aligns naturally with tree height, sum, or path validation.
- **Stack Depth**: Auxiliary space is bounded by the height of the tree.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5`  
**Expected Output**: `[5,10]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[5,10]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private Map<Integer, List<Integer>> g = new HashMap<>();
    private List<Integer> ans = new ArrayList<>();

    public List<Integer> killProcess(List<Integer> pid, List<Integer> ppid, int kill) {
        int n = pid.size();
        for (int i = 0; i < n; ++i) {
            g.computeIfAbsent(ppid.get(i), k -> new ArrayList<>()).add(pid.get(i));
        }
        dfs(kill);
        return ans;
    }

    private void dfs(int i) {
        ans.add(i);
        for (int j : g.getOrDefault(i, Collections.emptyList())) {
            dfs(j);
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        def dfs(i: int):
            ans.append(i)
            for j in g[i]:
                dfs(j)

        g = defaultdict(list)
        for i, p in zip(pid, ppid):
            g[p].append(i)
        ans = []
        dfs(kill)
        return ans
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(H)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Skewed trees where height H = N leading to recursion stack overflow.
2. Single-node trees or empty tree roots (root == null).
3. Handling leaf nodes vs single-child nodes.

---

### 💬 Follow-Up Questions You Might Get
*Can we do this in O(1) space?* Morris Traversal can achieve O(1) extra space by threading binary trees.
