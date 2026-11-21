# 712. Minimum ASCII Delete Sum for Two Strings

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings)
[![Topic: String & Dynamic Programming & Longest Common Subsequence](https://img.shields.io/badge/Topic-String%20&%20Dynamic%20Programming%20&%20Longest%20Common%20Subsequence-blue)](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings)

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
**Sample Input**: `s1 = &quot;sea&quot;, s2 = &quot;eat&quot;`  
**Expected Output**: `231`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s1 = &quot;sea&quot;, s2 = &quot;eat&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `231` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int[][] f = new int[m + 1][n + 1];
        for (int i = 1; i <= m; ++i) {
            f[i][0] = f[i - 1][0] + s1.charAt(i - 1);
        }
        for (int j = 1; j <= n; ++j) {
            f[0][j] = f[0][j - 1] + s2.charAt(j - 1);
        }
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    f[i][j] = f[i - 1][j - 1];
                } else {
                    f[i][j]
                        = Math.min(f[i - 1][j] + s1.charAt(i - 1), f[i][j - 1] + s2.charAt(j - 1));
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
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            f[i][0] = f[i - 1][0] + ord(s1[i - 1])
        for j in range(1, n + 1):
            f[0][j] = f[0][j - 1] + ord(s2[j - 1])
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(
                        f[i - 1][j] + ord(s1[i - 1]), f[i][j - 1] + ord(s2[j - 1])
                    )
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
