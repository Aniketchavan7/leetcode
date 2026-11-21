# 242. Valid Anagram

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/valid-anagram/)
[![Topic: Arrays & Hashing](https://img.shields.io/badge/Topic-Arrays%20%26%20Hashing-blue)](https://leetcode.com/problems/valid-anagram/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Two strings are anagrams if they have the exact same character counts. First check if lengths match (if not, return false). Then use a fixed-size integer array of length 26 to count frequencies. Increment for string s and decrement for string t. If all counts end at 0, they are anagrams."

---

### 💡 Intuition & Core Insight
- **Fixed-Size Bucket**: For lowercase English letters, a 26-element array provides O(1) space and faster operations than a dynamic Hash Map.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `s = "anagram"`, `t = "nagaram"`
- Lengths match (7 == 7).
- Frequency counts cancel out: 'a': +3 -3 = 0, 'n': +1 -1 = 0, 'g': +1 -1 = 0, 'r': +1 -1 = 0, 'm': +1 -1 = 0.
- All array cells 0 -> True.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        for (int c : count) {
            if (c != 0) return false;
        }
        return true;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord('a')] += 1
            count[ord(char_t) - ord('a')] -= 1
        return all(c == 0 for c in count)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — One pass through the strings of length N, followed by checking 26 integer slots.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant 26-element array.

---

### ⚠️ Edge Cases & Interview Traps
1. Different lengths: fails in O(1) immediately.
2. Identical strings: passes successfully.

---

### 💬 Follow-Up Questions You Might Get
- *What if inputs contain Unicode?* Replace the 26-int array with a HashMap<Character, Integer>.
