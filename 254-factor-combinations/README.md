# 254. Factor Combinations

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/factor-combinations)
[![Topic: Backtracking & Prime Factorization](https://img.shields.io/badge/Topic-Backtracking%20&%20Prime%20Factorization-blue)](https://leetcode.com/problems/factor-combinations)

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
**Sample Input**: `n = 1`  
**Expected Output**: `[]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `n = 1` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private List<Integer> t = new ArrayList<>();
    private List<List<Integer>> ans = new ArrayList<>();

    public List<List<Integer>> getFactors(int n) {
        dfs(n, 2);
        return ans;
    }

    private void dfs(int n, int i) {
        if (!t.isEmpty()) {
            List<Integer> cp = new ArrayList<>(t);
            cp.add(n);
            ans.add(cp);
        }
        for (int j = i; j <= n / j; ++j) {
            if (n % j == 0) {
                t.add(j);
                dfs(n / j, j);
                t.remove(t.size() - 1);
            }
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def getFactors(self, n: int) -> list[list[int]]:
        def dfs(n, i):
            if t:
                ans.append(t + [n])
            j = i
            while j * j <= n:
                if n % j == 0:
                    t.append(j)
                    dfs(n // j, j)
                    t.pop()
                j += 1

        t = []
        ans = []
        dfs(n, 2)
        return ans
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
