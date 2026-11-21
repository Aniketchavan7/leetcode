# 628. Maximum Product of Three Numbers

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/maximum-product-of-three-numbers/)
[![Topic: Math / Sorting](https://img.shields.io/badge/Topic-Math%20/%20Sorting-blue)](https://leetcode.com/problems/maximum-product-of-three-numbers/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "The maximum product of three numbers in an array can only come from one of two possibilities: 1) The product of the three largest numbers (all positive or largest negatives). 2) The product of the two most negative numbers (which multiply to a large positive) and the single largest positive number. In a single scan, we track max1, max2, max3 and min1, min2, and return max(max1*max2*max3, min1*min2*max1)."

---

### 💡 Intuition & Core Insight
- **Two Negatives Make a Positive**: Two large negative numbers (e.g. -100 * -100 = 10,000) multiplied by a positive number can drastically exceed the product of three moderate positive numbers.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [-10, -10, 1, 3, 2]`
- Sorted: `[-10, -10, 1, 2, 3]`
- Option 1 (3 largest): 1 * 2 * 3 = 6
- Option 2 (2 smallest * 1 largest): (-10) * (-10) * 3 = 300
Max product: max(6, 300) = 300.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int maximumProduct(int[] nums) {
        int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;
        int max1 = Integer.MIN_VALUE, max2 = Integer.MIN_VALUE, max3 = Integer.MIN_VALUE;

        for (int n : nums) {
            if (n <= min1) {
                min2 = min1;
                min1 = n;
            } else if (n <= min2) {
                min2 = n;
            }

            if (n >= max1) {
                max3 = max2;
                max2 = max1;
                max1 = n;
            } else if (n >= max2) {
                max3 = max2;
                max2 = n;
            } else if (n >= max3) {
                max3 = n;
            }
        }
        return Math.max(max1 * max2 * max3, min1 * min2 * max1);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        min1 = min2 = float('inf')
        max1 = max2 = max3 = float('-inf')

        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:
                min2 = n

            if n >= max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:
                max3 = max2
                max2 = n
            elif n >= max3:
                max3 = n

        return max(max1 * max2 * max3, min1 * min2 * max1)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — One single pass tracking 5 variables.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary variables without sorting.

---

### ⚠️ Edge Cases & Interview Traps
1. All negative numbers [-5, -4, -3, -2, -1]: product of three least negative numbers is correctly selected.
2. Exactly three numbers: immediately computes product.

---

### 💬 Follow-Up Questions You Might Get
- *What if we need the maximum product of K numbers?* Dynamic programming tracking both max and min products.
