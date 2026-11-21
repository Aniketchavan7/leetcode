# 956. Tallest Billboard

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/tallest-billboard)
[![Topic: Array & Dynamic Programming & Knapsack](https://img.shields.io/badge/Topic-Array%20&%20Dynamic%20Programming%20&%20Knapsack-blue)](https://leetcode.com/problems/tallest-billboard)

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
**Sample Input**: `rods = [1,2,3,6]`  
**Expected Output**: `6`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `rods = [1,2,3,6]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `6` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private Integer[][] f;
    private int[] rods;
    private int n;

    public int tallestBillboard(int[] rods) {
        int s = 0;
        for (int x : rods) {
            s += x;
        }
        n = rods.length;
        this.rods = rods;
        f = new Integer[n][s + 1];
        return dfs(0, 0);
    }

    private int dfs(int i, int j) {
        if (i >= n) {
            return j == 0 ? 0 : -(1 << 30);
        }
        if (f[i][j] != null) {
            return f[i][j];
        }
        int ans = Math.max(dfs(i + 1, j), dfs(i + 1, j + rods[i]));
        ans = Math.max(ans, dfs(i + 1, Math.abs(rods[i] - j)) + Math.min(j, rods[i]));
        return f[i][j] = ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= len(rods):
                return 0 if j == 0 else -inf
            ans = max(dfs(i + 1, j), dfs(i + 1, j + rods[i]))
            ans = max(ans, dfs(i + 1, abs(rods[i] - j)) + min(j, rods[i]))
            return ans

        return dfs(0, 0)
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
