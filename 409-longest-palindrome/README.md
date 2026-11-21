# 409. Longest Palindrome

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/longest-palindrome/)
[![Topic: Hash Table / Greedy](https://img.shields.io/badge/Topic-Hash%20Table%20/%20Greedy-blue)](https://leetcode.com/problems/longest-palindrome/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To form the longest palindrome from a set of characters: characters paired in even counts can be split symmetrically on both sides of the center. If any character has an odd frequency, all of its pairs can be used, plus at most one single odd character can be placed in the dead center. In a single scan, sum `count / 2 * 2` for every character, and add 1 if any odd frequency was found."

---

### 💡 Intuition & Core Insight
- **Symmetry and the Single Center Pivot**: A palindrome can hold as many pairs as available, but can only tolerate a single unpaired pivot in the center.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `s = "abccccdd"`
- 'a': 1 -> 0 paired, 1 odd
- 'b': 1 -> 0 paired, 1 odd
- 'c': 4 -> 4 paired (2 pairs)
- 'd': 2 -> 2 paired (1 pair)
Total paired = 4 + 2 = 6. Has odd frequencies? Yes ('a', 'b'). Add 1 for center.
Result: 6 + 1 = 7 ("dccaccd").

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int longestPalindrome(String s) {
        int[] freq = new int[128];
        for (char c : s.toCharArray()) freq[c]++;

        int length = 0;
        boolean hasOdd = false;

        for (int count : freq) {
            length += (count / 2) * 2;
            if (count % 2 == 1) hasOdd = true;
        }

        return hasOdd ? length + 1 : length;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd = False
        for count in counts.values():
            length += (count // 2) * 2
            if count % 2 == 1:
                has_odd = True
        return length + 1 if has_odd else length
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — One pass to count characters in string of length N.
- **Space Complexity**: $\mathcal{O}(1)$ — Fixed 128-element ASCII array.

---

### ⚠️ Edge Cases & Interview Traps
1. Single character "a": returns 1.
2. All pairs "aabb": returns 4 (no odd leftover).

---

### 💬 Follow-Up Questions You Might Get
- *What if palindrome must be a subsequence of original order?* Longest Palindromic Subsequence DP (LeetCode 516).
