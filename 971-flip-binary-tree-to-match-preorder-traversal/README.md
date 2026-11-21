# 971. Flip Binary Tree To Match Preorder Traversal

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal)
[![Topic: Tree & Depth-First Search & Binary Tree](https://img.shields.io/badge/Topic-Tree%20&%20Depth-First%20Search%20&%20Binary%20Tree-blue)](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "For tree structures, we leverage recursive DFS or iterative BFS to traverse nodes. In **Flip Binary Tree To Match Preorder Traversal**, processing each node once while maintaining tree invariants allows linear-time resolution."

---

### 💡 Intuition & Core Insight
- **Recursive Invariant**: At each subtree, we compute left and right subtree properties and aggregate the result.
- **Traversal Choice**: Pre-order / In-order / Post-order aligns naturally with tree height, sum, or path validation.
- **Stack Depth**: Auxiliary space is bounded by the height of the tree.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `root = [1,2], voyage = [2,1]`  
**Expected Output**: `[-1]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `root = [1,2], voyage = [2,1]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[-1]` |

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
    private int i;
    private boolean ok;
    private int[] voyage;
    private List<Integer> ans = new ArrayList<>();

    public List<Integer> flipMatchVoyage(TreeNode root, int[] voyage) {
        this.voyage = voyage;
        ok = true;
        dfs(root);
        return ok ? ans : List.of(-1);
    }

    private void dfs(TreeNode root) {
        if (root == null || !ok) {
            return;
        }
        if (root.val != voyage[i]) {
            ok = false;
            return;
        }
        ++i;
        if (root.left == null || root.left.val == voyage[i]) {
            dfs(root.left);
            dfs(root.right);
        } else {
            ans.add(root.val);
            dfs(root.right);
            dfs(root.left);
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
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: list[int]) -> list[int]:
        def dfs(root):
            nonlocal i, ok
            if root is None or not ok:
                return
            if root.val != voyage[i]:
                ok = False
                return
            i += 1
            if root.left is None or root.left.val == voyage[i]:
                dfs(root.left)
                dfs(root.right)
            else:
                ans.append(root.val)
                dfs(root.right)
                dfs(root.left)

        ans = []
        i = 0
        ok = True
        dfs(root)
        return ans if ok else [-1]
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
