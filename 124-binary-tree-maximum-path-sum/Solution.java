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
