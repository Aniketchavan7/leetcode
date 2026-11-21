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
