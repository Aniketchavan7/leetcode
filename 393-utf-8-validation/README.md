# 393. UTF-8 Validation

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/utf-8-validation)
[![Topic: Bit Manipulation & Array](https://img.shields.io/badge/Topic-Bit%20Manipulation%20&%20Array-blue)](https://leetcode.com/problems/utf-8-validation)

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
**Sample Input**: `data = [197,130,1]`  
**Expected Output**: `true`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `data = [197,130,1]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `true` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean validUtf8(int[] data) {
        int cnt = 0;
        for (int v : data) {
            if (cnt > 0) {
                if (v >> 6 != 0b10) {
                    return false;
                }
                --cnt;
            } else if (v >> 7 == 0) {
                cnt = 0;
            } else if (v >> 5 == 0b110) {
                cnt = 1;
            } else if (v >> 4 == 0b1110) {
                cnt = 2;
            } else if (v >> 3 == 0b11110) {
                cnt = 3;
            } else {
                return false;
            }
        }
        return cnt == 0;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        cnt = 0
        for v in data:
            if cnt > 0:
                if v >> 6 != 0b10:
                    return False
                cnt -= 1
            elif v >> 7 == 0:
                cnt = 0
            elif v >> 5 == 0b110:
                cnt = 1
            elif v >> 4 == 0b1110:
                cnt = 2
            elif v >> 3 == 0b11110:
                cnt = 3
            else:
                return False
        return cnt == 0
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
