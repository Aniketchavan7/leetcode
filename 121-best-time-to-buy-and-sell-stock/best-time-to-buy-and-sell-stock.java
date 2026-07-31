class Solution {
    public int maxProfit(int[] prices) {

        int maxp=0,minp=prices[0];

        for(int i=1;i<prices.length;i++)
        {
            int cost=prices[i]-minp;
            maxp=Math.max(maxp,cost);
            minp=Math.min(minp,prices[i]);
        }
        return maxp;

    }
}