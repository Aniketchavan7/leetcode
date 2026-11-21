# 879. Profitable Schemes

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/profitable-schemes)
[![Topic: Array & Dynamic Programming & Knapsack](https://img.shields.io/badge/Topic-Array%20&%20Dynamic%20Programming%20&%20Knapsack-blue)](https://leetcode.com/problems/profitable-schemes)

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
**Sample Input**: `n = 5, minProfit = 3, group = [2,2], profit = [2,3]`  
**Expected Output**: `2`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `n = 5, minProfit = 3, group = [2,2], profit = [2,3]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `2` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private Integer[][][] f;
    private int m;
    private int n;
    private int minProfit;
    private int[] group;
    private int[] profit;
    private final int mod = (int) 1e9 + 7;

    public int profitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        m = group.length;
        this.n = n;
        f = new Integer[m][n + 1][minProfit + 1];
        this.minProfit = minProfit;
        this.group = group;
        this.profit = profit;
        return dfs(0, 0, 0);
    }

    private int dfs(int i, int j, int k) {
        if (i >= m) {
            return k == minProfit ? 1 : 0;
        }
        if (f[i][j][k] != null) {
            return f[i][j][k];
        }
        int ans = dfs(i + 1, j, k);
        if (j + group[i] <= n) {
            ans += dfs(i + 1, j + group[i], Math.min(k + profit[i], minProfit));
        }
        ans %= mod;
        return f[i][j][k] = ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: list[int], profit: list[int]
    ) -> int:
        @cache
        def dfs(i: int, j: int, k: int) -> int:
            if i >= len(group):
                return 1 if k == minProfit else 0
            ans = dfs(i + 1, j, k)
            if j + group[i] <= n:
                ans += dfs(i + 1, j + group[i], min(k + profit[i], minProfit))
            return ans % (10**9 + 7)

        return dfs(0, 0, 0)
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
