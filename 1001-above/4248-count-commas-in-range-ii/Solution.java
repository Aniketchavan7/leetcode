class Solution {
    public long countCommasRange(long L, long R) {
        return prefixCommas(R) - prefixCommas(L - 1);
    }

    private long prefixCommas(long n) {
        if (n < 1000) return 0;
        long commas = 0;
        long threshold = 1000;
        while (n >= threshold) {
            commas += (n - threshold + 1);
            if (threshold > Long.MAX_VALUE / 1000) break;
            threshold *= 1000;
        }
        return commas;
    }
}
