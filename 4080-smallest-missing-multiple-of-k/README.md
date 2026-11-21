# 4080. Smallest Missing Multiple of K

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/smallest-missing-multiple-of-k/)
[![Topic: Hash Set / Math](https://img.shields.io/badge/Topic-Hash%20Set%20/%20Math-blue)](https://leetcode.com/problems/smallest-missing-multiple-of-k/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To find the smallest positive multiple of k (i.e. k, 2k, 3k, 4k...) that does not appear in the array: Insert all array elements into a Hash Set. Then check multiples `k, 2k, 3k...` sequentially. The first multiple not present in the set is returned."

---

### 💡 Intuition & Core Insight
- **Sequential Multiple Step**: Starting from 1*k and incrementing by k guarantees that the first missing element discovered is the smallest possible missing multiple.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [5, 10, 20]`, `k = 5`
- Check 5: in set
- Check 10: in set
- Check 15: NOT in set!
Result: 15.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int findSmallestMissingMultiple(int[] nums, int k) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);

        int multiple = k;
        while (set.contains(multiple)) {
            multiple += k;
        }
        return multiple;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findSmallestMissingMultiple(self, nums: list[int], k: int) -> int:
        num_set = set(nums)
        multiple = k
        while multiple in num_set:
            multiple += k
        return multiple
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Building set takes O(N); while loop executes at most N + 1 times with O(1) set lookups.
- **Space Complexity**: $\mathcal{O}(N)$ — Hash set stores up to N elements.

---

### ⚠️ Edge Cases & Interview Traps
1. k is missing: returns k immediately in step 1.
2. Array contains no multiples of k: returns k.

---

### 💬 Follow-Up Questions You Might Get
- *What if array elements are already sorted?* Binary search or step pointers without a hash set.
