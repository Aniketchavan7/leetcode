# 230. Kth Smallest Element in a BST

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
[![Topic: Tree / BST Inorder](https://img.shields.io/badge/Topic-Tree%20/%20BST%20Inorder-blue)](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "An In-Order traversal (Left -> Node -> Right) of a Binary Search Tree visits values in strictly ascending sorted order. Using an explicit stack, we traverse to the leftmost node. We pop nodes, decrement k, and when k reaches 0, the current node is the kth smallest element."

---

### 💡 Intuition & Core Insight
- **BST Invariant = Sorted Sequence**: We don't need to traverse the entire tree! Early termination when k reaches 0 saves visiting remaining nodes.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `root = [3, 1, 4, null, 2]`, `k = 1`
- Stack push 3, push 1
- Pop 1: k=1 -> k=0! Return 1 immediately.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode curr = root;

        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            if (--k == 0) return curr.val;
            curr = curr.right;
        }
        return -1;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        return -1
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(H + k)$ — Reaches leftmost node in O(H) and traverses k nodes.
- **Space Complexity**: $\mathcal{O}(H)$ — Stack holds at most H nodes.

---

### ⚠️ Edge Cases & Interview Traps
1. k = 1: returns minimum element (leftmost node).
2. k = N: visits all nodes and returns maximum element.

---

### 💬 Follow-Up Questions You Might Get
- *What if the BST is modified often with frequent kth queries?* Augment each node with a `subtree_count` field to achieve O(H) search without traversal.
