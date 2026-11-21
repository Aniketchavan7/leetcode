# 935. Knight Dialer

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/knight-dialer)
[![Topic: Dynamic Programming](https://img.shields.io/badge/Topic-Dynamic%20Programming-blue)](https://leetcode.com/problems/knight-dialer)

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
**Sample Input**: `n = 1`  
**Expected Output**: `10`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `n = 1` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `10` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int knightDialer(int n) {
        final int mod = (int) 1e9 + 7;
        long[] f = new long[10];
        Arrays.fill(f, 1);
        while (--n > 0) {
            long[] g = new long[10];
            g[0] = (f[4] + f[6]) % mod;
            g[1] = (f[6] + f[8]) % mod;
            g[2] = (f[7] + f[9]) % mod;
            g[3] = (f[4] + f[8]) % mod;
            g[4] = (f[0] + f[3] + f[9]) % mod;
            g[6] = (f[0] + f[1] + f[7]) % mod;
            g[7] = (f[2] + f[6]) % mod;
            g[8] = (f[1] + f[3]) % mod;
            g[9] = (f[2] + f[4]) % mod;
            f = g;
        }
        return (int) (Arrays.stream(f).sum() % mod);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def knightDialer(self, n: int) -> int:
        f = [1] * 10
        for _ in range(n - 1):
            g = [0] * 10
            g[0] = f[4] + f[6]
            g[1] = f[6] + f[8]
            g[2] = f[7] + f[9]
            g[3] = f[4] + f[8]
            g[4] = f[0] + f[3] + f[9]
            g[6] = f[0] + f[1] + f[7]
            g[7] = f[2] + f[6]
            g[8] = f[1] + f[3]
            g[9] = f[2] + f[4]
            f = g
        return sum(f) % (10**9 + 7)
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
