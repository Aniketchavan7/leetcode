# 140. Word Break II

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/word-break-ii)
[![Topic: Trie & Memoization & Array](https://img.shields.io/badge/Topic-Trie%20&%20Memoization%20&%20Array-blue)](https://leetcode.com/problems/word-break-ii)

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
**Sample Input**: `s = &quot;catsanddog&quot;, wordDict = [&quot;cat&quot;,&quot;cats&quot;,&quot;and&quot;,&quot;sand&quot;,&quot;dog&quot;]`  
**Expected Output**: `[&quot;cats and dog&quot;,&quot;cat sand dog&quot;]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s = &quot;catsanddog&quot;, wordDict = [&quot;cat&quot;,&quot;cats&quot;,&quot;and&quot;,&quot;sand&quot;,&quot;dog&quot;]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[&quot;cats and dog&quot;,&quot;cat sand dog&quot;]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Trie {
    Trie[] children = new Trie[26];
    boolean isEnd;

    void insert(String word) {
        Trie node = this;
        for (char c : word.toCharArray()) {
            c -= 'a';
            if (node.children[c] == null) {
                node.children[c] = new Trie();
            }
            node = node.children[c];
        }
        node.isEnd = true;
    }

    boolean search(String word) {
        Trie node = this;
        for (char c : word.toCharArray()) {
            c -= 'a';
            if (node.children[c] == null) {
                return false;
            }
            node = node.children[c];
        }
        return node.isEnd;
    }
}

class Solution {
    private Trie trie = new Trie();

    public List<String> wordBreak(String s, List<String> wordDict) {
        for (String w : wordDict) {
            trie.insert(w);
        }
        List<List<String>> res = dfs(s);
        return res.stream().map(e -> String.join(" ", e)).collect(Collectors.toList());
    }

    private List<List<String>> dfs(String s) {
        List<List<String>> res = new ArrayList<>();
        if ("".equals(s)) {
            res.add(new ArrayList<>());
            return res;
        }
        for (int i = 1; i <= s.length(); ++i) {
            if (trie.search(s.substring(0, i))) {
                for (List<String> v : dfs(s.substring(i))) {
                    v.add(0, s.substring(0, i));
                    res.add(v);
                }
            }
        }
        return res;
    }
}
```

#### Python 3 Solution
```python
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word):
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

    def search(self, word):
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return node.is_end


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        def dfs(s):
            if not s:
                return [[]]
            res = []
            for i in range(1, len(s) + 1):
                if trie.search(s[:i]):
                    for v in dfs(s[i:]):
                        res.append([s[:i]] + v)
            return res

        trie = Trie()
        for w in wordDict:
            trie.insert(w)
        ans = dfs(s)
        return [' '.join(v) for v in ans]
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
