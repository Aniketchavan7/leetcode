# 2347. Count Nodes Equal to Average of Subtree

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/)
[![Topic: Tree / Postorder DFS](https://img.shields.io/badge/Topic-Tree%20/%20Postorder%20DFS-blue)](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To compute whether each node equals the integer average of its subtree, a postorder DFS traversal returns a 2-element tuple `[sum, count]` for each subtree. At node: `sum = node.val + left.sum + right.sum`, `count = 1 + left.count + right.count`. If `node.val == sum / count`, increment our answer."

---

### 💡 Intuition & Core Insight
- **Bottom-Up Aggregation**: Both the sum and count of a subtree can be calculated in O(1) from child subtrees, avoiding redundant re-traversals.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `[4, 8, 5, 0, 1, null, 6]`
- Node 0: sum=0, count=1, avg=0 == 0 -> match! (1)
- Node 1: sum=1, count=1, avg=1 == 1 -> match! (2)
- Node 8: sum=8+0+1=9, count=3, avg=9/3=3 != 8
- Node 6: sum=6, count=1, avg=6 == 6 -> match! (3)
- Node 5: sum=5+6=11, count=2, avg=11/2=5 == 5 -> match! (4)
- Node 4: sum=4+9+11=24, count=6, avg=24/6=4 == 4 -> match! (5)
Total: 5 nodes.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int matchingNodes = 0;

    public int averageOfSubtree(TreeNode root) {
        dfs(root);
        return matchingNodes;
    }

    private int[] dfs(TreeNode node) {
        if (node == null) return new int[] {0, 0}; // sum, count

        int[] left = dfs(node.left);
        int[] right = dfs(node.right);

        int sum = node.val + left[0] + right[0];
        int count = 1 + left[1] + right[1];

        if (node.val == sum / count) {
            matchingNodes++;
        }
        return new int[] {sum, count};
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return (0, 0)
            l_sum, l_cnt = dfs(node.left)
            r_sum, r_cnt = dfs(node.right)

            total_sum = node.val + l_sum + r_sum
            total_cnt = 1 + l_cnt + r_cnt

            if node.val == total_sum // total_cnt:
                self.count += 1

            return (total_sum, total_cnt)

        dfs(root)
        return self.count
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Postorder DFS visits each node exactly once.
- **Space Complexity**: $\mathcal{O}(H)$ — Call stack height H.

---

### ⚠️ Edge Cases & Interview Traps
1. Single node tree: sum / count = val / 1 = val -> returns 1.
2. All leaf nodes: always equal their own average.

---

### 💬 Follow-Up Questions You Might Get
- *What if rounded to nearest integer instead of truncated?* Use Math.round((double)sum / count).
