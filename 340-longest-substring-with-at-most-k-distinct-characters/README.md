# 340. Longest Substring with At Most K Distinct Characters

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters)
[![Topic: Hash Table & String & Sliding Window](https://img.shields.io/badge/Topic-Hash%20Table%20&%20String%20&%20Sliding%20Window-blue)](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "By maintaining window boundaries or dual pointers, we convert a quadratic pair search into a linear scan, dynamically expanding or shrinking based on feasibility invariants."

---

### 💡 Intuition & Core Insight
- **Monotonicity**: As the right pointer advances, the search space moves monotonically without backtracking.
- **Window Invariant**: Validating window conditions with a frequency counter guarantees correctness.
- **Two-Ended Traversal**: Squeezing inward from boundaries avoids evaluating redundant pairs.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `s = &quot;eceba&quot;, k = 2`  
**Expected Output**: `3`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s = &quot;eceba&quot;, k = 2` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `3` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        Map<Character, Integer> cnt = new HashMap<>();
        int l = 0;
        char[] cs = s.toCharArray();
        for (char c : cs) {
            cnt.merge(c, 1, Integer::sum);
            if (cnt.size() > k) {
                if (cnt.merge(cs[l], -1, Integer::sum) == 0) {
                    cnt.remove(cs[l]);
                }
                ++l;
            }
        }
        return cs.length - l;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        cnt = Counter()
        for c in s:
            cnt[c] += 1
            if len(cnt) > k:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1
        return len(s) - l
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(1)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Off-by-one errors on window size (right - left + 1).
2. Empty arrays or arrays with all identical elements.
3. Forgetting to update state counters when shrinking the left boundary.

---

### 💬 Follow-Up Questions You Might Get
*What if the array cannot fit into memory?* We can stream data through a bounded circular buffer or sliding window chunk.
