# 497. Random Point in Non-overlapping Rectangles

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles)
[![Topic: Reservoir Sampling & Array & Math](https://img.shields.io/badge/Topic-Reservoir%20Sampling%20&%20Array%20&%20Math-blue)](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles)

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
class Solution {
    private int[] s;
    private int[][] rects;
    private Random random = new Random();

    public Solution(int[][] rects) {
        int n = rects.length;
        s = new int[n + 1];
        for (int i = 0; i < n; ++i) {
            s[i + 1] = s[i] + (rects[i][2] - rects[i][0] + 1) * (rects[i][3] - rects[i][1] + 1);
        }
        this.rects = rects;
    }

    public int[] pick() {
        int n = rects.length;
        int v = 1 + random.nextInt(s[n]);
        int left = 0, right = n;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (s[mid] >= v) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        int[] rect = rects[left - 1];
        return new int[] {rect[0] + random.nextInt(rect[2] - rect[0] + 1),
            rect[1] + random.nextInt(rect[3] - rect[1] + 1)};
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(rects);
 * int[] param_1 = obj.pick();
 */
```

#### Python 3 Solution
```python
class Solution:
    def __init__(self, rects: list[list[int]]):
        self.rects = rects
        self.s = [0] * len(rects)
        for i, (x1, y1, x2, y2) in enumerate(rects):
            self.s[i] = self.s[i - 1] + (x2 - x1 + 1) * (y2 - y1 + 1)

    def pick(self) -> list[int]:
        v = random.randint(1, self.s[-1])
        idx = bisect_left(self.s, v)
        x1, y1, x2, y2 = self.rects[idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
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
