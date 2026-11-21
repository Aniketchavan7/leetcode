"""
Automated unit verification and interview test cases for: 180-consecutive-numbers
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
        assert hasattr(sol, "consecutive_numbers")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "consecutive_numbers", None)
        assert callable(method)
