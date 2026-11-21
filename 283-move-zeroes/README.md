# 283. Move Zeroes

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/move-zeroes/)
[![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-blue)](https://leetcode.com/problems/move-zeroes/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We must move all 0s to the end of the array while maintaining the relative order of non-zero elements in-place. We use a slow pointer `insertPos` tracking where the next non-zero should be placed. As the fast pointer scans the array, whenever it encounters a non-zero, we swap `nums[insertPos]` with `nums[i]` and increment `insertPos`."

---

### 💡 Intuition & Core Insight
- **Snowball of Zeroes**: Swapping automatically pushes zeroes forward while preserving the relative sequence of non-zero numbers without a second fill-zeroes pass.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [0, 1, 0, 3, 12]`
- i=0: val=0 (skip)
- i=1: val=1 != 0 -> swap(0, 1) -> `[1, 0, 0, 3, 12]`, insertPos=1
- i=2: val=0 (skip)
- i=3: val=3 != 0 -> swap(1, 3) -> `[1, 3, 0, 0, 12]`, insertPos=2
- i=4: val=12 != 0 -> swap(2, 4) -> `[1, 3, 12, 0, 0]`, insertPos=3
Result: `[1, 3, 12, 0, 0]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public void moveZeroes(int[] nums) {
        int insertPos = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                if (i != insertPos) {
                    int tmp = nums[insertPos];
                    nums[insertPos] = nums[i];
                    nums[i] = tmp;
                }
                insertPos++;
            }
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Single linear pass with at most N swaps.
- **Space Complexity**: $\mathcal{O}(1)$ — In-place pointer modifications.

---

### ⚠️ Edge Cases & Interview Traps
1. No zeroes in array: elements stay in place, 0 swaps.
2. All zeroes: insertPos stays 0, 0 swaps.

---

### 💬 Follow-Up Questions You Might Get
- *How to minimize total writes if most elements are zero?* Only write when insertPos != i.
