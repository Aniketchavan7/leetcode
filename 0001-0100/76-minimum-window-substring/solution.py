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
