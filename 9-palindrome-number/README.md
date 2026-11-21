# 9. Palindrome Number

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/palindrome-number/)
[![Topic: Math](https://img.shields.io/badge/Topic-Math-blue)](https://leetcode.com/problems/palindrome-number/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To determine if an integer reads the same forwards and backwards without converting to a string, we reverse the second half of the number mathematically using modulo and division. When the reversed second half equals the first half (or reversed / 10 for odd digits), it is a palindrome."

---

### 💡 Intuition & Core Insight
- **Negative Numbers**: Negative signs make palindromes impossible (e.g. -121 reversed is 121-).
- **Trailing Zeros**: Any number ending in 0 (except 0 itself) cannot be a palindrome.
- **Reversing Half**: Reversing the entire number risks 32-bit integer overflow; stopping when reversed >= original avoids overflow completely.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `x = 1221`

| Step | `x` (remaining) | `reversed` | Condition `x > reversed` |
| :---: | :---: | :---: | :---: |
| Start | 1221 | 0 | True |
| 1 | 122 | 1 | True |
| 2 | 12 | 12 | False (Stop) |

Result: `x == reversed` (12 == 12) -> True.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;
        int reversed = 0;
        while (x > reversed) {
            reversed = reversed * 10 + x % 10;
            x /= 10;
        }
        return x == reversed || x == reversed / 10;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log_{10}(N))$ — We divide the input by 10 each step, taking half the number of total decimal digits.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant extra variables.

---

### ⚠️ Edge Cases & Interview Traps
1. Negative integers: always false.
2. Multiples of 10: e.g. 10, 100 cannot start with 0, so always false unless x == 0.

---

### 💬 Follow-Up Questions You Might Get
- *Can we solve this by string conversion?* Yes, but string conversion allocates extra heap memory.
