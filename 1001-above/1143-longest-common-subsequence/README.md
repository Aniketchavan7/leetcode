# 1143. Longest Common Subsequence

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/longest-common-subsequence/)
[![Topic: 2D Dynamic Programming](https://img.shields.io/badge/Topic-2D%20Dynamic%20Programming-blue)](https://leetcode.com/problems/longest-common-subsequence/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We define `dp[i][j]` as the length of the longest common subsequence of text1[0..i-1] and text2[0..j-1]. If `text1[i - 1] == text2[j - 1]`, the characters match, so `dp[i][j] = 1 + dp[i - 1][j - 1]`. Otherwise, `dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1])` (either skip character from text1 or from text2). Return dp[m][n]."

---

### 💡 Intuition & Core Insight
- **Match Extends Diagonal; Mismatch Inherits Neighbors**: When characters match, they uniquely extend the LCS of both prefixes without competing against each other.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `text1 = "abcde"`, `text2 = "ace"`
- Match 'a' & 'a': 1 + dp[0][0] = 1
- Match 'c' & 'c': 1 + dp[1][1] = 2
- Match 'e' & 'e': 1 + dp[4][2] = 3
Result: 3 ("ace").

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[m][n];
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(M \cdot N)$ — Nested loops filling M x N grid.
- **Space Complexity**: $\mathcal{O}(\min(M, N))$ — Can be space-optimized to two 1D rows.

---

### ⚠️ Edge Cases & Interview Traps
1. Completely disjoint strings "abc", "def": returns 0.
2. Identical strings: returns length.

---

### 💬 Follow-Up Questions You Might Get
- *How to reconstruct the LCS string?* Backtrack from dp[m][n] moving diagonally when characters match.
