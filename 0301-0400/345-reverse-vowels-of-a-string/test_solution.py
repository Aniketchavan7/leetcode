"""
Automated unit verification and interview test cases for: 345-reverse-vowels-of-a-string
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
        assert hasattr(sol, "reverseVowels")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "reverseVowels", None)
        assert callable(method)
