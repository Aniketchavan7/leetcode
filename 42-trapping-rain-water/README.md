# 42. Trapping Rain Water

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/trapping-rain-water/)
[![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-blue)](https://leetcode.com/problems/trapping-rain-water/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Water trapped above any bar is determined by min(maxLeft, maxRight) - height[i]. Using two pointers from left and right, we maintain leftMax and rightMax. We always process the pointer with the smaller max, because the water level at that position is strictly bounded by its own max, regardless of how tall the other side might be."

---

### 💡 Intuition & Core Insight
- **The Elevation Bottleneck**: Water can only pool up to the height of the shorter wall surrounding it.
- **Why Two Pointers Work**: If `leftMax < rightMax`, the water on the left side is guaranteed to be trapped by `leftMax`, even if there's a 1000-ft tower somewhere to the right.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`
- Left=0 (0), Right=11 (1): leftMax=0, rightMax=1. Process Left, water+=0, Left++
- Left=1 (1), Right=11 (1): leftMax=1, rightMax=1. Process Right, water+=0, Right--
- Left=1 (1), Right=10 (2): leftMax=1, rightMax=2. Left < Right -> process Left...
Total water accumulated = 6.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0;
        int totalWater = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    totalWater += leftMax - height[left];
                }
                left++;
            } else {
                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    totalWater += rightMax - height[right];
                }
                right--;
            }
        }
        return totalWater;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Each index is visited exactly once by the converging two pointers.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary variables without prefix/suffix arrays.

---

### ⚠️ Edge Cases & Interview Traps
1. Less than 3 bars: cannot trap any water (returns 0).
2. Strictly increasing or decreasing slopes: no valleys, returns 0.

---

### 💬 Follow-Up Questions You Might Get
- *Can we solve this with a Monotonic Stack?* Yes, a decreasing monotonic stack calculates trapped water horizontally layer by layer.
