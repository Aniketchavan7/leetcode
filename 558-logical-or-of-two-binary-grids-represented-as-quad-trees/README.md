# 558. Logical OR of Two Binary Grids Represented as Quad-Trees

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees)
[![Topic: Tree & Divide and Conquer](https://img.shields.io/badge/Topic-Tree%20&%20Divide%20and%20Conquer-blue)](https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "For tree structures, we leverage recursive DFS or iterative BFS to traverse nodes. In **Logical OR of Two Binary Grids Represented as Quad-Trees**, processing each node once while maintaining tree invariants allows linear-time resolution."

---

### 💡 Intuition & Core Insight
- **Recursive Invariant**: At each subtree, we compute left and right subtree properties and aggregate the result.
- **Traversal Choice**: Pre-order / In-order / Post-order aligns naturally with tree height, sum, or path validation.
- **Stack Depth**: Auxiliary space is bounded by the height of the tree.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `quadTree1 = [[0,1],[1,1],[1,1],[1,0],[1,0]]`  
**Expected Output**: `[[0,0],[1,1],[1,1],[1,1],[1,0]]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `quadTree1 = [[0,1],[1,1],[1,1],[1,0],[1,0]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[[0,0],[1,1],[1,1],[1,1],[1,0]]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    public Node() {}

    public Node(boolean _val,boolean _isLeaf,Node _topLeft,Node _topRight,Node _bottomLeft,Node
_bottomRight) { val = _val; isLeaf = _isLeaf; topLeft = _topLeft; topRight = _topRight; bottomLeft =
_bottomLeft; bottomRight = _bottomRight;
    }
};
*/

class Solution {
    public Node intersect(Node quadTree1, Node quadTree2) {
        return dfs(quadTree1, quadTree2);
    }

    private Node dfs(Node t1, Node t2) {
        if (t1.isLeaf && t2.isLeaf) {
            return new Node(t1.val || t2.val, true);
        }
        if (t1.isLeaf) {
            return t1.val ? t1 : t2;
        }
        if (t2.isLeaf) {
            return t2.val ? t2 : t1;
        }
        Node res = new Node();
        res.topLeft = dfs(t1.topLeft, t2.topLeft);
        res.topRight = dfs(t1.topRight, t2.topRight);
        res.bottomLeft = dfs(t1.bottomLeft, t2.bottomLeft);
        res.bottomRight = dfs(t1.bottomRight, t2.bottomRight);
        boolean isLeaf = res.topLeft.isLeaf && res.topRight.isLeaf && res.bottomLeft.isLeaf
            && res.bottomRight.isLeaf;
        boolean sameVal = res.topLeft.val == res.topRight.val
            && res.topRight.val == res.bottomLeft.val && res.bottomLeft.val == res.bottomRight.val;
        if (isLeaf && sameVal) {
            res = res.topLeft;
        }
        return res;
    }
}
```

#### Python 3 Solution
```python
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def intersect(self, quadTree1: "Node", quadTree2: "Node") -> "Node":
        def dfs(t1, t2):
            if t1.isLeaf and t2.isLeaf:
                return Node(t1.val or t2.val, True)
            if t1.isLeaf:
                return t1 if t1.val else t2
            if t2.isLeaf:
                return t2 if t2.val else t1
            res = Node()
            res.topLeft = dfs(t1.topLeft, t2.topLeft)
            res.topRight = dfs(t1.topRight, t2.topRight)
            res.bottomLeft = dfs(t1.bottomLeft, t2.bottomLeft)
            res.bottomRight = dfs(t1.bottomRight, t2.bottomRight)
            isLeaf = (
                res.topLeft.isLeaf
                and res.topRight.isLeaf
                and res.bottomLeft.isLeaf
                and res.bottomRight.isLeaf
            )
            sameVal = (
                res.topLeft.val
                == res.topRight.val
                == res.bottomLeft.val
                == res.bottomRight.val
            )
            if isLeaf and sameVal:
                res = res.topLeft
            return res

        return dfs(quadTree1, quadTree2)
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
