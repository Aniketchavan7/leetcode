# 825. Friends Of Appropriate Ages

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/friends-of-appropriate-ages)
[![Topic: Array & Two Pointers & Binary Search](https://img.shields.io/badge/Topic-Array%20&%20Two%20Pointers%20&%20Binary%20Search-blue)](https://leetcode.com/problems/friends-of-appropriate-ages)

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
**Sample Input**: `ages = [16,16]`  
**Expected Output**: `2`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `ages = [16,16]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `2` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int numFriendRequests(int[] ages) {
        final int m = 121;
        int[] cnt = new int[m];
        for (int x : ages) {
            ++cnt[x];
        }
        int ans = 0;
        for (int ax = 1; ax < m; ++ax) {
            for (int ay = 1; ay < m; ++ay) {
                if (!(ay <= 0.5 * ax + 7 || ay > ax || (ay > 100 && ax < 100))) {
                    ans += cnt[ax] * (cnt[ay] - (ax == ay ? 1 : 0));
                }
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        cnt = [0] * 121
        for x in ages:
            cnt[x] += 1
        ans = 0
        for ax, x in enumerate(cnt):
            for ay, y in enumerate(cnt):
                if not (ay <= 0.5 * ax + 7 or ay > ax or (ay > 100 and ax < 100)):
                    ans += x * (y - int(ax == ay))
        return ans
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
