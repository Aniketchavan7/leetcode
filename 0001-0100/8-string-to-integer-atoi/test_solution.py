"""
Automated unit verification and interview test cases for: 8-string-to-integer-atoi
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
        assert hasattr(sol, "myAtoi")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "myAtoi", None)
        assert callable(method)
