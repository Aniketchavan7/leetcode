class Solution {
    public int largestRectangleArea(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(-1); // Sentinel left boundary
        int maxArea = 0;
        int n = heights.length;

        for (int i = 0; i < n; i++) {
            while (stack.peek() != -1 && heights[stack.peek()] >= heights[i]) {
                int height = heights[stack.pop()];
                int width = i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            stack.push(i);
        }

        while (stack.peek() != -1) {
            int height = heights[stack.pop()];
            int width = n - stack.peek() - 1;
            maxArea = Math.max(maxArea, height * width);
        }
        return maxArea;
    }
}
