class Solution {
    public boolean isPalindrome(String s) {
        
        StringBuilder str=new StringBuilder();

        for(int i=0;i<s.length();i++)
        {

            char ch=s.charAt(i);

            if(Character.isLetterOrDigit(ch))
            {
                str.append(Character.toLowerCase(ch));
            }


        }

        int start=0,end=str.length()-1;
        while(start<end)
        {
            if(str.charAt(start++)!=str.charAt(end--)) return false;

        }
        return true;



    }
}