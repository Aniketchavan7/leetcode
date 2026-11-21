# 291. Word Pattern II

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/word-pattern-ii)
[![Topic: Hash Table & String & Backtracking](https://img.shields.io/badge/Topic-Hash%20Table%20&%20String%20&%20Backtracking-blue)](https://leetcode.com/problems/word-pattern-ii)

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
**Sample Input**: `pattern = &quot;abab&quot;, s = &quot;redblueredblue&quot;`  
**Expected Output**: `true`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `pattern = &quot;abab&quot;, s = &quot;redblueredblue&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `true` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private Set<String> vis;
    private Map<Character, String> d;
    private String p;
    private String s;
    private int m;
    private int n;

    public boolean wordPatternMatch(String pattern, String s) {
        vis = new HashSet<>();
        d = new HashMap<>();
        this.p = pattern;
        this.s = s;
        m = p.length();
        n = s.length();
        return dfs(0, 0);
    }

    private boolean dfs(int i, int j) {
        if (i == m && j == n) {
            return true;
        }
        if (i == m || j == n || m - i > n - j) {
            return false;
        }
        char c = p.charAt(i);
        for (int k = j + 1; k <= n; ++k) {
            String t = s.substring(j, k);
            if (d.getOrDefault(c, "").equals(t)) {
                if (dfs(i + 1, k)) {
                    return true;
                }
            }
            if (!d.containsKey(c) && !vis.contains(t)) {
                d.put(c, t);
                vis.add(t);
                if (dfs(i + 1, k)) {
                    return true;
                }
                vis.remove(t);
                d.remove(c);
            }
        }
        return false;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def dfs(i, j):
            if i == m and j == n:
                return True
            if i == m or j == n or n - j < m - i:
                return False
            for k in range(j, n):
                t = s[j : k + 1]
                if d.get(pattern[i]) == t:
                    if dfs(i + 1, k + 1):
                        return True
                if pattern[i] not in d and t not in vis:
                    d[pattern[i]] = t
                    vis.add(t)
                    if dfs(i + 1, k + 1):
                        return True
                    d.pop(pattern[i])
                    vis.remove(t)
            return False

        m, n = len(pattern), len(s)
        d = {}
        vis = set()
        return dfs(0, 0)
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
