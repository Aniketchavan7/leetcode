class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(remain, start, path):
            if remain == 0:
                res.append(list(path))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                backtrack(remain - candidates[i], i, path)
                path.pop()

        backtrack(target, 0, [])
        return res
