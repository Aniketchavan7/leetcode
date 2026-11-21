# 104. Maximum Depth of Binary Tree

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
[![Topic: Tree / DFS](https://img.shields.io/badge/Topic-Tree%20/%20DFS-blue)](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "The maximum depth of a binary tree is 1 plus the maximum depth of its left and right subtrees. If root is null, depth is 0. Otherwise, recursively return `1 + Math.max(maxDepth(root.left), maxDepth(root.right))`."

---

### 💡 Intuition & Core Insight
- **Bottom-Up Post-Order**: The depth of a subtree cannot be known until both child branches report their maximum depths.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `[3, 9, 20, null, null, 15, 7]`
- Left child 9 has children null -> maxDepth(9) = 1 + max(0, 0) = 1
- Right child 20 has children 15, 7 -> maxDepth(20) = 1 + max(1, 1) = 2
- Root 3 -> maxDepth(3) = 1 + max(1, 2) = 3.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Every node in the tree is visited once.
- **Space Complexity**: $\mathcal{O}(H)$ — Recursion call stack equals height H (O(log N) balanced, O(N) worst case).

---

### ⚠️ Edge Cases & Interview Traps
1. Null tree: returns 0.
2. Single node: returns 1.

---

### 💬 Follow-Up Questions You Might Get
- *Can we solve with BFS?* Yes, count the number of while-loop iterations in level-order traversal.
