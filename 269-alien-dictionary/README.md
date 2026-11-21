# 269. Alien Dictionary

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/alien-dictionary)
[![Topic: Depth-First Search & Breadth-First Search & Graph](https://img.shields.io/badge/Topic-Depth-First%20Search%20&%20Breadth-First%20Search%20&%20Graph-blue)](https://leetcode.com/problems/alien-dictionary)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We model the problem as a graph of vertices and edges. Using standard BFS/DFS or Topological Sort / Union-Find, we explore connectivity and paths systematically."

---

### 💡 Intuition & Core Insight
- **Visited State**: Maintaining a visited set prevents infinite cycles in directed/undirected graphs.
- **Topological Invariant**: In-degree tracking identifies dependency resolution order.
- **Connectivity**: Disjoint Set Union (DSU) provides near O(1) amortized path compression.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `words = [&quot;wrt&quot;,&quot;wrf&quot;,&quot;er&quot;,&quot;ett&quot;,&quot;rftt&quot;]`  
**Expected Output**: `&quot;wertf&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `words = [&quot;wrt&quot;,&quot;wrf&quot;,&quot;er&quot;,&quot;ett&quot;,&quot;rftt&quot;]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;wertf&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {

    public String alienOrder(String[] words) {
        boolean[][] g = new boolean[26][26];
        boolean[] s = new boolean[26];
        int cnt = 0;
        int n = words.length;
        for (int i = 0; i < n - 1; ++i) {
            for (char c : words[i].toCharArray()) {
                if (cnt == 26) {
                    break;
                }
                c -= 'a';
                if (!s[c]) {
                    ++cnt;
                    s[c] = true;
                }
            }
            int m = words[i].length();
            for (int j = 0; j < m; ++j) {
                if (j >= words[i + 1].length()) {
                    return "";
                }
                char c1 = words[i].charAt(j), c2 = words[i + 1].charAt(j);
                if (c1 == c2) {
                    continue;
                }
                if (g[c2 - 'a'][c1 - 'a']) {
                    return "";
                }
                g[c1 - 'a'][c2 - 'a'] = true;
                break;
            }
        }
        for (char c : words[n - 1].toCharArray()) {
            if (cnt == 26) {
                break;
            }
            c -= 'a';
            if (!s[c]) {
                ++cnt;
                s[c] = true;
            }
        }

        int[] indegree = new int[26];
        for (int i = 0; i < 26; ++i) {
            for (int j = 0; j < 26; ++j) {
                if (i != j && s[i] && s[j] && g[i][j]) {
                    ++indegree[j];
                }
            }
        }
        Deque<Integer> q = new LinkedList<>();
        for (int i = 0; i < 26; ++i) {
            if (s[i] && indegree[i] == 0) {
                q.offerLast(i);
            }
        }
        StringBuilder ans = new StringBuilder();
        while (!q.isEmpty()) {
            int t = q.pollFirst();
            ans.append((char) (t + 'a'));
            for (int i = 0; i < 26; ++i) {
                if (i != t && s[i] && g[t][i]) {
                    if (--indegree[i] == 0) {
                        q.offerLast(i);
                    }
                }
            }
        }
        return ans.length() < cnt ? "" : ans.toString();
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def alienOrder(self, words: list[str]) -> str:
        g = [[False] * 26 for _ in range(26)]
        s = [False] * 26
        cnt = 0
        n = len(words)
        for i in range(n - 1):
            for c in words[i]:
                if cnt == 26:
                    break
                o = ord(c) - ord('a')
                if not s[o]:
                    cnt += 1
                    s[o] = True
            m = len(words[i])
            for j in range(m):
                if j >= len(words[i + 1]):
                    return ''
                c1, c2 = words[i][j], words[i + 1][j]
                if c1 == c2:
                    continue
                o1, o2 = ord(c1) - ord('a'), ord(c2) - ord('a')
                if g[o2][o1]:
                    return ''
                g[o1][o2] = True
                break
        for c in words[n - 1]:
            if cnt == 26:
                break
            o = ord(c) - ord('a')
            if not s[o]:
                cnt += 1
                s[o] = True

        indegree = [0] * 26
        for i in range(26):
            for j in range(26):
                if i != j and s[i] and s[j] and g[i][j]:
                    indegree[j] += 1
        q = deque()
        ans = []
        for i in range(26):
            if s[i] and indegree[i] == 0:
                q.append(i)
        while q:
            t = q.popleft()
            ans.append(chr(t + ord('a')))
            for i in range(26):
                if s[i] and i != t and g[t][i]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)
        return '' if len(ans) < cnt else ''.join(ans)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(V + E)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(V)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Disconnected graph components.
2. Self-loops and multi-edges between the same vertex pair.
3. Cyclic dependencies causing deadlock.

---

### 💬 Follow-Up Questions You Might Get
*What if edges have arbitrary weights?* Use Dijkstra's algorithm for non-negative weights or Bellman-Ford / SPFA for negative edge weights.
