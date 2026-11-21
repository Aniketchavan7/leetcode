class Solution {
    public int longestPalindrome(String s) {
        Map<Character,Integer> charcount=new HashMap<>();

        for(char c:s.toCharArray()){
            charcount.put(c,charcount.getOrDefault(c,0)+1);

        }

        int len=0;
        boolean hashodd=false;

        for(int co:charcount.values()){
            if(co%2==0){
                len=len+co;
            }
            else{
                len=len+co-1;
                hashodd=true;
            }
        }

        if(hashodd){
            len++;
        }

        return len;

    }
}