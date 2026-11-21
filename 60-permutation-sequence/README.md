# 60. Permutation Sequence

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/permutation-sequence)
[![Topic: Recursion & Math](https://img.shields.io/badge/Topic-Recursion%20&%20Math-blue)](https://leetcode.com/problems/permutation-sequence)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Recursion strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `n = 3, k = 3`  
**Expected Output**: `"213"`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `n = 3, k = 3` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `"213"` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String getPermutation(int n, int k) {
        StringBuilder ans = new StringBuilder();
        boolean[] vis = new boolean[n + 1];
        for (int i = 0; i < n; ++i) {
            int fact = 1;
            for (int j = 1; j < n - i; ++j) {
                fact *= j;
            }
            for (int j = 1; j <= n; ++j) {
                if (!vis[j]) {
                    if (k > fact) {
                        k -= fact;
                    } else {
                        ans.append(j);
                        vis[j] = true;
                        break;
                    }
                }
            }
        }
        return ans.toString();
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        vis = [False] * (n + 1)
        for i in range(n):
            fact = 1
            for j in range(1, n - i):
                fact *= j
            for j in range(1, n + 1):
                if not vis[j]:
                    if k > fact:
                        k -= fact
                    else:
                        ans.append(str(j))
                        vis[j] = True
                        break
        return ''.join(ans)
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
