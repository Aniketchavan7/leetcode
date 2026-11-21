# 4256. Construct Uniform Parity Array I

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/construct-uniform-parity-array-i/)
[![Topic: Arrays / Math](https://img.shields.io/badge/Topic-Arrays%20/%20Math-blue)](https://leetcode.com/problems/construct-uniform-parity-array-i/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Given an array, determine if we can make all elements have uniform parity (all even or all odd) using allowed operations. We count the number of even numbers and odd numbers. If all are already even or all already odd, return true. Otherwise, check if an odd parity transition is possible using the smallest odd element."

---

### 💡 Intuition & Core Insight
- **Parity Arithmetic**: Even - Even = Even; Odd - Odd = Even; Odd - Even = Odd. A single odd number can transform other odd numbers into even numbers.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [2, 4, 6]` -> All even -> True. `nums = [1, 3, 5]` -> All odd -> True.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean canMakeUniform(int[] nums) {
        int oddCount = 0, evenCount = 0;
        int minOdd = Integer.MAX_VALUE;

        for (int num : nums) {
            if (num % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
                minOdd = Math.min(minOdd, num);
            }
        }
        if (oddCount == 0 || evenCount == 0) return true;
        return oddCount > 0;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def canMakeUniform(self, nums: list[int]) -> bool:
        odd_count = sum(1 for x in nums if x % 2 != 0)
        even_count = len(nums) - odd_count
        if odd_count == 0 or even_count == 0:
            return True
        return odd_count > 0
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Single linear pass over nums.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant counters.

---

### ⚠️ Edge Cases & Interview Traps
1. Uniform array: returns true immediately.
2. Mixed parities: evaluated by parity transition rules.

---

### 💬 Follow-Up Questions You Might Get
- *What if operations cost weight?* Shortest path / BFS on parity states.
