# 105. Construct Binary Tree from Preorder and Inorder Traversal

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
[![Topic: Tree / Divide & Conquer](https://img.shields.io/badge/Topic-Tree%20/%20Divide%20%26%20Conquer-blue)](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Preorder traversal visits `[Root, Left Subtree, Right Subtree]`, meaning the first element is always the root. Inorder traversal visits `[Left Subtree, Root, Right Subtree]`, meaning finding the root's value in inorder splits the tree into left and right subtrees. We use a Hash Map to look up root indices in inorder in O(1), and recursively construct the left and right children."

---

### 💡 Intuition & Core Insight
- **Preorder gives Roots; Inorder gives Boundaries**: Knowing the root index `mid` in inorder tells us the exact size of the left subtree (`mid - inStart`), which lets us slice the preorder array accordingly.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `preorder = [3, 9, 20, 15, 7]`, `inorder = [9, 3, 15, 20, 7]`
- Root is 3. Inorder has 3 at index 1.
- Left subtree: inorder `[9]`, preorder `[9]` -> node 9
- Right subtree: inorder `[15, 20, 7]`, preorder `[20, 15, 7]` -> node 20 with children 15, 7.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int preIdx = 0;
    private final Map<Integer, Integer> inMap = new HashMap<>();

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++) {
            inMap.put(inorder[i], i);
        }
        return helper(preorder, 0, inorder.length - 1);
    }

    private TreeNode helper(int[] preorder, int inStart, int inEnd) {
        if (inStart > inEnd) return null;

        int rootVal = preorder[preIdx++];
        TreeNode root = new TreeNode(rootVal);
        int inMid = inMap.get(rootVal);

        root.left = helper(preorder, inStart, inMid - 1);
        root.right = helper(preorder, inMid + 1, inEnd);

        return root;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        in_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(in_start, in_end):
            if in_start > in_end:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            in_mid = in_map[root_val]

            root.left = helper(in_start, in_mid - 1)
            root.right = helper(in_mid + 1, in_end)
            return root

        return helper(0, len(inorder) - 1)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Building hash map takes O(N); each tree node is created once in O(1).
- **Space Complexity**: $\mathcal{O}(N)$ — Hash map stores N elements; recursion stack is O(H).

---

### ⚠️ Edge Cases & Interview Traps
1. Single node: creates root without children.
2. Skewed tree: handled cleanly without index out of bounds.

---

### 💬 Follow-Up Questions You Might Get
- *What if duplicate values exist?* Unique trees cannot be uniquely constructed if values repeat.
