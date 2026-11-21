# 238. Product of Array Except Self

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/product-of-array-except-self/)
[![Topic: Prefix & Suffix Products](https://img.shields.io/badge/Topic-Prefix%20%26%20Suffix%20Products-blue)](https://leetcode.com/problems/product-of-array-except-self/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We must compute the product of all elements except nums[i] in O(N) time without using the division operator. The product of all numbers except index i is simply (prefix product of elements before i) * (suffix product of elements after i). In the first pass, we populate output[i] with the prefix product up to i. In the second pass, we iterate backwards maintaining a running suffix product and multiply it into output[i]."

---

### 💡 Intuition & Core Insight
- **Why Division is Forbidden**: Division by zero occurs if any element is 0. Furthermore, division fails on finite field arithmetic.
- **Prefix * Suffix Decomposition**: Any element's exclusion splits the array into two independent subarrays: left and right.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [1, 2, 3, 4]`
1. Prefix pass: `output = [1, 1, 2, 6]` (output[i] holds product of nums[0..i-1])
2. Suffix pass with running `suffix = 1`:
   - i=3: output[3] = 6 * 1 = 6, suffix = 1 * 4 = 4
   - i=2: output[2] = 2 * 4 = 8, suffix = 4 * 3 = 12
   - i=1: output[1] = 1 * 12 = 12, suffix = 12 * 2 = 24
   - i=0: output[0] = 1 * 24 = 24
Result: `[24, 12, 8, 6]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        // Pass 1: Prefix products
        res[0] = 1;
        for (int i = 1; i < n; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }
        // Pass 2: Multiply running suffix products
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= suffix;
            suffix *= nums[i];
        }
        return res;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Two linear passes through the array.
- **Space Complexity**: $\mathcal{O}(1)$ — O(1) extra space excluding the returned output array.

---

### ⚠️ Edge Cases & Interview Traps
1. Single zero in array: only the zero index has a non-zero product.
2. Multiple zeros: all output elements become zero.

---

### 💬 Follow-Up Questions You Might Get
- *Can this handle large products without overflow?* Standard 32-bit integers fit LeetCode constraints; in production use BigInteger or log transforms.
