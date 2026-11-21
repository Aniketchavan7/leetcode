# 625. Minimum Factorization

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/minimum-factorization)
[![Topic: Greedy & Math & Prime Factorization](https://img.shields.io/badge/Topic-Greedy%20&%20Math%20&%20Prime%20Factorization-blue)](https://leetcode.com/problems/minimum-factorization)

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
**Sample Input**: `num = 48`  
**Expected Output**: `68`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `num = 48` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `68` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int smallestFactorization(int num) {
        if (num < 2) {
            return num;
        }
        long ans = 0, mul = 1;
        for (int i = 9; i >= 2; --i) {
            if (num % i == 0) {
                while (num % i == 0) {
                    num /= i;
                    ans = mul * i + ans;
                    mul *= 10;
                }
            }
        }
        return num < 2 && ans <= Integer.MAX_VALUE ? (int) ans : 0;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num < 2:
            return num
        ans, mul = 0, 1
        for i in range(9, 1, -1):
            while num % i == 0:
                num //= i
                ans = mul * i + ans
                mul *= 10
        return ans if num < 2 and ans <= 2**31 - 1 else 0
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
