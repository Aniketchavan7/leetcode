# 402. Remove K Digits

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/remove-k-digits)
[![Topic: Stack & Greedy & String](https://img.shields.io/badge/Topic-Stack%20&%20Greedy%20&%20String-blue)](https://leetcode.com/problems/remove-k-digits)

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
**Sample Input**: `num = &quot;1432219&quot;, k = 3`  
**Expected Output**: `&quot;1219&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `num = &quot;1432219&quot;, k = 3` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;1219&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String removeKdigits(String num, int k) {
        StringBuilder stk = new StringBuilder();
        for (char c : num.toCharArray()) {
            while (k > 0 && stk.length() > 0 && stk.charAt(stk.length() - 1) > c) {
                stk.deleteCharAt(stk.length() - 1);
                --k;
            }
            stk.append(c);
        }
        for (; k > 0; --k) {
            stk.deleteCharAt(stk.length() - 1);
        }
        int i = 0;
        for (; i < stk.length() && stk.charAt(i) == '0'; ++i) {
        }
        String ans = stk.substring(i);
        return "".equals(ans) ? "0" : ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        remain = len(num) - k
        for c in num:
            while k and stk and stk[-1] > c:
                stk.pop()
                k -= 1
            stk.append(c)
        return ''.join(stk[:remain]).lstrip('0') or '0'
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
