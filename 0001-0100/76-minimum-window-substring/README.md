# 76. Minimum Window Substring

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/minimum-window-substring/)
[![Topic: Sliding Window](https://img.shields.io/badge/Topic-Sliding%20Window-blue)](https://leetcode.com/problems/minimum-window-substring/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We need to find the shortest substring in s that contains all characters of t (including multiplicity). We maintain a frequency map for t and a `required` count of distinct matched characters. As the right pointer expands the window, we record characters. When all required character counts are satisfied, we contract the left pointer to find the minimal valid window, updating our best answer before the window becomes invalid."

---

### 💡 Intuition & Core Insight
- **Expand to Satisfy, Shrink to Optimize**: Right pointer searches for feasibility; left pointer removes excess baggage to minimize length.
- **The Matched Counter**: Instead of comparing maps of size 26 or 128 each step, tracking the count of fully satisfied characters gives an O(1) condition check.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `s = "ADOBECODEBANC"`, `t = "ABC"`
- Expand until window has 'A', 'B', 'C' -> "ADOBEC" (len 6).
- Shrink left -> 'A' is lost, window no longer valid -> expand right again.
- Window reaches "BECODEBA" -> shrinks -> "CODEBA" -> "ODEBANC" -> "BANC" (len 4).
Minimal window found: "BANC".

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";
        Map<Character, Integer> targetMap = new HashMap<>();
        for (char c : t.toCharArray()) targetMap.put(c, targetMap.getOrDefault(c, 0) + 1);

        Map<Character, Integer> windowMap = new HashMap<>();
        int required = targetMap.size(), formed = 0;
        int left = 0, minLen = Integer.MAX_VALUE, startIdx = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            windowMap.put(c, windowMap.getOrDefault(c, 0) + 1);
            if (targetMap.containsKey(c) && windowMap.get(c).intValue() == targetMap.get(c).intValue()) {
                formed++;
            }

            while (left <= right && formed == required) {
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    startIdx = left;
                }
                char leftChar = s.charAt(left);
                windowMap.put(leftChar, windowMap.get(leftChar) - 1);
                if (targetMap.containsKey(leftChar) && windowMap.get(leftChar) < targetMap.get(leftChar)) {
                    formed--;
                }
                left++;
            }
        }
        return minLen == Integer.MAX_VALUE ? "" : s.substring(startIdx, startIdx + minLen);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        target_counts = Counter(t)
        required = len(target_counts)
        formed = 0
        window_counts = defaultdict(int)
        min_len = float('inf')
        res_indices = (0, 0)
        left = 0

        for right, char in enumerate(s):
            window_counts[char] += 1
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
            while left <= right and formed == required:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res_indices = (left, right)
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed -= 1
                left += 1
        return "" if min_len == float('inf') else s[res_indices[0]:res_indices[1] + 1]
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N + M)$ — O(M) to build target map; left and right pointers each traverse s of length N at most once (2N steps).
- **Space Complexity**: $\mathcal{O}(N + M)$ — Hash maps store unique characters in s and t.

---

### ⚠️ Edge Cases & Interview Traps
1. t longer than s: returns empty string immediately.
2. No valid window: returns empty string.
3. Exact match s == t: returns s.

---

### 💬 Follow-Up Questions You Might Get
- *Can we optimize using array lookups?* Yes, an int[128] ASCII array eliminates Map object boxing overhead.
