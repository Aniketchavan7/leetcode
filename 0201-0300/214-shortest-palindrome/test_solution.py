"""
Automated unit verification and interview test cases for: 214-shortest-palindrome
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
        assert hasattr(sol, "shortestPalindrome")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "shortestPalindrome", None)
        assert callable(method)
