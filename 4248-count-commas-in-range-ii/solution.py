class Solution:
    def countCommasRange(self, L: int, R: int) -> int:
        def prefix_commas(n):
            if n < 1000:
                return 0
            commas = 0
            threshold = 1000
            while n >= threshold:
                commas += (n - threshold + 1)
                threshold *= 1000
            return commas

        return prefix_commas(R) - prefix_commas(L - 1)
