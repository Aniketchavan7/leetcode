"""
Automated unit verification and interview test cases for: 357-count-numbers-with-unique-digits
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
        assert hasattr(sol, "countNumbersWithUniqueDigits")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "countNumbersWithUniqueDigits", None)
        assert callable(method)
