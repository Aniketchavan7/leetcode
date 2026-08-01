class Solution {
    public int longestConsecutive(int[] nums) {

        int n=nums.length;
        if(n==0)
        {
            return 0;
        }

        Set<Integer> ans=new HashSet<>();

        for(int i:nums)
        {
            ans.add(i);
        }
        int lstre=1;

        for(int num:ans){
            if(!ans.contains(num-1)){
                int nun=num;
                int cnt=1;
                while(ans.contains(nun+1)){
                    cnt++;
                    nun++;
                }
                lstre=Math.max(lstre,cnt);
            }
        }
        return lstre;


        }


        
    }
