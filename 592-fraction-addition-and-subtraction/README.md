# 592. Fraction Addition and Subtraction

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/fraction-addition-and-subtraction)
[![Topic: Math & String & Greatest Common Divisor](https://img.shields.io/badge/Topic-Math%20&%20String%20&%20Greatest%20Common%20Divisor-blue)](https://leetcode.com/problems/fraction-addition-and-subtraction)

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
**Sample Input**: `expression = &quot;-1/2+1/2&quot;`  
**Expected Output**: `&quot;0/1&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `expression = &quot;-1/2+1/2&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;0/1&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String fractionAddition(String expression) {
        int x = 0, y = 6 * 7 * 8 * 9 * 10;
        if (Character.isDigit(expression.charAt(0))) {
            expression = "+" + expression;
        }
        int i = 0, n = expression.length();
        while (i < n) {
            int sign = expression.charAt(i) == '-' ? -1 : 1;
            ++i;
            int j = i;
            while (j < n && expression.charAt(j) != '+' && expression.charAt(j) != '-') {
                ++j;
            }
            String s = expression.substring(i, j);
            String[] t = s.split("/");
            int a = Integer.parseInt(t[0]), b = Integer.parseInt(t[1]);
            x += sign * a * y / b;
            i = j;
        }
        int z = gcd(Math.abs(x), y);
        x /= z;
        y /= z;
        return x + "/" + y;
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def fractionAddition(self, expression: str) -> str:
        x, y = 0, 6 * 7 * 8 * 9 * 10
        if expression[0].isdigit():
            expression = '+' + expression
        i, n = 0, len(expression)
        while i < n:
            sign = -1 if expression[i] == '-' else 1
            i += 1
            j = i
            while j < n and expression[j] not in '+-':
                j += 1
            s = expression[i:j]
            a, b = s.split('/')
            x += sign * int(a) * y // int(b)
            i = j
        z = gcd(x, y)
        x //= z
        y //= z
        return f'{x}/{y}'
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
