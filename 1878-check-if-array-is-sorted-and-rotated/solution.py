class Solution:
    def check(self, nums: list[int]) -> bool:
        drops = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
        return drops <= 1
