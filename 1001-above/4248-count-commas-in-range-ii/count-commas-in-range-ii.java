class Solution {
    public long countCommas(long n) {
        if(n<=999)return 0;

        long total=0;
        long start=1000;

        while(start<=n){
            total=total+n-start+1;
            start*=1000;
        }

        return total;
    }
}