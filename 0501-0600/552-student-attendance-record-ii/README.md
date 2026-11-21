# 552. Student Attendance Record II

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/student-attendance-record-ii)
[![Topic: Dynamic Programming](https://img.shields.io/badge/Topic-Dynamic%20Programming-blue)](https://leetcode.com/problems/student-attendance-record-ii)

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
**Sample Input**: `n = 2`  
**Expected Output**: `8`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `n = 2` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `8` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int checkRecord(int n) {
        final int mod = (int) 1e9 + 7;
        int[][] f = {{1, 1, 1}, {1, 1, 1}};
        for (int i = 0; i < n; ++i) {
            int[][] g = new int[2][3];
            for (int j = 0; j < 2; ++j) {
                for (int k = 0; k < 3; ++k) {
                    int ans = f[j][0];
                    if (j == 0) {
                        ans = (ans + f[1][0]) % mod;
                    }
                    if (k < 2) {
                        ans = (ans + f[j][k + 1]) % mod;
                    }
                    g[j][k] = ans % mod;
                }
            }
            f = g;
        }
        return f[0][0];
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        f = [[1] * 3 for _ in range(2)]
        for _ in range(n):
            g = [[0] * 3 for _ in range(2)]
            for j in range(2):
                for k in range(3):
                    ans = f[j][0]
                    if j == 0:
                        ans += f[1][0]
                    if k < 2:
                        ans += f[j][k + 1]
                    g[j][k] = ans % mod
            f = g
        return f[0][0]
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
