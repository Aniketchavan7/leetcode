# 682. Baseball Game

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/baseball-game)
[![Topic: Stack & Array & Simulation](https://img.shields.io/badge/Topic-Stack%20&%20Array%20&%20Simulation-blue)](https://leetcode.com/problems/baseball-game)

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
**Sample Input**: `ops = [&quot;5&quot;,&quot;2&quot;,&quot;C&quot;,&quot;D&quot;,&quot;+&quot;]`  
**Expected Output**: `30`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `ops = [&quot;5&quot;,&quot;2&quot;,&quot;C&quot;,&quot;D&quot;,&quot;+&quot;]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `30` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int calPoints(String[] operations) {
        Deque<Integer> stk = new ArrayDeque<>();
        for (String op : operations) {
            if ("+".equals(op)) {
                int a = stk.pop();
                int b = stk.peek();
                stk.push(a);
                stk.push(a + b);
            } else if ("D".equals(op)) {
                stk.push(stk.peek() << 1);
            } else if ("C".equals(op)) {
                stk.pop();
            } else {
                stk.push(Integer.valueOf(op));
            }
        }
        return stk.stream().mapToInt(Integer::intValue).sum();
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stk = []
        for op in operations:
            if op == "+":
                stk.append(stk[-1] + stk[-2])
            elif op == "D":
                stk.append(stk[-1] << 1)
            elif op == "C":
                stk.pop()
            else:
                stk.append(int(op))
        return sum(stk)
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
