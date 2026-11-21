# 645. Set Mismatch

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/set-mismatch)
[![Topic: Bit Manipulation & Array & Hash Table](https://img.shields.io/badge/Topic-Bit%20Manipulation%20&%20Array%20&%20Hash%20Table-blue)](https://leetcode.com/problems/set-mismatch)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Bit Manipulation strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `nums = [1,2,2,4]`  
**Expected Output**: `[2,3]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [1,2,2,4]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[2,3]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        int s1 = (1 + n) * n / 2;
        int s2 = 0;
        Set<Integer> set = new HashSet<>();
        int s = 0;
        for (int x : nums) {
            if (set.add(x)) {
                s2 += x;
            }
            s += x;
        }
        return new int[] {s - s2, s1 - s2};
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        s1 = (1 + n) * n // 2
        s2 = sum(set(nums))
        s = sum(nums)
        return [s - s2, s1 - s2]
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
