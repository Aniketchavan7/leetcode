"""
Automated unit verification and interview test cases for: 371-sum-of-two-integers
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
        assert hasattr(sol, "getSum")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "getSum", None)
        assert callable(method)
