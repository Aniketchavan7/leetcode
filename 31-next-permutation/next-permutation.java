class Solution {

    void rev(int[] nums,int s,int e)
    {
        while(s<e){
            int temp=nums[s];
            nums[s]=nums[e];
            nums[e]=temp;
            s++;
            e--;
        }
    }


    public void nextPermutation(int[] nums) {
        
        int idx=-1;
        int n=nums.length;
    
        for(int i=n-2;i>=0;i--){

            if(nums[i]<nums[i+1]){
                idx=i;
                break;
            }
            
        }
        if(idx==-1){
            rev(nums,0,n-1);

        }
        else{
        for(int i=n-1;i>idx;i--){

            if(nums[idx]<nums[i]){
                int temp=nums[idx];
                nums[idx]=nums[i];
                nums[i]=temp;
                break;
            }


        }

        rev(nums,idx+1,n-1);

        }



    }
}