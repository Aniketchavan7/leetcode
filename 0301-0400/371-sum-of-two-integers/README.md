# 371. Sum of Two Integers

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/sum-of-two-integers/)
[![Topic: Bit Manipulation](https://img.shields.io/badge/Topic-Bit%20Manipulation-blue)](https://leetcode.com/problems/sum-of-two-integers/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To add two integers without using + or -: In binary addition, `a ^ b` computes the sum without carry (XOR simulates half-adder sum), and `(a & b) << 1` computes the carry (AND finds matching 1s, shifted left). We repeat `a = a ^ b` and `b = (a & b) << 1` until carry b becomes 0."

---

### 💡 Intuition & Core Insight
- **Hardware ALU Simulation**: This is the exact circuit logic of an arithmetic half-adder.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `a = 1 (01)`, `b = 2 (10)`
- sum = 1 ^ 2 = 3 (11)
- carry = (1 & 2) << 1 = 0
Result: 3.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & mask) if b > 0 else a
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(1)$ — At most 32 loop iterations for 32-bit integers.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant variables.

---

### ⚠️ Edge Cases & Interview Traps
1. Negative numbers: handled correctly in 2's complement.
2. Carry rolls across all 32 bits: loop terminates in <= 32 steps.

---

### 💬 Follow-Up Questions You Might Get
- *How to do subtraction?* `a - b` is `getSum(a, getSum(~b, 1))`.
