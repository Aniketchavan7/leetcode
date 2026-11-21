# 106. Construct Binary Tree from Inorder and Postorder Traversal

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal)
[![Topic: Tree & Array & Hash Table](https://img.shields.io/badge/Topic-Tree%20&%20Array%20&%20Hash%20Table-blue)](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "For tree structures, we leverage recursive DFS or iterative BFS to traverse nodes. In **Construct Binary Tree from Inorder and Postorder Traversal**, processing each node once while maintaining tree invariants allows linear-time resolution."

---

### 💡 Intuition & Core Insight
- **Recursive Invariant**: At each subtree, we compute left and right subtree properties and aggregate the result.
- **Traversal Choice**: Pre-order / In-order / Post-order aligns naturally with tree height, sum, or path validation.
- **Stack Depth**: Auxiliary space is bounded by the height of the tree.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]`  
**Expected Output**: `[3,9,20,null,null,15,7]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[3,9,20,null,null,15,7]` |

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
    private Map<Integer, Integer> d = new HashMap<>();
    private int[] postorder;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        this.postorder = postorder;
        int n = inorder.length;
        for (int i = 0; i < n; ++i) {
            d.put(inorder[i], i);
        }
        return dfs(0, 0, n);
    }

    private TreeNode dfs(int i, int j, int n) {
        if (n <= 0) {
            return null;
        }
        int v = postorder[j + n - 1];
        int k = d.get(v);
        TreeNode l = dfs(i, j, k - i);
        TreeNode r = dfs(k + 1, j + k - i, n - k + i - 1);
        return new TreeNode(v, l, r);
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
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        def dfs(i: int, j: int, n: int) -> Optional[TreeNode]:
            if n <= 0:
                return None
            v = postorder[j + n - 1]
            k = d[v]
            l = dfs(i, j, k - i)
            r = dfs(k + 1, j + k - i, n - k + i - 1)
            return TreeNode(v, l, r)

        d = {v: i for i, v in enumerate(inorder)}
        return dfs(0, 0, len(inorder))
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
