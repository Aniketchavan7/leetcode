# 727. Minimum Window Subsequence

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/minimum-window-subsequence)
[![Topic: String & Dynamic Programming & Sliding Window](https://img.shields.io/badge/Topic-String%20&%20Dynamic%20Programming%20&%20Sliding%20Window-blue)](https://leetcode.com/problems/minimum-window-subsequence)

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
**Sample Input**: `s1 = &quot;abcdebdde&quot;, s2 = &quot;bde&quot;`  
**Expected Output**: `&quot;bcde&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s1 = &quot;abcdebdde&quot;, s2 = &quot;bde&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;bcde&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String minWindow(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int[][] f = new int[m + 1][n + 1];
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    f[i][j] = j == 1 ? i : f[i - 1][j - 1];
                } else {
                    f[i][j] = f[i - 1][j];
                }
            }
        }
        int p = 0, k = m + 1;
        for (int i = 1; i <= m; ++i) {
            if (s1.charAt(i - 1) == s2.charAt(n - 1) && f[i][n] > 0) {
                int j = f[i][n] - 1;
                if (i - j < k) {
                    k = i - j;
                    p = j;
                }
            }
        }
        return k > m ? "" : s1.substring(p, p + k);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i, a in enumerate(s1, 1):
            for j, b in enumerate(s2, 1):
                if a == b:
                    f[i][j] = i if j == 1 else f[i - 1][j - 1]
                else:
                    f[i][j] = f[i - 1][j]
        p, k = 0, m + 1
        for i, a in enumerate(s1, 1):
            if a == s2[n - 1] and f[i][n]:
                j = f[i][n] - 1
                if i - j < k:
                    k = i - j
                    p = j
        return "" if k > m else s1[p : p + k]
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
