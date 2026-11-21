# 553. Optimal Division

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/optimal-division)
[![Topic: Array & Math & Dynamic Programming](https://img.shields.io/badge/Topic-Array%20&%20Math%20&%20Dynamic%20Programming-blue)](https://leetcode.com/problems/optimal-division)

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
**Sample Input**: `nums = [1000,100,10,2]`  
**Expected Output**: `&quot;1000/(100/10/2)&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [1000,100,10,2]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;1000/(100/10/2)&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String optimalDivision(int[] nums) {
        int n = nums.length;
        if (n == 1) {
            return nums[0] + "";
        }
        if (n == 2) {
            return nums[0] + "/" + nums[1];
        }
        StringBuilder ans = new StringBuilder(nums[0] + "/(");
        for (int i = 1; i < n - 1; ++i) {
            ans.append(nums[i] + "/");
        }
        ans.append(nums[n - 1] + ")");
        return ans.toString();
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def optimalDivision(self, nums: list[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f'{nums[0]}/{nums[1]}'
        return f'{nums[0]}/({"/".join(map(str, nums[1:]))})'
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
