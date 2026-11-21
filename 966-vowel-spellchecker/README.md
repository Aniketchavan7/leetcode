# 966. Vowel Spellchecker

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/vowel-spellchecker)
[![Topic: Array & Hash Table & String](https://img.shields.io/badge/Topic-Array%20&%20Hash%20Table%20&%20String-blue)](https://leetcode.com/problems/vowel-spellchecker)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Array strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]`  
**Expected Output**: `["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String[] spellchecker(String[] wordlist, String[] queries) {
        Set<String> s = new HashSet<>();
        Map<String, String> low = new HashMap<>();
        Map<String, String> pat = new HashMap<>();
        for (String w : wordlist) {
            s.add(w);
            String t = w.toLowerCase();
            low.putIfAbsent(t, w);
            pat.putIfAbsent(f(t), w);
        }
        int m = queries.length;
        String[] ans = new String[m];
        for (int i = 0; i < m; ++i) {
            String q = queries[i];
            if (s.contains(q)) {
                ans[i] = q;
                continue;
            }
            q = q.toLowerCase();
            if (low.containsKey(q)) {
                ans[i] = low.get(q);
                continue;
            }
            q = f(q);
            if (pat.containsKey(q)) {
                ans[i] = pat.get(q);
                continue;
            }
            ans[i] = "";
        }
        return ans;
    }

    private String f(String w) {
        char[] cs = w.toCharArray();
        for (int i = 0; i < cs.length; ++i) {
            char c = cs[i];
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                cs[i] = '*';
            }
        }
        return String.valueOf(cs);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        def f(w):
            t = []
            for c in w:
                t.append("*" if c in "aeiou" else c)
            return "".join(t)

        s = set(wordlist)
        low, pat = {}, {}
        for w in wordlist:
            t = w.lower()
            low.setdefault(t, w)
            pat.setdefault(f(t), w)

        ans = []
        for q in queries:
            if q in s:
                ans.append(q)
                continue
            q = q.lower()
            if q in low:
                ans.append(low[q])
                continue
            q = f(q)
            if q in pat:
                ans.append(pat[q])
                continue
            ans.append("")
        return ans
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Handling empty or single-element inputs.
2. Boundary index arithmetic and potential overflow.
3. Duplicate or negative values in input collections.

---

### 💬 Follow-Up Questions You Might Get
*How does this scale to distributed streams?* Hash partitioning across shards or MapReduce pipelines can process data in parallel.
