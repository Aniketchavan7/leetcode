# 400. Nth Digit

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/nth-digit)
[![Topic: Math & Binary Search](https://img.shields.io/badge/Topic-Math%20&%20Binary%20Search-blue)](https://leetcode.com/problems/nth-digit)

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
**Sample Input**: `n = 3`  
**Expected Output**: `3`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `n = 3` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `3` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int findNthDigit(int n) {
        int k = 1, cnt = 9;
        while ((long) k * cnt < n) {
            n -= k * cnt;
            ++k;
            cnt *= 10;
        }
        int num = (int) Math.pow(10, k - 1) + (n - 1) / k;
        int idx = (n - 1) % k;
        return String.valueOf(num).charAt(idx) - '0';
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        k, cnt = 1, 9
        while k * cnt < n:
            n -= k * cnt
            k += 1
            cnt *= 10
        num = 10 ** (k - 1) + (n - 1) // k
        idx = (n - 1) % k
        return int(str(num)[idx])
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
