class Solution:
    def canMakeUniform(self, nums: list[int]) -> bool:
        odd_count = sum(1 for x in nums if x % 2 != 0)
        even_count = len(nums) - odd_count
        if odd_count == 0 or even_count == 0:
            return True
        return odd_count > 0
