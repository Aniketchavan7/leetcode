# 666. Path Sum IV

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/path-sum-iv)
[![Topic: Tree & Depth-First Search & Array](https://img.shields.io/badge/Topic-Tree%20&%20Depth-First%20Search%20&%20Array-blue)](https://leetcode.com/problems/path-sum-iv)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "For tree structures, we leverage recursive DFS or iterative BFS to traverse nodes. In **Path Sum IV**, processing each node once while maintaining tree invariants allows linear-time resolution."

---

### 💡 Intuition & Core Insight
- **Recursive Invariant**: At each subtree, we compute left and right subtree properties and aggregate the result.
- **Traversal Choice**: Pre-order / In-order / Post-order aligns naturally with tree height, sum, or path validation.
- **Stack Depth**: Auxiliary space is bounded by the height of the tree.

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
    private int ans;
    private Map<Integer, Integer> mp;

    public int pathSum(int[] nums) {
        ans = 0;
        mp = new HashMap<>(nums.length);
        for (int num : nums) {
            mp.put(num / 10, num % 10);
        }
        dfs(11, 0);
        return ans;
    }

    private void dfs(int node, int t) {
        if (!mp.containsKey(node)) {
            return;
        }
        t += mp.get(node);
        int d = node / 10, p = node % 10;
        int l = (d + 1) * 10 + (p * 2) - 1;
        int r = l + 1;
        if (!mp.containsKey(l) && !mp.containsKey(r)) {
            ans += t;
            return;
        }
        dfs(l, t);
        dfs(r, t);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def pathSum(self, nums: list[int]) -> int:
        def dfs(node, t):
            if node not in mp:
                return
            t += mp[node]
            d, p = divmod(node, 10)
            l = (d + 1) * 10 + (p * 2) - 1
            r = l + 1
            nonlocal ans
            if l not in mp and r not in mp:
                ans += t
                return
            dfs(l, t)
            dfs(r, t)

        ans = 0
        mp = {num // 10: num % 10 for num in nums}
        dfs(11, 0)
        return ans
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(H)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Skewed trees where height H = N leading to recursion stack overflow.
2. Single-node trees or empty tree roots (root == null).
3. Handling leaf nodes vs single-child nodes.

---

### 💬 Follow-Up Questions You Might Get
*Can we do this in O(1) space?* Morris Traversal can achieve O(1) extra space by threading binary trees.
