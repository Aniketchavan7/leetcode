class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(start, path):
            res.append(list(path))
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
