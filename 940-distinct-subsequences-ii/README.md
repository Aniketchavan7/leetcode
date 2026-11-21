# 940. Distinct Subsequences II

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/distinct-subsequences-ii)
[![Topic: String & Dynamic Programming](https://img.shields.io/badge/Topic-String%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/distinct-subsequences-ii)

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
**Sample Input**: `s = &quot;abc&quot;`  
**Expected Output**: `7`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s = &quot;abc&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `7` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int distinctSubseqII(String s) {
        final int mod = (int) 1e9 + 7;
        int[] f = new int[26];
        for (int i = 0; i < s.length(); ++i) {
            int x = 1;
            for (int v : f) {
                x = (x + v) % mod;
            }
            f[s.charAt(i) - 'a'] = x;
        }
        int ans = 0;
        for (int v : f) {
            ans = (ans + v) % mod;
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        f = [0] * 26
        for c in s:
            f[ord(c) - ord("a")] = (sum(f) + 1) % mod
        return sum(f) % mod
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
