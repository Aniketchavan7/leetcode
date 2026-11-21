# 770. Basic Calculator IV

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/basic-calculator-iv)
[![Topic: Stack & Recursion & Hash Table](https://img.shields.io/badge/Topic-Stack%20&%20Recursion%20&%20Hash%20Table-blue)](https://leetcode.com/problems/basic-calculator-iv)

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
**Sample Input**: `expression = &quot;e + 8 - a + 5&quot;, evalvars = [&quot;e&quot;], evalints = [1]`  
**Expected Output**: `[&quot;-1*a&quot;,&quot;14&quot;]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `expression = &quot;e + 8 - a + 5&quot;, evalvars = [&quot;e&quot;], evalints = [1]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[&quot;-1*a&quot;,&quot;14&quot;]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
// Implementation provided in Solution.java
```

#### Python 3 Solution
```python
# Implementation provided in solution.py
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
