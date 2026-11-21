# 125. Valid Palindrome

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/valid-palindrome/)
[![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-blue)](https://leetcode.com/problems/valid-palindrome/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "A phrase is a palindrome if after converting all uppercase letters to lowercase and removing all non-alphanumeric characters, it reads the same forward and backward. We place two pointers at opposite ends of the string. Both pointers skip non-alphanumeric characters, and we compare characters case-insensitively. If any mismatch occurs, it is not a palindrome."

---

### 💡 Intuition & Core Insight
- **In-Place Two Pointers**: Avoids creating a new cleaned string, saving O(N) allocation space.
- **Early Exit**: Fails immediately on the first mismatch instead of pre-filtering the entire string.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `"A man, a plan, a canal: Panama"`
- L='A', R='a' -> match ('a'=='a') -> L++, R--
- L=' ', skip -> L='m'. R='m' -> match -> L++, R--
- Both pointers converge in the center without mismatch -> True.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Each character is examined by left or right pointer at most once.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant extra variables, zero string allocations.

---

### ⚠️ Edge Cases & Interview Traps
1. Empty string or only punctuation "   ": returns True.
2. Single character: returns True.

---

### 💬 Follow-Up Questions You Might Get
- *What if at most one character can be deleted?* Branch into two sub-checks when a mismatch is found (LeetCode 680).
