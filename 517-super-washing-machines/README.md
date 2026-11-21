# 517. Super Washing Machines

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/super-washing-machines)
[![Topic: Greedy & Array](https://img.shields.io/badge/Topic-Greedy%20&%20Array-blue)](https://leetcode.com/problems/super-washing-machines)

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
**Sample Input**: `machines = [1,0,5]`  
**Expected Output**: `3`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `machines = [1,0,5]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `3` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int findMinMoves(int[] machines) {
        int n = machines.length;
        int s = 0;
        for (int x : machines) {
            s += x;
        }
        if (s % n != 0) {
            return -1;
        }
        int k = s / n;
        s = 0;
        int ans = 0;
        for (int x : machines) {
            x -= k;
            s += x;
            ans = Math.max(ans, Math.max(Math.abs(s), x));
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        n = len(machines)
        k, mod = divmod(sum(machines), n)
        if mod:
            return -1
        ans = s = 0
        for x in machines:
            x -= k
            s += x
            ans = max(ans, abs(s), x)
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
