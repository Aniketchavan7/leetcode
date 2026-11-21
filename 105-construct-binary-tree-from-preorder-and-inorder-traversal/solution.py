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
