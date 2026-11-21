class Solution {
    public int smallestStableIndex(int[] nums) {
        int n = nums.length;
        int[] prefixMin = new int[n];
        int[] suffixMax = new int[n];

        prefixMin[0] = nums[0];
        for (int i = 1; i < n; i++) prefixMin[i] = Math.min(prefixMin[i - 1], nums[i]);

        suffixMax[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) suffixMax[i] = Math.max(suffixMax[i + 1], nums[i]);

        for (int i = 0; i < n; i++) {
            boolean leftOk = (i == 0) || (nums[i] >= prefixMin[i - 1]);
            boolean rightOk = (i == n - 1) || (nums[i] <= suffixMax[i + 1]);
            if (leftOk && rightOk) return i;
        }
        return -1;
    }
}
