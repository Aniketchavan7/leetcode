# 70. Climbing Stairs

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/climbing-stairs/)
[![Topic: 1D Dynamic Programming](https://img.shields.io/badge/Topic-1D%20Dynamic%20Programming-blue)](https://leetcode.com/problems/climbing-stairs/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To reach step n, you can only arrive from step n - 1 (1 step jump) or step n - 2 (2 step jump). Therefore, `ways(n) = ways(n - 1) + ways(n - 2)`. This is identical to the Fibonacci sequence with base cases ways(1) = 1, ways(2) = 2. We compute it iteratively in O(N) time and O(1) space."

---

### 💡 Intuition & Core Insight
- **Optimal Substructure**: The number of distinct ways to reach the current floor is the sum of the ways to reach the preceding two floors.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `n = 3`
- ways(1) = 1
- ways(2) = 2
- ways(3) = 1 + 2 = 3 (paths: 1+1+1, 1+2, 2+1).

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int a = 1, b = 2;
        for (int i = 3; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Single loop running n - 2 times.
- **Space Complexity**: $\mathcal{O}(1)$ — Two rolling integer variables.

---

### ⚠️ Edge Cases & Interview Traps
1. n = 1: returns 1.
2. n = 2: returns 2.

---

### 💬 Follow-Up Questions You Might Get
- *What if each step costs money?* Min Cost Climbing Stairs (LeetCode 746).
