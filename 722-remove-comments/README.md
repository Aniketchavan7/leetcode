# 722. Remove Comments

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/remove-comments)
[![Topic: Array & String](https://img.shields.io/badge/Topic-Array%20&%20String-blue)](https://leetcode.com/problems/remove-comments)

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
**Sample Input**: `source = [&quot;/*Test program */&quot;, &quot;int main()&quot;, &quot;{ &quot;, &quot;  // variable declaration &quot;, &quot;int a, b, c;&quot;, &quot;/* This is a test&quot;, &quot;   multiline  &quot;, &quot;   comment for &quot;, &quot;   testing */&quot;, &quot;a = b + c;&quot;, &quot;}&quot;]`  
**Expected Output**: `[&quot;int main()&quot;,&quot;{ &quot;,&quot;  &quot;,&quot;int a, b, c;&quot;,&quot;a = b + c;&quot;,&quot;}&quot;]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `source = [&quot;/*Test program */&quot;, &quot;int main()&quot;, &quot;{ &quot;, &quot;  // variable declaration &quot;, &quot;int a, b, c;&quot;, &quot;/* This is a test&quot;, &quot;   multiline  &quot;, &quot;   comment for &quot;, &quot;   testing */&quot;, &quot;a = b + c;&quot;, &quot;}&quot;]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[&quot;int main()&quot;,&quot;{ &quot;,&quot;  &quot;,&quot;int a, b, c;&quot;,&quot;a = b + c;&quot;,&quot;}&quot;]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<String> removeComments(String[] source) {
        List<String> ans = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        boolean blockComment = false;
        for (String s : source) {
            int m = s.length();
            for (int i = 0; i < m; ++i) {
                if (blockComment) {
                    if (i + 1 < m && s.charAt(i) == '*' && s.charAt(i + 1) == '/') {
                        blockComment = false;
                        ++i;
                    }
                } else {
                    if (i + 1 < m && s.charAt(i) == '/' && s.charAt(i + 1) == '*') {
                        blockComment = true;
                        ++i;
                    } else if (i + 1 < m && s.charAt(i) == '/' && s.charAt(i + 1) == '/') {
                        break;
                    } else {
                        sb.append(s.charAt(i));
                    }
                }
            }
            if (!blockComment && sb.length() > 0) {
                ans.add(sb.toString());
                sb.setLength(0);
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        ans = []
        t = []
        block_comment = False
        for s in source:
            i, m = 0, len(s)
            while i < m:
                if block_comment:
                    if i + 1 < m and s[i : i + 2] == "*/":
                        block_comment = False
                        i += 1
                else:
                    if i + 1 < m and s[i : i + 2] == "/*":
                        block_comment = True
                        i += 1
                    elif i + 1 < m and s[i : i + 2] == "//":
                        break
                    else:
                        t.append(s[i])
                i += 1
            if not block_comment and t:
                ans.append("".join(t))
                t.clear()
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
