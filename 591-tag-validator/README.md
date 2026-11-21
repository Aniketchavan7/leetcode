# 591. Tag Validator

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/tag-validator)
[![Topic: Stack & String](https://img.shields.io/badge/Topic-Stack%20&%20String-blue)](https://leetcode.com/problems/tag-validator)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We use a monotonic stack to maintain elements in sorted order. As we iterate through the input, elements that violate the monotonicity are popped, resolving next greater/smaller queries in linear time."

---

### 💡 Intuition & Core Insight
- **Monotonic Invariant**: Stack elements remain strictly increasing or decreasing.
- **One-Pass Resolution**: Each element is pushed and popped at most once, yielding amortized O(N) time.
- **Local vs Global Extremum**: Stack top immediately exposes the nearest boundary.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `code = &quot;&lt;DIV&gt;This is the first line &lt;![CDATA[&lt;div&gt;]]&gt;&lt;/DIV&gt;&quot;`  
**Expected Output**: `true`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `code = &quot;&lt;DIV&gt;This is the first line &lt;![CDATA[&lt;div&gt;]]&gt;&lt;/DIV&gt;&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `true` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean isValid(String code) {
        Deque<String> stk = new ArrayDeque<>();
        for (int i = 0; i < code.length(); ++i) {
            if (i > 0 && stk.isEmpty()) {
                return false;
            }
            if (code.startsWith("<![CDATA[", i)) {
                i = code.indexOf("]]>", i + 9);
                if (i < 0) {
                    return false;
                }
                i += 2;
            } else if (code.startsWith("</", i)) {
                int j = i + 2;
                i = code.indexOf(">", j);
                if (i < 0) {
                    return false;
                }
                String t = code.substring(j, i);
                if (!check(t) || stk.isEmpty() || !stk.pop().equals(t)) {
                    return false;
                }
            } else if (code.startsWith("<", i)) {
                int j = i + 1;
                i = code.indexOf(">", j);
                if (i < 0) {
                    return false;
                }
                String t = code.substring(j, i);
                if (!check(t)) {
                    return false;
                }
                stk.push(t);
            }
        }
        return stk.isEmpty();
    }

    private boolean check(String tag) {
        int n = tag.length();
        if (n < 1 || n > 9) {
            return false;
        }
        for (char c : tag.toCharArray()) {
            if (!Character.isUpperCase(c)) {
                return false;
            }
        }
        return true;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def isValid(self, code: str) -> bool:
        def check(tag):
            return 1 <= len(tag) <= 9 and all(c.isupper() for c in tag)

        stk = []
        i, n = 0, len(code)
        while i < n:
            if i and not stk:
                return False
            if code[i : i + 9] == '<![CDATA[':
                i = code.find(']]>', i + 9)
                if i < 0:
                    return False
                i += 2
            elif code[i : i + 2] == '</':
                j = i + 2
                i = code.find('>', j)
                if i < 0:
                    return False
                t = code[j:i]
                if not check(t) or not stk or stk.pop() != t:
                    return False
            elif code[i] == '<':
                j = i + 1
                i = code.find('>', j)
                if i < 0:
                    return False
                t = code[j:i]
                if not check(t):
                    return False
                stk.append(t)
            i += 1
        return not stk
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Empty stack pops.
2. Strict vs non-strict inequality when popping.
3. Elements remaining on the stack after array traversal ends.

---

### 💬 Follow-Up Questions You Might Get
*What if the array is circular?* Traverse the array twice (length 2N) using modulo indexing (i % N).
