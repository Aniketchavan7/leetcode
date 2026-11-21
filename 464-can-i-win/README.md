# 464. Can I Win

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/can-i-win)
[![Topic: Bit Manipulation & Memoization & Math](https://img.shields.io/badge/Topic-Bit%20Manipulation%20&%20Memoization%20&%20Math-blue)](https://leetcode.com/problems/can-i-win)

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
**Sample Input**: `maxChoosableInteger = 10, desiredTotal = 11`  
**Expected Output**: `false`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `maxChoosableInteger = 10, desiredTotal = 11` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `false` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private Map<Integer, Boolean> f = new HashMap<>();
    private int maxChoosableInteger;
    private int desiredTotal;

    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        if ((1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal) {
            return false;
        }
        this.maxChoosableInteger = maxChoosableInteger;
        this.desiredTotal = desiredTotal;
        return dfs(0, 0);
    }

    private boolean dfs(int mask, int s) {
        if (f.containsKey(mask)) {
            return f.get(mask);
        }
        for (int i = 0; i < maxChoosableInteger; ++i) {
            if ((mask >> i & 1) == 0) {
                if (s + i + 1 >= desiredTotal || !dfs(mask | 1 << i, s + i + 1)) {
                    f.put(mask, true);
                    return true;
                }
            }
        }
        f.put(mask, false);
        return false;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def dfs(mask: int, s: int) -> bool:
            for i in range(1, maxChoosableInteger + 1):
                if mask >> i & 1 ^ 1:
                    if s + i >= desiredTotal or not dfs(mask | 1 << i, s + i):
                        return True
            return False

        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
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
