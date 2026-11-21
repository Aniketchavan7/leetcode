class Solution {
    public boolean check(int[] nums) {
        int drops = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] > nums[(i + 1) % n]) {
                drops++;
            }
        }
        return drops <= 1;
    }
}
