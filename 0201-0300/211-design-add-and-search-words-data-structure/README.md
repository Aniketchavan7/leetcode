# 211. Design Add and Search Words Data Structure

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
[![Topic: Trie / DFS](https://img.shields.io/badge/Topic-Trie%20/%20DFS-blue)](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We store words in a Trie. For `search(word)`, if the character is a standard letter, follow its single child branch. If the character is '.', branch recursively via DFS into all 26 non-null children. If any child path returns true, the word is found."

---

### 💡 Intuition & Core Insight
- **Trie Prunes Invalid Paths**: Even with wildcards, if an edge doesn't exist, search terminates immediately without exploring whole subtrees.

---

### 🔍 Step-by-Step Visual Dry Run
- addWord("bad"), addWord("dad"), addWord("mad")
- search("pad"): 'p' not in root -> false
- search(".ad"): '.' tries 'b', 'd', 'm'. 'b'->'a'->'d' matches! -> true.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class WordDictionary {
    private static class Node {
        Node[] children = new Node[26];
        boolean isEnd = false;
    }

    private final Node root = new Node();

    public WordDictionary() {}

    public void addWord(String word) {
        Node curr = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (curr.children[idx] == null) curr.children[idx] = new Node();
            curr = curr.children[idx];
        }
        curr.isEnd = true;
    }

    public boolean search(String word) {
        return dfs(word, 0, root);
    }

    private boolean dfs(String word, int idx, Node curr) {
        if (curr == null) return false;
        if (idx == word.length()) return curr.isEnd;

        char c = word.charAt(idx);
        if (c == '.') {
            for (Node child : curr.children) {
                if (child != null && dfs(word, idx + 1, child)) {
                    return true;
                }
            }
            return false;
        } else {
            return dfs(word, idx + 1, curr.children[c - 'a']);
        }
    }
}
```

#### Python 3 Solution
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            if idx == len(word):
                return node.is_end
            c = word[idx]
            if c == '.':
                for child in node.children.values():
                    if dfs(idx + 1, child):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(idx + 1, node.children[c])

        return dfs(0, self.root)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(M)$ — O(M) for words without wildcards where M is length; O(26^M) worst-case if all characters are '.' with full branching.
- **Space Complexity**: $\mathcal{O}(N \cdot M)$ — Space to store words in the Trie.

---

### ⚠️ Edge Cases & Interview Traps
1. Search string consisting solely of dots "...": searches all paths of length 3.
2. Word length greater than any stored word: terminates false at null node.

---

### 💬 Follow-Up Questions You Might Get
- *How to optimize if '.' is very frequent?* Index words by word length in separate hash maps.
