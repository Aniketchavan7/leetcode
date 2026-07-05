class Solution {
    public boolean isPalindrome(int x) {
        
        if(x<0 || (x%10==0 && x!=0))
        {
            return false;
        }

        int h=0;
        while(h<x)
        {
            h=h*10+x%10;
            x=x/10;
        }
        return h==x|| h/10==x;
    }
}