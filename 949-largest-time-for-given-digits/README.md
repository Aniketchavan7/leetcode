# 949. Largest Time for Given Digits

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/largest-time-for-given-digits)
[![Topic: Array & String & Backtracking](https://img.shields.io/badge/Topic-Array%20&%20String%20&%20Backtracking-blue)](https://leetcode.com/problems/largest-time-for-given-digits)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We frame the problem as exploring a state-space decision tree. At each step, we make a choice, recurse, and then undo the choice (backtrack) while pruning invalid paths early."

---

### 💡 Intuition & Core Insight
- **Pruning Optimization**: Pruning dead ends prevents traversing deep subtrees that violate constraints.
- **State Restoration**: Symmetrically appending and removing choices preserves state across recursion frames.
- **Deduplication**: Sorting inputs initially enables skipping duplicate branches with `if (i > start && nums[i] == nums[i-1]) continue`.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `arr = [1,2,3,4]`  
**Expected Output**: `&quot;23:41&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `arr = [1,2,3,4]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;23:41&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
// Implementation provided in Solution.java
```

#### Python 3 Solution
```python
class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        cnt = [0] * 10
        for v in arr:
            cnt[v] += 1
        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                t = [0] * 10
                t[h // 10] += 1
                t[h % 10] += 1
                t[m // 10] += 1
                t[m % 10] += 1
                if cnt == t:
                    return f'{h:02}:{m:02}'
        return ''
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(2^N \text{ or } N!)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Failing to create a deep copy of the current state before adding to results.
2. Infinite recursion due to incorrect base case condition.
3. Duplicate combinations generated from identical elements.

---

### 💬 Follow-Up Questions You Might Get
*How can we optimize memory overhead?* Use bitmasks instead of boolean arrays to track used elements.
