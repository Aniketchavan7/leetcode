# 54. Spiral Matrix

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/spiral-matrix/)
[![Topic: Matrix](https://img.shields.io/badge/Topic-Matrix-blue)](https://leetcode.com/problems/spiral-matrix/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We simulate walking the perimeter of a rectangle inward. We track four boundaries: `top`, `bottom`, `left`, `right`. At each cycle: 1) Traverse left to right across `top`, increment `top`. 2) Traverse top to bottom down `right`, decrement `right`. 3) Traverse right to left across `bottom` (if top <= bottom), decrement `bottom`. 4) Traverse bottom to top up `left` (if left <= right), increment `left`."

---

### 💡 Intuition & Core Insight
- **Shrinking Boundaries**: After exhausting each edge, contracting that boundary prevents re-visiting cells in future spiral layers.
- **Check Before Returning Backward**: If the matrix is a single row or single column, top > bottom or left > right after the first two traversals; checking prevents double-counting.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: 3x3 matrix `[[1,2,3],[4,5,6],[7,8,9]]`
- top=0, bottom=2, left=0, right=2
- 1->2->3 across top, top becomes 1
- 6->9 down right, right becomes 1
- 8->7 across bottom, bottom becomes 1
- 4 up left, left becomes 1
- top <= bottom & left <= right: visit 5.
Result: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        if (matrix.length == 0) return res;
        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            for (int j = left; j <= right; j++) res.add(matrix[top][j]);
            top++;
            for (int i = top; i <= bottom; i++) res.add(matrix[i][right]);
            right--;
            if (top <= bottom) {
                for (int j = right; j >= left; j--) res.add(matrix[bottom][j]);
                bottom--;
            }
            if (left <= right) {
                for (int i = bottom; i >= top; i--) res.add(matrix[i][left]);
                left++;
            }
        }
        return res;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        if not matrix:
            return res
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(M \cdot N)$ — Every single element in the M x N matrix is visited exactly once.
- **Space Complexity**: $\mathcal{O}(1)$ — O(1) extra auxiliary space excluding the output list.

---

### ⚠️ Edge Cases & Interview Traps
1. Single row [[1, 2, 3]]: visited left-to-right, top increments, bottom traversal correctly suppressed.
2. Single column [[1], [2], [3]]: visited top-to-bottom, left increments, left traversal correctly suppressed.

---

### 💬 Follow-Up Questions You Might Get
- *Can we generate an N x N spiral matrix from 1 to N^2?* Use the exact same boundary variables filling numbers sequentially (LeetCode 59).
