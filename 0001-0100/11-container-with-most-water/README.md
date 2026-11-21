# 11. Container With Most Water

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/container-with-most-water/)
[![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-blue)](https://leetcode.com/problems/container-with-most-water/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We place two pointers at the widest boundaries (index 0 and n-1). The area is limited by the shorter line multiplied by distance. To have any chance of finding a larger area as the width shrinks, we must move the pointer with the smaller height inward."

---

### 💡 Intuition & Core Insight
- **Greedy Pointer Movement**: Moving the taller pointer cannot increase the area because width decreases and height is still bottlenecked by the shorter pointer.
- **Proof of Correctness**: Discarding the shorter pointer never discards a maximum container because any container formed with it and an interior line has smaller width and at best the same height.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `height = [1,8,6,2,5,4,8,3,7]`
- Left=0 (h=1), Right=8 (h=7): width=8, area=min(1,7)*8 = 8. Move left (shorter).
- Left=1 (h=8), Right=8 (h=7): width=7, area=min(8,7)*7 = 49. Move right (shorter).
- Continues until pointers meet. Max recorded area is 49.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxWater = 0;
        while (left < right) {
            int h = Math.min(height[left], height[right]);
            maxWater = Math.max(maxWater, h * (right - left));
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxWater;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            h = min(height[left], height[right])
            max_water = max(max_water, h * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Each step moves either left or right pointer inward by 1, visiting each element once.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary variables.

---

### ⚠️ Edge Cases & Interview Traps
1. Two elements: while loop runs once and returns min * 1.
2. Flat heights: moving either pointer when heights match is safe.

---

### 💬 Follow-Up Questions You Might Get
- *What if slopes or diagonal shapes are allowed?* Becomes geometric trapezoidal integration.
