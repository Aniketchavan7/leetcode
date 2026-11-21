# 655. Print Binary Tree

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/print-binary-tree)
[![Topic: Tree & Depth-First Search & Breadth-First Search](https://img.shields.io/badge/Topic-Tree%20&%20Depth-First%20Search%20&%20Breadth-First%20Search-blue)](https://leetcode.com/problems/print-binary-tree)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "For tree structures, we leverage recursive DFS or iterative BFS to traverse nodes. In **Print Binary Tree**, processing each node once while maintaining tree invariants allows linear-time resolution."

---

### 💡 Intuition & Core Insight
- **Recursive Invariant**: At each subtree, we compute left and right subtree properties and aggregate the result.
- **Traversal Choice**: Pre-order / In-order / Post-order aligns naturally with tree height, sum, or path validation.
- **Stack Depth**: Auxiliary space is bounded by the height of the tree.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `root = [1,2]`  
**Expected Output**: `[[&quot;&quot;,&quot;1&quot;,&quot;&quot;],`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `root = [1,2]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[[&quot;&quot;,&quot;1&quot;,&quot;&quot;],` |

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
    public List<List<String>> printTree(TreeNode root) {
        int h = height(root);
        int m = h + 1, n = (1 << (h + 1)) - 1;
        String[][] res = new String[m][n];
        for (int i = 0; i < m; ++i) {
            Arrays.fill(res[i], "");
        }
        dfs(root, res, h, 0, (n - 1) / 2);
        List<List<String>> ans = new ArrayList<>();
        for (String[] t : res) {
            ans.add(Arrays.asList(t));
        }
        return ans;
    }

    private void dfs(TreeNode root, String[][] res, int h, int r, int c) {
        if (root == null) {
            return;
        }
        res[r][c] = String.valueOf(root.val);
        dfs(root.left, res, h, r + 1, c - (1 << (h - r - 1)));
        dfs(root.right, res, h, r + 1, c + (1 << (h - r - 1)));
    }

    private int height(TreeNode root) {
        if (root == null) {
            return -1;
        }
        return 1 + Math.max(height(root.left), height(root.right));
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
    def printTree(self, root: Optional[TreeNode]) -> list[list[str]]:
        def height(root):
            if root is None:
                return -1
            return 1 + max(height(root.left), height(root.right))

        def dfs(root, r, c):
            if root is None:
                return
            ans[r][c] = str(root.val)
            dfs(root.left, r + 1, c - 2 ** (h - r - 1))
            dfs(root.right, r + 1, c + 2 ** (h - r - 1))

        h = height(root)
        m, n = h + 1, 2 ** (h + 1) - 1
        ans = [[""] * n for _ in range(m)]
        dfs(root, 0, (n - 1) // 2)
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
