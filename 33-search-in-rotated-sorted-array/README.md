# 33. Search in Rotated Sorted Array

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/search-in-rotated-sorted-array/)
[![Topic: Binary Search](https://img.shields.io/badge/Topic-Binary%20Search-blue)](https://leetcode.com/problems/search-in-rotated-sorted-array/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Even though the array is rotated, whenever we divide it at midpoint `mid`, at least one of the two halves [left, mid] or [mid, right] is guaranteed to be normally sorted. We check if the left half is sorted (nums[left] <= nums[mid]). If it is, we check if target falls inside that range. If not, the right half must be sorted, and we check if target falls in the right range. This preserves O(log N) binary search."

---

### 💡 Intuition & Core Insight
- **One Half is Always Sorted**: A single rotation inflection point cannot break both halves simultaneously.
- **Boundary Test**: If a half is sorted, testing `nums[low] <= target <= nums[high]` definitively tells us whether target is inside that half.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`
- L=0 (4), R=6 (2), mid=3 (7)
- Is left [4..7] sorted? Yes (4 <= 7). Is 0 in [4..7]? No -> L = mid + 1 = 4
- L=4 (0), R=6 (2), mid=5 (1)
- nums[mid] == 1. Left [0..1] sorted. Is 0 in [0..1]? Yes! -> R = mid - 1 = 4
- L=4 (0), R=4 (0), mid=4 (0) -> nums[mid] == target -> Return 4!

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;

            // Check if left half is sorted
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else { // Right half is sorted
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log N)$ — Search space is halved at each step via binary search.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary pointers.

---

### ⚠️ Edge Cases & Interview Traps
1. Unrotated array: behaves like standard binary search.
2. Target not present: returns -1.

---

### 💬 Follow-Up Questions You Might Get
- *What if duplicate elements are allowed?* nums[left] == nums[mid] prevents determining the sorted half; increment left++ degrading to O(N) worst-case (LeetCode 81).
