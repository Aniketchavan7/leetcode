# 782. Transform to Chessboard

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/transform-to-chessboard)
[![Topic: Bit Manipulation & Array & Math](https://img.shields.io/badge/Topic-Bit%20Manipulation%20&%20Array%20&%20Math-blue)](https://leetcode.com/problems/transform-to-chessboard)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Bit Manipulation strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]`  
**Expected Output**: `2`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `2` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int n;

    public int movesToChessboard(int[][] board) {
        n = board.length;
        int mask = (1 << n) - 1;
        int rowMask = 0, colMask = 0;
        for (int i = 0; i < n; ++i) {
            rowMask |= board[0][i] << i;
            colMask |= board[i][0] << i;
        }
        int revRowMask = mask ^ rowMask;
        int revColMask = mask ^ colMask;
        int sameRow = 0, sameCol = 0;
        for (int i = 0; i < n; ++i) {
            int curRowMask = 0, curColMask = 0;
            for (int j = 0; j < n; ++j) {
                curRowMask |= board[i][j] << j;
                curColMask |= board[j][i] << j;
            }
            if (curRowMask != rowMask && curRowMask != revRowMask) {
                return -1;
            }
            if (curColMask != colMask && curColMask != revColMask) {
                return -1;
            }
            sameRow += curRowMask == rowMask ? 1 : 0;
            sameCol += curColMask == colMask ? 1 : 0;
        }
        int t1 = f(rowMask, sameRow);
        int t2 = f(colMask, sameCol);
        return t1 == -1 || t2 == -1 ? -1 : t1 + t2;
    }

    private int f(int mask, int cnt) {
        int ones = Integer.bitCount(mask);
        if (n % 2 == 1) {
            if (Math.abs(n - ones * 2) != 1 || Math.abs(n - cnt * 2) != 1) {
                return -1;
            }
            if (ones == n / 2) {
                return n / 2 - Integer.bitCount(mask & 0xAAAAAAAA);
            }
            return (n / 2 + 1) - Integer.bitCount(mask & 0x55555555);
        } else {
            if (ones != n / 2 || cnt != n / 2) {
                return -1;
            }
            int cnt0 = n / 2 - Integer.bitCount(mask & 0xAAAAAAAA);
            int cnt1 = n / 2 - Integer.bitCount(mask & 0x55555555);
            return Math.min(cnt0, cnt1);
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        def f(mask, cnt):
            ones = mask.bit_count()
            if n & 1:
                if abs(n - 2 * ones) != 1 or abs(n - 2 * cnt) != 1:
                    return -1
                if ones == n // 2:
                    return n // 2 - (mask & 0xAAAAAAAA).bit_count()
                return (n + 1) // 2 - (mask & 0x55555555).bit_count()
            else:
                if ones != n // 2 or cnt != n // 2:
                    return -1
                cnt0 = n // 2 - (mask & 0xAAAAAAAA).bit_count()
                cnt1 = n // 2 - (mask & 0x55555555).bit_count()
                return min(cnt0, cnt1)

        n = len(board)
        mask = (1 << n) - 1
        rowMask = colMask = 0
        for i in range(n):
            rowMask |= board[0][i] << i
            colMask |= board[i][0] << i
        revRowMask = mask ^ rowMask
        revColMask = mask ^ colMask
        sameRow = sameCol = 0
        for i in range(n):
            curRowMask = curColMask = 0
            for j in range(n):
                curRowMask |= board[i][j] << j
                curColMask |= board[j][i] << j
            if curRowMask not in (rowMask, revRowMask) or curColMask not in (
                colMask,
                revColMask,
            ):
                return -1
            sameRow += curRowMask == rowMask
            sameCol += curColMask == colMask
        t1 = f(rowMask, sameRow)
        t2 = f(colMask, sameCol)
        return -1 if t1 == -1 or t2 == -1 else t1 + t2
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Handling empty or single-element inputs.
2. Boundary index arithmetic and potential overflow.
3. Duplicate or negative values in input collections.

---

### 💬 Follow-Up Questions You Might Get
*How does this scale to distributed streams?* Hash partitioning across shards or MapReduce pipelines can process data in parallel.
