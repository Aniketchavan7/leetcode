# 415. Add Strings

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/add-strings)
[![Topic: Math & String & Simulation](https://img.shields.io/badge/Topic-Math%20&%20String%20&%20Simulation-blue)](https://leetcode.com/problems/add-strings)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Math strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `num1 = &quot;11&quot;, num2 = &quot;123&quot;`  
**Expected Output**: `&quot;134&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `num1 = &quot;11&quot;, num2 = &quot;123&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;134&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String addStrings(String num1, String num2) {
        int i = num1.length() - 1, j = num2.length() - 1;
        StringBuilder ans = new StringBuilder();
        for (int c = 0; i >= 0 || j >= 0 || c > 0; --i, --j) {
            int a = i < 0 ? 0 : num1.charAt(i) - '0';
            int b = j < 0 ? 0 : num2.charAt(j) - '0';
            c += a + b;
            ans.append(c % 10);
            c /= 10;
        }
        return ans.reverse().toString();
    }

    public String subStrings(String num1, String num2) {
        int m = num1.length(), n = num2.length();
        boolean neg = m < n || (m == n && num1.compareTo(num2) < 0);
        if (neg) {
            String t = num1;
            num1 = num2;
            num2 = t;
        }
        int i = num1.length() - 1, j = num2.length() - 1;
        StringBuilder ans = new StringBuilder();
        for (int c = 0; i >= 0; --i, --j) {
            c = (num1.charAt(i) - '0') - c - (j < 0 ? 0 : num2.charAt(j) - '0');
            ans.append((c + 10) % 10);
            c = c < 0 ? 1 : 0;
        }
        while (ans.length() > 1 && ans.charAt(ans.length() - 1) == '0') {
            ans.deleteCharAt(ans.length() - 1);
        }
        if (neg) {
            ans.append('-');
        }
        return ans.reverse().toString();
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        ans = []
        c = 0
        while i >= 0 or j >= 0 or c:
            a = 0 if i < 0 else int(num1[i])
            b = 0 if j < 0 else int(num2[j])
            c, v = divmod(a + b + c, 10)
            ans.append(str(v))
            i, j = i - 1, j - 1
        return "".join(ans[::-1])

    def subStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        neg = m < n or (m == n and num1 < num2)
        if neg:
            num1, num2 = num2, num1
        i, j = len(num1) - 1, len(num2) - 1
        ans = []
        c = 0
        while i >= 0:
            c = int(num1[i]) - c - (0 if j < 0 else int(num2[j]))
            ans.append(str((c + 10) % 10))
            c = 1 if c < 0 else 0
            i, j = i - 1, j - 1
        while len(ans) > 1 and ans[-1] == '0':
            ans.pop()
        if neg:
            ans.append('-')
        return ''.join(ans[::-1])
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
