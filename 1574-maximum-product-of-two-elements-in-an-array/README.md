# 1574. Maximum Product of Two Elements in an Array

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)
[![Topic: Greedy / Sorting](https://img.shields.io/badge/Topic-Greedy%20/%20Sorting-blue)](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Given an array of positive integers, we choose two indices i and j to maximize `(nums[i]-1)*(nums[j]-1)`. Since all numbers are positive, maximizing the product simply requires finding the two largest numbers `max1` and `max2` in the array. In a single pass, track the top two largest elements and return `(max1 - 1) * (max2 - 1)`."

---

### 💡 Intuition & Core Insight
- **Top-Two Extraction**: No need to sort in O(N log N); tracking two variables finds the two greatest elements in O(N) time and O(1) space.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [3, 4, 5, 2]`
- Largest: 5, Second largest: 4
- (5 - 1) * (4 - 1) = 4 * 3 = 12.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int maxProduct(int[] nums) {
        int max1 = 0, max2 = 0;
        for (int num : nums) {
            if (num > max1) {
                max2 = max1;
                max1 = num;
            } else if (num > max2) {
                max2 = num;
            }
        }
        return (max1 - 1) * (max2 - 1);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max1, max2 = 0, 0
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        return (max1 - 1) * (max2 - 1)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Single linear scan over array.
- **Space Complexity**: $\mathcal{O}(1)$ — Two integer tracking variables.

---

### ⚠️ Edge Cases & Interview Traps
1. Duplicate maximums [5, 5]: max1=5, max2=5, correctly computes 4 * 4 = 16.
2. Array of length 2: computes product of both.

---

### 💬 Follow-Up Questions You Might Get
- *What if negative numbers were allowed?* Also track two smallest minimums.
