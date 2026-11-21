class Solution {
    public int reverse(int x) {
        int rev=0;
        int x1=Math.abs(x);
        while(x1!=0)
        {
            int rem=x1%10;
            if(rev>(Integer.MAX_VALUE-rem)/10){
                return 0;
            }
            rev=rev*10+rem;
            x1=x1/10;
        }
        return (x < 0) ? (-rev) : rev; 
    }
}