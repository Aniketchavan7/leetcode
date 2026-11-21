# 723. Candy Crush

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/candy-crush)
[![Topic: Array & Two Pointers & Matrix](https://img.shields.io/badge/Topic-Array%20&%20Two%20Pointers%20&%20Matrix-blue)](https://leetcode.com/problems/candy-crush)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "By maintaining window boundaries or dual pointers, we convert a quadratic pair search into a linear scan, dynamically expanding or shrinking based on feasibility invariants."

---

### 💡 Intuition & Core Insight
- **Monotonicity**: As the right pointer advances, the search space moves monotonically without backtracking.
- **Window Invariant**: Validating window conditions with a frequency counter guarantees correctness.
- **Two-Ended Traversal**: Squeezing inward from boundaries avoids evaluating redundant pairs.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]`  
**Expected Output**: `[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[][] candyCrush(int[][] board) {
        int m = board.length, n = board[0].length;
        boolean run = true;

        while (run) {
            run = false;
            for (int i = 0; i < m; i++) {
                for (int j = 2; j < n; j++) {
                    if (board[i][j] != 0 && Math.abs(board[i][j]) == Math.abs(board[i][j - 1])
                        && Math.abs(board[i][j]) == Math.abs(board[i][j - 2])) {
                        run = true;
                        int val = Math.abs(board[i][j]);
                        board[i][j] = board[i][j - 1] = board[i][j - 2] = -val;
                    }
                }
            }
            for (int j = 0; j < n; j++) {
                for (int i = 2; i < m; i++) {
                    if (board[i][j] != 0 && Math.abs(board[i][j]) == Math.abs(board[i - 1][j])
                        && Math.abs(board[i][j]) == Math.abs(board[i - 2][j])) {
                        run = true;
                        int val = Math.abs(board[i][j]);
                        board[i][j] = board[i - 1][j] = board[i - 2][j] = -val;
                    }
                }
            }
            if (run) {
                for (int j = 0; j < n; j++) {
                    int k = m - 1;
                    for (int i = m - 1; i >= 0; i--) {
                        if (board[i][j] > 0) {
                            board[k][j] = board[i][j];
                            k--;
                        }
                    }
                    while (k >= 0) {
                        board[k][j] = 0;
                        k--;
                    }
                }
            }
        }

        return board;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def candyCrush(self, board: list[list[int]]) -> list[list[int]]:
        m, n = len(board), len(board[0])
        run = True
        while run:
            run = False
            for i in range(m):
                for j in range(2, n):
                    if board[i][j] and abs(board[i][j]) == abs(board[i][j - 1]) == abs(
                        board[i][j - 2]
                    ):
                        run = True
                        board[i][j] = board[i][j - 1] = board[i][j - 2] = -abs(
                            board[i][j]
                        )
            for j in range(n):
                for i in range(2, m):
                    if board[i][j] and abs(board[i][j]) == abs(board[i - 1][j]) == abs(
                        board[i - 2][j]
                    ):
                        run = True
                        board[i][j] = board[i - 1][j] = board[i - 2][j] = -abs(
                            board[i][j]
                        )
            if run:
                for j in range(n):
                    k = m - 1
                    for i in range(m - 1, -1, -1):
                        if board[i][j] > 0:
                            board[k][j] = board[i][j]
                            k -= 1
                    while k >= 0:
                        board[k][j] = 0
                        k -= 1
        return board
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(1)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Off-by-one errors on window size (right - left + 1).
2. Empty arrays or arrays with all identical elements.
3. Forgetting to update state counters when shrinking the left boundary.

---

### 💬 Follow-Up Questions You Might Get
*What if the array cannot fit into memory?* We can stream data through a bounded circular buffer or sliding window chunk.
