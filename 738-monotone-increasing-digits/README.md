# 738. Monotone Increasing Digits

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/monotone-increasing-digits)
[![Topic: Greedy & Math](https://img.shields.io/badge/Topic-Greedy%20&%20Math-blue)](https://leetcode.com/problems/monotone-increasing-digits)

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
**Sample Input**: `n = 10`  
**Expected Output**: `9`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `n = 10` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `9` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int monotoneIncreasingDigits(int n) {
        char[] s = String.valueOf(n).toCharArray();
        int i = 1;
        for (; i < s.length && s[i - 1] <= s[i]; ++i)
            ;
        if (i < s.length) {
            for (; i > 0 && s[i - 1] > s[i]; --i) {
                --s[i - 1];
            }
            ++i;
            for (; i < s.length; ++i) {
                s[i] = '9';
            }
        }
        return Integer.parseInt(String.valueOf(s));
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        i = 1
        while i < len(s) and s[i - 1] <= s[i]:
            i += 1
        if i < len(s):
            while i and s[i - 1] > s[i]:
                s[i - 1] = str(int(s[i - 1]) - 1)
                i -= 1
            i += 1
            while i < len(s):
                s[i] = '9'
                i += 1
        return int(''.join(s))
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
