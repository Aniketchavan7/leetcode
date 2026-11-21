# 79. Word Search

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/word-search/)
[![Topic: Backtracking / Matrix DFS](https://img.shields.io/badge/Topic-Backtracking%20/%20Matrix%20DFS-blue)](https://leetcode.com/problems/word-search/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We search for a word in an M x N grid of characters. Starting from each cell where board[r][c] == word[0], we execute a DFS exploring four adjacent directions. To prevent reusing the same cell within a path without extra memory, we temporarily mask `board[r][c] = '#'`, recurse to find index + 1, and restore the original character upon backtracking. If all letters match, return true."

---

### 💡 Intuition & Core Insight
- **In-Place Marking**: Modifying the board character avoids allocating an M x N visited array.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `word = "ABCCED"`
- Start at (0, 0) 'A' -> match (index 0) -> mask '#'
- Move right (0, 1) 'B' -> match (index 1) -> mask '#'
- Move right (0, 2) 'C' -> match (index 2) -> mask '#'
- Move down (1, 2) 'C' -> match (index 3) -> mask '#'
- Move down (2, 2) 'E' -> match (index 4) -> mask '#'
- Move left (2, 1) 'D' -> match (index 5 == word.len - 1) -> True!

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int r, int c, int idx) {
        if (idx == word.length()) return true;
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(idx)) {
            return false;
        }

        char original = board[r][c];
        board[r][c] = '#'; // Mark visited

        boolean found = dfs(board, word, r + 1, c, idx + 1) ||
                        dfs(board, word, r - 1, c, idx + 1) ||
                        dfs(board, word, r, c + 1, idx + 1) ||
                        dfs(board, word, r, c - 1, idx + 1);

        board[r][c] = original; // Backtrack
        return found;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]:
                return False

            orig = board[r][c]
            board[r][c] = '#'
            found = (dfs(r + 1, c, idx + 1) or
                     dfs(r - 1, c, idx + 1) or
                     dfs(r, c + 1, idx + 1) or
                     dfs(r, c - 1, idx + 1))
            board[r][c] = orig
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(M \cdot N \cdot 3^L)$ — M x N starting cells; each step branches in 3 directions (excluding backward) up to word length L.
- **Space Complexity**: $\mathcal{O}(L)$ — Call stack depth equals word length L.

---

### ⚠️ Edge Cases & Interview Traps
1. Word longer than total board cells: returns false immediately.
2. Single letter word: matches in 1 step.

---

### 💬 Follow-Up Questions You Might Get
- *How to optimize if word frequency is unbalanced?* Reverse word if the first character appears more frequently on the board than the last character.
