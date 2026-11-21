# 336. Palindrome Pairs

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/palindrome-pairs)
[![Topic: Trie & Array & Hash Table](https://img.shields.io/badge/Topic-Trie%20&%20Array%20&%20Hash%20Table-blue)](https://leetcode.com/problems/palindrome-pairs)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Trie strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `words = [&quot;abcd&quot;,&quot;dcba&quot;,&quot;lls&quot;,&quot;s&quot;,&quot;sssll&quot;]`  
**Expected Output**: `[[0,1],[1,0],[3,2],[2,4]]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `words = [&quot;abcd&quot;,&quot;dcba&quot;,&quot;lls&quot;,&quot;s&quot;,&quot;sssll&quot;]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[[0,1],[1,0],[3,2],[2,4]]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        Map<String, Integer> d = new HashMap<>();
        for (int i = 0; i < words.length; ++i) {
            d.put(words[i], i);
        }
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < words.length; ++i) {
            String w = words[i];
            int m = w.length();
            for (int j = 0; j <= m; ++j) {
                String a = w.substring(0, j);
                String b = w.substring(j);
                String ra = new StringBuilder(a).reverse().toString();
                String rb = new StringBuilder(b).reverse().toString();
                if (d.containsKey(ra) && d.get(ra) != i && b.equals(rb)) {
                    ans.add(Arrays.asList(i, d.get(ra)));
                }
                if (j > 0 && d.containsKey(rb) && d.get(rb) != i && a.equals(ra)) {
                    ans.add(Arrays.asList(d.get(rb), i));
                }
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        d = {w: i for i, w in enumerate(words)}
        ans = []
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                a, b = w[:j], w[j:]
                ra, rb = a[::-1], b[::-1]
                if ra in d and d[ra] != i and b == rb:
                    ans.append([i, d[ra]])
                if j and rb in d and d[rb] != i and a == ra:
                    ans.append([d[rb], i])
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
