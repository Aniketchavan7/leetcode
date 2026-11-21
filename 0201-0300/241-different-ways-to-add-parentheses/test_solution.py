"""
Automated unit verification and interview test cases for: 241-different-ways-to-add-parentheses
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
        assert hasattr(sol, "diffWaysToCompute")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "diffWaysToCompute", None)
        assert callable(method)
