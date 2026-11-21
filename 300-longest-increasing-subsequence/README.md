# 300. Longest Increasing Subsequence

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/longest-increasing-subsequence/)
[![Topic: Dynamic Programming / Patience Sorting](https://img.shields.io/badge/Topic-Dynamic%20Programming%20/%20Patience%20Sorting-blue)](https://leetcode.com/problems/longest-increasing-subsequence/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We can find the length of the longest strictly increasing subsequence in O(N log N) using Patience Sorting / Binary Search. We maintain a list `tails` where `tails[i]` stores the smallest tail of all increasing subsequences of length i + 1. For each number x: binary search in `tails` for the first element >= x. If found, replace it with x (making that length's tail smaller and more welcoming to future elements). If not found (x is greater than all tails), append x. The length of `tails` at the end is our answer."

---

### 💡 Intuition & Core Insight
- **Greedy Tail Minimization**: Having a smaller tail for a subsequence of length k gives more opportunities for future numbers to extend it.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [10, 9, 2, 5, 3, 7, 101, 18]`
- 10: tails=[10]
- 9: replace 10 -> tails=[9]
- 2: replace 9 -> tails=[2]
- 5: append 5 -> tails=[2, 5]
- 3: replace 5 -> tails=[2, 3]
- 7: append 7 -> tails=[2, 3, 7]
- 101: append 101 -> tails=[2, 3, 7, 101]
- 18: replace 101 -> tails=[2, 3, 7, 18]
Length of tails = 4.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;

        for (int x : nums) {
            int left = 0, right = size;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (tails[mid] < x) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            tails[left] = x;
            if (left == size) size++;
        }
        return size;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []
        for x in nums:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        return len(tails)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log N)$ — Binary search of size <= N for each of the N numbers.
- **Space Complexity**: $\mathcal{O}(N)$ — tails array stores at most N elements.

---

### ⚠️ Edge Cases & Interview Traps
1. Strictly decreasing array [5, 4, 3, 2, 1]: tails length remains 1.
2. All identical [7, 7, 7]: bisect_left replaces index 0, length remains 1.

---

### 💬 Follow-Up Questions You Might Get
- *How to reconstruct the actual subsequence elements?* Store parent pointer indices during binary search replacement.
