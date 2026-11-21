# 730. Count Different Palindromic Subsequences

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/count-different-palindromic-subsequences)
[![Topic: String & Dynamic Programming](https://img.shields.io/badge/Topic-String%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/count-different-palindromic-subsequences)

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
**Sample Input**: `s = &quot;bccb&quot;`  
**Expected Output**: `6`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s = &quot;bccb&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `6` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private final int MOD = (int) 1e9 + 7;

    public int countPalindromicSubsequences(String s) {
        int n = s.length();
        long[][][] dp = new long[n][n][4];
        for (int i = 0; i < n; ++i) {
            dp[i][i][s.charAt(i) - 'a'] = 1;
        }
        for (int l = 2; l <= n; ++l) {
            for (int i = 0; i + l <= n; ++i) {
                int j = i + l - 1;
                for (char c = 'a'; c <= 'd'; ++c) {
                    int k = c - 'a';
                    if (s.charAt(i) == c && s.charAt(j) == c) {
                        dp[i][j][k] = 2 + dp[i + 1][j - 1][0] + dp[i + 1][j - 1][1]
                            + dp[i + 1][j - 1][2] + dp[i + 1][j - 1][3];
                        dp[i][j][k] %= MOD;
                    } else if (s.charAt(i) == c) {
                        dp[i][j][k] = dp[i][j - 1][k];
                    } else if (s.charAt(j) == c) {
                        dp[i][j][k] = dp[i + 1][j][k];
                    } else {
                        dp[i][j][k] = dp[i + 1][j - 1][k];
                    }
                }
            }
        }
        long ans = 0;
        for (int k = 0; k < 4; ++k) {
            ans += dp[0][n - 1][k];
        }
        return (int) (ans % MOD);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        dp = [[[0] * 4 for _ in range(n)] for _ in range(n)]
        for i, c in enumerate(s):
            dp[i][i][ord(c) - ord('a')] = 1
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for c in 'abcd':
                    k = ord(c) - ord('a')
                    if s[i] == s[j] == c:
                        dp[i][j][k] = 2 + sum(dp[i + 1][j - 1])
                    elif s[i] == c:
                        dp[i][j][k] = dp[i][j - 1][k]
                    elif s[j] == c:
                        dp[i][j][k] = dp[i + 1][j][k]
                    else:
                        dp[i][j][k] = dp[i + 1][j - 1][k]
        return sum(dp[0][-1]) % mod
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
