# 119. Pascal's Triangle II

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/pascals-triangle-ii)
[![Topic: Array & Dynamic Programming](https://img.shields.io/badge/Topic-Array%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/pascals-triangle-ii)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "In this problem, subproblems overlap and possess optimal substructure. Instead of an exponential recursive tree, we define a memoized state array where dp[i] captures the optimal decision up to index i, transitioning in polynomial time."

---

### 💡 Intuition & Core Insight
- **Brute Force Bottleneck**: Exploring all state combinations yields exponential O(2^N) or O(N!) complexity.
- **Optimal Substructure**: The optimal solution at state i depends strictly on already computed sub-states.
- **State Invariant**: Maintaining optimal transitions avoids re-evaluating subproblems.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `rowIndex = 3`  
**Expected Output**: `[1,3,3,1]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `rowIndex = 3` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[1,3,3,1]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> f = new ArrayList<>();
        for (int i = 0; i < rowIndex + 1; ++i) {
            f.add(1);
        }
        for (int i = 2; i < rowIndex + 1; ++i) {
            for (int j = i - 1; j > 0; --j) {
                f.set(j, f.get(j) + f.get(j - 1));
            }
        }
        return f;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        f = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                f[j] += f[j - 1]
        return f
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Boundary states at index 0 and 1.
2. Integer overflow when accumulating large transitions.
3. Base case initialization of unreachable states.

---

### 💬 Follow-Up Questions You Might Get
*Can we optimize space?* Yes, if each state depends only on the previous k states, we can reduce space from O(N) to O(1) using rolling variables.
