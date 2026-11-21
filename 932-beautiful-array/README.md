# 932. Beautiful Array

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/beautiful-array)
[![Topic: Array & Math & Divide and Conquer](https://img.shields.io/badge/Topic-Array%20&%20Math%20&%20Divide%20and%20Conquer-blue)](https://leetcode.com/problems/beautiful-array)

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
**Sample Input**: `n = 4`  
**Expected Output**: `[2,1,4,3]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `n = 4` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[2,1,4,3]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] beautifulArray(int n) {
        if (n == 1) {
            return new int[] {1};
        }
        int[] left = beautifulArray((n + 1) >> 1);
        int[] right = beautifulArray(n >> 1);
        int[] ans = new int[n];
        int i = 0;
        for (int x : left) {
            ans[i++] = x * 2 - 1;
        }
        for (int x : right) {
            ans[i++] = x * 2;
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        if n == 1:
            return [1]
        left = self.beautifulArray((n + 1) >> 1)
        right = self.beautifulArray(n >> 1)
        left = [x * 2 - 1 for x in left]
        right = [x * 2 for x in right]
        return left + right
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
