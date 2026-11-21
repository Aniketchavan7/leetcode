# 208. Implement Trie (Prefix Tree)

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/implement-trie-prefix-tree/)
[![Topic: Trie](https://img.shields.io/badge/Topic-Trie-blue)](https://leetcode.com/problems/implement-trie-prefix-tree/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "A Trie (Prefix Tree) stores strings character-by-character along directed edges. Each node contains a fixed array of children `TrieNode[26]` and a boolean `isEnd`. To insert, traverse or create child nodes down the word's characters and set isEnd=true on the final node. To search, follow the path; if a node is missing return false; return isEnd on the final node. For startsWith, return true as long as the prefix path exists."

---

### 💡 Intuition & Core Insight
- **Prefix Sharing**: All words sharing a prefix (e.g. 'app', 'apple', 'application') share identical ancestor nodes, enabling O(L) retrieval independent of the total dictionary size.

---

### 🔍 Step-by-Step Visual Dry Run
- insert("apple"): creates path a->p->p->l->e (isEnd=true)
- search("apple"): traverses a->p->p->l->e, isEnd is true -> returns true
- search("app"): reaches 'p', isEnd is false -> returns false
- startsWith("app"): reaches 'p' -> returns true.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Trie {
    private static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd = false;
    }

    private final TrieNode root = new TrieNode();

    public Trie() {}

    public void insert(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (curr.children[idx] == null) {
                curr.children[idx] = new TrieNode();
            }
            curr = curr.children[idx];
        }
        curr.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode node = findNode(word);
        return node != null && node.isEnd;
    }

    public boolean startsWith(String prefix) {
        return findNode(prefix) != null;
    }

    private TrieNode findNode(String str) {
        TrieNode curr = root;
        for (char c : str.toCharArray()) {
            int idx = c - 'a';
            if (curr.children[idx] == null) return null;
            curr = curr.children[idx];
        }
        return curr;
    }
}
```

#### Python 3 Solution
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, s: str):
        curr = self.root
        for c in s:
            if c not in curr.children:
                return None
            curr = curr.children[c]
        return curr
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(L)$ — L is the length of the word/prefix; each character lookup is O(1).
- **Space Complexity**: $\mathcal{O}(N \cdot L)$ — Worst case stores N words of length L with no common prefixes.

---

### ⚠️ Edge Cases & Interview Traps
1. Single-character strings: handled cleanly.
2. Searching prefix that isn't a word: returns false for search, true for startsWith.

---

### 💬 Follow-Up Questions You Might Get
- *How to support wildcard search '.'?* Use DFS over all non-null children (LeetCode 211).
