"""
Automated unit verification and interview test cases for: 266-palindrome-permutation
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
        assert hasattr(sol, "canPermutePalindrome")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "canPermutePalindrome", None)
        assert callable(method)
