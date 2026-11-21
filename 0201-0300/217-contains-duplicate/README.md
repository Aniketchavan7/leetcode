# 217. Contains Duplicate

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/contains-duplicate/)
[![Topic: Arrays & Hashing](https://img.shields.io/badge/Topic-Arrays%20%26%20Hashing-blue)](https://leetcode.com/problems/contains-duplicate/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To check if any value appears at least twice in an array, we maintain a Hash Set of visited numbers. As we iterate, if the current number is already in the set, we immediately return true. If the loop completes without finding a duplicate, return false."

---

### 💡 Intuition & Core Insight
- **Lookup Optimization**: Checking against a Hash Set takes O(1) time per element compared to O(N^2) for brute nested comparisons or O(N log N) for sorting.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [1, 2, 3, 1]`
- num=1: set={1}
- num=2: set={1, 2}
- num=3: set={1, 2, 3}
- num=1: 1 already in set -> return True!

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (!seen.add(num)) {
                return true;
            }
        }
        return false;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — One single pass over the array with O(1) set operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Hash set stores up to N unique elements.

---

### ⚠️ Edge Cases & Interview Traps
1. All distinct elements: returns False after N iterations.
2. Length 0 or 1: returns False.

---

### 💬 Follow-Up Questions You Might Get
- *What if extra memory is not allowed?* Sort in-place in O(N log N) and check adjacent elements.
