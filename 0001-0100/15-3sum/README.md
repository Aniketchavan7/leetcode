# 15. 3Sum

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/3sum/)
[![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-blue)](https://leetcode.com/problems/3sum/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To find all unique triplets that sum to 0, we first sort the array. We then iterate through each element as the first number, and use two pointers (left and right) on the remaining subarray to find pairs that sum to -nums[i]. To guarantee uniqueness, we skip identical consecutive elements for both the outer element and the two pointers."

---

### 💡 Intuition & Core Insight
- **Sorting Simplifies Search**: Sorting costs O(N log N), which is dominated by the O(N^2) pointer traversal, but makes duplicate skipping trivial.
- **Two Pointers per Pivot**: Reduces an O(N^3) brute search to N two-pointer scans taking O(N) each.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [-1, 0, 1, 2, -1, -4]` -> Sorted: `[-4, -1, -1, 0, 1, 2]`
- i=0 (-4): target=4. Pointers cannot reach 4.
- i=1 (-1): target=1. L=2 (-1), R=5 (2): sum=1 -> Triplet `[-1, -1, 2]`. Skip duplicates, L=3 (0), R=4 (1): sum=1 -> Triplet `[-1, 0, 1]`.
- i=2 (-1): Duplicate of i=1 -> skip!
Output: `[[-1,-1,2], [-1,0,1]]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < n - 2; i++) {
            if (nums[i] > 0) break; // Cannot sum to 0 with only positive numbers
            if (i > 0 && nums[i] == nums[i - 1]) continue; // Skip duplicates

            int left = i + 1, right = n - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return res;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N^2)$ — Sorting takes O(N log N). Outer loop runs N times with an O(N) two-pointer scan inside.
- **Space Complexity**: $\mathcal{O}(1)$ — O(1) extra space ignoring output list and sorting call stack.

---

### ⚠️ Edge Cases & Interview Traps
1. Array length < 3: returns empty list.
2. All zeros: [0, 0, 0] produces exactly one [[0, 0, 0]] without duplicate repeats.

---

### 💬 Follow-Up Questions You Might Get
- *How to generalize to 4Sum or KSum?* Recursively reduce kSum to (k-1)Sum down to 2Sum base case.
