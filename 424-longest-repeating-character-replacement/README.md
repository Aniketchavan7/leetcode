# 424. Longest Repeating Character Replacement

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/longest-repeating-character-replacement/)
[![Topic: Sliding Window](https://img.shields.io/badge/Topic-Sliding%20Window-blue)](https://leetcode.com/problems/longest-repeating-character-replacement/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "A window of length L is valid if `L - maxFrequency <= k` (meaning the number of letters we need to replace does not exceed k). We expand the window to the right, updating character counts and the max frequency seen. When the window becomes invalid, we shift the left pointer forward by 1, preserving the maximum window size seen so far."

---

### 💡 Intuition & Core Insight
- **The Core Invariant**: `(window_length - count_of_most_frequent_char) <= k`.
- **Why maxFreq Doesn't Need to Shrink**: We only care about finding a window strictly larger than our current max. If maxFreq decreases during a left shift, it cannot produce a new record anyway, so recalculating maxFreq on shrink is unnecessary.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `s = "AABABBA"`, `k = 1`
- R=0 'A': len=1, maxF=1, replacements=0 <= 1 -> valid, max=1
- R=1 'A': len=2, maxF=2, replacements=0 <= 1 -> valid, max=2
- R=2 'B': len=3, maxF=2, replacements=1 <= 1 -> valid, max=3
- R=3 'A': len=4, maxF=3, replacements=1 <= 1 -> valid, max=4
- R=4 'B': len=5, maxF=3, replacements=2 > 1 -> invalid! L moves 1 step.
Result: 4.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int left = 0, maxFreq = 0, maxLen = 0;
        for (int right = 0; right < s.length(); right++) {
            maxFreq = Math.max(maxFreq, ++count[s.charAt(right) - 'A']);
            while ((right - left + 1) - maxFreq > k) {
                count[s.charAt(left) - 'A']--;
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_freq = 0
        max_len = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Both left and right pointers traverse the string at most once.
- **Space Complexity**: $\mathcal{O}(1)$ — Array of 26 integers for uppercase English letters.

---

### ⚠️ Edge Cases & Interview Traps
1. k >= length of s: can replace all characters to be uniform, returns length.
2. All same characters: replacements needed is 0, returns length.

---

### 💬 Follow-Up Questions You Might Get
- *What if s contains arbitrary Unicode characters?* Use a dynamic hash map instead of a 26-int array.
