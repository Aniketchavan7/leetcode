# 964. Least Operators to Express Number

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/least-operators-to-express-number)
[![Topic: Memoization & Math & Dynamic Programming](https://img.shields.io/badge/Topic-Memoization%20&%20Math%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/least-operators-to-express-number)

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
**Sample Input**: `x = 3, target = 19`  
**Expected Output**: `5`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `x = 3, target = 19` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `5` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int x;
    private Map<Integer, Integer> f = new HashMap<>();

    public int leastOpsExpressTarget(int x, int target) {
        this.x = x;
        return dfs(target);
    }

    private int dfs(int v) {
        if (x >= v) {
            return Math.min(v * 2 - 1, 2 * (x - v));
        }
        if (f.containsKey(v)) {
            return f.get(v);
        }
        int k = 2;
        long y = (long) x * x;
        while (y < v) {
            y *= x;
            ++k;
        }
        int ans = k - 1 + dfs(v - (int) (y / x));
        if (y - v < v) {
            ans = Math.min(ans, k + dfs((int) y - v));
        }
        f.put(v, ans);
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @cache
        def dfs(v: int) -> int:
            if x >= v:
                return min(v * 2 - 1, 2 * (x - v))
            k = 2
            while x**k < v:
                k += 1
            if x**k - v < v:
                return min(k + dfs(x**k - v), k - 1 + dfs(v - x ** (k - 1)))
            return k - 1 + dfs(v - x ** (k - 1))

        return dfs(target)
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
