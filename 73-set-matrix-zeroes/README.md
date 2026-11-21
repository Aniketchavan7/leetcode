# 73. Set Matrix Zeroes

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/set-matrix-zeroes/)
[![Topic: Matrix](https://img.shields.io/badge/Topic-Matrix-blue)](https://leetcode.com/problems/set-matrix-zeroes/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To set an entire row and column to 0 if an element is 0 in-place with O(1) extra space, we use the first row and first column of the matrix itself as our markers! We use a boolean variable `firstColZero` to track whether the first column originally contained a zero. Then we iterate through the rest of the matrix marking `matrix[i][0] = 0` and `matrix[0][j] = 0`. Finally, we use these markers to zero out the cells, finishing with the first row and column."

---

### 💡 Intuition & Core Insight
- **Reusing Matrix State**: Instead of allocating O(M + N) boolean arrays, storing flags in row 0 and column 0 requires O(1) auxiliary space.
- **Overlapping Corner Cell**: Cell (0,0) represents both row 0 and col 0. Separating col 0 into a distinct boolean `firstColZero` prevents collision.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**:
`[[1, 1, 1],`
` [1, 0, 1],`
` [1, 1, 1]]`
- At (1, 1), value is 0 -> mark row header `matrix[1][0] = 0` and col header `matrix[0][1] = 0`.
- Second pass uses headers to zero out row 1 and col 1.
Result:
`[[1, 0, 1],`
` [0, 0, 0],`
` [1, 0, 1]]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean firstColZero = false;

        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) firstColZero = true;
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        if (matrix[0][0] == 0) {
            for (int j = 0; j < n; j++) matrix[0][j] = 0;
        }

        if (firstColZero) {
            for (int i = 0; i < m; i++) matrix[i][0] = 0;
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_col_zero = False

        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(M \cdot N)$ — Two passes over the matrix of size M x N.
- **Space Complexity**: $\mathcal{O}(1)$ — Uses row 0 and column 0 as markers with one boolean variable.

---

### ⚠️ Edge Cases & Interview Traps
1. Zero in first row: handled properly by zeroing row 0 at the end.
2. Zero in first col: handled by firstColZero boolean.

---

### 💬 Follow-Up Questions You Might Get
- *Why not use a sentinel value like -999999?* Elements can be any integer, so sentinel collisions cause bugs.
