# 265. Paint House II

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/paint-house-ii)
[![Topic: Array & Dynamic Programming](https://img.shields.io/badge/Topic-Array%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/paint-house-ii)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "In this problem, subproblems overlap and possess optimal substructure. Instead of an exponential recursive tree, we define a memoized state array where dp[i] captures the optimal decision up to index i, transitioning in polynomial time."

---

### 💡 Intuition & Core Insight
- **Brute Force Bottleneck**: Exploring all state combinations yields exponential O(2^N) or O(N!) complexity.
- **Optimal Substructure**: The optimal solution at state i depends strictly on already computed sub-states.
- **State Invariant**: Maintaining optimal transitions avoids re-evaluating subproblems.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `costs = [[1,5,3],[2,9,4]]`  
**Expected Output**: `5`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `costs = [[1,5,3],[2,9,4]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `5` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int minCostII(int[][] costs) {
        int n = costs.length, k = costs[0].length;
        int[] f = costs[0].clone();
        for (int i = 1; i < n; ++i) {
            int[] g = costs[i].clone();
            for (int j = 0; j < k; ++j) {
                int t = Integer.MAX_VALUE;
                for (int h = 0; h < k; ++h) {
                    if (h != j) {
                        t = Math.min(t, f[h]);
                    }
                }
                g[j] += t;
            }
            f = g;
        }
        return Arrays.stream(f).min().getAsInt();
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:
        n, k = len(costs), len(costs[0])
        f = costs[0][:]
        for i in range(1, n):
            g = costs[i][:]
            for j in range(k):
                t = min(f[h] for h in range(k) if h != j)
                g[j] += t
            f = g
        return min(f)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Boundary states at index 0 and 1.
2. Integer overflow when accumulating large transitions.
3. Base case initialization of unreachable states.

---

### 💬 Follow-Up Questions You Might Get
*Can we optimize space?* Yes, if each state depends only on the previous k states, we can reduce space from O(N) to O(1) using rolling variables.
