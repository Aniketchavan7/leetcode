# 124. Binary Tree Maximum Path Sum

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
[![Topic: Tree / Post-order DFS](https://img.shields.io/badge/Topic-Tree%20/%20Post-order%20DFS-blue)](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "A path in a binary tree can peak at any node, connecting a path from its left subtree, through the node, to its right subtree. At each node during post-order traversal: 1) Recursively compute the maximum branch gain from left and right subtrees (ignoring negative gains via Math.max(0, gain)). 2) Update global maximum path sum with `node.val + leftGain + rightGain`. 3) Return to parent `node.val + max(leftGain, rightGain)` because a path to parent cannot fork into both children."

---

### 💡 Intuition & Core Insight
- **Fork vs Branch**: At the peak node, we can combine both left and right paths. But when returning to an ancestor, the path can only continue along one single branch.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `[-10, 9, 20, null, null, 15, 7]`
- Node 15: left=0, right=0 -> returns 15, maxPath=15
- Node 7: left=0, right=0 -> returns 7, maxPath=15
- Node 20: left=15, right=7 -> fork=20+15+7=42! maxPath=42. Returns 20+max(15,7)=35
- Node 9: returns 9
- Root -10: left=9, right=35 -> fork=-10+9+35=34 < 42.
Global max = 42.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        maxGain(root);
        return maxSum;
    }

    private int maxGain(TreeNode node) {
        if (node == null) return 0;

        // Max gain from left and right; ignore negative paths
        int leftGain = Math.max(0, maxGain(node.left));
        int rightGain = Math.max(0, maxGain(node.right));

        // Path peaking at current node
        int currentPath = node.val + leftGain + rightGain;
        maxSum = Math.max(maxSum, currentPath);

        // Return maximum branch gain to parent
        return node.val + Math.max(leftGain, rightGain);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0
            left_gain = max(0, max_gain(node.left))
            right_gain = max(0, max_gain(node.right))

            current_path = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path)

            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Visits every node once during post-order DFS traversal.
- **Space Complexity**: $\mathcal{O}(H)$ — Recursion call stack equals height H.

---

### ⚠️ Edge Cases & Interview Traps
1. All negative values [-3, -2, -1]: maxSum correctly records the least negative single node (-1) because 0-cutoff discards negative children.
2. Single node: returns root.val.

---

### 💬 Follow-Up Questions You Might Get
- *What if the path must start and end at leaves?* Only update global max when both children are non-null.
