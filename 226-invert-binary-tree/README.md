# 226. Invert Binary Tree

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/invert-binary-tree/)
[![Topic: Tree / Recursion](https://img.shields.io/badge/Topic-Tree%20/%20Recursion-blue)](https://leetcode.com/problems/invert-binary-tree/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To invert a binary tree into its mirror image: if root is null, return null. Swap root.left and root.right, then recursively invert the left and right subtrees."

---

### 💡 Intuition & Core Insight
- **Mirror Property**: Inverting a tree means reflecting it across the vertical axis. Every node swaps its two children.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `[4, 2, 7, 1, 3, 6, 9]`
- Root 4: swap 2 and 7 -> left becomes 7, right becomes 2
- Invert 7: swap 6 and 9 -> left 9, right 6
- Invert 2: swap 1 and 3 -> left 3, right 1
Result: `[4, 7, 2, 9, 6, 3, 1]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        TreeNode tmp = root.left;
        root.left = invertTree(root.right);
        root.right = invertTree(tmp);
        return root;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Visits every node in the tree once.
- **Space Complexity**: $\mathcal{O}(H)$ — Recursion call stack equals height H.

---

### ⚠️ Edge Cases & Interview Traps
1. Null tree: returns null.
2. Leaf node: children null swap to null, returns node.

---

### 💬 Follow-Up Questions You Might Get
- *Can this be done iteratively?* Yes, using a Queue or Stack popping nodes and swapping left/right.
