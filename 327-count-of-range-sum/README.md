# 327. Count of Range Sum

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/count-of-range-sum)
[![Topic: Binary Indexed Tree & Segment Tree & Array](https://img.shields.io/badge/Topic-Binary%20Indexed%20Tree%20&%20Segment%20Tree%20&%20Array-blue)](https://leetcode.com/problems/count-of-range-sum)

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
**Sample Input**: `nums = [-2,5,-1], lower = -2, upper = 2`  
**Expected Output**: `3`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [-2,5,-1], lower = -2, upper = 2` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `3` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class BinaryIndexedTree {
    private int n;
    private int[] c;

    public BinaryIndexedTree(int n) {
        this.n = n;
        this.c = new int[n + 1];
    }

    public void update(int x, int v) {
        while (x <= n) {
            c[x] += v;
            x += x & -x;
        }
    }

    public int query(int x) {
        int s = 0;
        while (x != 0) {
            s += c[x];
            x -= x & -x;
        }
        return s;
    }
}

class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        int n = nums.length;
        long[] s = new long[n + 1];
        for (int i = 0; i < n; ++i) {
            s[i + 1] = s[i] + nums[i];
        }
        long[] arr = new long[n * 3 + 3];
        for (int i = 0, j = 0; i <= n; ++i, j += 3) {
            arr[j] = s[i];
            arr[j + 1] = s[i] - lower;
            arr[j + 2] = s[i] - upper;
        }
        Arrays.sort(arr);
        int m = 0;
        for (int i = 0; i < arr.length; ++i) {
            if (i == 0 || arr[i] != arr[i - 1]) {
                arr[m++] = arr[i];
            }
        }
        BinaryIndexedTree tree = new BinaryIndexedTree(m);
        int ans = 0;
        for (long x : s) {
            int l = search(arr, m, x - upper);
            int r = search(arr, m, x - lower);
            ans += tree.query(r) - tree.query(l - 1);
            tree.update(search(arr, m, x), 1);
        }
        return ans;
    }

    private int search(long[] nums, int r, long x) {
        int l = 0;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (nums[mid] >= x) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l + 1;
    }
}
```

#### Python 3 Solution
```python
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x, v):
        while x <= self.n:
            self.c[x] += v
            x += x & -x

    def query(self, x):
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s


class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        s = list(accumulate(nums, initial=0))
        arr = sorted(set(v for x in s for v in (x, x - lower, x - upper)))
        tree = BinaryIndexedTree(len(arr))
        ans = 0
        for x in s:
            l = bisect_left(arr, x - upper) + 1
            r = bisect_left(arr, x - lower) + 1
            ans += tree.query(r) - tree.query(l - 1)
            tree.update(bisect_left(arr, x) + 1, 1)
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
