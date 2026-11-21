# 48. Rotate Image

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/rotate-image/)
[![Topic: Matrix](https://img.shields.io/badge/Topic-Matrix-blue)](https://leetcode.com/problems/rotate-image/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Rotating an N x N 2D matrix clockwise by 90 degrees in-place is equivalent to two standard matrix operations: 1) Transpose the matrix (swap matrix[i][j] with matrix[j][i] along the main diagonal). 2) Reflect the matrix horizontally (reverse each individual row)."

---

### 💡 Intuition & Core Insight
- **Geometric Decomposition**: Clockwise 90-degree rotation maps `(row, col)` to `(col, n - 1 - row)`. Transpose maps `(row, col)` to `(col, row)`; reversing row maps `(col, row)` to `(col, n - 1 - row)`. Combining both achieves the rotation without complex four-way index bookkeeping.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**:
`[[1, 2, 3],`
` [4, 5, 6],`
` [7, 8, 9]]`
1. Transpose along diagonal:
`[[1, 4, 7],`
` [2, 5, 8],`
` [3, 6, 9]]`
2. Reverse each row:
`[[7, 4, 1],`
` [8, 5, 2],`
` [9, 6, 3]]`
Done in-place!

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        // Step 1: Transpose matrix
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
        // Step 2: Reverse each row
        for (int i = 0; i < n; i++) {
            int left = 0, right = n - 1;
            while (left < right) {
                int tmp = matrix[i][left];
                matrix[i][left++] = matrix[i][right];
                matrix[i][right--] = tmp;
            }
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse rows
        for row in matrix:
            row.reverse()
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N^2)$ — Visiting all N*N matrix cells twice (once for transpose, once for row reversal).
- **Space Complexity**: $\mathcal{O}(1)$ — In-place modifications with constant temporary variables.

---

### ⚠️ Edge Cases & Interview Traps
1. 1x1 matrix: loops execute 0 swaps, correctly remains identical.
2. 2x2 matrix: works seamlessly.

---

### 💬 Follow-Up Questions You Might Get
- *How to rotate 90 degrees counter-clockwise?* Transpose then reverse columns vertically (or reverse rows first then transpose).
