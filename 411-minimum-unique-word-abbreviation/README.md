# 411. Minimum Unique Word Abbreviation

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/minimum-unique-word-abbreviation)
[![Topic: Bit Manipulation & Array & String](https://img.shields.io/badge/Topic-Bit%20Manipulation%20&%20Array%20&%20String-blue)](https://leetcode.com/problems/minimum-unique-word-abbreviation)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We frame the problem as exploring a state-space decision tree. At each step, we make a choice, recurse, and then undo the choice (backtrack) while pruning invalid paths early."

---

### 💡 Intuition & Core Insight
- **Pruning Optimization**: Pruning dead ends prevents traversing deep subtrees that violate constraints.
- **State Restoration**: Symmetrically appending and removing choices preserves state across recursion frames.
- **Deduplication**: Sorting inputs initially enables skipping duplicate branches with `if (i > start && nums[i] == nums[i-1]) continue`.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `target = &quot;apple&quot;, dictionary = [&quot;blade&quot;]`  
**Expected Output**: `&quot;a4&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `target = &quot;apple&quot;, dictionary = [&quot;blade&quot;]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;a4&quot;` |

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
- **Time Complexity**: $\mathcal{O}(2^N \text{ or } N!)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Failing to create a deep copy of the current state before adding to results.
2. Infinite recursion due to incorrect base case condition.
3. Duplicate combinations generated from identical elements.

---

### 💬 Follow-Up Questions You Might Get
*How can we optimize memory overhead?* Use bitmasks instead of boolean arrays to track used elements.
