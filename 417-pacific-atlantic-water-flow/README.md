# 417. Pacific Atlantic Water Flow

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/pacific-atlantic-water-flow/)
[![Topic: Graph / Multi-source BFS](https://img.shields.io/badge/Topic-Graph%20/%20Multi-source%20BFS-blue)](https://leetcode.com/problems/pacific-atlantic-water-flow/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Water flows downhill from cells to the Pacific (top/left) and Atlantic (bottom/right). Instead of running DFS from every cell downhill (which is slow and repetitive), we invert the problem: flow water UPHILL from the ocean boundaries! 1) Run BFS/DFS from the Pacific borders to find all cells reachable by Pacific. 2) Run BFS/DFS from Atlantic borders. 3) The intersection of cells reachable by both oceans is our answer."

---

### 💡 Intuition & Core Insight
- **Reverse Flow Direction**: Flowing from the ocean inward is a multi-source reachability problem that visits each cell at most twice.

---

### 🔍 Step-by-Step Visual Dry Run
- Pacific BFS starts from row 0 and col 0, climbing cells where neighbor.height >= curr.height.
- Atlantic BFS starts from row m-1 and col n-1, climbing similarly.
- Cells where `pacific[r][c] && atlantic[r][c]` are added to output.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        int m = heights.length, n = heights[0].length;
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0, heights[i][0]);
            dfs(heights, atlantic, i, n - 1, heights[i][n - 1]);
        }
        for (int j = 0; j < n; j++) {
            dfs(heights, pacific, 0, j, heights[0][j]);
            dfs(heights, atlantic, m - 1, j, heights[m - 1][j]);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    res.add(Arrays.asList(i, j));
                }
            }
        }
        return res;
    }

    private void dfs(int[][] heights, boolean[][] ocean, int r, int c, int prevHeight) {
        if (r < 0 || r >= heights.length || c < 0 || c >= heights[0].length || ocean[r][c] || heights[r][c] < prevHeight) {
            return;
        }
        ocean[r][c] = true;
        dfs(heights, ocean, r + 1, c, heights[r][c]);
        dfs(heights, ocean, r - 1, c, heights[r][c]);
        dfs(heights, ocean, r, c + 1, heights[r][c]);
        dfs(heights, ocean, r, c - 1, heights[r][c]);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prev_height):
            if ((r, c) in visit or r < 0 or c < 0 or r == m or c == n or heights[r][c] < prev_height):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(n):
            dfs(0, c, pac, heights[0][c])
            dfs(m - 1, c, atl, heights[m - 1][c])
        for r in range(m):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, n - 1, atl, heights[r][n - 1])

        return [[r, c] for (r, c) in pac.intersection(atl)]
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(M \cdot N)$ — Each cell is visited at most twice (once for Pacific, once for Atlantic).
- **Space Complexity**: $\mathcal{O}(M \cdot N)$ — Matrices or sets tracking ocean reachability.

---

### ⚠️ Edge Cases & Interview Traps
1. 1x1 grid: cell touches both oceans, returns [[0, 0]].
2. Flat heights: all cells equal, every cell reaches both oceans.

---

### 💬 Follow-Up Questions You Might Get
- *Can we use BFS instead of DFS?* Yes, queue-based multi-source BFS avoids deep recursion call stacks.
