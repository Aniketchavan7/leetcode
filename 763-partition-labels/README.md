# 763. Partition Labels

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/partition-labels)
[![Topic: Greedy & Hash Table & Two Pointers](https://img.shields.io/badge/Topic-Greedy%20&%20Hash%20Table%20&%20Two%20Pointers-blue)](https://leetcode.com/problems/partition-labels)

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
**Sample Input**: `s = &quot;ababcbacadefegdehijhklij&quot;`  
**Expected Output**: `[9,7,8]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s = &quot;ababcbacadefegdehijhklij&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[9,7,8]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<Integer> partitionLabels(String s) {
        int[] last = new int[26];
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            last[s.charAt(i) - 'a'] = i;
        }
        List<Integer> ans = new ArrayList<>();
        int mx = 0, j = 0;
        for (int i = 0; i < n; ++i) {
            mx = Math.max(mx, last[s.charAt(i) - 'a']);
            if (mx == i) {
                ans.add(i - j + 1);
                j = i + 1;
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {c: i for i, c in enumerate(s)}
        mx = j = 0
        ans = []
        for i, c in enumerate(s):
            mx = max(mx, last[c])
            if mx == i:
                ans.append(i - j + 1)
                j = i + 1
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
