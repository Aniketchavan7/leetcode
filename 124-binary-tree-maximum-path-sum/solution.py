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
