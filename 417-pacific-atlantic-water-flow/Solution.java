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
