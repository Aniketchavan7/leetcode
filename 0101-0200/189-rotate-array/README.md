# 189. Rotate Array

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/rotate-array/)
[![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-blue)](https://leetcode.com/problems/rotate-array/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To rotate an array of length N to the right by k steps in-place with O(1) extra memory: First normalize k = k % n. Then apply the three-reversal trick: 1) Reverse the entire array. 2) Reverse the first k elements. 3) Reverse the remaining n - k elements."

---

### 💡 Intuition & Core Insight
- **Why Reversals Work**:
  - Initial: `[1, 2, 3, 4, | 5, 6, 7]` with k=3
  - Reverse all: `[7, 6, 5, | 4, 3, 2, 1]` (puts the last k elements at the front, but backwards)
  - Reverse first k: `[5, 6, 7, | 4, 3, 2, 1]` (restores order of rotated elements)
  - Reverse rest: `[5, 6, 7, | 1, 2, 3, 4]` (restores order of remaining elements)

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [1, 2, 3, 4, 5, 6, 7]`, `k = 3`
1. Reverse all: `[7, 6, 5, 4, 3, 2, 1]`
2. Reverse `[0..2]`: `[5, 6, 7, 4, 3, 2, 1]`
3. Reverse `[3..6]`: `[5, 6, 7, 1, 2, 3, 4]`
Done!

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;
        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int tmp = nums[start];
            nums[start++] = nums[end];
            nums[end--] = tmp;
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Three array segment reversals sum to 2N swaps, which is O(N).
- **Space Complexity**: $\mathcal{O}(1)$ — In-place swaps with constant pointers.

---

### ⚠️ Edge Cases & Interview Traps
1. k >= n: k %= n prevents out-of-bounds.
2. k == 0: array remains unchanged.

---

### 💬 Follow-Up Questions You Might Get
- *Can we do cyclic replacements?* Yes, moving elements into their target spots using gcd(n, k) cycles.
