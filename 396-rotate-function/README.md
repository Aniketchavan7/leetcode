# 396. Rotate Function

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/rotate-function)
[![Topic: Array & Math & Dynamic Programming](https://img.shields.io/badge/Topic-Array%20&%20Math%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/rotate-function)

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
**Sample Input**: `nums = [4,3,2,6]`  
**Expected Output**: `26`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [4,3,2,6]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `26` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int maxRotateFunction(int[] nums) {
        long f = 0;
        long s = 0;
        int n = nums.length;
        for (int i = 0; i < n; ++i) {
            f += 1L * i * nums[i];
            s += nums[i];
        }
        long ans = f;
        for (int i = 1; i < n; ++i) {
            f = f + s - 1L * n * nums[n - i];
            ans = Math.max(ans, f);
        }
        return (int) ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        f = sum(i * v for i, v in enumerate(nums))
        n, s = len(nums), sum(nums)
        ans = f
        for i in range(1, n):
            f = f + s - n * nums[n - i]
            ans = max(ans, f)
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
