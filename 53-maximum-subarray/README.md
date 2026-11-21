# 53. Maximum Subarray

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/maximum-subarray/)
[![Topic: Dynamic Programming / Kadane's Algorithm](https://img.shields.io/badge/Topic-Dynamic%20Programming%20/%20Kadane's%20Algorithm-blue)](https://leetcode.com/problems/maximum-subarray/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To find the contiguous subarray with the largest sum: Kadane's Algorithm maintains a running `currentSum`. At each element x, we decide whether to add x to currentSum, or discard currentSum and start a fresh subarray at x (`currentSum = Math.max(x, currentSum + x)`). We update `maxSum` at every step."

---

### 💡 Intuition & Core Insight
- **Negative Prefixes are Dead Weight**: If your current subarray sum drops below 0, dragging it forward will only hurt any future elements. You are always better off resetting and starting fresh.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
- x=-2: curr=-2, max=-2
- x=1: curr=max(1, -2+1)=1, max=1
- x=-3: curr=max(-3, 1-3)=-2, max=1
- x=4: curr=max(4, -2+4)=4, max=4 (reset!)
- x=-1: curr=3, max=4
- x=2: curr=5, max=5
- x=1: curr=6, max=**6**
Result: 6 (from subarray `[4, -1, 2, 1]`).

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int maxSubArray(int[] nums) {
        int currentSum = nums[0];
        int maxSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }
        return maxSum;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — One single linear scan over the array.
- **Space Complexity**: $\mathcal{O}(1)$ — Two rolling integer variables.

---

### ⚠️ Edge Cases & Interview Traps
1. All negative numbers [-5, -2, -8]: correctly selects the least negative single number (-2).
2. Single element: returns that element.

---

### 💬 Follow-Up Questions You Might Get
- *Can we solve this using Divide and Conquer?* Yes, split into left, right, and crossing subarrays in O(N log N) time.
