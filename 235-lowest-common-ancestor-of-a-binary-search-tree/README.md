# 235. Lowest Common Ancestor of a Binary Search Tree

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
[![Topic: Tree / BST](https://img.shields.io/badge/Topic-Tree%20/%20BST-blue)](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "In a BST, values are partitioned around each node. Starting from root: 1) If both p and q have values strictly less than root.val, the LCA must lie in the left subtree. 2) If both p and q have values strictly greater than root.val, the LCA must lie in the right subtree. 3) The moment p and q split (one is less, one is greater, or root equals p or q), root is the Lowest Common Ancestor."

---

### 💡 Intuition & Core Insight
- **The Fork Point**: As long as both target nodes are on the same side, a deeper common ancestor exists. The first node where their paths diverge is their LCA.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `root = [6, 2, 8, 0, 4, 7, 9]`, `p = 2`, `q = 8`
- Root=6: p.val (2) < 6 and q.val (8) > 6 -> Path splits! Root 6 is LCA.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode curr = root;
        while (curr != null) {
            if (p.val < curr.val && q.val < curr.val) {
                curr = curr.left;
            } else if (p.val > curr.val && q.val > curr.val) {
                curr = curr.right;
            } else {
                return curr; // Split point or match
            }
        }
        return null;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
        return None
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(H)$ — Follows a single path from root down to LCA of length at most tree height H.
- **Space Complexity**: $\mathcal{O}(1)$ — Iterative traversal using O(1) pointers.

---

### ⚠️ Edge Cases & Interview Traps
1. One node is ancestor of the other (e.g. p is ancestor of q): loop terminates when curr == p, returning p.
2. Root is LCA: returns on first check.

---

### 💬 Follow-Up Questions You Might Get
- *What if the tree is a generic Binary Tree (not a BST)?* Use post-order DFS checking if left and right subtrees return non-null (LeetCode 236).
