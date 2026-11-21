# 467. Unique Substrings in Wraparound String

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/unique-substrings-in-wraparound-string)
[![Topic: String & Dynamic Programming](https://img.shields.io/badge/Topic-String%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/unique-substrings-in-wraparound-string)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "In this problem, subproblems overlap and possess optimal substructure. Instead of an exponential recursive tree, we define a memoized state array where dp[i] captures the optimal decision up to index i, transitioning in polynomial time."

---

### 💡 Intuition & Core Insight
- **Brute Force Bottleneck**: Exploring all state combinations yields exponential O(2^N) or O(N!) complexity.
- **Optimal Substructure**: The optimal solution at state i depends strictly on already computed sub-states.
- **State Invariant**: Maintaining optimal transitions avoids re-evaluating subproblems.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `s = &quot;a&quot;`  
**Expected Output**: `1`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s = &quot;a&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `1` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int findSubstringInWraproundString(String s) {
        int[] f = new int[26];
        int n = s.length();
        for (int i = 0, k = 0; i < n; ++i) {
            if (i > 0 && (s.charAt(i) - s.charAt(i - 1) + 26) % 26 == 1) {
                ++k;
            } else {
                k = 1;
            }
            f[s.charAt(i) - 'a'] = Math.max(f[s.charAt(i) - 'a'], k);
        }
        return Arrays.stream(f).sum();
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        f = defaultdict(int)
        k = 0
        for i, c in enumerate(s):
            if i and (ord(c) - ord(s[i - 1])) % 26 == 1:
                k += 1
            else:
                k = 1
            f[c] = max(f[c], k)
        return sum(f.values())
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Boundary states at index 0 and 1.
2. Integer overflow when accumulating large transitions.
3. Base case initialization of unreachable states.

---

### 💬 Follow-Up Questions You Might Get
*Can we optimize space?* Yes, if each state depends only on the previous k states, we can reduce space from O(N) to O(1) using rolling variables.
