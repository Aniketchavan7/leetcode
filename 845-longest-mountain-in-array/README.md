# 845. Longest Mountain in Array

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/longest-mountain-in-array)
[![Topic: Array & Two Pointers & Dynamic Programming](https://img.shields.io/badge/Topic-Array%20&%20Two%20Pointers%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/longest-mountain-in-array)

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
**Sample Input**: `arr = [2,1,4,7,3,2,5]`  
**Expected Output**: `5`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `arr = [2,1,4,7,3,2,5]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `5` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int longestMountain(int[] arr) {
        int n = arr.length;
        int[] f = new int[n];
        int[] g = new int[n];
        Arrays.fill(f, 1);
        Arrays.fill(g, 1);
        for (int i = 1; i < n; ++i) {
            if (arr[i] > arr[i - 1]) {
                f[i] = f[i - 1] + 1;
            }
        }
        int ans = 0;
        for (int i = n - 2; i >= 0; --i) {
            if (arr[i] > arr[i + 1]) {
                g[i] = g[i + 1] + 1;
                if (f[i] > 1) {
                    ans = Math.max(ans, f[i] + g[i] - 1);
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
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        f = [1] * n
        g = [1] * n
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                f[i] = f[i - 1] + 1
        ans = 0
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                g[i] = g[i + 1] + 1
                if f[i] > 1:
                    ans = max(ans, f[i] + g[i] - 1)
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
