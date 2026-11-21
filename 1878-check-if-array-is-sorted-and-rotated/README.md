# 1878. Check if Array Is Sorted and Rotated

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)
[![Topic: Arrays](https://img.shields.io/badge/Topic-Arrays-blue)](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "A sorted array is non-decreasing. When rotated, there can be at most ONE point where `nums[i] > nums[(i + 1) % n]` (the rotation drop point). We iterate through the array and count how many times `nums[i] > nums[(i + 1) % n]`. If this drop count is <= 1, return true; otherwise false."

---

### 💡 Intuition & Core Insight
- **Circular Invariant**: Connecting the array circularly, an originally sorted array has 0 drops; a rotated sorted array has exactly 1 drop; an unsorted array has 2 or more drops.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [3, 4, 5, 1, 2]`
- 3 <= 4 (ok)
- 4 <= 5 (ok)
- 5 > 1 (drop 1!)
- 1 <= 2 (ok)
- 2 <= 3 (circular wrap ok)
Total drops = 1 <= 1 -> True!

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean check(int[] nums) {
        int drops = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] > nums[(i + 1) % n]) {
                drops++;
            }
        }
        return drops <= 1;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def check(self, nums: list[int]) -> bool:
        drops = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
        return drops <= 1
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Single circular pass of length N.
- **Space Complexity**: $\mathcal{O}(1)$ — One drop counter variable.

---

### ⚠️ Edge Cases & Interview Traps
1. Unrotated sorted array [1, 2, 3]: drops = 0 <= 1 -> returns true.
2. All identical elements [1, 1, 1]: drops = 0 -> returns true.

---

### 💬 Follow-Up Questions You Might Get
- *What if strict increasing is required?* Change comparison to >=.
