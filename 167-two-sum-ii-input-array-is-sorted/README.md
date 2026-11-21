# 167. Two Sum II - Input Array Is Sorted

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted)
[![Topic: Array & Two Pointers & Binary Search](https://img.shields.io/badge/Topic-Array%20&%20Two%20Pointers%20&%20Binary%20Search-blue)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted)

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
**Sample Input**: `numbers = [`  
**Expected Output**: `[1,2]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `numbers = [` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[1,2]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        for (int i = 0, n = numbers.length;; ++i) {
            int x = target - numbers[i];
            int l = i + 1, r = n - 1;
            while (l < r) {
                int mid = (l + r) >> 1;
                if (numbers[mid] >= x) {
                    r = mid;
                } else {
                    l = mid + 1;
                }
            }
            if (numbers[l] == x) {
                return new int[] {i + 1, l + 1};
            }
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        for i in range(n - 1):
            x = target - numbers[i]
            j = bisect_left(numbers, x, lo=i + 1)
            if j < n and numbers[j] == x:
                return [i + 1, j + 1]
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
