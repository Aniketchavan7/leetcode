class Solution:
    def smallestStableIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_min = [0] * n
        suffix_max = [0] * n

        prefix_min[0] = nums[0]
        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], nums[i])

        suffix_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])

        for i in range(n):
            left_ok = (i == 0) or (nums[i] >= prefix_min[i - 1])
            right_ok = (i == n - 1) or (nums[i] <= suffix_max[i + 1])
            if left_ok and right_ok:
                return i
        return -1
