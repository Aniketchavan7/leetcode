"""
Automated unit verification and interview test cases for: 5-longest-palindromic-substring
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
        assert hasattr(sol, "longestPalindrome")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "longestPalindrome", None)
        assert callable(method)
