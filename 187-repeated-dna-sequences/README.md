# 187. Repeated DNA Sequences

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/repeated-dna-sequences)
[![Topic: Bit Manipulation & Hash Table & String](https://img.shields.io/badge/Topic-Bit%20Manipulation%20&%20Hash%20Table%20&%20String-blue)](https://leetcode.com/problems/repeated-dna-sequences)

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
**Sample Input**: `s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"`  
**Expected Output**: `["AAAAACCCCC","CCCCCAAAAA"]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `["AAAAACCCCC","CCCCCAAAAA"]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        Map<String, Integer> cnt = new HashMap<>();
        List<String> ans = new ArrayList<>();
        for (int i = 0; i < s.length() - 10 + 1; ++i) {
            String t = s.substring(i, i + 10);
            if (cnt.merge(t, 1, Integer::sum) == 2) {
                ans.add(t);
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        cnt = Counter()
        ans = []
        for i in range(len(s) - 10 + 1):
            t = s[i : i + 10]
            cnt[t] += 1
            if cnt[t] == 2:
                ans.append(t)
        return ans
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
