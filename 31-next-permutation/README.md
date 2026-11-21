# 31. Next Permutation

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/next-permutation/)
[![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-blue)](https://leetcode.com/problems/next-permutation/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To find the next lexicographically greater permutation in-place: 1) Scan from right to left to find the first decreasing element `i` (pivot). 2) If found, find the smallest element to its right that is greater than `nums[i]` and swap them. 3) Reverse the suffix starting at `i + 1` to minimize its lexicographical order."

---

### 💡 Intuition & Core Insight
- **Why Right-to-Left?**: Any suffix in descending order is already at its maximum possible permutation.
- **Reversing Suffix**: After swapping the pivot with the next-greater element, the suffix remains in descending order. Reversing it turns it into ascending order (the smallest possible sequence).

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [1, 2, 3]`
1. Pivot i = 1 (val 2), since 2 < 3.
2. Smallest greater in suffix is 3 (index 2). Swap: `[1, 3, 2]`.
3. Reverse suffix after i (just `[2]`): `[1, 3, 2]`.

**Descending Input**: `nums = [3, 2, 1]`
No pivot found (i = -1). Reverse whole array -> `[1, 2, 3]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int i = n - 2;
        // Step 1: Find first decreasing element from right
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        // Step 2: Find element just larger than nums[i] and swap
        if (i >= 0) {
            int j = n - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }
        // Step 3: Reverse the descending suffix
        reverse(nums, i + 1, n - 1);
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start++, end--);
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — At most two linear scans and one linear array reversal.
- **Space Complexity**: $\mathcal{O}(1)$ — In-place modifications with constant pointers.

---

### ⚠️ Edge Cases & Interview Traps
1. Strictly decreasing array (e.g. [5,4,3,2,1]): reverses to [1,2,3,4,5].
2. All elements identical: remains identical.

---

### 💬 Follow-Up Questions You Might Get
- *Can this generate all permutations?* Yes, repeated calls generate all N! permutations in lexicographical order.
