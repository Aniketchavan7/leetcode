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
