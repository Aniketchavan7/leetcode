class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [-1]
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = n - stack[-1] - 1
            max_area = max(max_area, h * w)

        return max_area
