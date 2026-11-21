# 862. Shortest Subarray with Sum at Least K

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k)
[![Topic: Queue & Array & Binary Search](https://img.shields.io/badge/Topic-Queue%20&%20Array%20&%20Binary%20Search-blue)](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k)

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
**Sample Input**: `nums = [1], k = 1`  
**Expected Output**: `1`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [1], k = 1` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `1` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int shortestSubarray(int[] nums, int k) {
        int n = nums.length;
        long[] s = new long[n + 1];
        for (int i = 0; i < n; ++i) {
            s[i + 1] = s[i] + nums[i];
        }
        Deque<Integer> q = new ArrayDeque<>();
        int ans = n + 1;
        for (int i = 0; i <= n; ++i) {
            while (!q.isEmpty() && s[i] - s[q.peek()] >= k) {
                ans = Math.min(ans, i - q.poll());
            }
            while (!q.isEmpty() && s[q.peekLast()] >= s[i]) {
                q.pollLast();
            }
            q.offer(i);
        }
        return ans > n ? -1 : ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        s = list(accumulate(nums, initial=0))
        q = deque()
        ans = inf
        for i, v in enumerate(s):
            while q and v - s[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            while q and s[q[-1]] >= v:
                q.pop()
            q.append(i)
        return -1 if ans == inf else ans
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
