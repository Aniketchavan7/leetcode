# 870. Advantage Shuffle

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/advantage-shuffle)
[![Topic: Greedy & Array & Two Pointers](https://img.shields.io/badge/Topic-Greedy%20&%20Array%20&%20Two%20Pointers-blue)](https://leetcode.com/problems/advantage-shuffle)

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
**Sample Input**: `nums1 = [2,7,11,15], nums2 = [1,10,4,11]`  
**Expected Output**: `[2,11,7,15]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums1 = [2,7,11,15], nums2 = [1,10,4,11]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[2,11,7,15]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] advantageCount(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int[][] t = new int[n][2];
        for (int i = 0; i < n; ++i) {
            t[i] = new int[] {nums2[i], i};
        }
        Arrays.sort(t, (a, b) -> a[0] - b[0]);
        Arrays.sort(nums1);
        int[] ans = new int[n];
        int i = 0, j = n - 1;
        for (int v : nums1) {
            if (v <= t[i][0]) {
                ans[t[j--][1]] = v;
            } else {
                ans[t[i++][1]] = v;
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        t = sorted((v, i) for i, v in enumerate(nums2))
        n = len(nums2)
        ans = [0] * n
        i, j = 0, n - 1
        for v in nums1:
            if v <= t[i][0]:
                ans[t[j][1]] = v
                j -= 1
            else:
                ans[t[i][1]] = v
                i += 1
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
