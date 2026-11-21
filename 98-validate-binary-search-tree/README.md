# 98. Validate Binary Search Tree

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/validate-binary-search-tree/)
[![Topic: Tree / BST](https://img.shields.io/badge/Topic-Tree%20/%20BST-blue)](https://leetcode.com/problems/validate-binary-search-tree/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "A Binary Search Tree requires that every node in a left subtree is strictly less than the root, and every node in a right subtree is strictly greater. We validate this using recursive DFS by passing valid range boundaries `(minAllowed, maxAllowed)`. When traversing left, update maxAllowed = node.val; when traversing right, update minAllowed = node.val. Alternatively, an In-Order traversal of a BST must yield strictly monotonically increasing values."

---

### 💡 Intuition & Core Insight
- **Local vs Global Invariant**: Checking only `left.val < root.val < right.val` is insufficient! A node in root's right subtree must also be greater than root's ancestor. Range constraints carry down the entire tree hierarchy.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `[5, 1, 4, null, null, 3, 6]`
- Root 5: valid range (-inf, +inf)
- Left child 1: valid range (-inf, 5) -> 1 is valid
- Right child 4: valid range (5, +inf) -> 4 < 5! Fails range check -> False!

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return validate(root, null, null);
    }

    private boolean validate(TreeNode node, Integer min, Integer max) {
        if (node == null) return true;
        if ((min != null && node.val <= min) || (max != null && node.val >= max)) {
            return false;
        }
        return validate(node.left, min, node.val) && validate(node.right, node.val, max);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True
            if (min_val is not None and node.val <= min_val) or (max_val is not None and node.val >= max_val):
                return False
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        return validate(root, None, None)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Visits each node in the tree of size N once.
- **Space Complexity**: $\mathcal{O}(H)$ — Recursion stack proportional to tree height H (O(log N) balanced, O(N) worst-case skewed).

---

### ⚠️ Edge Cases & Interview Traps
1. Integer.MIN_VALUE or Integer.MAX_VALUE values in nodes: using Integer object or Long avoids overflow.
2. Single-node tree: returns true.

---

### 💬 Follow-Up Questions You Might Get
- *Can this be done iteratively?* In-order traversal using an explicit stack comparing each popped node with prev.
