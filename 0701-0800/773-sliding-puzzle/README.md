# 773. Sliding Puzzle

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/sliding-puzzle)
[![Topic: Breadth-First Search & Memoization & Array](https://img.shields.io/badge/Topic-Breadth-First%20Search%20&%20Memoization%20&%20Array-blue)](https://leetcode.com/problems/sliding-puzzle)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "In this problem, subproblems overlap and possess optimal substructure. Instead of an exponential recursive tree, we define a memoized state array where dp[i] captures the optimal decision up to index i, transitioning in polynomial time."

---

### 💡 Intuition & Core Insight
- **Brute Force Bottleneck**: Exploring all state combinations yields exponential O(2^N) or O(N!) complexity.
- **Optimal Substructure**: The optimal solution at state i depends strictly on already computed sub-states.
- **State Invariant**: Maintaining optimal transitions avoids re-evaluating subproblems.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `board = [[1,2,3],[4,0,5]]`  
**Expected Output**: `1`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `board = [[1,2,3],[4,0,5]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `1` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private String[] t = new String[6];
    private int[][] board;

    public int slidingPuzzle(int[][] board) {
        this.board = board;
        String start = gets();
        String end = "123450";
        if (end.equals(start)) {
            return 0;
        }
        Set<String> vis = new HashSet<>();
        Deque<String> q = new ArrayDeque<>();
        q.offer(start);
        vis.add(start);
        int ans = 0;
        while (!q.isEmpty()) {
            ++ans;
            for (int n = q.size(); n > 0; --n) {
                String x = q.poll();
                setb(x);
                for (String y : next()) {
                    if (y.equals(end)) {
                        return ans;
                    }
                    if (!vis.contains(y)) {
                        vis.add(y);
                        q.offer(y);
                    }
                }
            }
        }
        return -1;
    }

    private String gets() {
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 3; ++j) {
                t[i * 3 + j] = String.valueOf(board[i][j]);
            }
        }
        return String.join("", t);
    }

    private void setb(String s) {
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 3; ++j) {
                board[i][j] = s.charAt(i * 3 + j) - '0';
            }
        }
    }

    private int[] find0() {
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 3; ++j) {
                if (board[i][j] == 0) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[] {0, 0};
    }

    private List<String> next() {
        int[] p = find0();
        int i = p[0], j = p[1];
        int[] dirs = {-1, 0, 1, 0, -1};
        List<String> res = new ArrayList<>();
        for (int k = 0; k < 4; ++k) {
            int x = i + dirs[k];
            int y = j + dirs[k + 1];
            if (x >= 0 && x < 2 && y >= 0 && y < 3) {
                swap(i, j, x, y);
                res.add(gets());
                swap(i, j, x, y);
            }
        }
        return res;
    }

    private void swap(int i, int j, int x, int y) {
        int t = board[i][j];
        board[i][j] = board[x][y];
        board[x][y] = t;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        t = [None] * 6

        def gets():
            for i in range(2):
                for j in range(3):
                    t[i * 3 + j] = str(board[i][j])
            return ''.join(t)

        def setb(s):
            for i in range(2):
                for j in range(3):
                    board[i][j] = int(s[i * 3 + j])

        def f():
            res = []
            i, j = next((i, j) for i in range(2) for j in range(3) if board[i][j] == 0)
            for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                x, y = i + a, j + b
                if 0 <= x < 2 and 0 <= y < 3:
                    board[i][j], board[x][y] = board[x][y], board[i][j]
                    res.append(gets())
                    board[i][j], board[x][y] = board[x][y], board[i][j]
            return res

        start = gets()
        end = "123450"
        if start == end:
            return 0
        vis = {start}
        q = deque([start])
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                x = q.popleft()
                setb(x)
                for y in f():
                    if y == end:
                        return ans
                    if y not in vis:
                        vis.add(y)
                        q.append(y)
        return -1
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Boundary states at index 0 and 1.
2. Integer overflow when accumulating large transitions.
3. Base case initialization of unreachable states.

---

### 💬 Follow-Up Questions You Might Get
*Can we optimize space?* Yes, if each state depends only on the previous k states, we can reduce space from O(N) to O(1) using rolling variables.
