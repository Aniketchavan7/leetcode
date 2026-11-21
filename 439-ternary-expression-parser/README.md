# 439. Ternary Expression Parser

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/ternary-expression-parser)
[![Topic: Stack & Recursion & String](https://img.shields.io/badge/Topic-Stack%20&%20Recursion%20&%20String-blue)](https://leetcode.com/problems/ternary-expression-parser)

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
**Sample Input**: `expression = &quot;T?2:3&quot;`  
**Expected Output**: `&quot;2&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `expression = &quot;T?2:3&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;2&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String parseTernary(String expression) {
        Deque<Character> stk = new ArrayDeque<>();
        boolean cond = false;
        for (int i = expression.length() - 1; i >= 0; --i) {
            char c = expression.charAt(i);
            if (c == ':') {
                continue;
            }
            if (c == '?') {
                cond = true;
            } else {
                if (cond) {
                    if (c == 'T') {
                        char x = stk.pop();
                        stk.pop();
                        stk.push(x);
                    } else {
                        stk.pop();
                    }
                    cond = false;
                } else {
                    stk.push(c);
                }
            }
        }
        return String.valueOf(stk.peek());
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def parseTernary(self, expression: str) -> str:
        stk = []
        cond = False
        for c in expression[::-1]:
            if c == ':':
                continue
            if c == '?':
                cond = True
            else:
                if cond:
                    if c == 'T':
                        x = stk.pop()
                        stk.pop()
                        stk.append(x)
                    else:
                        stk.pop()
                    cond = False
                else:
                    stk.append(c)
        return stk[0]
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
