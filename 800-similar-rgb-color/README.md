# 800. Similar RGB Color

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/similar-rgb-color)
[![Topic: Math & String & Enumeration](https://img.shields.io/badge/Topic-Math%20&%20String%20&%20Enumeration-blue)](https://leetcode.com/problems/similar-rgb-color)

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
**Sample Input**: `color = &quot;#09f166&quot;`  
**Expected Output**: `&quot;#11ee66&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `color = &quot;#09f166&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;#11ee66&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String similarRGB(String color) {
        String a = color.substring(1, 3), b = color.substring(3, 5), c = color.substring(5, 7);
        return "#" + f(a) + f(b) + f(c);
    }

    private String f(String x) {
        int q = Integer.parseInt(x, 16);
        q = q / 17 + (q % 17 > 8 ? 1 : 0);
        return String.format("%02x", 17 * q);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def similarRGB(self, color: str) -> str:
        def f(x):
            y, z = divmod(int(x, 16), 17)
            if z > 8:
                y += 1
            return '{:02x}'.format(17 * y)

        a, b, c = color[1:3], color[3:5], color[5:7]
        return f'#{f(a)}{f(b)}{f(c)}'
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
