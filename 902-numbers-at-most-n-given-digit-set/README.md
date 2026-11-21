# 902. Numbers At Most N Given Digit Set

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/numbers-at-most-n-given-digit-set)
[![Topic: Array & Math & String](https://img.shields.io/badge/Topic-Array%20&%20Math%20&%20String-blue)](https://leetcode.com/problems/numbers-at-most-n-given-digit-set)

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
**Sample Input**: `digits = [&quot;1&quot;,&quot;3&quot;,&quot;5&quot;,&quot;7&quot;], n = 100`  
**Expected Output**: `20`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `digits = [&quot;1&quot;,&quot;3&quot;,&quot;5&quot;,&quot;7&quot;], n = 100` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `20` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private Set<Integer> nums = new HashSet<>();
    private char[] s;
    private Integer[] f;

    public int atMostNGivenDigitSet(String[] digits, int n) {
        s = String.valueOf(n).toCharArray();
        f = new Integer[s.length];
        for (var x : digits) {
            nums.add(Integer.parseInt(x));
        }
        return dfs(0, true, true);
    }

    private int dfs(int i, boolean lead, boolean limit) {
        if (i >= s.length) {
            return lead ? 0 : 1;
        }
        if (!lead && !limit && f[i] != null) {
            return f[i];
        }
        int up = limit ? s[i] - '0' : 9;
        int ans = 0;
        for (int j = 0; j <= up; ++j) {
            if (j == 0 && lead) {
                ans += dfs(i + 1, true, limit && j == up);
            } else if (nums.contains(j)) {
                ans += dfs(i + 1, false, limit && j == up);
            }
        }
        if (!lead && !limit) {
            f[i] = ans;
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        @cache
        def dfs(i: int, lead: int, limit: bool) -> int:
            if i >= len(s):
                return lead ^ 1

            up = int(s[i]) if limit else 9
            ans = 0
            for j in range(up + 1):
                if j == 0 and lead:
                    ans += dfs(i + 1, 1, limit and j == up)
                elif j in nums:
                    ans += dfs(i + 1, 0, limit and j == up)
            return ans

        s = str(n)
        nums = {int(x) for x in digits}
        return dfs(0, 1, True)
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
