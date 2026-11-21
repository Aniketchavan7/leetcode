# 460. LFU Cache

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/lfu-cache)
[![Topic: Design & Hash Table & Linked List](https://img.shields.io/badge/Topic-Design%20&%20Hash%20Table%20&%20Linked%20List-blue)](https://leetcode.com/problems/lfu-cache)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "When manipulating linked lists in **LFU Cache**, pointer management and dummy head techniques allow in-place operations with O(1) auxiliary memory while avoiding boundary null-pointer checks."

---

### 💡 Intuition & Core Insight
- **Pointer Mechanics**: Using a dummy node simplifies edge cases where the head of the list changes.
- **Carry & Traversal**: Traversing node-by-node with carry propagation mirrors manual column addition.
- **In-place Re-wiring**: Reusing existing node pointers eliminates unnecessary heap allocations.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `Standard sample testcase`  
**Expected Output**: `Computed result`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `Input elements` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `Optimal Result` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class LFUCache {

    private final Map<Integer, Node> map;
    private final Map<Integer, DoublyLinkedList> freqMap;
    private final int capacity;
    private int minFreq;

    public LFUCache(int capacity) {
        this.capacity = capacity;
        map = new HashMap<>(capacity, 1);
        freqMap = new HashMap<>();
    }

    public int get(int key) {
        if (capacity == 0) {
            return -1;
        }
        if (!map.containsKey(key)) {
            return -1;
        }
        Node node = map.get(key);
        incrFreq(node);
        return node.value;
    }

    public void put(int key, int value) {
        if (capacity == 0) {
            return;
        }
        if (map.containsKey(key)) {
            Node node = map.get(key);
            node.value = value;
            incrFreq(node);
            return;
        }
        if (map.size() == capacity) {
            DoublyLinkedList list = freqMap.get(minFreq);
            map.remove(list.removeLast().key);
        }
        Node node = new Node(key, value);
        addNode(node);
        map.put(key, node);
        minFreq = 1;
    }

    private void incrFreq(Node node) {
        int freq = node.freq;
        DoublyLinkedList list = freqMap.get(freq);
        list.remove(node);
        if (list.isEmpty()) {
            freqMap.remove(freq);
            if (freq == minFreq) {
                minFreq++;
            }
        }
        node.freq++;
        addNode(node);
    }

    private void addNode(Node node) {
        int freq = node.freq;
        DoublyLinkedList list = freqMap.getOrDefault(freq, new DoublyLinkedList());
        list.addFirst(node);
        freqMap.put(freq, list);
    }

    private static class Node {
        int key;
        int value;
        int freq;
        Node prev;
        Node next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
            this.freq = 1;
        }
    }

    private static class DoublyLinkedList {

        private final Node head;
        private final Node tail;

        public DoublyLinkedList() {
            head = new Node(-1, -1);
            tail = new Node(-1, -1);
            head.next = tail;
            tail.prev = head;
        }

        public void addFirst(Node node) {
            node.prev = head;
            node.next = head.next;
            head.next.prev = node;
            head.next = node;
        }

        public Node remove(Node node) {
            node.next.prev = node.prev;
            node.prev.next = node.next;
            node.next = null;
            node.prev = null;
            return node;
        }

        public Node removeLast() {
            return remove(tail.prev);
        }

        public boolean isEmpty() {
            return head.next == tail;
        }
    }
}
```

#### Python 3 Solution
```python
class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_first(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node: Node) -> Node:
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next, node.prev = None, None
        return node

    def remove_last(self) -> Node:
        return self.remove(self.tail.prev)

    def is_empty(self) -> bool:
        return self.head.next == self.tail


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.map = defaultdict(Node)
        self.freq_map = defaultdict(DoublyLinkedList)

    def get(self, key: int) -> int:
        if self.capacity == 0 or key not in self.map:
            return -1
        node = self.map[key]
        self.incr_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.incr_freq(node)
            return
        if len(self.map) == self.capacity:
            ls = self.freq_map[self.min_freq]
            node = ls.remove_last()
            self.map.pop(node.key)
        node = Node(key, value)
        self.add_node(node)
        self.map[key] = node
        self.min_freq = 1

    def incr_freq(self, node: Node) -> None:
        freq = node.freq
        ls = self.freq_map[freq]
        ls.remove(node)
        if ls.is_empty():
            self.freq_map.pop(freq)
            if freq == self.min_freq:
                self.min_freq += 1
        node.freq += 1
        self.add_node(node)

    def add_node(self, node: Node) -> None:
        freq = node.freq
        ls = self.freq_map[freq]
        ls.add_first(node)
        self.freq_map[freq] = ls


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(1)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Null head or empty list edge cases.
2. Lists of unequal lengths.
3. Lingering carry value after exhausting both lists.

---

### 💬 Follow-Up Questions You Might Get
*What if the list contains cycles?* We can employ Floyd's Cycle-Finding algorithm (fast and slow pointers) to detect or break cycles.
