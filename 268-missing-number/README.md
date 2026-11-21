# 268. Missing Number

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/missing-number/)
[![Topic: Bit Manipulation / Math](https://img.shields.io/badge/Topic-Bit%20Manipulation%20/%20Math-blue)](https://leetcode.com/problems/missing-number/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Given an array containing n distinct numbers in the range [0, n], one number is missing. Using Gauss's formula, the expected sum is `n * (n + 1) / 2`. Subtracting the sum of all elements in the array gives the missing number in O(N) time and O(1) space. Alternatively, XORing all array elements with all indices 0..n cancels present numbers and leaves the missing one without overflow risk."

---

### 💡 Intuition & Core Insight
- **Expected vs Actual**: The delta between expected total and actual total reveals the exact omitted element.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [3, 0, 1]` (n=3)
- Expected sum: 3 * (3 + 1) / 2 = 6
- Actual sum: 3 + 0 + 1 = 4
- Missing: 6 - 4 = 2.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int expectedSum = n * (n + 1) / 2;
        int actualSum = 0;
        for (int num : nums) actualSum += num;
        return expectedSum - actualSum;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Single linear pass to sum array elements.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary variables.

---

### ⚠️ Edge Cases & Interview Traps
1. Missing number is 0: sum delta correctly yields 0.
2. Missing number is n: sum delta yields n.

---

### 💬 Follow-Up Questions You Might Get
- *What if n is large and n*(n+1)/2 could overflow?* Use the XOR method: `res ^= i ^ nums[i]`.
