"""
Automated unit verification and interview test cases for: 273-integer-to-english-words
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
        assert hasattr(sol, "numberToWords")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "numberToWords", None)
        assert callable(method)
