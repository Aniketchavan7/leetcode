# 473. Matchsticks to Square

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/matchsticks-to-square)
[![Topic: Bit Manipulation & Array & Dynamic Programming](https://img.shields.io/badge/Topic-Bit%20Manipulation%20&%20Array%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/matchsticks-to-square)

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
**Sample Input**: `matchsticks = [1,1,2,2,2]`  
**Expected Output**: `true`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `matchsticks = [1,1,2,2,2]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `true` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean makesquare(int[] matchsticks) {
        int s = 0, mx = 0;
        for (int v : matchsticks) {
            s += v;
            mx = Math.max(mx, v);
        }
        int x = s / 4, mod = s % 4;
        if (mod != 0 || x < mx) {
            return false;
        }
        Arrays.sort(matchsticks);
        int[] edges = new int[4];
        return dfs(matchsticks.length - 1, x, matchsticks, edges);
    }

    private boolean dfs(int u, int x, int[] matchsticks, int[] edges) {
        if (u < 0) {
            return true;
        }
        for (int i = 0; i < 4; ++i) {
            if (i > 0 && edges[i - 1] == edges[i]) {
                continue;
            }
            edges[i] += matchsticks[u];
            if (edges[i] <= x && dfs(u - 1, x, matchsticks, edges)) {
                return true;
            }
            edges[i] -= matchsticks[u];
        }
        return false;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        def dfs(u):
            if u == len(matchsticks):
                return True
            for i in range(4):
                if i > 0 and edges[i - 1] == edges[i]:
                    continue
                edges[i] += matchsticks[u]
                if edges[i] <= x and dfs(u + 1):
                    return True
                edges[i] -= matchsticks[u]
            return False

        x, mod = divmod(sum(matchsticks), 4)
        if mod or x < max(matchsticks):
            return False
        edges = [0] * 4
        matchsticks.sort(reverse=True)
        return dfs(0)
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
