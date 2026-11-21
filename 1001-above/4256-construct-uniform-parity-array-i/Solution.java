class Solution {
    public boolean canMakeUniform(int[] nums) {
        int oddCount = 0, evenCount = 0;
        int minOdd = Integer.MAX_VALUE;

        for (int num : nums) {
            if (num % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
                minOdd = Math.min(minOdd, num);
            }
        }
        if (oddCount == 0 || evenCount == 0) return true;
        return oddCount > 0;
    }
}
