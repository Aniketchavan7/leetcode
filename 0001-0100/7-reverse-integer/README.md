# 7. Reverse Integer

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/reverse-integer/)
[![Topic: Math / Bit Manipulation](https://img.shields.io/badge/Topic-Math%20/%20Bit%20Manipulation-blue)](https://leetcode.com/problems/reverse-integer/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To reverse the digits of a 32-bit signed integer without using 64-bit integers: In each step, extract the last digit `pop = x % 10` and divide `x /= 10`. Before pushing `pop` onto `reversed = reversed * 10 + pop`, check for 32-bit overflow against Integer.MAX_VALUE / 10 and Integer.MIN_VALUE / 10. If overflow would occur, return 0."

---

### 💡 Intuition & Core Insight
- **Pre-Overflow Detection**: Once an integer overflows, undefined behavior occurs in C/C++ or silent wraparound occurs. Checking bounds *before* multiplying by 10 guarantees 32-bit safety.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `x = 123`
- pop = 3, rev = 3, x = 12
- pop = 2, rev = 32, x = 1
- pop = 1, rev = 321, x = 0
Result: 321.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE / 10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
            if (rev < Integer.MIN_VALUE / 10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = 0
        while x_abs != 0:
            pop = x_abs % 10
            x_abs //= 10
            rev = rev * 10 + pop
        res = sign * rev
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log_{10}(N))$ — At most 10 iterations for a 32-bit integer.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary variables.

---

### ⚠️ Edge Cases & Interview Traps
1. Overflowing reverses (e.g. 1534236469): returns 0.
2. Negative numbers: preserved by sign handling.

---

### 💬 Follow-Up Questions You Might Get
- *Can this be handled on 64-bit systems?* Yes, compute in long and check `(int)rev == rev`.
