# 496. Next Greater Element I

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/next-greater-element-i)
[![Topic: Stack & Array & Hash Table](https://img.shields.io/badge/Topic-Stack%20&%20Array%20&%20Hash%20Table-blue)](https://leetcode.com/problems/next-greater-element-i)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We use a monotonic stack to maintain elements in sorted order. As we iterate through the input, elements that violate the monotonicity are popped, resolving next greater/smaller queries in linear time."

---

### 💡 Intuition & Core Insight
- **Monotonic Invariant**: Stack elements remain strictly increasing or decreasing.
- **One-Pass Resolution**: Each element is pushed and popped at most once, yielding amortized O(N) time.
- **Local vs Global Extremum**: Stack top immediately exposes the nearest boundary.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `nums1 = [4,1,2], nums2 = [1,3,4,2]`  
**Expected Output**: `[-1,3,-1]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums1 = [4,1,2], nums2 = [1,3,4,2]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[-1,3,-1]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Deque<Integer> stk = new ArrayDeque<>();
        int m = nums1.length, n = nums2.length;
        Map<Integer, Integer> d = new HashMap(n);
        for (int i = n - 1; i >= 0; --i) {
            int x = nums2[i];
            while (!stk.isEmpty() && stk.peek() < x) {
                stk.pop();
            }
            if (!stk.isEmpty()) {
                d.put(x, stk.peek());
            }
            stk.push(x);
        }
        int[] ans = new int[m];
        for (int i = 0; i < m; ++i) {
            ans[i] = d.getOrDefault(nums1[i], -1);
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stk = []
        d = {}
        for x in nums2[::-1]:
            while stk and stk[-1] < x:
                stk.pop()
            if stk:
                d[x] = stk[-1]
            stk.append(x)
        return [d.get(x, -1) for x in nums1]
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Empty stack pops.
2. Strict vs non-strict inequality when popping.
3. Elements remaining on the stack after array traversal ends.

---

### 💬 Follow-Up Questions You Might Get
*What if the array is circular?* Traverse the array twice (length 2N) using modulo indexing (i % N).
