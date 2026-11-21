# 251. Flatten 2D Vector

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/flatten-2d-vector)
[![Topic: Design & Array & Two Pointers](https://img.shields.io/badge/Topic-Design%20&%20Array%20&%20Two%20Pointers-blue)](https://leetcode.com/problems/flatten-2d-vector)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "By maintaining window boundaries or dual pointers, we convert a quadratic pair search into a linear scan, dynamically expanding or shrinking based on feasibility invariants."

---

### 💡 Intuition & Core Insight
- **Monotonicity**: As the right pointer advances, the search space moves monotonically without backtracking.
- **Window Invariant**: Validating window conditions with a frequency counter guarantees correctness.
- **Two-Ended Traversal**: Squeezing inward from boundaries avoids evaluating redundant pairs.

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
class Vector2D {
    private int i;
    private int j;
    private int[][] vec;

    public Vector2D(int[][] vec) {
        this.vec = vec;
    }

    public int next() {
        forward();
        return vec[i][j++];
    }

    public boolean hasNext() {
        forward();
        return i < vec.length;
    }

    private void forward() {
        while (i < vec.length && j >= vec[i].length) {
            ++i;
            j = 0;
        }
    }
}

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D obj = new Vector2D(vec);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
```

#### Python 3 Solution
```python
class Vector2D:
    def __init__(self, vec: list[list[int]]):
        self.i = 0
        self.j = 0
        self.vec = vec

    def next(self) -> int:
        self.forward()
        ans = self.vec[self.i][self.j]
        self.j += 1
        return ans

    def hasNext(self) -> bool:
        self.forward()
        return self.i < len(self.vec)

    def forward(self):
        while self.i < len(self.vec) and self.j >= len(self.vec[self.i]):
            self.i += 1
            self.j = 0


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(1)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Off-by-one errors on window size (right - left + 1).
2. Empty arrays or arrays with all identical elements.
3. Forgetting to update state counters when shrinking the left boundary.

---

### 💬 Follow-Up Questions You Might Get
*What if the array cannot fit into memory?* We can stream data through a bounded circular buffer or sliding window chunk.
