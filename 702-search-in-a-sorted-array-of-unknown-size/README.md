# 702. Search in a Sorted Array of Unknown Size

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size)
[![Topic: Array & Binary Search & Interactive](https://img.shields.io/badge/Topic-Array%20&%20Binary%20Search%20&%20Interactive-blue)](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size)

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
**Sample Input**: `secret = [-1,0,3,5,9,12], target = 9`  
**Expected Output**: `4`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `secret = [-1,0,3,5,9,12], target = 9` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `4` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
/**
 * // This is ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface ArrayReader {
 *     public int get(int index) {}
 * }
 */

class Solution {
    public int search(ArrayReader reader, int target) {
        int r = 1;
        while (reader.get(r) < target) {
            r <<= 1;
        }
        int l = r >> 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (reader.get(mid) >= target) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return reader.get(l) == target ? l : -1;
    }
}
```

#### Python 3 Solution
```python
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:


class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        r = 1
        while reader.get(r) < target:
            r <<= 1
        l = r >> 1
        while l < r:
            mid = (l + r) >> 1
            if reader.get(mid) >= target:
                r = mid
            else:
                l = mid + 1
        return l if reader.get(l) == target else -1
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
