# 855. Exam Room

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/exam-room)
[![Topic: Design & Ordered Set & Heap (Priority Queue)](https://img.shields.io/badge/Topic-Design%20&%20Ordered%20Set%20&%20Heap%20(Priority%20Queue)-blue)](https://leetcode.com/problems/exam-room)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "By maintaining a min-heap or max-heap of size K, we process dynamic streams or Top-K queries in O(N log K) time without sorting the entire collection."

---

### 💡 Intuition & Core Insight
- **Bounded Memory**: Restricting heap size to K keeps space bounded and insertion at O(log K).
- **Extremum Access**: The root always exposes the current threshold in O(1) time.
- **Streaming Feasibility**: New incoming data is evaluated against the root in constant time before heapifying.

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
class ExamRoom {
    private TreeSet<int[]> ts = new TreeSet<>((a, b) -> {
        int d1 = dist(a), d2 = dist(b);
        return d1 == d2 ? a[0] - b[0] : d2 - d1;
    });
    private Map<Integer, Integer> left = new HashMap<>();
    private Map<Integer, Integer> right = new HashMap<>();
    private int n;

    public ExamRoom(int n) {
        this.n = n;
        add(new int[] {-1, n});
    }

    public int seat() {
        int[] s = ts.first();
        int p = (s[0] + s[1]) >> 1;
        if (s[0] == -1) {
            p = 0;
        } else if (s[1] == n) {
            p = n - 1;
        }
        del(s);
        add(new int[] {s[0], p});
        add(new int[] {p, s[1]});
        return p;
    }

    public void leave(int p) {
        int l = left.get(p), r = right.get(p);
        del(new int[] {l, p});
        del(new int[] {p, r});
        add(new int[] {l, r});
    }

    private int dist(int[] s) {
        int l = s[0], r = s[1];
        return l == -1 || r == n ? r - l - 1 : (r - l) >> 1;
    }

    private void add(int[] s) {
        ts.add(s);
        left.put(s[1], s[0]);
        right.put(s[0], s[1]);
    }

    private void del(int[] s) {
        ts.remove(s);
        left.remove(s[1]);
        right.remove(s[0]);
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(n);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */
```

#### Python 3 Solution
```python
class ExamRoom:
    def __init__(self, n: int):
        def dist(x):
            l, r = x
            return r - l - 1 if l == -1 or r == n else (r - l) >> 1

        self.n = n
        self.ts = SortedList(key=lambda x: (-dist(x), x[0]))
        self.left = {}
        self.right = {}
        self.add((-1, n))

    def seat(self) -> int:
        s = self.ts[0]
        p = (s[0] + s[1]) >> 1
        if s[0] == -1:
            p = 0
        elif s[1] == self.n:
            p = self.n - 1
        self.delete(s)
        self.add((s[0], p))
        self.add((p, s[1]))
        return p

    def leave(self, p: int) -> None:
        l, r = self.left[p], self.right[p]
        self.delete((l, p))
        self.delete((p, r))
        self.add((l, r))

    def add(self, s):
        self.ts.add(s)
        self.left[s[1]] = s[0]
        self.right[s[0]] = s[1]

    def delete(self, s):
        self.ts.remove(s)
        self.left.pop(s[1])
        self.right.pop(s[0])


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log K)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(K)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Inverting comparator logic (min-heap vs max-heap).
2. Handling duplicate frequency or tie-breaking order.
3. Empty heap exceptions.

---

### 💬 Follow-Up Questions You Might Get
*Can we do Top-K in O(N) average time?* Quickselect achieves O(N) average time complexity.
