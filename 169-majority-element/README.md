# 169. Majority Element

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/majority-element/)
[![Topic: Boyer-Moore Voting](https://img.shields.io/badge/Topic-Boyer-Moore%20Voting-blue)](https://leetcode.com/problems/majority-element/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "The majority element appears more than n/2 times. Using the Boyer-Moore Voting Algorithm, we maintain a `candidate` and a `count`. For each element, if count is 0, we adopt the current element as candidate. If the element equals candidate, we increment count; otherwise decrement count. Because the majority element appears more than all other elements combined, it will survive to the end."

---

### 💡 Intuition & Core Insight
- **The Battle Royale Analogy**: Imagine every non-majority element canceling out one instance of the majority element. Since the majority element has count > n/2, even after every other element sacrifices itself to cancel one majority element, at least one majority element remains.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [2, 2, 1, 1, 1, 2, 2]`
- i=0: cand=2, count=1
- i=1: cand=2, count=2
- i=2: cand=2, count=1
- i=3: cand=2, count=0
- i=4: count=0 -> cand=1, count=1
- i=5: cand=1, count=0
- i=6: count=0 -> cand=2, count=1
Final candidate = 2.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int majorityElement(int[] nums) {
        int candidate = nums[0];
        int count = 0;
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }
        return candidate;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — One single pass over the array of size N.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary memory.

---

### ⚠️ Edge Cases & Interview Traps
1. Single element [1]: immediately returns 1.
2. Elements strictly alternating: majority element still guaranteed to survive.

---

### 💬 Follow-Up Questions You Might Get
- *What if a majority is not guaranteed to exist?* Run a second verification pass to confirm candidate count > n/2.
