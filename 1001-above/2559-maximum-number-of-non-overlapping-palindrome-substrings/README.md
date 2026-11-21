# 2559. Maximum Number of Non-Overlapping Palindrome Substrings

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)
[![Topic: Dynamic Programming / Greedy](https://img.shields.io/badge/Topic-Dynamic%20Programming%20/%20Greedy-blue)](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To find the maximum number of non-overlapping palindromic substrings of length at least k: Greedily, we want each palindrome to be as SHORT as possible (either length k or length k + 1) because any longer palindrome of length L >= k contains an interior palindrome of length k or k + 1. We iterate through the string with a pointer i. We check if a palindrome of length k or k + 1 ends at index i. If so, we greedily lock in that palindrome, increment count, and jump our search pointer past this substring to ensure non-overlap."

---

### 💡 Intuition & Core Insight
- **Greedy Substring Minimization**: If an interval [L, R] forms a palindrome of length k, taking it immediately never prevents finding more palindromes than waiting for a longer one.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `s = "abaccdbbd"`, `k = 3`
- Check substrings of length 3 ending at each index:
  - "aba" (0..2) is palindrome of len 3! Count = 1, jump to index 3.
  - "bbd" at end: "dbbd" contains "dbbd" (len 4 >= 3) -> Count = 2.
Total non-overlapping = 2.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int maxPalindromes(String s, int k) {
        int count = 0;
        int n = s.length();
        int lastEnd = -1;

        for (int center = 0; center < 2 * n - 1; center++) {
            int left = center / 2;
            int right = left + center % 2;

            while (left >= 0 && right < n && s.charAt(left) == s.charAt(right)) {
                if (right - left + 1 >= k) {
                    if (left > lastEnd) {
                        count++;
                        lastEnd = right;
                        break;
                    }
                }
                left--;
                right++;
            }
        }
        return count;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        last_end = -1

        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= k:
                    if left > last_end:
                        count += 1
                        last_end = right
                        break
                left -= 1
                right += 1

        return count
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \cdot k)$ — Each center expands at most O(k) before finding or failing a length k/k+1 palindrome.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant pointers.

---

### ⚠️ Edge Cases & Interview Traps
1. k = 1: every single character is a palindrome, returns n.
2. No valid palindrome of length >= k: returns 0.

---

### 💬 Follow-Up Questions You Might Get
- *How to solve with standard DP?* `dp[i] = max(dp[i-1], 1 + dp[j-1])` for valid palindrome s[j..i].
