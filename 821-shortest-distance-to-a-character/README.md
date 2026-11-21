# 821. Shortest Distance to a Character

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/shortest-distance-to-a-character)
[![Topic: Array & Two Pointers & String](https://img.shields.io/badge/Topic-Array%20&%20Two%20Pointers%20&%20String-blue)](https://leetcode.com/problems/shortest-distance-to-a-character)

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
**Sample Input**: `s = &quot;loveleetcode&quot;, c = &quot;e&quot;`  
**Expected Output**: `[3,2,1,0,1,0,0,1,2,2,1,0]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s = &quot;loveleetcode&quot;, c = &quot;e&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[3,2,1,0,1,0,0,1,2,2,1,0]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] shortestToChar(String s, char c) {
        int n = s.length();
        int[] ans = new int[n];
        final int inf = 1 << 30;
        Arrays.fill(ans, inf);
        for (int i = 0, pre = -inf; i < n; ++i) {
            if (s.charAt(i) == c) {
                pre = i;
            }
            ans[i] = Math.min(ans[i], i - pre);
        }
        for (int i = n - 1, suf = inf; i >= 0; --i) {
            if (s.charAt(i) == c) {
                suf = i;
            }
            ans[i] = Math.min(ans[i], suf - i);
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        ans = [n] * n
        pre = -inf
        for i, ch in enumerate(s):
            if ch == c:
                pre = i
            ans[i] = min(ans[i], i - pre)
        suf = inf
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                suf = i
            ans[i] = min(ans[i], suf - i)
        return ans
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
