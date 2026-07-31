class Solution {
    public int maxProductDifference(int[] nums) {
        Arrays.sort(nums);
        int n=nums.length;
        int max=nums[n-1]*nums[n-2];
        int min=nums[0]*nums[1];
        
        return max-min;
    }
}