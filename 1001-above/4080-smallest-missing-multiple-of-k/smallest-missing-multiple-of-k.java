class Solution {
    public int missingMultiple(int[] nums, int k) {
        boolean[] present =new boolean[101];

        for(int num:nums){
            present[num]=true;
        }

        for(int mu=k; ; mu+=k){
            if(mu>100 || !present[mu]){
                return mu;
            }
        }

      

    }
}