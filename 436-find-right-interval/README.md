# 436. Find Right Interval

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/find-right-interval)
[![Topic: Array & Binary Search & Sorting](https://img.shields.io/badge/Topic-Array%20&%20Binary%20Search%20&%20Sorting-blue)](https://leetcode.com/problems/find-right-interval)

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
**Sample Input**: `intervals = [[1,2]]`  
**Expected Output**: `[-1]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `intervals = [[1,2]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[-1]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] findRightInterval(int[][] intervals) {
        int n = intervals.length;
        int[][] arr = new int[n][0];
        for (int i = 0; i < n; ++i) {
            arr[i] = new int[] {intervals[i][0], i};
        }
        Arrays.sort(arr, (a, b) -> a[0] - b[0]);
        int[] ans = new int[n];
        for (int i = 0; i < n; ++i) {
            int j = search(arr, intervals[i][1]);
            ans[i] = j < n ? arr[j][1] : -1;
        }
        return ans;
    }

    private int search(int[][] arr, int x) {
        int l = 0, r = arr.length;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (arr[mid][0] >= x) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        ans = [-1] * n
        arr = sorted((st, i) for i, (st, _) in enumerate(intervals))
        for i, (_, ed) in enumerate(intervals):
            j = bisect_left(arr, (ed, -inf))
            if j < n:
                ans[i] = arr[j][1]
        return ans
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
