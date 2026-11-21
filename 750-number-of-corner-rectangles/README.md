# 750. Number Of Corner Rectangles

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/number-of-corner-rectangles)
[![Topic: Array & Math & Dynamic Programming](https://img.shields.io/badge/Topic-Array%20&%20Math%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/number-of-corner-rectangles)

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
**Sample Input**: `grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]`  
**Expected Output**: `1`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `1` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int countCornerRectangles(int[][] grid) {
        int n = grid[0].length;
        int ans = 0;
        Map<List<Integer>, Integer> cnt = new HashMap<>();
        for (var row : grid) {
            for (int i = 0; i < n; ++i) {
                if (row[i] == 1) {
                    for (int j = i + 1; j < n; ++j) {
                        if (row[j] == 1) {
                            List<Integer> t = List.of(i, j);
                            ans += cnt.getOrDefault(t, 0);
                            cnt.merge(t, 1, Integer::sum);
                        }
                    }
                }
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def countCornerRectangles(self, grid: list[list[int]]) -> int:
        ans = 0
        cnt = Counter()
        n = len(grid[0])
        for row in grid:
            for i, c1 in enumerate(row):
                if c1:
                    for j in range(i + 1, n):
                        if row[j]:
                            ans += cnt[(i, j)]
                            cnt[(i, j)] += 1
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
