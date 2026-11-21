# 644. Maximum Average Subarray II

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/maximum-average-subarray-ii)
[![Topic: Array & Binary Search & Prefix Sum](https://img.shields.io/badge/Topic-Array%20&%20Binary%20Search%20&%20Prefix%20Sum-blue)](https://leetcode.com/problems/maximum-average-subarray-ii)

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
**Sample Input**: `nums = [1,12,-5,-6,50,3], k = 4`  
**Expected Output**: `12.75000`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [1,12,-5,-6,50,3], k = 4` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `12.75000` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double eps = 1e-5;
        double l = 1e10, r = -1e10;
        for (int x : nums) {
            l = Math.min(l, x);
            r = Math.max(r, x);
        }
        while (r - l >= eps) {
            double mid = (l + r) / 2;
            if (check(nums, k, mid)) {
                l = mid;
            } else {
                r = mid;
            }
        }
        return l;
    }

    private boolean check(int[] nums, int k, double v) {
        double s = 0;
        for (int i = 0; i < k; ++i) {
            s += nums[i] - v;
        }
        if (s >= 0) {
            return true;
        }
        double t = 0;
        double mi = 0;
        for (int i = k; i < nums.length; ++i) {
            s += nums[i] - v;
            t += nums[i - k] - v;
            mi = Math.min(mi, t);
            if (s >= mi) {
                return true;
            }
        }
        return false;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        def check(v: float) -> bool:
            s = sum(nums[:k]) - k * v
            if s >= 0:
                return True
            t = mi = 0
            for i in range(k, len(nums)):
                s += nums[i] - v
                t += nums[i - k] - v
                mi = min(mi, t)
                if s >= mi:
                    return True
            return False

        eps = 1e-5
        l, r = min(nums), max(nums)
        while r - l >= eps:
            mid = (l + r) / 2
            if check(mid):
                l = mid
            else:
                r = mid
        return l
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
