# 891. Sum of Subsequence Widths

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/sum-of-subsequence-widths)
[![Topic: Array & Math & Sorting](https://img.shields.io/badge/Topic-Array%20&%20Math%20&%20Sorting-blue)](https://leetcode.com/problems/sum-of-subsequence-widths)

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
**Sample Input**: `nums = [2,1,3]`  
**Expected Output**: `6`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [2,1,3]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `6` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private static final int MOD = (int) 1e9 + 7;

    public int sumSubseqWidths(int[] nums) {
        Arrays.sort(nums);
        long ans = 0, p = 1;
        int n = nums.length;
        for (int i = 0; i < n; ++i) {
            ans = (ans + (nums[i] - nums[n - i - 1]) * p + MOD) % MOD;
            p = (p << 1) % MOD;
        }
        return (int) ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def sumSubseqWidths(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        nums.sort()
        ans, p = 0, 1
        for i, v in enumerate(nums):
            ans = (ans + (v - nums[-i - 1]) * p) % mod
            p = (p << 1) % mod
        return ans
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
