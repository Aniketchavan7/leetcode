# 736. Parse Lisp Expression

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/parse-lisp-expression)
[![Topic: Stack & Recursion & Hash Table](https://img.shields.io/badge/Topic-Stack%20&%20Recursion%20&%20Hash%20Table-blue)](https://leetcode.com/problems/parse-lisp-expression)

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
**Sample Input**: `expression = &quot;(let x 2 (mult x (let x 3 y 4 (add x y))))&quot;`  
**Expected Output**: `14`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `expression = &quot;(let x 2 (mult x (let x 3 y 4 (add x y))))&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `14` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int i;
    private String expr;
    private Map<String, Deque<Integer>> scope = new HashMap<>();

    public int evaluate(String expression) {
        expr = expression;
        return eval();
    }

    private int eval() {
        char c = expr.charAt(i);
        if (c != '(') {
            return Character.isLowerCase(c) ? scope.get(parseVar()).peekLast() : parseInt();
        }
        ++i;
        c = expr.charAt(i);
        int ans = 0;
        if (c == 'l') {
            i += 4;
            List<String> vars = new ArrayList<>();
            while (true) {
                String var = parseVar();
                if (expr.charAt(i) == ')') {
                    ans = scope.get(var).peekLast();
                    break;
                }
                vars.add(var);
                ++i;
                scope.computeIfAbsent(var, k -> new ArrayDeque<>()).offer(eval());
                ++i;
                if (!Character.isLowerCase(expr.charAt(i))) {
                    ans = eval();
                    break;
                }
            }
            for (String v : vars) {
                scope.get(v).pollLast();
            }
        } else {
            boolean add = c == 'a';
            i += add ? 4 : 5;
            int a = eval();
            ++i;
            int b = eval();
            ans = add ? a + b : a * b;
        }
        ++i;
        return ans;
    }

    private String parseVar() {
        int j = i;
        while (i < expr.length() && expr.charAt(i) != ' ' && expr.charAt(i) != ')') {
            ++i;
        }
        return expr.substring(j, i);
    }

    private int parseInt() {
        int sign = 1;
        if (expr.charAt(i) == '-') {
            sign = -1;
            ++i;
        }
        int v = 0;
        while (i < expr.length() && Character.isDigit(expr.charAt(i))) {
            v = v * 10 + (expr.charAt(i) - '0');
            ++i;
        }
        return sign * v;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def evaluate(self, expression: str) -> int:
        def parseVar():
            nonlocal i
            j = i
            while i < n and expression[i] not in " )":
                i += 1
            return expression[j:i]

        def parseInt():
            nonlocal i
            sign, v = 1, 0
            if expression[i] == "-":
                sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                v = v * 10 + int(expression[i])
                i += 1
            return sign * v

        def eval():
            nonlocal i
            if expression[i] != "(":
                return scope[parseVar()][-1] if expression[i].islower() else parseInt()
            i += 1
            if expression[i] == "l":
                i += 4
                vars = []
                while 1:
                    var = parseVar()
                    if expression[i] == ")":
                        ans = scope[var][-1]
                        break
                    vars.append(var)
                    i += 1
                    scope[var].append(eval())
                    i += 1
                    if not expression[i].islower():
                        ans = eval()
                        break
                for v in vars:
                    scope[v].pop()
            else:
                add = expression[i] == "a"
                i += 4 if add else 5
                a = eval()
                i += 1
                b = eval()
                ans = a + b if add else a * b
            i += 1
            return ans

        i, n = 0, len(expression)
        scope = defaultdict(list)
        return eval()
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
