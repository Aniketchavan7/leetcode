# 198. House Robber

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/house-robber/)
[![Topic: 1D Dynamic Programming](https://img.shields.io/badge/Topic-1D%20Dynamic%20Programming-blue)](https://leetcode.com/problems/house-robber/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Adjacent houses trigger alarms. For house i, we have two choices: 1) Rob house i, which earns `nums[i] + maxLoot(i - 2)`. 2) Skip house i, which earns `maxLoot(i - 1)`. Thus, `dp[i] = Math.max(dp[i - 1], nums[i] + dp[i - 2])`. We only need to remember the last two states, achieving O(1) space."

---

### 💡 Intuition & Core Insight
- **Binary Recurrence**: You either take the current loot and inherit the best from two houses ago, or skip current and inherit the best from the immediate neighbor.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [2, 7, 9, 3, 1]`
- House 2: rob1=0, rob2=2
- House 7: newRob = max(2, 7+0) = 7 -> rob1=2, rob2=7
- House 9: newRob = max(7, 9+2) = 11 -> rob1=7, rob2=11
- House 3: newRob = max(11, 3+7) = 11 -> rob1=11, rob2=11
- House 1: newRob = max(11, 1+11) = 12 -> rob1=11, rob2=12
Max loot: 12.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int rob(int[] nums) {
        int rob1 = 0, rob2 = 0;
        for (int num : nums) {
            int newRob = Math.max(rob2, rob1 + num);
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
        rob1, rob2 = 0, 0
        for num in nums:
            new_rob = max(rob2, rob1 + num)
            rob1 = rob2
            rob2 = new_rob
        return rob2
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Single linear pass.
- **Space Complexity**: $\mathcal{O}(1)$ — Two rolling integer variables.

---

### ⚠️ Edge Cases & Interview Traps
1. Single house [5]: returns 5.
2. Two houses [1, 2]: returns max(1, 2) = 2.

---

### 💬 Follow-Up Questions You Might Get
- *What if houses are arranged in a circle?* House Robber II (LeetCode 213).
