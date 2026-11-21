# 890. Find and Replace Pattern

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/find-and-replace-pattern)
[![Topic: Array & Hash Table & String](https://img.shields.io/badge/Topic-Array%20&%20Hash%20Table%20&%20String-blue)](https://leetcode.com/problems/find-and-replace-pattern)

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
**Sample Input**: `words = [&quot;abc&quot;,&quot;deq&quot;,&quot;mee&quot;,&quot;aqq&quot;,&quot;dkd&quot;,&quot;ccc&quot;], pattern = &quot;abb&quot;`  
**Expected Output**: `[&quot;mee&quot;,&quot;aqq&quot;]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `words = [&quot;abc&quot;,&quot;deq&quot;,&quot;mee&quot;,&quot;aqq&quot;,&quot;dkd&quot;,&quot;ccc&quot;], pattern = &quot;abb&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[&quot;mee&quot;,&quot;aqq&quot;]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> ans = new ArrayList<>();
        for (String word : words) {
            if (match(word, pattern)) {
                ans.add(word);
            }
        }
        return ans;
    }

    private boolean match(String s, String t) {
        int[] m1 = new int[128];
        int[] m2 = new int[128];
        for (int i = 0; i < s.length(); ++i) {
            char c1 = s.charAt(i);
            char c2 = t.charAt(i);
            if (m1[c1] != m2[c2]) {
                return false;
            }
            m1[c1] = i + 1;
            m2[c2] = i + 1;
        }
        return true;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        def match(s, t):
            m1, m2 = [0] * 128, [0] * 128
            for i, (a, b) in enumerate(zip(s, t), 1):
                if m1[ord(a)] != m2[ord(b)]:
                    return False
                m1[ord(a)] = m2[ord(b)] = i
            return True

        return [word for word in words if match(word, pattern)]
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
