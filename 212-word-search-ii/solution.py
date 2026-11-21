class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = {}
        for word in words:
            curr = trie
            for c in word:
                curr = curr.setdefault(c, {})
            curr['#'] = word

        res = []
        m, n = len(board), len(board[0])

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node:
                return
            nxt = node[char]
            if '#' in nxt:
                res.append(nxt.pop('#'))

            board[r][c] = '$'
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '$':
                    dfs(nr, nc, nxt)
            board[r][c] = char

            if not nxt:
                node.pop(char)

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)
        return res
