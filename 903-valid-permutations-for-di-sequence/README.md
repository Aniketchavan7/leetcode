# 903. Valid Permutations for DI Sequence

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/valid-permutations-for-di-sequence)
[![Topic: String & Dynamic Programming & Prefix Sum](https://img.shields.io/badge/Topic-String%20&%20Dynamic%20Programming%20&%20Prefix%20Sum-blue)](https://leetcode.com/problems/valid-permutations-for-di-sequence)

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
**Sample Input**: `s = &quot;DID&quot;`  
**Expected Output**: `5`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s = &quot;DID&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `5` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int numPermsDISequence(String s) {
        final int mod = (int) 1e9 + 7;
        int n = s.length();
        int[][] f = new int[n + 1][n + 1];
        f[0][0] = 1;
        for (int i = 1; i <= n; ++i) {
            if (s.charAt(i - 1) == 'D') {
                for (int j = 0; j <= i; ++j) {
                    for (int k = j; k < i; ++k) {
                        f[i][j] = (f[i][j] + f[i - 1][k]) % mod;
                    }
                }
            } else {
                for (int j = 0; j <= i; ++j) {
                    for (int k = 0; k < j; ++k) {
                        f[i][j] = (f[i][j] + f[i - 1][k]) % mod;
                    }
                }
            }
        }
        int ans = 0;
        for (int j = 0; j <= n; ++j) {
            ans = (ans + f[n][j]) % mod;
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        f = [[0] * (n + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i, c in enumerate(s, 1):
            if c == "D":
                for j in range(i + 1):
                    for k in range(j, i):
                        f[i][j] = (f[i][j] + f[i - 1][k]) % mod
            else:
                for j in range(i + 1):
                    for k in range(j):
                        f[i][j] = (f[i][j] + f[i - 1][k]) % mod
        return sum(f[n][j] for j in range(n + 1)) % mod
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
