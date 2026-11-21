# 133. Clone Graph

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/clone-graph/)
[![Topic: Graph / BFS/DFS](https://img.shields.io/badge/Topic-Graph%20/%20BFS/DFS-blue)](https://leetcode.com/problems/clone-graph/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To create a deep copy of a connected undirected graph: We maintain a Hash Map mapping `originalNode -> clonedNode`. When visiting a node via DFS, if it's already in the map, return the cloned copy. Otherwise, create the new clone node, register it in the map, and recursively clone each of its neighbors and add them to clone.neighbors."

---

### 💡 Intuition & Core Insight
- **Cycle Handling via Visited Map**: Undirected graphs contain cycles. Registering the clone in the map BEFORE recurring into neighbors prevents infinite recursion loops.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `1 -- 2, 2 -- 3, 3 -- 4, 4 -- 1`
- clone(1): create C1, map[1]=C1
  - neighbor 2: clone(2) -> create C2, map[2]=C2
    - neighbor 3: clone(3) -> create C3, map[3]=C3
      - neighbor 4: clone(4) -> create C4, map[4]=C4
        - neighbor 1: map contains 1 -> returns C1 directly! Closes cycle safely.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private final Map<Node, Node> map = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) return null;
        if (map.containsKey(node)) return map.get(node);

        Node clone = new Node(node.val);
        map.put(node, clone);

        for (Node neighbor : node.neighbors) {
            clone.neighbors.add(cloneGraph(neighbor));
        }
        return clone;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned = {}

        def dfs(curr):
            if curr in cloned:
                return cloned[curr]
            copy = Node(curr.val)
            cloned[curr] = copy
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(V + E)$ — Visits each vertex V and traverses each undirected edge E once.
- **Space Complexity**: $\mathcal{O}(V)$ — Hash map and recursion stack store up to V vertices.

---

### ⚠️ Edge Cases & Interview Traps
1. Null input graph: returns null.
2. Single node with no neighbors: returns clone with empty neighbor list.

---

### 💬 Follow-Up Questions You Might Get
- *Can we solve this using BFS?* Yes, use a Queue and clone neighbor nodes when enqueueing.
