# 324. Wiggle Sort II

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/wiggle-sort-ii)
[![Topic: Greedy & Array & Divide and Conquer](https://img.shields.io/badge/Topic-Greedy%20&%20Array%20&%20Divide%20and%20Conquer-blue)](https://leetcode.com/problems/wiggle-sort-ii)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Greedy strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `nums = [1,5,1,1,6,4]`  
**Expected Output**: `[1,6,1,5,1,4]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [1,5,1,1,6,4]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[1,6,1,5,1,4]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public void wiggleSort(int[] nums) {
        int[] arr = nums.clone();
        Arrays.sort(arr);
        int n = nums.length;
        int i = (n - 1) >> 1, j = n - 1;
        for (int k = 0; k < n; ++k) {
            if (k % 2 == 0) {
                nums[k] = arr[i--];
            } else {
                nums[k] = arr[j--];
            }
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        n = len(arr)
        i, j = (n - 1) >> 1, n - 1
        for k in range(n):
            if k % 2 == 0:
                nums[k] = arr[i]
                i -= 1
            else:
                nums[k] = arr[j]
                j -= 1
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
