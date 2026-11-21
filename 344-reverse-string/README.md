# 344. Reverse String

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/reverse-string/)
[![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-blue)](https://leetcode.com/problems/reverse-string/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To reverse an array of characters in-place with O(1) extra memory, initialize two pointers at the left and right ends. In a loop while left < right, swap the characters at left and right, then move left forward and right backward."

---

### 💡 Intuition & Core Insight
- **Symmetry**: Reversal is symmetric around the midpoint. Swapping pairs from outside-in reverses the entire sequence.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `s = ["h","e","l","l","o"]`
- L=0 ('h'), R=4 ('o'): swap -> `["o","e","l","l","h"]`, L=1, R=3
- L=1 ('e'), R=3 ('l'): swap -> `["o","l","l","e","h"]`, L=2, R=2 (stop)
Result: `["o","l","l","e","h"]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public void reverseString(char[] s) {
        int left = 0, right = s.length - 1;
        while (left < right) {
            char tmp = s[left];
            s[left++] = s[right];
            s[right--] = tmp;
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Iterates N/2 times, performing N/2 swaps.
- **Space Complexity**: $\mathcal{O}(1)$ — In-place swapping with two pointers.

---

### ⚠️ Edge Cases & Interview Traps
1. Length 0 or 1: loop terminates immediately, unchanged.
2. Even vs odd length: works identically.

---

### 💬 Follow-Up Questions You Might Get
- *Can we do this recursively?* Yes, but recursive call stack consumes O(N) memory.
