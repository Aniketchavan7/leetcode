# 279. Perfect Squares

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/perfect-squares)
[![Topic: Breadth-First Search & Math & Dynamic Programming](https://img.shields.io/badge/Topic-Breadth-First%20Search%20&%20Math%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/perfect-squares)

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
**Sample Input**: `n = 12`  
**Expected Output**: `3`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `n = 12` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `3` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int numSquares(int n) {
        int m = (int) Math.sqrt(n);
        int[][] f = new int[m + 1][n + 1];
        for (var g : f) {
            Arrays.fill(g, 1 << 30);
        }
        f[0][0] = 0;
        for (int i = 1; i <= m; ++i) {
            for (int j = 0; j <= n; ++j) {
                f[i][j] = f[i - 1][j];
                if (j >= i * i) {
                    f[i][j] = Math.min(f[i][j], f[i][j - i * i] + 1);
                }
            }
        }
        return f[m][n];
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def numSquares(self, n: int) -> int:
        m = int(sqrt(n))
        f = [[inf] * (n + 1) for _ in range(m + 1)]
        f[0][0] = 0
        for i in range(1, m + 1):
            for j in range(n + 1):
                f[i][j] = f[i - 1][j]
                if j >= i * i:
                    f[i][j] = min(f[i][j], f[i][j - i * i] + 1)
        return f[m][n]
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
