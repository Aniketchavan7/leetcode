# 1013. Fibonacci Number

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/fibonacci-number/)
[![Topic: Dynamic Programming / Math](https://img.shields.io/badge/Topic-Dynamic%20Programming%20/%20Math-blue)](https://leetcode.com/problems/fibonacci-number/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "The Fibonacci sequence follows F(n) = F(n-1) + F(n-2) with F(0)=0 and F(1)=1. We can compute F(n) in O(n) time and O(1) space iteratively by maintaining two rolling variables `a` and `b`. In each step, `c = a + b`, then advance `a = b` and `b = c`."

---

### 💡 Intuition & Core Insight
- **State Reduction**: To compute the next state, only the immediate past two states are needed, reducing O(N) array storage down to two variables.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `n = 4`
- Start: a=0, b=1
- i=2: c = 0 + 1 = 1, a=1, b=1
- i=3: c = 1 + 1 = 2, a=1, b=2
- i=4: c = 1 + 2 = 3, a=2, b=3
Result: 3.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int fib(int n) {
        if (n <= 1) return n;
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
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
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Simple loop running n - 1 times.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary variables.

---

### ⚠️ Edge Cases & Interview Traps
1. n = 0: returns 0.
2. n = 1: returns 1.

---

### 💬 Follow-Up Questions You Might Get
- *Can we solve in O(log N)?* Yes, using 2x2 Matrix Exponentiation.
