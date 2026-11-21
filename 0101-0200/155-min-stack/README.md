# 155. Min Stack

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/min-stack/)
[![Topic: Stack Design](https://img.shields.io/badge/Topic-Stack%20Design-blue)](https://leetcode.com/problems/min-stack/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To support push, pop, top, and retrieving the minimum element in O(1) time, we maintain two parallel stacks: a primary `stack` storing all values, and a `minStack` where each entry represents the minimum value present in the primary stack at that depth. When pushing x, push min(x, currentMin) to minStack."

---

### 💡 Intuition & Core Insight
- **Prefix Minimum Snapshot**: Every stack height corresponds to a unique history of operations. Storing the minimum along with each layer freezes the historical minimum for that exact stack state.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `push(-2), push(0), push(-3), getMin(), pop(), top(), getMin()`
- push(-2): stack=[-2], minStack=[-2]
- push(0): stack=[-2, 0], minStack=[-2, -2]
- push(-3): stack=[-2, 0, -3], minStack=[-2, -2, -3]
- getMin() -> top of minStack is -3
- pop(): pops -3 from both -> stack=[-2, 0], minStack=[-2, -2]
- top() -> 0
- getMin() -> -2.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class MinStack {
    private final Deque<Integer> stack = new ArrayDeque<>();
    private final Deque<Integer> minStack = new ArrayDeque<>();

    public MinStack() {}

    public void push(int val) {
        stack.push(val);
        int currentMin = minStack.isEmpty() ? val : Math.min(val, minStack.peek());
        minStack.push(currentMin);
    }

    public void pop() {
        stack.pop();
        minStack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}
```

#### Python 3 Solution
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(1)$ — All operations (push, pop, top, getMin) execute in O(1) time.
- **Space Complexity**: $\mathcal{O}(N)$ — Stores 2N integers across both stacks.

---

### ⚠️ Edge Cases & Interview Traps
1. Negative numbers: min correctly compares negative values.
2. Duplicate minimums: pushing duplicate min records duplicates in minStack, so popping one doesn't lose the min.

---

### 💬 Follow-Up Questions You Might Get
- *Can this be done using only a single stack?* Yes, store differences `val - min` or pairs `(val, min)` in one stack.
