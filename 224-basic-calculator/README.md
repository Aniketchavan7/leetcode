# 224. Basic Calculator

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/basic-calculator)
[![Topic: Stack & Recursion & Math](https://img.shields.io/badge/Topic-Stack%20&%20Recursion%20&%20Math-blue)](https://leetcode.com/problems/basic-calculator)

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
**Sample Input**: `s = &quot;1 + 1&quot;`  
**Expected Output**: `2`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s = &quot;1 + 1&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `2` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int calculate(String s) {
        Deque<Integer> stk = new ArrayDeque<>();
        int sign = 1;
        int ans = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                int j = i;
                int x = 0;
                while (j < n && Character.isDigit(s.charAt(j))) {
                    x = x * 10 + s.charAt(j) - '0';
                    j++;
                }
                ans += sign * x;
                i = j - 1;
            } else if (c == '+') {
                sign = 1;
            } else if (c == '-') {
                sign = -1;
            } else if (c == '(') {
                stk.push(ans);
                stk.push(sign);
                ans = 0;
                sign = 1;
            } else if (c == ')') {
                ans = stk.pop() * ans + stk.pop();
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        ans, sign = 0, 1
        i, n = 0, len(s)
        while i < n:
            if s[i].isdigit():
                x = 0
                j = i
                while j < n and s[j].isdigit():
                    x = x * 10 + int(s[j])
                    j += 1
                ans += sign * x
                i = j - 1
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                stk.append(ans)
                stk.append(sign)
                ans, sign = 0, 1
            elif s[i] == ")":
                ans = stk.pop() * ans + stk.pop()
            i += 1
        return ans
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
