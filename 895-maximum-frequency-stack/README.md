# 895. Maximum Frequency Stack

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/maximum-frequency-stack)
[![Topic: Stack & Design & Hash Table](https://img.shields.io/badge/Topic-Stack%20&%20Design%20&%20Hash%20Table-blue)](https://leetcode.com/problems/maximum-frequency-stack)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We use a monotonic stack to maintain elements in sorted order. As we iterate through the input, elements that violate the monotonicity are popped, resolving next greater/smaller queries in linear time."

---

### 💡 Intuition & Core Insight
- **Monotonic Invariant**: Stack elements remain strictly increasing or decreasing.
- **One-Pass Resolution**: Each element is pushed and popped at most once, yielding amortized O(N) time.
- **Local vs Global Extremum**: Stack top immediately exposes the nearest boundary.

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
class FreqStack {
    private Map<Integer, Integer> cnt = new HashMap<>();
    private PriorityQueue<int[]> q
        = new PriorityQueue<>((a, b) -> a[0] == b[0] ? b[1] - a[1] : b[0] - a[0]);
    private int ts;

    public FreqStack() {
    }

    public void push(int val) {
        cnt.put(val, cnt.getOrDefault(val, 0) + 1);
        q.offer(new int[] {cnt.get(val), ++ts, val});
    }

    public int pop() {
        int val = q.poll()[2];
        cnt.put(val, cnt.get(val) - 1);
        return val;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(val);
 * int param_2 = obj.pop();
 */
```

#### Python 3 Solution
```python
class FreqStack:
    def __init__(self):
        self.cnt = defaultdict(int)
        self.q = []
        self.ts = 0

    def push(self, val: int) -> None:
        self.ts += 1
        self.cnt[val] += 1
        heappush(self.q, (-self.cnt[val], -self.ts, val))

    def pop(self) -> int:
        val = heappop(self.q)[2]
        self.cnt[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Empty stack pops.
2. Strict vs non-strict inequality when popping.
3. Elements remaining on the stack after array traversal ends.

---

### 💬 Follow-Up Questions You Might Get
*What if the array is circular?* Traverse the array twice (length 2N) using modulo indexing (i % N).
