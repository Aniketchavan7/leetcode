# 465. Optimal Account Balancing

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/optimal-account-balancing)
[![Topic: Bit Manipulation & Array & Dynamic Programming](https://img.shields.io/badge/Topic-Bit%20Manipulation%20&%20Array%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/optimal-account-balancing)

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
**Sample Input**: `transactions = [[0,1,10],[2,0,5]]`  
**Expected Output**: `2`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `transactions = [[0,1,10],[2,0,5]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `2` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int minTransfers(int[][] transactions) {
        int[] g = new int[12];
        for (var t : transactions) {
            g[t[0]] -= t[2];
            g[t[1]] += t[2];
        }
        List<Integer> nums = new ArrayList<>();
        for (int x : g) {
            if (x != 0) {
                nums.add(x);
            }
        }
        int m = nums.size();
        int[] f = new int[1 << m];
        Arrays.fill(f, 1 << 29);
        f[0] = 0;
        for (int i = 1; i < 1 << m; ++i) {
            int s = 0;
            for (int j = 0; j < m; ++j) {
                if ((i >> j & 1) == 1) {
                    s += nums.get(j);
                }
            }
            if (s == 0) {
                f[i] = Integer.bitCount(i) - 1;
                for (int j = (i - 1) & i; j > 0; j = (j - 1) & i) {
                    f[i] = Math.min(f[i], f[j] + f[i ^ j]);
                }
            }
        }
        return f[(1 << m) - 1];
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def minTransfers(self, transactions: list[list[int]]) -> int:
        g = defaultdict(int)
        for f, t, x in transactions:
            g[f] -= x
            g[t] += x
        nums = [x for x in g.values() if x]
        m = len(nums)
        f = [inf] * (1 << m)
        f[0] = 0
        for i in range(1, 1 << m):
            s = 0
            for j, x in enumerate(nums):
                if i >> j & 1:
                    s += x
            if s == 0:
                f[i] = i.bit_count() - 1
                j = (i - 1) & i
                while j > 0:
                    f[i] = min(f[i], f[j] + f[i ^ j])
                    j = (j - 1) & i
        return f[-1]
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
