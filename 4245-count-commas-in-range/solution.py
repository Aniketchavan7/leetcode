class Solution:
    def countCommas(self, n: int) -> int:
        commas = 0
        threshold = 1000
        while n >= threshold:
            commas += (n - threshold + 1)
            threshold *= 1000
        return commas
