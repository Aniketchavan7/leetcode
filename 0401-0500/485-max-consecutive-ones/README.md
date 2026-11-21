# 485. Max Consecutive Ones

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/max-consecutive-ones/)
[![Topic: Arrays](https://img.shields.io/badge/Topic-Arrays-blue)](https://leetcode.com/problems/max-consecutive-ones/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Given a binary array, we find the maximum number of consecutive 1s by maintaining a running count. For each element, if it is 1, increment count and update maxCount; if it is 0, reset count to 0."

---

### 💡 Intuition & Core Insight
- **Reset on Zero**: A 0 acts as a wall that resets the streak back to 0.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [1, 1, 0, 1, 1, 1]`
- 1 -> count=1, max=1
- 1 -> count=2, max=2
- 0 -> count=0, max=2
- 1 -> count=1, max=2
- 1 -> count=2, max=2
- 1 -> count=3, max=3
Result: 3.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0;
        int currentCount = 0;
        for (int num : nums) {
            if (num == 1) {
                currentCount++;
                maxCount = Math.max(maxCount, currentCount);
            } else {
                currentCount = 0;
            }
        }
        return maxCount;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        return max_count
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Single linear pass over the binary array.
- **Space Complexity**: $\mathcal{O}(1)$ — Two integer counters.

---

### ⚠️ Edge Cases & Interview Traps
1. Array with only 0s: returns 0.
2. Array with only 1s: returns nums.length.

---

### 💬 Follow-Up Questions You Might Get
- *What if we can flip at most one 0?* Sliding window keeping at most one zero (LeetCode 487).
