# 689. Maximum Sum of 3 Non-Overlapping Subarrays

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays)
[![Topic: Array & Dynamic Programming & Prefix Sum](https://img.shields.io/badge/Topic-Array%20&%20Dynamic%20Programming%20&%20Prefix%20Sum-blue)](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays)

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
**Sample Input**: `nums = [1,2,1,2,6,7,5,1], k = 2`  
**Expected Output**: `[0,3,5]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [1,2,1,2,6,7,5,1], k = 2` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[0,3,5]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int[] ans = new int[3];
        int s = 0, s1 = 0, s2 = 0, s3 = 0;
        int mx1 = 0, mx12 = 0;
        int idx1 = 0, idx121 = 0, idx122 = 0;
        for (int i = k * 2; i < nums.length; ++i) {
            s1 += nums[i - k * 2];
            s2 += nums[i - k];
            s3 += nums[i];
            if (i >= k * 3 - 1) {
                if (s1 > mx1) {
                    mx1 = s1;
                    idx1 = i - k * 3 + 1;
                }
                if (mx1 + s2 > mx12) {
                    mx12 = mx1 + s2;
                    idx121 = idx1;
                    idx122 = i - k * 2 + 1;
                }
                if (mx12 + s3 > s) {
                    s = mx12 + s3;
                    ans = new int[] {idx121, idx122, i - k + 1};
                }
                s1 -= nums[i - k * 3 + 1];
                s2 -= nums[i - k * 2 + 1];
                s3 -= nums[i - k + 1];
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        s = s1 = s2 = s3 = 0
        mx1 = mx12 = 0
        idx1, idx12 = 0, ()
        ans = []
        for i in range(k * 2, len(nums)):
            s1 += nums[i - k * 2]
            s2 += nums[i - k]
            s3 += nums[i]
            if i >= k * 3 - 1:
                if s1 > mx1:
                    mx1 = s1
                    idx1 = i - k * 3 + 1
                if mx1 + s2 > mx12:
                    mx12 = mx1 + s2
                    idx12 = (idx1, i - k * 2 + 1)
                if mx12 + s3 > s:
                    s = mx12 + s3
                    ans = [*idx12, i - k + 1]
                s1 -= nums[i - k * 3 + 1]
                s2 -= nums[i - k * 2 + 1]
                s3 -= nums[i - k + 1]
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
