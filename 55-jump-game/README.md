# 55. Jump Game

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/jump-game/)
[![Topic: Greedy](https://img.shields.io/badge/Topic-Greedy-blue)](https://leetcode.com/problems/jump-game/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We maintain the furthest reachable index `maxReach`. As we iterate through index i, if i > maxReach, we have stalled and cannot move forward (return false). Otherwise, update `maxReach = Math.max(maxReach, i + nums[i])`. If maxReach >= n - 1, we can reach the end (return true)."

---

### 💡 Intuition & Core Insight
- **Reach Horizon**: As long as index i is within your current reachable horizon, you can jump from it to expand your horizon.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [2, 3, 1, 1, 4]`
- i=0: maxReach = max(0, 0+2) = 2
- i=1: 1 <= 2 -> maxReach = max(2, 1+3) = 4 >= last index (4) -> True!

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) return false;
            maxReach = Math.max(maxReach, i + nums[i]);
            if (maxReach >= nums.length - 1) return true;
        }
        return true;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) - 1:
                return True
        return True
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Single linear scan with early exit.
- **Space Complexity**: $\mathcal{O}(1)$ — One integer variable.

---

### ⚠️ Edge Cases & Interview Traps
1. Single element [0]: returns true (already at last index).
2. Trap zero [3, 2, 1, 0, 4]: maxReach peaks at index 3 and cannot cross zero -> returns false.

---

### 💬 Follow-Up Questions You Might Get
- *How to find the MINIMUM number of jumps to reach the end?* Jump Game II (BFS / greedy level intervals).
