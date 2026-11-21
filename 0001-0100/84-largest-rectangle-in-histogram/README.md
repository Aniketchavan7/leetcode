# 84. Largest Rectangle in Histogram

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/largest-rectangle-in-histogram/)
[![Topic: Monotonic Stack](https://img.shields.io/badge/Topic-Monotonic%20Stack-blue)](https://leetcode.com/problems/largest-rectangle-in-histogram/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "For each bar in the histogram, the largest rectangle using that bar's full height extends left and right until encountering a bar with strictly smaller height. We maintain a Monotonic Increasing Stack of indices. When the current bar is shorter than the bar at the top of the stack, we pop the top bar and compute its rectangle area: height is `heights[popped]`, width is `i - stack.peek() - 1`."

---

### 💡 Intuition & Core Insight
- **Monotonic Stack Boundary Resolution**: The stack guarantees that the element below `popped` is the first smaller bar to the left, and the current index `i` is the first smaller bar to the right. Both boundaries are discovered simultaneously in O(1).

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `heights = [2, 1, 5, 6, 2, 3]`
- i=0: push 0 (h=2)
- i=1: h=1 < 2 -> pop 0 (h=2), width=1, area=2. Push 1 (h=1)
- i=2: push 2 (h=5)
- i=3: push 3 (h=6)
- i=4: h=2 < 6 -> pop 3 (h=6), width=4-2-1=1, area=6. Pop 2 (h=5), width=4-1-1=2, area=10!
Max area = 10.

---

### 💻 Optimal Implementations

#### Java Solution
```java
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
```

#### Python 3 Solution
```python
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
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Every index is pushed onto the stack once and popped at most once.
- **Space Complexity**: $\mathcal{O}(N)$ — Monotonic stack stores up to N indices.

---

### ⚠️ Edge Cases & Interview Traps
1. Uniform heights [2, 2, 2]: stack handles >= safely.
2. Strictly increasing heights [1, 2, 3]: drained at the end with right boundary = n.

---

### 💬 Follow-Up Questions You Might Get
- *How to extend to 2D binary matrix?* Treat each row as a histogram base and call this algorithm row-by-row (LeetCode 85 - Maximal Rectangle).
