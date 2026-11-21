# 638. Shopping Offers

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/shopping-offers)
[![Topic: Bit Manipulation & Memoization & Array](https://img.shields.io/badge/Topic-Bit%20Manipulation%20&%20Memoization%20&%20Array-blue)](https://leetcode.com/problems/shopping-offers)

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
**Sample Input**: `price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]`  
**Expected Output**: `14`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `14` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private final int bits = 4;
    private int n;
    private List<Integer> price;
    private List<List<Integer>> special;
    private Map<Integer, Integer> f = new HashMap<>();

    public int shoppingOffers(
        List<Integer> price, List<List<Integer>> special, List<Integer> needs) {
        n = needs.size();
        this.price = price;
        this.special = special;
        int mask = 0;
        for (int i = 0; i < n; ++i) {
            mask |= needs.get(i) << (i * bits);
        }
        return dfs(mask);
    }

    private int dfs(int cur) {
        if (f.containsKey(cur)) {
            return f.get(cur);
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += price.get(i) * (cur >> (i * bits) & 0xf);
        }
        for (List<Integer> offer : special) {
            int nxt = cur;
            boolean ok = true;
            for (int j = 0; j < n; ++j) {
                if ((cur >> (j * bits) & 0xf) < offer.get(j)) {
                    ok = false;
                    break;
                }
                nxt -= offer.get(j) << (j * bits);
            }
            if (ok) {
                ans = Math.min(ans, offer.get(n) + dfs(nxt));
            }
        }
        f.put(cur, ans);
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def shoppingOffers(
        self, price: list[int], special: list[list[int]], needs: list[int]
    ) -> int:
        @cache
        def dfs(cur: int) -> int:
            ans = sum(p * (cur >> (i * bits) & 0xF) for i, p in enumerate(price))
            for offer in special:
                nxt = cur
                for j in range(len(needs)):
                    if (cur >> (j * bits) & 0xF) < offer[j]:
                        break
                    nxt -= offer[j] << (j * bits)
                else:
                    ans = min(ans, offer[-1] + dfs(nxt))
            return ans

        bits, mask = 4, 0
        for i, need in enumerate(needs):
            mask |= need << i * bits
        return dfs(mask)
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
