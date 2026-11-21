# 829. Consecutive Numbers Sum

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/consecutive-numbers-sum)
[![Topic: Math & Enumeration](https://img.shields.io/badge/Topic-Math%20&%20Enumeration-blue)](https://leetcode.com/problems/consecutive-numbers-sum)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Math strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `n = 5`  
**Expected Output**: `2`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `n = 5` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `2` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {

    public int consecutiveNumbersSum(int n) {
        n <<= 1;
        int ans = 0;
        for (int k = 1; k * (k + 1) <= n; ++k) {
            if (n % k == 0 && (n / k + 1 - k) % 2 == 0) {
                ++ans;
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        n <<= 1
        ans, k = 0, 1
        while k * (k + 1) <= n:
            if n % k == 0 and (n // k - k + 1) % 2 == 0:
                ans += 1
            k += 1
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
