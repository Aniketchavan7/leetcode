# 860. Lemonade Change

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/lemonade-change)
[![Topic: Greedy & Array](https://img.shields.io/badge/Topic-Greedy%20&%20Array-blue)](https://leetcode.com/problems/lemonade-change)

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
**Sample Input**: `bills = [5,5,5,10,20]`  
**Expected Output**: `true`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `bills = [5,5,5,10,20]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `true` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean lemonadeChange(int[] bills) {
        int five = 0, ten = 0;
        for (int v : bills) {
            switch (v) {
                case 5 -> ++five;
                case 10 -> {
                    ++ten;
                    --five;
                }
                case 20 -> {
                    if (ten > 0) {
                        --ten;
                        --five;
                    } else {
                        five -= 3;
                    }
                }
            }
            if (five < 0) {
                return false;
            }
        }
        return true;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = ten = 0
        for v in bills:
            if v == 5:
                five += 1
            elif v == 10:
                ten += 1
                five -= 1
            else:
                if ten:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0:
                return False
        return True
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
