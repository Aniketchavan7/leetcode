# 665. Non-decreasing Array

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/non-decreasing-array)
[![Topic: Array](https://img.shields.io/badge/Topic-Array-blue)](https://leetcode.com/problems/non-decreasing-array)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Array strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `nums = [4,2,3]`  
**Expected Output**: `true`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [4,2,3]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `true` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean checkPossibility(int[] nums) {
        for (int i = 0; i < nums.length - 1; ++i) {
            int a = nums[i], b = nums[i + 1];
            if (a > b) {
                nums[i] = b;
                if (isSorted(nums)) {
                    return true;
                }
                nums[i] = a;
                nums[i + 1] = a;
                return isSorted(nums);
            }
        }
        return true;
    }

    private boolean isSorted(int[] nums) {
        for (int i = 0; i < nums.length - 1; ++i) {
            if (nums[i] > nums[i + 1]) {
                return false;
            }
        }
        return true;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        def is_sorted(nums: list[int]) -> bool:
            return all(a <= b for a, b in pairwise(nums))

        n = len(nums)
        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            if a > b:
                nums[i] = b
                if is_sorted(nums):
                    return True
                nums[i] = nums[i + 1] = a
                return is_sorted(nums)
        return True
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Handling empty or single-element inputs.
2. Boundary index arithmetic and potential overflow.
3. Duplicate or negative values in input collections.

---

### 💬 Follow-Up Questions You Might Get
*How does this scale to distributed streams?* Hash partitioning across shards or MapReduce pipelines can process data in parallel.
