# 493. Reverse Pairs

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/reverse-pairs)
[![Topic: Binary Indexed Tree & Segment Tree & Array](https://img.shields.io/badge/Topic-Binary%20Indexed%20Tree%20&%20Segment%20Tree%20&%20Array-blue)](https://leetcode.com/problems/reverse-pairs)

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
**Sample Input**: `nums = [1,3,2,3,1]`  
**Expected Output**: `2`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [1,3,2,3,1]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `2` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int[] nums;
    private int[] t;

    public int reversePairs(int[] nums) {
        this.nums = nums;
        int n = nums.length;
        this.t = new int[n];
        return mergeSort(0, n - 1);
    }

    private int mergeSort(int l, int r) {
        if (l >= r) {
            return 0;
        }
        int mid = (l + r) >> 1;
        int ans = mergeSort(l, mid) + mergeSort(mid + 1, r);
        int i = l, j = mid + 1, k = 0;
        while (i <= mid && j <= r) {
            if (nums[i] <= nums[j] * 2L) {
                ++i;
            } else {
                ans += mid - i + 1;
                ++j;
            }
        }
        i = l;
        j = mid + 1;
        while (i <= mid && j <= r) {
            if (nums[i] <= nums[j]) {
                t[k++] = nums[i++];
            } else {
                t[k++] = nums[j++];
            }
        }
        while (i <= mid) {
            t[k++] = nums[i++];
        }
        while (j <= r) {
            t[k++] = nums[j++];
        }
        for (i = l; i <= r; ++i) {
            nums[i] = t[i - l];
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge_sort(l, r):
            if l >= r:
                return 0
            mid = (l + r) >> 1
            ans = merge_sort(l, mid) + merge_sort(mid + 1, r)
            t = []
            i, j = l, mid + 1
            while i <= mid and j <= r:
                if nums[i] <= 2 * nums[j]:
                    i += 1
                else:
                    ans += mid - i + 1
                    j += 1
            i, j = l, mid + 1
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    t.append(nums[i])
                    i += 1
                else:
                    t.append(nums[j])
                    j += 1
            t.extend(nums[i : mid + 1])
            t.extend(nums[j : r + 1])
            nums[l : r + 1] = t
            return ans

        return merge_sort(0, len(nums) - 1)
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
