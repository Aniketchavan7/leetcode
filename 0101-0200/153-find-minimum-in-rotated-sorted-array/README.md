# 153. Find Minimum in Rotated Sorted Array

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
[![Topic: Binary Search](https://img.shields.io/badge/Topic-Binary%20Search-blue)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "In an original sorted array, the rightmost element is always greater than or equal to the minimum. When rotated, if `nums[mid] > nums[right]`, the rotation point (and the minimum element) must lie strictly to the right of `mid` (left = mid + 1). If `nums[mid] <= nums[right]`, the minimum lies at `mid` or to its left (right = mid). When left == right, we have found the minimum."

---

### 💡 Intuition & Core Insight
- **Comparing Against Right Boundary**: Comparing `mid` against `right` cleanly detects whether the inflection cliff is in the left half or the right half.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [3, 4, 5, 1, 2]`
- L=0 (3), R=4 (2), mid=2 (5)
- nums[2]=5 > nums[4]=2 -> Cliff is on the right -> L = mid + 1 = 3
- L=3 (1), R=4 (2), mid=3 (1)
- nums[3]=1 <= nums[4]=2 -> Minimum is at mid or left -> R = mid = 3
- L == R == 3 -> nums[3] = 1.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return nums[left];
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log N)$ — Binary search divides the array size by two in each iteration.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary pointers.

---

### ⚠️ Edge Cases & Interview Traps
1. Unrotated array: nums[mid] <= nums[right] holds throughout, returns nums[0].
2. Two elements: cleanly resolves in one iteration.

---

### 💬 Follow-Up Questions You Might Get
- *What if duplicates are present?* When nums[mid] == nums[right], decrement right-- (LeetCode 154).
