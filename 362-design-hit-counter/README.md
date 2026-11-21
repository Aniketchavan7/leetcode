# 362. Design Hit Counter

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/design-hit-counter)
[![Topic: Design & Queue & Array](https://img.shields.io/badge/Topic-Design%20&%20Queue%20&%20Array-blue)](https://leetcode.com/problems/design-hit-counter)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Given a monotonic condition or sorted space, we eliminate half the search candidates at each iteration, achieving optimal logarithmic time."

---

### 💡 Intuition & Core Insight
- **Search Space Invariant**: The target value or optimal boundary always lies within [left, right].
- **Mid Calculation**: Using left + (right - left) // 2 prevents 32-bit integer overflow.
- **Termination**: Strict comparison bounds avoid infinite loops on 2-element ranges.

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
class HitCounter {
    private List<Integer> ts = new ArrayList<>();

    public HitCounter() {
    }

    public void hit(int timestamp) {
        ts.add(timestamp);
    }

    public int getHits(int timestamp) {
        int l = search(timestamp - 300 + 1);
        return ts.size() - l;
    }

    private int search(int x) {
        int l = 0, r = ts.size();
        while (l < r) {
            int mid = (l + r) >> 1;
            if (ts.get(mid) >= x) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
}

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */
```

#### Python 3 Solution
```python
class HitCounter:

    def __init__(self):
        self.ts = []

    def hit(self, timestamp: int) -> None:
        self.ts.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        return len(self.ts) - bisect_left(self.ts, timestamp - 300 + 1)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(1)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Integer overflow in (left + right) / 2 in Java/C++.
2. Choosing between left < right vs left <= right.
3. Updating left = mid vs left = mid + 1 depending on target inclusion.

---

### 💬 Follow-Up Questions You Might Get
*Can binary search be applied to unsorted inputs?* Yes, if the answer space possesses a monotonic predicate (Binary Search on Answer).
