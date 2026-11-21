# 267. Palindrome Permutation II

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/palindrome-permutation-ii)
[![Topic: Hash Table & String & Backtracking](https://img.shields.io/badge/Topic-Hash%20Table%20&%20String%20&%20Backtracking-blue)](https://leetcode.com/problems/palindrome-permutation-ii)

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
**Sample Input**: `s = "aabb"`  
**Expected Output**: `["abba","baab"]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s = "aabb"` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `["abba","baab"]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private List<String> ans = new ArrayList<>();
    private int[] cnt = new int[26];
    private int n;

    public List<String> generatePalindromes(String s) {
        n = s.length();
        for (char c : s.toCharArray()) {
            ++cnt[c - 'a'];
        }
        String mid = "";
        for (int i = 0; i < 26; ++i) {
            if (cnt[i] % 2 == 1) {
                if (!"".equals(mid)) {
                    return ans;
                }
                mid = String.valueOf((char) (i + 'a'));
            }
        }
        dfs(mid);
        return ans;
    }

    private void dfs(String t) {
        if (t.length() == n) {
            ans.add(t);
            return;
        }
        for (int i = 0; i < 26; ++i) {
            if (cnt[i] > 1) {
                String c = String.valueOf((char) (i + 'a'));
                cnt[i] -= 2;
                dfs(c + t + c);
                cnt[i] += 2;
            }
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def generatePalindromes(self, s: str) -> list[str]:
        def dfs(t):
            if len(t) == len(s):
                ans.append(t)
                return
            for c, v in cnt.items():
                if v > 1:
                    cnt[c] -= 2
                    dfs(c + t + c)
                    cnt[c] += 2

        cnt = Counter(s)
        mid = ''
        for c, v in cnt.items():
            if v & 1:
                if mid:
                    return []
                mid = c
                cnt[c] -= 1
        ans = []
        dfs(mid)
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
