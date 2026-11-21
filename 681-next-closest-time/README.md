# 681. Next Closest Time

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/next-closest-time)
[![Topic: Hash Table & String & Backtracking](https://img.shields.io/badge/Topic-Hash%20Table%20&%20String%20&%20Backtracking-blue)](https://leetcode.com/problems/next-closest-time)

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
**Sample Input**: `time = &quot;19:34&quot;`  
**Expected Output**: `&quot;19:39&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `time = &quot;19:34&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;19:39&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int t;
    private int d;
    private String ans;
    private Set<Character> s;

    public String nextClosestTime(String time) {
        t = Integer.parseInt(time.substring(0, 2)) * 60 + Integer.parseInt(time.substring(3));
        d = Integer.MAX_VALUE;
        s = new HashSet<>();
        char mi = 'z';
        for (char c : time.toCharArray()) {
            if (c != ':') {
                s.add(c);
                if (c < mi) {
                    mi = c;
                }
            }
        }
        ans = null;
        dfs("");
        if (ans == null) {
            ans = "" + mi + mi + ":" + mi + mi;
        }
        return ans;
    }

    private void dfs(String curr) {
        if (curr.length() == 4) {
            if (!check(curr)) {
                return;
            }
            int p
                = Integer.parseInt(curr.substring(0, 2)) * 60 + Integer.parseInt(curr.substring(2));
            if (p > t && p - t < d) {
                d = p - t;
                ans = curr.substring(0, 2) + ":" + curr.substring(2);
            }
            return;
        }
        for (char c : s) {
            dfs(curr + c);
        }
    }

    private boolean check(String t) {
        int h = Integer.parseInt(t.substring(0, 2));
        int m = Integer.parseInt(t.substring(2));
        return 0 <= h && h < 24 && 0 <= m && m < 60;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def nextClosestTime(self, time: str) -> str:
        def check(t):
            h, m = int(t[:2]), int(t[2:])
            return 0 <= h < 24 and 0 <= m < 60

        def dfs(curr):
            if len(curr) == 4:
                if not check(curr):
                    return
                nonlocal ans, d
                p = int(curr[:2]) * 60 + int(curr[2:])
                if t < p < t + d:
                    d = p - t
                    ans = curr[:2] + ':' + curr[2:]
                return
            for c in s:
                dfs(curr + c)

        s = {c for c in time if c != ':'}
        t = int(time[:2]) * 60 + int(time[3:])
        d = inf
        ans = None
        dfs('')
        if ans is None:
            mi = min(int(c) for c in s)
            ans = f'{mi}{mi}:{mi}{mi}'
        return ans
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
