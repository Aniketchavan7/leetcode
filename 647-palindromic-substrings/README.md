# 647. Palindromic Substrings

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/palindromic-substrings/)
[![Topic: Two Pointers / DP](https://img.shields.io/badge/Topic-Two%20Pointers%20/%20DP-blue)](https://leetcode.com/problems/palindromic-substrings/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "A palindrome expands symmetrically around its center. There are 2N - 1 possible centers in a string of length N: N single-character centers (odd-length palindromes) and N - 1 two-character centers (even-length palindromes). For each center (i, i) and (i, i + 1), expand two pointers outward while characters match, incrementing the total count."

---

### 💡 Intuition & Core Insight
- **Expand Around Centers**: Avoids checking all O(N^2) substrings in O(N) time (which would be O(N^3)). Expanding directly counts all palindromes in O(N^2) total time with O(1) space.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `s = "aaa"`
- Center (0, 0): "a" (1)
- Center (0, 1): "aa" (1)
- Center (1, 1): "a", "aaa" (2)
- Center (1, 2): "aa" (1)
- Center (2, 2): "a" (1)
Total palindromic substrings = 6.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int countSubstrings(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            count += expandAroundCenter(s, i, i);     // Odd length
            count += expandAroundCenter(s, i, i + 1); // Even length
        }
        return count;
    }

    private int expandAroundCenter(String s, int left, int right) {
        int matches = 0;
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            matches++;
            left--;
            right++;
        }
        return matches;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(left, right):
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return count
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N^2)$ — 2N - 1 centers, each expanding at most N/2 steps.
- **Space Complexity**: $\mathcal{O}(1)$ — O(1) extra space with two pointers.

---

### ⚠️ Edge Cases & Interview Traps
1. Single character "a": returns 1.
2. All same characters: returns N*(N+1)/2.

---

### 💬 Follow-Up Questions You Might Get
- *Can we achieve O(N) linear time?* Yes, using Manacher's Algorithm.
