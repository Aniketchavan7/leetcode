# 1. Two Sum

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/two-sum/)
[![Topic: Arrays & Hashing](https://img.shields.io/badge/Topic-Arrays%20%26%20Hashing-blue)](https://leetcode.com/problems/two-sum/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Given an array of integers and a target sum, we need to return the indices of the two numbers that add up to target. Instead of checking every pair in O(N^2) brute force, we use a Hash Map to store numbers we have seen so far. As we iterate through each element x, we check if target - x is already in the map. If it is, we have our answer immediately in O(N) time and O(N) space."

---

### 💡 Intuition & Core Insight
- **The Brute Force Bottleneck**: Checking every pair (i, j) computes sums N*(N-1)/2 times, doing repetitive work without memory.
- **The Hash Map Lookup Trade-off**: Trading O(N) auxiliary space for O(1) average lookup transforms a nested quadratic search into a single linear scan.
- **Single-Pass Safety**: Checking the map before inserting ensures an element cannot pair with itself.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [2, 7, 11, 15]`, `target = 9`

| Step | Index `i` | Value `nums[i]` | Needed Complement (`9 - nums[i]`) | Map State Before `{val: idx}` | Match Found? | Action |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | 0 | 2 | 7 | `{}` | ❌ No | Put `2 -> 0` |
| 2 | 1 | 7 | 2 | `{2: 0}` | ✅ **Yes!** | Match at index `0`. Return `[0, 1]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Map value -> index
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[] { seen.get(complement), i };
            }
            seen.put(nums[i], i);
        }
        return new int[0];
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Single pass through the array of length N with O(1) hash map operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Hash map stores up to N - 1 elements in the worst case.

---

### ⚠️ Edge Cases & Interview Traps
1. Negative numbers: target - num arithmetic works identically.
2. Duplicates: numbers with identical values are handled correctly because current element pairs with the prior stored duplicate.

---

### 💬 Follow-Up Questions You Might Get
- *What if the array is sorted?* Use two pointers at opposite ends for O(N) time and O(1) space (LeetCode 167).
