# 931. Minimum Falling Path Sum

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/minimum-falling-path-sum)
[![Topic: Array & Dynamic Programming & Matrix](https://img.shields.io/badge/Topic-Array%20&%20Dynamic%20Programming%20&%20Matrix-blue)](https://leetcode.com/problems/minimum-falling-path-sum)

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
**Sample Input**: `matrix = [[2,1,3],[6,5,4],[7,8,9]]`  
**Expected Output**: `13`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `matrix = [[2,1,3],[6,5,4],[7,8,9]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `13` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        var f = new int[n];
        for (var row : matrix) {
            var g = f.clone();
            for (int j = 0; j < n; ++j) {
                if (j > 0) {
                    g[j] = Math.min(g[j], f[j - 1]);
                }
                if (j + 1 < n) {
                    g[j] = Math.min(g[j], f[j + 1]);
                }
                g[j] += row[j];
            }
            f = g;
        }
        // return Arrays.stream(f).min().getAsInt();
        int ans = 1 << 30;
        for (int x : f) {
            ans = Math.min(ans, x);
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        f = [0] * n
        for row in matrix:
            g = [0] * n
            for j, x in enumerate(row):
                l, r = max(0, j - 1), min(n, j + 2)
                g[j] = min(f[l:r]) + x
            f = g
        return min(f)
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
