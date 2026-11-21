# 212. Word Search II

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/word-search-ii/)
[![Topic: Trie + Backtracking](https://img.shields.io/badge/Topic-Trie%20+%20Backtracking-blue)](https://leetcode.com/problems/word-search-ii/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Instead of running a separate matrix DFS search for every word in the dictionary (which would be slow), we build a Trie of all words and search the 2D grid once! Starting from each grid cell, DFS walks adjacent cells while simultaneously stepping down the Trie. When a Trie node marks a complete word, add it to our result list and clear the word mark to prevent duplicate additions. If a Trie branch becomes empty, prune it."

---

### 💡 Intuition & Core Insight
- **Simultaneous Prefix Pruning**: If the board prefix 'zxy' is not in the Trie, DFS backtracks immediately in O(1), pruning millions of fruitless board exploration paths.

---

### 🔍 Step-by-Step Visual Dry Run
- Board contains ["o","a","a","n"], ["e","t","a","e"], ["i","h","k","r"], ["i","f","l","v"]
- Trie holds "oath", "pea", "eat", "rain"
- Starting at (0, 0) 'o': matches Trie root child 'o' -> moves to (1, 0) 'a' -> 't' -> 'h' -> found "oath"!

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        String word = null;
    }

    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = new TrieNode();
        for (String w : words) {
            TrieNode curr = root;
            for (char c : w.toCharArray()) {
                int idx = c - 'a';
                if (curr.children[idx] == null) curr.children[idx] = new TrieNode();
                curr = curr.children[idx];
            }
            curr.word = w;
        }

        List<String> res = new ArrayList<>();
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dfs(board, i, j, root, res);
            }
        }
        return res;
    }

    private void dfs(char[][] board, int r, int c, TrieNode node, List<String> res) {
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] == '#') return;

        char ch = board[r][c];
        TrieNode next = node.children[ch - 'a'];
        if (next == null) return;

        if (next.word != null) {
            res.add(next.word);
            next.word = null; // Prevent duplicates
        }

        board[r][c] = '#'; // Mark visited
        dfs(board, r + 1, c, next, res);
        dfs(board, r - 1, c, next, res);
        dfs(board, r, c + 1, next, res);
        dfs(board, r, c - 1, next, res);
        board[r][c] = ch; // Backtrack
    }
}
```

#### Python 3 Solution
```python
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
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(M \cdot N \cdot 4^{L})$ — M x N board cells, each DFS branches up to 4 directions bounded by word length L and pruned heavily by Trie lookups.
- **Space Complexity**: $\mathcal{O}(W \cdot L)$ — Space to store W words of length L in the Trie.

---

### ⚠️ Edge Cases & Interview Traps
1. Duplicate words found via different paths: setting `next.word = null` guarantees each word is added at most once.
2. Single cell board: checks 1-character words cleanly.

---

### 💬 Follow-Up Questions You Might Get
- *How to prune dead Trie branches?* Remove leaf nodes after all words below it have been matched.
