# 161. One Edit Distance

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/one-edit-distance)
[![Topic: Two Pointers & String](https://img.shields.io/badge/Topic-Two%20Pointers%20&%20String-blue)](https://leetcode.com/problems/one-edit-distance)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "By maintaining window boundaries or dual pointers, we convert a quadratic pair search into a linear scan, dynamically expanding or shrinking based on feasibility invariants."

---

### 💡 Intuition & Core Insight
- **Monotonicity**: As the right pointer advances, the search space moves monotonically without backtracking.
- **Window Invariant**: Validating window conditions with a frequency counter guarantees correctness.
- **Two-Ended Traversal**: Squeezing inward from boundaries avoids evaluating redundant pairs.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `s = &quot;ab&quot;, t = &quot;acb&quot;`  
**Expected Output**: `true`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s = &quot;ab&quot;, t = &quot;acb&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `true` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int m = s.length(), n = t.length();
        if (m < n) {
            return isOneEditDistance(t, s);
        }
        if (m - n > 1) {
            return false;
        }
        for (int i = 0; i < n; ++i) {
            if (s.charAt(i) != t.charAt(i)) {
                if (m == n) {
                    return s.substring(i + 1).equals(t.substring(i + 1));
                }
                return s.substring(i + 1).equals(t.substring(i));
            }
        }
        return m == n + 1;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            return self.isOneEditDistance(t, s)
        m, n = len(s), len(t)
        if m - n > 1:
            return False
        for i, c in enumerate(t):
            if c != s[i]:
                return s[i + 1 :] == t[i + 1 :] if m == n else s[i + 1 :] == t[i:]
        return m == n + 1
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(1)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Off-by-one errors on window size (right - left + 1).
2. Empty arrays or arrays with all identical elements.
3. Forgetting to update state counters when shrinking the left boundary.

---

### 💬 Follow-Up Questions You Might Get
*What if the array cannot fit into memory?* We can stream data through a bounded circular buffer or sliding window chunk.
