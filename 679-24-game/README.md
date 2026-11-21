# 679. 24 Game

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/24-game)
[![Topic: Array & Math & Backtracking](https://img.shields.io/badge/Topic-Array%20&%20Math%20&%20Backtracking-blue)](https://leetcode.com/problems/24-game)

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
**Sample Input**: `cards = [4,1,8,7]`  
**Expected Output**: `true`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `cards = [4,1,8,7]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `true` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private final char[] ops = {'+', '-', '*', '/'};

    public boolean judgePoint24(int[] cards) {
        List<Double> nums = new ArrayList<>();
        for (int num : cards) {
            nums.add((double) num);
        }
        return dfs(nums);
    }

    private boolean dfs(List<Double> nums) {
        int n = nums.size();
        if (n == 1) {
            return Math.abs(nums.get(0) - 24) < 1e-6;
        }
        boolean ok = false;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i != j) {
                    List<Double> nxt = new ArrayList<>();
                    for (int k = 0; k < n; ++k) {
                        if (k != i && k != j) {
                            nxt.add(nums.get(k));
                        }
                    }
                    for (char op : ops) {
                        switch (op) {
                            case '/' -> {
                                if (nums.get(j) == 0) {
                                    continue;
                                }
                                nxt.add(nums.get(i) / nums.get(j));
                            }
                            case '*' -> {
                                nxt.add(nums.get(i) * nums.get(j));
                            }
                            case '+' -> {
                                nxt.add(nums.get(i) + nums.get(j));
                            }
                            case '-' -> {
                                nxt.add(nums.get(i) - nums.get(j));
                            }
                        }
                        ok |= dfs(nxt);
                        if (ok) {
                            return true;
                        }
                        nxt.remove(nxt.size() - 1);
                    }
                }
            }
        }
        return ok;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        def dfs(nums: list[float]):
            n = len(nums)
            if n == 1:
                if abs(nums[0] - 24) < 1e-6:
                    return True
                return False
            ok = False
            for i in range(n):
                for j in range(n):
                    if i != j:
                        nxt = [nums[k] for k in range(n) if k != i and k != j]
                        for op in ops:
                            match op:
                                case "/":
                                    if nums[j] == 0:
                                        continue
                                    ok |= dfs(nxt + [nums[i] / nums[j]])
                                case "*":
                                    ok |= dfs(nxt + [nums[i] * nums[j]])
                                case "+":
                                    ok |= dfs(nxt + [nums[i] + nums[j]])
                                case "-":
                                    ok |= dfs(nxt + [nums[i] - nums[j]])
                            if ok:
                                return True
            return ok

        ops = ("+", "-", "*", "/")
        nums = [float(x) for x in cards]
        return dfs(nums)
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
