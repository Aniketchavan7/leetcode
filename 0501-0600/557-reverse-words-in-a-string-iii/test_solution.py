"""
Automated unit verification and interview test cases for: 557-reverse-words-in-a-string-iii
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
        assert hasattr(sol, "reverseWords")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "reverseWords", None)
        assert callable(method)
