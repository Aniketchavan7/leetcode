# 4284. Smallest Stable Index I

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/smallest-stable-index-i/)
[![Topic: Arrays / Prefix Minimums](https://img.shields.io/badge/Topic-Arrays%20/%20Prefix%20Minimums-blue)](https://leetcode.com/problems/smallest-stable-index-i/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "An index i is stable if the element at i is greater than or equal to the minimum of elements to its left, and less than or equal to the maximum of elements to its right. We precompute prefix minimums and suffix maximums, then scan left-to-right to return the first index satisfying the stability condition."

---

### 💡 Intuition & Core Insight
- **Prefix/Suffix Boundary Verification**: Comparing an element against the extremes of its left and right partitions in O(1) time.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [2, 1, 3, 5, 4]`
- Precompute prefix min and suffix max.
- Scan i from 0 to n-1: first index matching condition is returned.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int smallestStableIndex(int[] nums) {
        int n = nums.length;
        int[] prefixMin = new int[n];
        int[] suffixMax = new int[n];

        prefixMin[0] = nums[0];
        for (int i = 1; i < n; i++) prefixMin[i] = Math.min(prefixMin[i - 1], nums[i]);

        suffixMax[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) suffixMax[i] = Math.max(suffixMax[i + 1], nums[i]);

        for (int i = 0; i < n; i++) {
            boolean leftOk = (i == 0) || (nums[i] >= prefixMin[i - 1]);
            boolean rightOk = (i == n - 1) || (nums[i] <= suffixMax[i + 1]);
            if (leftOk && rightOk) return i;
        }
        return -1;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def smallestStableIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_min = [0] * n
        suffix_max = [0] * n

        prefix_min[0] = nums[0]
        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], nums[i])

        suffix_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])

        for i in range(n):
            left_ok = (i == 0) or (nums[i] >= prefix_min[i - 1])
            right_ok = (i == n - 1) or (nums[i] <= suffix_max[i + 1])
            if left_ok and right_ok:
                return i
        return -1
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Three linear passes of size N.
- **Space Complexity**: $\mathcal{O}(N)$ — Prefix min and suffix max arrays.

---

### ⚠️ Edge Cases & Interview Traps
1. Boundary index 0 or n-1: edge bounds evaluated as true automatically.
2. Strictly increasing array: index 0 is returned.

---

### 💬 Follow-Up Questions You Might Get
- *Can space be reduced to O(1)?* Precompute suffixMax, and compute prefixMin on the fly.
