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
