class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cur=0;
        int res=0;

        for(int n:nums)
        {
            if(n==0)
            {
                cur=0;
            }
            else{
                cur++;
            }
            if(cur>res){
                res=cur;
            }


        }
        return res;
    }
}