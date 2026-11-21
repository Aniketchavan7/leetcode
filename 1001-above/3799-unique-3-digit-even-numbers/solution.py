class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        counts = Counter(digits)
        res = []
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            needed = Counter([d1, d2, d3])
            if all(counts[d] >= needed[d] for d in needed):
                res.append(num)
        return res
