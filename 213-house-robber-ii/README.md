# 213. House Robber II

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/house-robber-ii/)
[![Topic: 1D Dynamic Programming / Circular](https://img.shields.io/badge/Topic-1D%20Dynamic%20Programming%20/%20Circular-blue)](https://leetcode.com/problems/house-robber-ii/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Houses are arranged in a circle: the first house is adjacent to the last house. This means we cannot rob both house 0 and house n - 1 simultaneously. We can break the circular constraint into two simple linear House Robber subproblems: 1) Rob subarray `nums[0..n-2]` (excluding the last house). 2) Rob subarray `nums[1..n-1]` (excluding the first house). The maximum of these two linear runs is our answer."

---

### 💡 Intuition & Core Insight
- **Splitting the Cycle**: Any valid robbing sequence either excludes the first house, excludes the last house, or excludes both. Running the linear algorithm on both slices covers all valid possibilities.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [2, 3, 2]`
- Case 1: `[2, 3]` (excluding last) -> max loot = 3
- Case 2: `[3, 2]` (excluding first) -> max loot = 3
Max(3, 3) = 3.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        return Math.max(robLinear(nums, 0, nums.length - 2),
                        robLinear(nums, 1, nums.length - 1));
    }

    private int robLinear(int[] nums, int start, int end) {
        int rob1 = 0, rob2 = 0;
        for (int i = start; i <= end; i++) {
            int newRob = Math.max(rob2, rob1 + nums[i]);
            rob1 = rob2;
            rob2 = newRob;
        }
        return rob2;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            rob1, rob2 = 0, 0
            for num in arr:
                new_rob = max(rob2, rob1 + num)
                rob1 = rob2
                rob2 = new_rob
            return rob2

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Runs two linear passes of size N - 1.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant extra variables.

---

### ⚠️ Edge Cases & Interview Traps
1. Single house [1]: returns 1.
2. Three houses [1, 2, 3]: returns 3.

---

### 💬 Follow-Up Questions You Might Get
- *What if houses form a binary tree?* House Robber III (Tree DFS returning [robNode, skipNode]).
