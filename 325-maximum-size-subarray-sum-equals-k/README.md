# 325. Maximum Size Subarray Sum Equals k

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k)
[![Topic: Array & Hash Table & Prefix Sum](https://img.shields.io/badge/Topic-Array%20&%20Hash%20Table%20&%20Prefix%20Sum-blue)](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k)

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
**Sample Input**: `nums = [1,-1,5,-2,3], k = 3`  
**Expected Output**: `4`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [1,-1,5,-2,3], k = 3` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `4` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        Map<Long, Integer> d = new HashMap<>();
        d.put(0L, -1);
        int ans = 0;
        long s = 0;
        for (int i = 0; i < nums.length; ++i) {
            s += nums[i];
            ans = Math.max(ans, i - d.getOrDefault(s - k, i));
            d.putIfAbsent(s, i);
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        d = {0: -1}
        ans = s = 0
        for i, x in enumerate(nums):
            s += x
            if s - k in d:
                ans = max(ans, i - d[s - k])
            if s not in d:
                d[s] = i
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
