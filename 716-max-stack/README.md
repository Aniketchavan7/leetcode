# 716. Max Stack

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/max-stack)
[![Topic: Stack & Design & Linked List](https://img.shields.io/badge/Topic-Stack%20&%20Design%20&%20Linked%20List-blue)](https://leetcode.com/problems/max-stack)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "When manipulating linked lists in **Max Stack**, pointer management and dummy head techniques allow in-place operations with O(1) auxiliary memory while avoiding boundary null-pointer checks."

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
class Node {
    public int val;
    public Node prev, next;

    public Node() {
    }

    public Node(int val) {
        this.val = val;
    }
}

class DoubleLinkedList {
    private final Node head = new Node();
    private final Node tail = new Node();

    public DoubleLinkedList() {
        head.next = tail;
        tail.prev = head;
    }

    public Node append(int val) {
        Node node = new Node(val);
        node.next = tail;
        node.prev = tail.prev;
        tail.prev = node;
        node.prev.next = node;
        return node;
    }

    public static Node remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        return node;
    }

    public Node pop() {
        return remove(tail.prev);
    }

    public int peek() {
        return tail.prev.val;
    }
}

class MaxStack {
    private DoubleLinkedList stk = new DoubleLinkedList();
    private TreeMap<Integer, List<Node>> tm = new TreeMap<>();

    public MaxStack() {
    }

    public void push(int x) {
        Node node = stk.append(x);
        tm.computeIfAbsent(x, k -> new ArrayList<>()).add(node);
    }

    public int pop() {
        Node node = stk.pop();
        List<Node> nodes = tm.get(node.val);
        int x = nodes.remove(nodes.size() - 1).val;
        if (nodes.isEmpty()) {
            tm.remove(node.val);
        }
        return x;
    }

    public int top() {
        return stk.peek();
    }

    public int peekMax() {
        return tm.lastKey();
    }

    public int popMax() {
        int x = peekMax();
        List<Node> nodes = tm.get(x);
        Node node = nodes.remove(nodes.size() - 1);
        if (nodes.isEmpty()) {
            tm.remove(x);
        }
        DoubleLinkedList.remove(node);
        return x;
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.peekMax();
 * int param_5 = obj.popMax();
 */
```

#### Python 3 Solution
```python
class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev: Union[Node, None] = None
        self.next: Union[Node, None] = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, val) -> Node:
        node = Node(val)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        return node

    @staticmethod
    def remove(node) -> Node:
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def pop(self) -> Node:
        return self.remove(self.tail.prev)

    def peek(self):
        return self.tail.prev.val


class MaxStack:
    def __init__(self):
        self.stk = DoubleLinkedList()
        self.sl = SortedList(key=lambda x: x.val)

    def push(self, x: int) -> None:
        node = self.stk.append(x)
        self.sl.add(node)

    def pop(self) -> int:
        node = self.stk.pop()
        self.sl.remove(node)
        return node.val

    def top(self) -> int:
        return self.stk.peek()

    def peekMax(self) -> int:
        return self.sl[-1].val

    def popMax(self) -> int:
        node = self.sl.pop()
        DoubleLinkedList.remove(node)
        return node.val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
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
