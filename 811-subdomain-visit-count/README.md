# 811. Subdomain Visit Count

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/subdomain-visit-count)
[![Topic: Array & Hash Table & String](https://img.shields.io/badge/Topic-Array%20&%20Hash%20Table%20&%20String-blue)](https://leetcode.com/problems/subdomain-visit-count)

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
**Sample Input**: `cpdomains = [&quot;9001 discuss.leetcode.com&quot;]`  
**Expected Output**: `[&quot;9001 leetcode.com&quot;,&quot;9001 discuss.leetcode.com&quot;,&quot;9001 com&quot;]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `cpdomains = [&quot;9001 discuss.leetcode.com&quot;]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[&quot;9001 leetcode.com&quot;,&quot;9001 discuss.leetcode.com&quot;,&quot;9001 com&quot;]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> cnt = new HashMap<>();
        for (String s : cpdomains) {
            int i = s.indexOf(" ");
            int v = Integer.parseInt(s.substring(0, i));
            for (; i < s.length(); ++i) {
                if (s.charAt(i) == ' ' || s.charAt(i) == '.') {
                    String t = s.substring(i + 1);
                    cnt.put(t, cnt.getOrDefault(t, 0) + v);
                }
            }
        }
        List<String> ans = new ArrayList<>();
        for (var e : cnt.entrySet()) {
            ans.add(e.getValue() + " " + e.getKey());
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        cnt = Counter()
        for s in cpdomains:
            v = int(s[: s.index(' ')])
            for i, c in enumerate(s):
                if c in ' .':
                    cnt[s[i + 1 :]] += v
        return [f'{v} {s}' for s, v in cnt.items()]
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
