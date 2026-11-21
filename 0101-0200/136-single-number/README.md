# 136. Single Number

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/single-number/)
[![Topic: Bit Manipulation / XOR](https://img.shields.io/badge/Topic-Bit%20Manipulation%20/%20XOR-blue)](https://leetcode.com/problems/single-number/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Every element appears twice except for one. XOR has three fundamental properties: 1) `x ^ x = 0` (any number XORed with itself cancels to 0). 2) `x ^ 0 = x`. 3) XOR is commutative and associative. Therefore, XORing all numbers together cancels out all pairs, leaving solely the single number in O(N) time and O(1) space."

---

### 💡 Intuition & Core Insight
- **The Canceling Mirror**: Pairs of duplicate numbers erase each other like matter and antimatter, regardless of the order they appear in the array.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [4, 1, 2, 1, 2]`
- `4 ^ 1 ^ 2 ^ 1 ^ 2`
- `= 4 ^ (1 ^ 1) ^ (2 ^ 2)`
- `= 4 ^ 0 ^ 0 = 4`
Result: 4.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for (int num : nums) {
            res ^= num;
        }
        return res;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Single linear pass over the array.
- **Space Complexity**: $\mathcal{O}(1)$ — One single integer accumulator.

---

### ⚠️ Edge Cases & Interview Traps
1. Single element [1]: returns 1.
2. Negative numbers: bitwise XOR handles 2's complement negatives identically.

---

### 💬 Follow-Up Questions You Might Get
- *What if every element appears THREE times except one?* Use bitwise counters modulo 3 (LeetCode 137).
