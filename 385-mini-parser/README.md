# 385. Mini Parser

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/mini-parser)
[![Topic: Stack & Depth-First Search & String](https://img.shields.io/badge/Topic-Stack%20&%20Depth-First%20Search%20&%20String-blue)](https://leetcode.com/problems/mini-parser)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We use a monotonic stack to maintain elements in sorted order. As we iterate through the input, elements that violate the monotonicity are popped, resolving next greater/smaller queries in linear time."

---

### 💡 Intuition & Core Insight
- **Monotonic Invariant**: Stack elements remain strictly increasing or decreasing.
- **One-Pass Resolution**: Each element is pushed and popped at most once, yielding amortized O(N) time.
- **Local vs Global Extremum**: Stack top immediately exposes the nearest boundary.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `s = &quot;324&quot;`  
**Expected Output**: `324`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `s = &quot;324&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `324` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
class Solution {
    public NestedInteger deserialize(String s) {
        if ("".equals(s) || "[]".equals(s)) {
            return new NestedInteger();
        }
        if (s.charAt(0) != '[') {
            return new NestedInteger(Integer.parseInt(s));
        }
        NestedInteger ans = new NestedInteger();
        int depth = 0;
        for (int i = 1, j = 1; i < s.length(); ++i) {
            if (depth == 0 && (s.charAt(i) == ',' || i == s.length() - 1)) {
                ans.add(deserialize(s.substring(j, i)));
                j = i + 1;
            } else if (s.charAt(i) == '[') {
                ++depth;
            } else if (s.charAt(i) == ']') {
                --depth;
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype list[NestedInteger]
#        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s or s == '[]':
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))
        ans = NestedInteger()
        depth, j = 0, 1
        for i in range(1, len(s)):
            if depth == 0 and (s[i] == ',' or i == len(s) - 1):
                ans.add(self.deserialize(s[j:i]))
                j = i + 1
            elif s[i] == '[':
                depth += 1
            elif s[i] == ']':
                depth -= 1
        return ans
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Empty stack pops.
2. Strict vs non-strict inequality when popping.
3. Elements remaining on the stack after array traversal ends.

---

### 💬 Follow-Up Questions You Might Get
*What if the array is circular?* Traverse the array twice (length 2N) using modulo indexing (i % N).
