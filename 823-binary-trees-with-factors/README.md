# 823. Binary Trees With Factors

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/binary-trees-with-factors)
[![Topic: Array & Hash Table & Dynamic Programming](https://img.shields.io/badge/Topic-Array%20&%20Hash%20Table%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/binary-trees-with-factors)

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
**Sample Input**: `arr = [2,4]`  
**Expected Output**: `3`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `arr = [2,4]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `3` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int numFactoredBinaryTrees(int[] arr) {
        final int mod = (int) 1e9 + 7;
        Arrays.sort(arr);
        int n = arr.length;
        long[] f = new long[n];
        Arrays.fill(f, 1);
        Map<Integer, Integer> idx = new HashMap<>(n);
        for (int i = 0; i < n; ++i) {
            idx.put(arr[i], i);
        }
        for (int i = 0; i < n; ++i) {
            int a = arr[i];
            for (int j = 0; j < i; ++j) {
                int b = arr[j];
                if (a % b == 0) {
                    int c = a / b;
                    if (idx.containsKey(c)) {
                        int k = idx.get(c);
                        f[i] = (f[i] + f[j] * f[k]) % mod;
                    }
                }
            }
        }
        long ans = 0;
        for (long v : f) {
            ans = (ans + v) % mod;
        }
        return (int) ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        arr.sort()
        idx = {v: i for i, v in enumerate(arr)}
        f = [1] * n
        for i, a in enumerate(arr):
            for j in range(i):
                b = arr[j]
                if a % b == 0 and (c := (a // b)) in idx:
                    f[i] = (f[i] + f[j] * f[idx[c]]) % mod
        return sum(f) % mod
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
