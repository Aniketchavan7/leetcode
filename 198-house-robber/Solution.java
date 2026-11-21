class Solution {
    public int rob(int[] nums) {
        int rob1 = 0, rob2 = 0;
        for (int num : nums) {
            int newRob = Math.max(rob2, rob1 + num);
            rob1 = rob2;
            rob2 = newRob;
        }
        return rob2;
    }
}
