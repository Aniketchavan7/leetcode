# 2042. Maximum Product Difference Between Two Pairs

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/)
[![Topic: Greedy / Sorting](https://img.shields.io/badge/Topic-Greedy%20/%20Sorting-blue)](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To maximize `(a * b) - (c * d)`: pick `a` and `b` as the two largest numbers in the array, and `c` and `d` as the two smallest numbers. In a single pass, track max1, max2, min1, min2, and return `(max1 * max2) - (min1 * min2)`."

---

### 💡 Intuition & Core Insight
- **Greedy Extremes**: The product difference is maximized by maximizing the minuend and minimizing the subtrahend.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [5, 6, 2, 7, 4]`
- Largest two: 7, 6 -> product = 42
- Smallest two: 2, 4 -> product = 8
Difference = 42 - 8 = 34.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int maxProductDifference(int[] nums) {
        int max1 = 0, max2 = 0;
        int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;

        for (int num : nums) {
            if (num > max1) {
                max2 = max1;
                max1 = num;
            } else if (num > max2) {
                max2 = num;
            }

            if (num < min1) {
                min2 = min1;
                min1 = num;
            } else if (num < min2) {
                min2 = num;
            }
        }
        return (max1 * max2) - (min1 * min2);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        max1 = max2 = 0
        min1 = min2 = float('inf')

        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return (max1 * max2) - (min1 * min2)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — One single pass over the array.
- **Space Complexity**: $\mathcal{O}(1)$ — Four tracking variables.

---

### ⚠️ Edge Cases & Interview Traps
1. Duplicate numbers: duplicates properly fill max1/max2 or min1/min2.
2. Length 4: computes product difference of all 4 elements.

---

### 💬 Follow-Up Questions You Might Get
- *What if negative numbers are allowed?* Consider negative * negative products.
