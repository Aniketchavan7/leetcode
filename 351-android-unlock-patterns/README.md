# 351. Android Unlock Patterns

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/android-unlock-patterns)
[![Topic: Bit Manipulation & Dynamic Programming & Backtracking](https://img.shields.io/badge/Topic-Bit%20Manipulation%20&%20Dynamic%20Programming%20&%20Backtracking-blue)](https://leetcode.com/problems/android-unlock-patterns)

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
**Sample Input**: `m = 1, n = 1`  
**Expected Output**: `9`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `m = 1, n = 1` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `9` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int m;
    private int n;
    private int[][] cross = new int[10][10];
    private boolean[] vis = new boolean[10];

    public int numberOfPatterns(int m, int n) {
        this.m = m;
        this.n = n;
        cross[1][3] = cross[3][1] = 2;
        cross[1][7] = cross[7][1] = 4;
        cross[1][9] = cross[9][1] = 5;
        cross[2][8] = cross[8][2] = 5;
        cross[3][7] = cross[7][3] = 5;
        cross[3][9] = cross[9][3] = 6;
        cross[4][6] = cross[6][4] = 5;
        cross[7][9] = cross[9][7] = 8;
        return dfs(1, 1) * 4 + dfs(2, 1) * 4 + dfs(5, 1);
    }

    private int dfs(int i, int cnt) {
        if (cnt > n) {
            return 0;
        }
        vis[i] = true;
        int ans = cnt >= m ? 1 : 0;
        for (int j = 1; j < 10; ++j) {
            int x = cross[i][j];
            if (!vis[j] && (x == 0 || vis[x])) {
                ans += dfs(j, cnt + 1);
            }
        }
        vis[i] = false;
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def dfs(i: int, cnt: int = 1) -> int:
            if cnt > n:
                return 0
            vis[i] = True
            ans = int(cnt >= m)
            for j in range(1, 10):
                x = cross[i][j]
                if not vis[j] and (x == 0 or vis[x]):
                    ans += dfs(j, cnt + 1)
            vis[i] = False
            return ans

        cross = [[0] * 10 for _ in range(10)]
        cross[1][3] = cross[3][1] = 2
        cross[1][7] = cross[7][1] = 4
        cross[1][9] = cross[9][1] = 5
        cross[2][8] = cross[8][2] = 5
        cross[3][7] = cross[7][3] = 5
        cross[3][9] = cross[9][3] = 6
        cross[4][6] = cross[6][4] = 5
        cross[7][9] = cross[9][7] = 8
        vis = [False] * 10
        return dfs(1) * 4 + dfs(2) * 4 + dfs(5)
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
