# 139. Word Break

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/word-break/)
[![Topic: 1D Dynamic Programming](https://img.shields.io/badge/Topic-1D%20Dynamic%20Programming-blue)](https://leetcode.com/problems/word-break/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We define `dp[i]` as true if substring `s[0..i]` can be segmented into dictionary words. `dp[0] = true` (empty string). For each index i from 1 to n, we look back at all split points j < i. If `dp[j] == true` and substring `s[j..i]` is in our dictionary word set, then `dp[i] = true`. Finally, return `dp[n]`."

---

### 💡 Intuition & Core Insight
- **Prefix Reachability**: You only need to verify if the suffix `s[j..i]` is a word if the prefix `s[0..j]` was ALREADY verified as segmentable.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `s = "leetcode"`, `wordDict = ["leet", "code"]`
- dp[0] = true
- i=4: j=0, dp[0]=true, s[0..4]="leet" in dict -> dp[4] = true
- i=8: j=4, dp[4]=true, s[4..8]="code" in dict -> dp[8] = true
Result: dp[8] = True.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break; // Move to next i
                }
            }
        }
        return dp[n];
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N^2 \cdot L)$ — Outer loop N, inner loop N, substring extraction / hash check up to max word length L.
- **Space Complexity**: $\mathcal{O}(N + M)$ — dp array of size N + 1 and wordSet of size M.

---

### ⚠️ Edge Cases & Interview Traps
1. Dictionary word longer than s: correctly ignored.
2. No valid segmentation: dp[n] remains false.

---

### 💬 Follow-Up Questions You Might Get
- *How to return all valid sentence segmentations?* Word Break II (DFS + Memoization).
