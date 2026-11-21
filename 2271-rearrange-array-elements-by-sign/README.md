# 2271. Rearrange Array Elements by Sign

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/rearrange-array-elements-by-sign/)
[![Topic: Two Pointers / Arrays](https://img.shields.io/badge/Topic-Two%20Pointers%20/%20Arrays-blue)](https://leetcode.com/problems/rearrange-array-elements-by-sign/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We must rearrange an array with equal positive and negative numbers such that signs alternate, starting with a positive number, while preserving the relative order of positive and negative elements. We allocate a result array of size n, and maintain two write pointers: `posIdx = 0` (even indices) and `negIdx = 1` (odd indices). In a single pass, when we see a positive number, place it at res[posIdx] and advance posIdx += 2; when negative, place at res[negIdx] and advance negIdx += 2."

---

### 💡 Intuition & Core Insight
- **Even/Odd Slot Assignment**: Positive numbers belong at indices 0, 2, 4... and negative numbers at 1, 3, 5..., decoupling the placement into independent monotonic pointer advances.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [3, 1, -2, -5, 2, -4]`
- num=3 (+): res[0]=3, posIdx=2
- num=1 (+): res[2]=1, posIdx=4
- num=-2 (-): res[1]=-2, negIdx=3
- num=-5 (-): res[3]=-5, negIdx=5
- num=2 (+): res[4]=2, posIdx=6
- num=-4 (-): res[5]=-4, negIdx=7
Result: `[3, -2, 1, -5, 2, -4]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int posIdx = 0, negIdx = 1;

        for (int num : nums) {
            if (num > 0) {
                res[posIdx] = num;
                posIdx += 2;
            } else {
                res[negIdx] = num;
                negIdx += 2;
            }
        }
        return res;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        pos_idx, neg_idx = 0, 1
        for num in nums:
            if num > 0:
                res[pos_idx] = num
                pos_idx += 2
            else:
                res[neg_idx] = num
                neg_idx += 2
        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — One single pass filling the result array.
- **Space Complexity**: $\mathcal{O}(N)$ — Output array of size N.

---

### ⚠️ Edge Cases & Interview Traps
1. Length 2 [1, -1]: places 1 at 0, -1 at 1.
2. Preserves stability: relative order of positive and negative numbers is unchanged.

---

### 💬 Follow-Up Questions You Might Get
- *Can this be done in O(1) space?* In-place stable rearrangement without extra space requires complex block rotations in O(N log N).
