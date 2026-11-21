# 26. Remove Duplicates from Sorted Array

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
[![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-blue)](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Given a sorted array, we need to remove duplicates in-place such that each unique element appears once. We use two pointers: a slow pointer `k` pointing to the last confirmed unique slot, and a fast pointer `i` scanning ahead. Whenever `nums[i] != nums[k]`, we increment `k` and write `nums[k] = nums[i]`."

---

### 💡 Intuition & Core Insight
- **Sorted Invariant**: Identical elements are always contiguous in a sorted array.
- **Slow-Fast Reader/Writer**: The fast pointer reads every element; the slow pointer writes only when a strictly new value is encountered.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [0, 0, 1, 1, 1, 2, 2]`
- k = 0, nums[0] = 0
- i = 1: nums[1] == 0 (duplicate, skip)
- i = 2: nums[2] == 1 != nums[k] -> k=1, nums[1]=1
- i = 3, 4: duplicate 1s (skip)
- i = 5: nums[5] == 2 != nums[k] -> k=2, nums[2]=2
Result: k + 1 = 3 unique elements (`[0, 1, 2]`).

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int k = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[k]) {
                k++;
                nums[k] = nums[i];
            }
        }
        return k + 1;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k + 1
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Fast pointer scans the array of length N exactly once.
- **Space Complexity**: $\mathcal{O}(1)$ — In-place modification using constant variables.

---

### ⚠️ Edge Cases & Interview Traps
1. Length 1: loop never runs, returns 1.
2. All identical: loop skips all, returns 1.

---

### 💬 Follow-Up Questions You Might Get
- *What if at most two duplicates are allowed?* Compare with nums[k - 1] (LeetCode 80).
