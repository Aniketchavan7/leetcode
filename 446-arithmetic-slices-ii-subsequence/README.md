# 446. Arithmetic Slices II - Subsequence

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/arithmetic-slices-ii-subsequence)
[![Topic: Array & Dynamic Programming](https://img.shields.io/badge/Topic-Array%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/arithmetic-slices-ii-subsequence)

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
**Sample Input**: `nums = [2,4,6,8,10]`  
**Expected Output**: `7`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [2,4,6,8,10]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `7` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int n = nums.length;
        Map<Long, Integer>[] f = new Map[n];
        Arrays.setAll(f, k -> new HashMap<>());
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                Long d = 1L * nums[i] - nums[j];
                int cnt = f[j].getOrDefault(d, 0);
                ans += cnt;
                f[i].merge(d, cnt + 1, Integer::sum);
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        f = [defaultdict(int) for _ in nums]
        ans = 0
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[:i]):
                d = x - y
                ans += f[j][d]
                f[i][d] += f[j][d] + 1
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
