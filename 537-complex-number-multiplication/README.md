# 537. Complex Number Multiplication

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/complex-number-multiplication)
[![Topic: Math & String & Simulation](https://img.shields.io/badge/Topic-Math%20&%20String%20&%20Simulation-blue)](https://leetcode.com/problems/complex-number-multiplication)

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
**Sample Input**: `num1 = &quot;1+1i&quot;, num2 = &quot;1+1i&quot;`  
**Expected Output**: `&quot;0+2i&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `num1 = &quot;1+1i&quot;, num2 = &quot;1+1i&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;0+2i&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        int[] x = parse(num1);
        int[] y = parse(num2);
        int a1 = x[0], b1 = x[1], a2 = y[0], b2 = y[1];
        return (a1 * a2 - b1 * b2) + "+" + (a1 * b2 + a2 * b1) + "i";
    }

    private int[] parse(String s) {
        var cs = s.substring(0, s.length() - 1).split("\\+");
        return new int[] {Integer.parseInt(cs[0]), Integer.parseInt(cs[1])};
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1, b1 = map(int, num1[:-1].split("+"))
        a2, b2 = map(int, num2[:-1].split("+"))
        return f"{a1 * a2 - b1 * b2}+{a1 * b2 + a2 * b1}i"
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
