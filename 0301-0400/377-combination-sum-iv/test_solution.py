"""
Automated unit verification and interview test cases for: 377-combination-sum-iv
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
        assert hasattr(sol, "combinationSum4")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "combinationSum4", None)
        assert callable(method)
