# 523. Continuous Subarray Sum

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/continuous-subarray-sum)
[![Topic: Array & Hash Table & Math](https://img.shields.io/badge/Topic-Array%20&%20Hash%20Table%20&%20Math-blue)](https://leetcode.com/problems/continuous-subarray-sum)

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
**Sample Input**: `nums = [23,`  
**Expected Output**: `true`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [23,` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `true` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> d = new HashMap<>();
        d.put(0, -1);
        int s = 0;
        for (int i = 0; i < nums.length; ++i) {
            s = (s + nums[i]) % k;
            if (!d.containsKey(s)) {
                d.put(s, i);
            } else if (i - d.get(s) > 1) {
                return true;
            }
        }
        return false;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        d = {0: -1}
        s = 0
        for i, x in enumerate(nums):
            s = (s + x) % k
            if s not in d:
                d[s] = i
            elif i - d[s] > 1:
                return True
        return False
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
