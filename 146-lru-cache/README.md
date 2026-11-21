# 146. LRU Cache

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/lru-cache/)
[![Topic: Design / Doubly Linked List](https://img.shields.io/badge/Topic-Design%20/%20Doubly%20Linked%20List-blue)](https://leetcode.com/problems/lru-cache/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "An LRU Cache requires O(1) get and put operations. We achieve this by pairing a Hash Map (for O(1) key-to-node lookup) with a Doubly Linked List with dummy head and tail (for O(1) node insertion and removal). When a key is accessed or updated, we move its node to the head (most recently used). When capacity is exceeded, we evict the node right before the tail (least recently used)."

---

### 💡 Intuition & Core Insight
- **Why Doubly Linked List?**: Singly linked lists require O(N) to delete a node given its pointer (need to find predecessor). Doubly linked nodes can remove themselves in O(1) using `node.prev.next = node.next`.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: Capacity 2
- put(1, 1): Map={1: N1}, DLL: Head <-> N1 <-> Tail
- put(2, 2): Map={1: N1, 2: N2}, DLL: Head <-> N2 <-> N1 <-> Tail
- get(1): return 1, move N1 to head -> DLL: Head <-> N1 <-> N2 <-> Tail
- put(3, 3): Capacity exceeded! Evict tail.prev (N2) -> DLL: Head <-> N3 <-> N1 <-> Tail
- get(2): not found -> return -1.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class LRUCache {
    class Node {
        int key, val;
        Node prev, next;
        Node(int k, int v) { key = k; val = v; }
    }

    private final int capacity;
    private final Map<Integer, Node> map = new HashMap<>();
    private final Node head = new Node(0, 0);
    private final Node tail = new Node(0, 0);

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        if (!map.containsKey(key)) return -1;
        Node node = map.get(key);
        remove(node);
        insertAtHead(node);
        return node.val;
    }

    public void put(int key, int value) {
        if (map.containsKey(key)) {
            remove(map.get(key));
        }
        Node node = new Node(key, value);
        insertAtHead(node);
        map.put(key, node);

        if (map.size() > capacity) {
            Node lru = tail.prev;
            remove(lru);
            map.remove(lru.key);
        }
    }

    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void insertAtHead(Node node) {
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }
}
```

#### Python 3 Solution
```python
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._insert_at_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        node = Node(key, value)
        self._insert_at_head(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_head(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(1)$ — Both get and put execute in strictly O(1) time.
- **Space Complexity**: $\mathcal{O}(C)$ — Stores at most C key-value pairs where C is capacity.

---

### ⚠️ Edge Cases & Interview Traps
1. Capacity 1: every new key evicts the existing one.
2. Overwriting existing key: updates value and marks most recently used without increasing size.

---

### 💬 Follow-Up Questions You Might Get
- *How to make LRU Cache thread-safe?* Use synchronized blocks or ReadWriteLock on map and DLL operations.
