# 545. Boundary of Binary Tree

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/boundary-of-binary-tree)
[![Topic: Tree & Depth-First Search & Binary Tree](https://img.shields.io/badge/Topic-Tree%20&%20Depth-First%20Search%20&%20Binary%20Tree-blue)](https://leetcode.com/problems/boundary-of-binary-tree)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "For tree structures, we leverage recursive DFS or iterative BFS to traverse nodes. In **Boundary of Binary Tree**, processing each node once while maintaining tree invariants allows linear-time resolution."

---

### 💡 Intuition & Core Insight
- **Recursive Invariant**: At each subtree, we compute left and right subtree properties and aggregate the result.
- **Traversal Choice**: Pre-order / In-order / Post-order aligns naturally with tree height, sum, or path validation.
- **Stack Depth**: Auxiliary space is bounded by the height of the tree.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `root = [1,null,2,3,4]`  
**Expected Output**: `[1,3,4,2]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `root = [1,null,2,3,4]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[1,3,4,2]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        ans.add(root.val);
        if (root.left == root.right) {
            return ans;
        }
        List<Integer> left = new ArrayList<>();
        List<Integer> leaves = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        dfs(left, root.left, 0);
        dfs(leaves, root, 1);
        dfs(right, root.right, 2);

        ans.addAll(left);
        ans.addAll(leaves);
        Collections.reverse(right);
        ans.addAll(right);
        return ans;
    }

    private void dfs(List<Integer> nums, TreeNode root, int i) {
        if (root == null) {
            return;
        }
        if (i == 0) {
            if (root.left != root.right) {
                nums.add(root.val);
                if (root.left != null) {
                    dfs(nums, root.left, i);
                } else {
                    dfs(nums, root.right, i);
                }
            }
        } else if (i == 1) {
            if (root.left == root.right) {
                nums.add(root.val);
            } else {
                dfs(nums, root.left, i);
                dfs(nums, root.right, i);
            }
        } else {
            if (root.left != root.right) {
                nums.add(root.val);
                if (root.right != null) {
                    dfs(nums, root.right, i);
                } else {
                    dfs(nums, root.left, i);
                }
            }
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
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> list[int]:
        def dfs(nums: list[int], root: Optional[TreeNode], i: int):
            if root is None:
                return
            if i == 0:
                if root.left != root.right:
                    nums.append(root.val)
                    if root.left:
                        dfs(nums, root.left, i)
                    else:
                        dfs(nums, root.right, i)
            elif i == 1:
                if root.left == root.right:
                    nums.append(root.val)
                else:
                    dfs(nums, root.left, i)
                    dfs(nums, root.right, i)
            else:
                if root.left != root.right:
                    nums.append(root.val)
                    if root.right:
                        dfs(nums, root.right, i)
                    else:
                        dfs(nums, root.left, i)

        ans = [root.val]
        if root.left == root.right:
            return ans
        left, leaves, right = [], [], []
        dfs(left, root.left, 0)
        dfs(leaves, root, 1)
        dfs(right, root.right, 2)
        ans += left + leaves + right[::-1]
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
