# 100. Same Tree

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/same-tree/)
[![Topic: Tree / DFS](https://img.shields.io/badge/Topic-Tree%20/%20DFS-blue)](https://leetcode.com/problems/same-tree/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Two binary trees are identical if their roots have the same value, and their left subtrees are structurally identical, and their right subtrees are structurally identical. We check base cases: if both are null, return true; if only one is null or values differ, return false; otherwise recursively return isSameTree(p.left, q.left) && isSameTree(p.right, q.right)."

---

### 💡 Intuition & Core Insight
- **Structural Symmetry**: A divide-and-conquer recursion naturally asserts both structure and content simultaneously.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `p = [1, 2, 3]`, `q = [1, 2, 3]`
- p.val == q.val (1 == 1) -> check left & right
- Left: 2 == 2, both children null -> true
- Right: 3 == 3, both children null -> true
- True && True -> True.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null || p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Visits each node in the smaller tree at most once.
- **Space Complexity**: $\mathcal{O}(H)$ — Call stack height H.

---

### ⚠️ Edge Cases & Interview Traps
1. Both trees empty: returns true.
2. Structurally different: detected immediately at null check.

---

### 💬 Follow-Up Questions You Might Get
- *How to solve iteratively?* Use a Queue containing pairs of nodes (BFS).
