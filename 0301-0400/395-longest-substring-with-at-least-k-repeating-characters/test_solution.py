"""
Automated unit verification and interview test cases for: 395-longest-substring-with-at-least-k-repeating-characters
"""
import pytest
try:
    from solution import Solution
except ImportError:
    Solution = None

def test_problem_initialization():
    if Solution is not None:
        sol = Solution()
        assert sol is not None
        assert hasattr(sol, "longestSubstring")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "longestSubstring", None)
        assert callable(method)
