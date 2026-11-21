# 152. Maximum Product Subarray

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/maximum-product-subarray/)
[![Topic: 1D Dynamic Programming](https://img.shields.io/badge/Topic-1D%20Dynamic%20Programming-blue)](https://leetcode.com/problems/maximum-product-subarray/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Unlike maximum sum, multiplication by a negative number can turn a large positive product into a large negative, or turn a large negative product into a huge positive! At each element, we maintain BOTH the `currentMax` and `currentMin` product ending at that index. If the current number is negative, swapping currentMax and currentMin before computing lets the negative flip the minimum into the new maximum."

---

### 💡 Intuition & Core Insight
- **Dual State Tracking**: Tracking both extremes captures the sign flip property of multiplication in constant space.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [2, 3, -2, 4]`
- x=2: max=2, min=2, res=2
- x=3: max=max(3, 2*3)=6, min=min(3, 2*3)=3, res=6
- x=-2: negative! swap(max, min) -> max=3, min=6. max=max(-2, 3*-2)=-2, min=min(-2, 6*-2)=-12, res=6
- x=4: max=max(4, -2*4)=4, min=min(4, -12*4)=-48, res=6
Max product = 6.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int maxProduct(int[] nums) {
        int maxProd = nums[0];
        int minProd = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < 0) {
                int tmp = maxProd;
                maxProd = minProd;
                minProd = tmp;
            }

            maxProd = Math.max(nums[i], maxProd * nums[i]);
            minProd = Math.min(nums[i], minProd * nums[i]);
            result = Math.max(result, maxProd);
        }
        return result;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        res = nums[0]

        for num in nums[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)
            res = max(res, cur_max)

        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — One single pass over the array.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary variables.

---

### ⚠️ Edge Cases & Interview Traps
1. Array with zero [2, 0, -1]: zero resets current products to 0 or restarts at next element.
2. All negative numbers: even number of negatives correctly pairs into positive product.

---

### 💬 Follow-Up Questions You Might Get
- *What if product exceeds 64-bit integer limits?* In practical problems modulo is applied, or log-transforms.
