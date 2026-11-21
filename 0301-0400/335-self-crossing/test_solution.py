"""
Automated unit verification and interview test cases for: 335-self-crossing
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
        assert hasattr(sol, "isSelfCrossing")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "isSelfCrossing", None)
        assert callable(method)
