"""
Automated unit verification and interview test cases for: 176-second-highest-salary
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
        assert hasattr(sol, "second_highest_salary")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "second_highest_salary", None)
        assert callable(method)
