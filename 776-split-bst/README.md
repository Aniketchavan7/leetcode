# 776. Split BST

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/split-bst)
[![Topic: Tree & Binary Search Tree & Recursion](https://img.shields.io/badge/Topic-Tree%20&%20Binary%20Search%20Tree%20&%20Recursion-blue)](https://leetcode.com/problems/split-bst)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "For tree structures, we leverage recursive DFS or iterative BFS to traverse nodes. In **Split BST**, processing each node once while maintaining tree invariants allows linear-time resolution."

---

### 💡 Intuition & Core Insight
- **Recursive Invariant**: At each subtree, we compute left and right subtree properties and aggregate the result.
- **Traversal Choice**: Pre-order / In-order / Post-order aligns naturally with tree height, sum, or path validation.
- **Stack Depth**: Auxiliary space is bounded by the height of the tree.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `root = [4,2,6,1,3,5,7], target = 2`  
**Expected Output**: `[[2,1],[4,3,6,null,null,5,7]]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `root = [4,2,6,1,3,5,7], target = 2` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[[2,1],[4,3,6,null,null,5,7]]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int t;

    public TreeNode[] splitBST(TreeNode root, int target) {
        t = target;
        return dfs(root);
    }

    private TreeNode[] dfs(TreeNode root) {
        if (root == null) {
            return new TreeNode[] {null, null};
        }
        if (root.val <= t) {
            TreeNode[] ans = dfs(root.right);
            root.right = ans[0];
            ans[0] = root;
            return ans;
        } else {
            TreeNode[] ans = dfs(root.left);
            root.left = ans[1];
            ans[1] = root;
            return ans;
        }
    }
}
```

#### Python 3 Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(
        self, root: Optional[TreeNode], target: int
    ) -> list[Optional[TreeNode]]:
        def dfs(root):
            if root is None:
                return [None, None]
            if root.val <= target:
                l, r = dfs(root.right)
                root.right = l
                return [root, r]
            else:
                l, r = dfs(root.left)
                root.left = r
                return [l, root]

        return dfs(root)
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
