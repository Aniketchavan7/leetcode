# 726. Number of Atoms

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/number-of-atoms)
[![Topic: Stack & Hash Table & String](https://img.shields.io/badge/Topic-Stack%20&%20Hash%20Table%20&%20String-blue)](https://leetcode.com/problems/number-of-atoms)

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
**Sample Input**: `formula = &quot;H2O&quot;`  
**Expected Output**: `&quot;H2O&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `formula = &quot;H2O&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;H2O&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String countOfAtoms(String formula) {
        Map<String, Integer> map = new HashMap<>();
        int[] stack = new int[1000];
        int top = 0, multiplier = 1, freq = 0;
        char[] c = formula.toCharArray();
        for (int i = c.length - 1; i >= 0; i--) {
            if (c[i] >= 'a' && c[i] <= 'z') {
                int end = i--;
                while (i >= 0 && c[i] >= 'a' && c[i] <= 'z') i--;
                String key = new String(c, i, end - i + 1);
                map.put(key, map.getOrDefault(key, 0) + Math.max(freq, 1) * multiplier);
                freq = 0;
            } else if (c[i] >= 'A' && c[i] <= 'Z') {
                String key = new String(c, i, 1);
                map.put(key, map.getOrDefault(key, 0) + Math.max(freq, 1) * multiplier);
                freq = 0;
            } else if (c[i] >= '0' && c[i] <= '9') {
                freq = c[i] - '0';
                int p = 10;
                while (i - 1 >= 0 && c[i - 1] >= '0' && c[i - 1] <= '9') {
                    freq += p * (c[--i] - '0');
                    p *= 10;
                }
            } else if (c[i] == ')') {
                stack[top++] = multiplier;
                multiplier *= Math.max(freq, 1);
                freq = 0;
            } else {
                multiplier = stack[--top];
            }
        }
        List<String> keys = new ArrayList<>(map.keySet());
        Collections.sort(keys);
        StringBuilder sb = new StringBuilder();
        for (String key : keys) {
            sb.append(key);
            int f = map.get(key);
            if (f > 1) sb.append(f);
        }
        return sb.toString();
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        cnt = defaultdict(int)
        stack = []
        multiplier, freq = 1, 0
        i = len(formula) - 1
        while i >= 0:
            c = formula[i]
            if c.islower():
                end = i
                i -= 1
                while i >= 0 and formula[i].islower():
                    i -= 1
                cnt[formula[i : end + 1]] += max(freq, 1) * multiplier
                freq = 0
            elif c.isupper():
                cnt[c] += max(freq, 1) * multiplier
                freq = 0
            elif c.isdigit():
                freq = ord(c) - 48
                p = 10
                while i - 1 >= 0 and formula[i - 1].isdigit():
                    i -= 1
                    freq += p * (ord(formula[i]) - 48)
                    p *= 10
            elif c == ')':
                stack.append(multiplier)
                multiplier *= max(freq, 1)
                freq = 0
            else:
                multiplier = stack.pop()
            i -= 1
        ans = []
        for key in sorted(cnt):
            ans.append(key)
            if cnt[key] > 1:
                ans.append(str(cnt[key]))
        return ''.join(ans)
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
