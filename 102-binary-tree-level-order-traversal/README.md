# 102. Binary Tree Level Order Traversal

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/binary-tree-level-order-traversal/)
[![Topic: Tree / BFS](https://img.shields.io/badge/Topic-Tree%20/%20BFS-blue)](https://leetcode.com/problems/binary-tree-level-order-traversal/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To return values level by level, we use Breadth-First Search (BFS) with a Queue. We enqueue the root. In a while loop, we capture `levelSize = queue.size()`. We loop `levelSize` times to dequeue all nodes belonging strictly to the current level, record their values, and enqueue their non-null children. Each batch forms one row in the output."

---

### 💡 Intuition & Core Insight
- **Queue Size Snapshot**: Freezing `queue.size()` before processing a level ensures we only process the current generation of nodes, cleanly separating levels without needing a delimiter node.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `[3, 9, 20, null, null, 15, 7]`
- Level 0: Queue=[3], size=1 -> Pop 3, enqueue 9, 20 -> row=[3]
- Level 1: Queue=[9, 20], size=2 -> Pop 9, Pop 20, enqueue 15, 7 -> row=[9, 20]
- Level 2: Queue=[15, 7], size=2 -> Pop 15, Pop 7 -> row=[15, 7]
Result: `[[3], [9, 20], [15, 7]]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>();
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                currentLevel.add(node.val);
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            res.add(currentLevel);
        }
        return res;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Every node is enqueued and dequeued exactly once.
- **Space Complexity**: $\mathcal{O}(N)$ — Queue holds at most N/2 nodes (the maximum width of a complete binary tree).

---

### ⚠️ Edge Cases & Interview Traps
1. Empty root: returns empty list.
2. Skewed tree: operates with queue size 1 each iteration.

---

### 💬 Follow-Up Questions You Might Get
- *Can this be done with DFS?* Yes, pass depth as parameter and append to `res[depth]`.
