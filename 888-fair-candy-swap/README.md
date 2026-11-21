# 888. Fair Candy Swap

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/fair-candy-swap)
[![Topic: Array & Hash Table & Binary Search](https://img.shields.io/badge/Topic-Array%20&%20Hash%20Table%20&%20Binary%20Search-blue)](https://leetcode.com/problems/fair-candy-swap)

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
**Sample Input**: `aliceSizes = [1,1], bobSizes = [2,2]`  
**Expected Output**: `[1,2]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `aliceSizes = [1,1], bobSizes = [2,2]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[1,2]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] fairCandySwap(int[] aliceSizes, int[] bobSizes) {
        int s1 = 0, s2 = 0;
        Set<Integer> s = new HashSet<>();
        for (int a : aliceSizes) {
            s1 += a;
        }
        for (int b : bobSizes) {
            s.add(b);
            s2 += b;
        }
        int diff = (s1 - s2) >> 1;
        for (int a : aliceSizes) {
            int b = a - diff;
            if (s.contains(b)) {
                return new int[] {a, b};
            }
        }
        return null;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) >> 1
        s = set(bobSizes)
        for a in aliceSizes:
            if (b := (a - diff)) in s:
                return [a, b]
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
