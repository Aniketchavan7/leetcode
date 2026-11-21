# 3. Longest Substring Without Repeating Characters

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
[![Topic: Sliding Window](https://img.shields.io/badge/Topic-Sliding%20Window-blue)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We use a dynamically expanding and contracting sliding window [left, right] tracked with a Hash Map storing the most recent index of each character. As the right pointer advances, if a character was already seen inside our current window, we jump the left pointer forward to index + 1 of the duplicate, keeping all characters in the window unique at all times."

---

### 💡 Intuition & Core Insight
- **Why Jump Left Pointer?**: Instead of shrinking one character at a time, storing the previous index lets the left boundary skip directly past the duplicate.
- **Math.max for Left**: Ensure left pointer never moves backwards if the seen character lies before the current window boundary.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `s = "abcabcbb"`

| Right `r` | Char `s[r]` | Last Seen Idx | `left` before | `left` after | Window `[l, r]` | Window Len | Max Len |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 'a' | None | 0 | 0 | "a" | 1 | 1 |
| 1 | 'b' | None | 0 | 0 | "ab" | 2 | 2 |
| 2 | 'c' | None | 0 | 0 | "abc" | 3 | **3** |
| 3 | 'a' | 0 | 0 | 1 | "bca" | 3 | 3 |
| 4 | 'b' | 1 | 1 | 2 | "cab" | 3 | 3 |
| 5 | 'c' | 2 | 2 | 3 | "abc" | 3 | 3 |
| 6 | 'b' | 4 | 3 | 5 | "b" | 2 | 3 |
| 7 | 'b' | 6 | 5 | 7 | "b" | 1 | 3 |
Result: 3.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> lastSeen = new HashMap<>();
        int left = 0, maxLen = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (lastSeen.containsKey(c)) {
                left = Math.max(left, lastSeen.get(c) + 1);
            }
            lastSeen.put(c, right);
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0
        for right, c in enumerate(s):
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c] + 1
            last_seen[c] = right
            max_len = max(max_len, right - left + 1)
        return max_len
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Right pointer visits each character once; left pointer only jumps forward.
- **Space Complexity**: $\mathcal{O}(\min(N, M))$ — M is the size of the charset (at most 128 ASCII / 26 letters).

---

### ⚠️ Edge Cases & Interview Traps
1. Empty string "": returns 0.
2. All same characters "bbbbb": returns 1.

---

### 💬 Follow-Up Questions You Might Get
- *What if at most K distinct characters are allowed?* Maintain a frequency map and shrink left when map size > K (LeetCode 340).
