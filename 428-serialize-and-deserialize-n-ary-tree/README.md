# 428. Serialize and Deserialize N-ary Tree

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree)
[![Topic: Tree & Depth-First Search & Breadth-First Search](https://img.shields.io/badge/Topic-Tree%20&%20Depth-First%20Search%20&%20Breadth-First%20Search-blue)](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "For tree structures, we leverage recursive DFS or iterative BFS to traverse nodes. In **Serialize and Deserialize N-ary Tree**, processing each node once while maintaining tree invariants allows linear-time resolution."

---

### 💡 Intuition & Core Insight
- **Recursive Invariant**: At each subtree, we compute left and right subtree properties and aggregate the result.
- **Traversal Choice**: Pre-order / In-order / Post-order aligns naturally with tree height, sum, or path validation.
- **Stack Depth**: Auxiliary space is bounded by the height of the tree.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`  
**Expected Output**: `[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Codec {
    public String serialize(Node root) {
        if (root == null) {
            return "";
        }
        List<String> ans = new ArrayList<>();
        Deque<Node> q = new ArrayDeque<>();
        ans.add(String.valueOf(root.val));
        q.offer(root);
        while (!q.isEmpty()) {
            Node node = q.poll();
            if (node.children != null) {
                for (Node child : node.children) {
                    ans.add(String.valueOf(child.val));
                    q.offer(child);
                }
            }
            ans.add("#");
        }
        return String.join(",", ans);
    }

    public Node deserialize(String data) {
        if ("".equals(data)) {
            return null;
        }
        String[] vals = data.split(",");
        Node root = new Node(Integer.parseInt(vals[0]), new ArrayList<>());
        Deque<Node> q = new ArrayDeque<>();
        q.offer(root);
        int i = 1;
        while (!q.isEmpty()) {
            Node node = q.poll();
            while (!"#".equals(vals[i])) {
                Node child = new Node(Integer.parseInt(vals[i++]), new ArrayList<>());
                node.children.add(child);
                q.offer(child);
            }
            ++i;
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
```

#### Python 3 Solution
```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[list['Node']] = None):
        self.val = val
        self.children = children
"""


class Codec:
    def serialize(self, root: 'Node') -> str:
        if root is None:
            return ''
        ans = [str(root.val)]
        q = deque([root])
        while q:
            node = q.popleft()
            for child in node.children or []:
                ans.append(str(child.val))
                q.append(child)
            ans.append('#')
        return ','.join(ans)

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        vals = data.split(',')
        root = Node(int(vals[0]), [])
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            while vals[i] != '#':
                child = Node(int(vals[i]), [])
                node.children.append(child)
                q.append(child)
                i += 1
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(H)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Skewed trees where height H = N leading to recursion stack overflow.
2. Single-node trees or empty tree roots (root == null).
3. Handling leaf nodes vs single-child nodes.

---

### 💬 Follow-Up Questions You Might Get
*Can we do this in O(1) space?* Morris Traversal can achieve O(1) extra space by threading binary trees.
