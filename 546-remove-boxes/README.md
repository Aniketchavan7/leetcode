# 546. Remove Boxes

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/remove-boxes)
[![Topic: Memoization & Array & Dynamic Programming](https://img.shields.io/badge/Topic-Memoization%20&%20Array%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/remove-boxes)

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
**Sample Input**: `boxes = [1,3,2,2,2,3,4,3,1]`  
**Expected Output**: `23`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `boxes = [1,3,2,2,2,3,4,3,1]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `23` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int[][][] f;
    private int[] b;

    public int removeBoxes(int[] boxes) {
        b = boxes;
        int n = b.length;
        f = new int[n][n][n];
        return dfs(0, n - 1, 0);
    }

    private int dfs(int i, int j, int k) {
        if (i > j) {
            return 0;
        }
        while (i < j && b[j] == b[j - 1]) {
            --j;
            ++k;
        }
        if (f[i][j][k] > 0) {
            return f[i][j][k];
        }
        int ans = dfs(i, j - 1, 0) + (k + 1) * (k + 1);
        for (int h = i; h < j; ++h) {
            if (b[h] == b[j]) {
                ans = Math.max(ans, dfs(h + 1, j - 1, 0) + dfs(i, h, k + 1));
            }
        }
        f[i][j][k] = ans;
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        @cache
        def dfs(i, j, k):
            if i > j:
                return 0
            while i < j and boxes[j] == boxes[j - 1]:
                j, k = j - 1, k + 1
            ans = dfs(i, j - 1, 0) + (k + 1) * (k + 1)
            for h in range(i, j):
                if boxes[h] == boxes[j]:
                    ans = max(ans, dfs(h + 1, j - 1, 0) + dfs(i, h, k + 1))
            return ans

        n = len(boxes)
        ans = dfs(0, n - 1, 0)
        dfs.cache_clear()
        return ans
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
