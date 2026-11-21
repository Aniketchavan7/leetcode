# 128. Longest Consecutive Sequence

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/longest-consecutive-sequence/)
[![Topic: Arrays & Hashing](https://img.shields.io/badge/Topic-Arrays%20%26%20Hashing-blue)](https://leetcode.com/problems/longest-consecutive-sequence/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We need to find the length of the longest consecutive elements sequence in O(N) time. Sorting takes O(N log N), which is disallowed. Instead, we insert all numbers into a Hash Set. A number `x` is the START of a consecutive sequence only if `x - 1` is NOT in the set. If it is a start, we count upwards `x + 1, x + 2, ...` to measure the sequence length."

---

### 💡 Intuition & Core Insight
- **Avoiding Redundant Counting**: If we counted upwards for every number, [1, 2, 3, 4] would count 4 from 1, 3 from 2, 2 from 3, resulting in O(N^2).
- **Sequence Root Filtering**: Only initiating the while-loop when `x - 1` is absent guarantees that each consecutive sequence is traversed exactly once across the entire algorithm.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [100, 4, 200, 1, 3, 2]` -> Set: `{1, 2, 3, 4, 100, 200}`
- 100: 99 in set? No -> Start! Sequence: [100] (len=1)
- 4: 3 in set? Yes -> Not a start, skip!
- 200: 199 in set? No -> Start! Sequence: [200] (len=1)
- 1: 0 in set? No -> Start! 2 in set? Yes. 3? Yes. 4? Yes. 5? No. Sequence: [1, 2, 3, 4] (len=4)
- 3, 2: Predecessors exist -> skip!
Max length = 4.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) numSet.add(num);

        int longest = 0;
        for (int num : numSet) {
            // Only start counting if num is the beginning of a sequence
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;
                while (numSet.contains(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }
                longest = Math.max(longest, currentStreak);
            }
        }
        return longest;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                streak = 1
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                longest = max(longest, streak)
        return longest
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Each number is visited at most twice: once in the outer loop, and once during sequence counting.
- **Space Complexity**: $\mathcal{O}(N)$ — Hash set stores up to N distinct integers.

---

### ⚠️ Edge Cases & Interview Traps
1. Empty input: returns 0.
2. Duplicate numbers: set deduplicates automatically.

---

### 💬 Follow-Up Questions You Might Get
- *Can this be solved with Disjoint Set Union (Union-Find)?* Yes, union adjacent numbers `x` and `x + 1`.
