# 920. Number of Music Playlists

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/number-of-music-playlists)
[![Topic: Math & Dynamic Programming & Combinatorics](https://img.shields.io/badge/Topic-Math%20&%20Dynamic%20Programming%20&%20Combinatorics-blue)](https://leetcode.com/problems/number-of-music-playlists)

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
**Sample Input**: `n = 3, goal = 3, k = 1`  
**Expected Output**: `6`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `n = 3, goal = 3, k = 1` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `6` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int numMusicPlaylists(int n, int goal, int k) {
        final int mod = (int) 1e9 + 7;
        long[][] f = new long[goal + 1][n + 1];
        f[0][0] = 1;
        for (int i = 1; i <= goal; ++i) {
            for (int j = 1; j <= n; ++j) {
                f[i][j] = f[i - 1][j - 1] * (n - j + 1);
                if (j > k) {
                    f[i][j] += f[i - 1][j] * (j - k);
                }
                f[i][j] %= mod;
            }
        }
        return (int) f[goal][n];
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7
        f = [[0] * (n + 1) for _ in range(goal + 1)]
        f[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                f[i][j] = f[i - 1][j - 1] * (n - j + 1)
                if j > k:
                    f[i][j] += f[i - 1][j] * (j - k)
                f[i][j] %= mod
        return f[goal][n]
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
