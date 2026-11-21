# 791. Custom Sort String

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/custom-sort-string)
[![Topic: Hash Table & String & Sorting](https://img.shields.io/badge/Topic-Hash%20Table%20&%20String%20&%20Sorting-blue)](https://leetcode.com/problems/custom-sort-string)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Hash Table strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `Standard sample testcase`  
**Expected Output**: `Computed result`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `Input elements` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `Optimal Result` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String customSortString(String order, String s) {
        int[] d = new int[26];
        for (int i = 0; i < order.length(); ++i) {
            d[order.charAt(i) - 'a'] = i;
        }
        List<Character> cs = new ArrayList<>();
        for (int i = 0; i < s.length(); ++i) {
            cs.add(s.charAt(i));
        }
        cs.sort((a, b) -> d[a - 'a'] - d[b - 'a']);
        return cs.stream().map(String::valueOf).collect(Collectors.joining());
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: d.get(x, 0)))
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
