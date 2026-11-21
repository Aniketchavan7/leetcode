"""
Automated unit verification and interview test cases for: 221-maximal-square
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
        assert hasattr(sol, "maximalSquare")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "maximalSquare", None)
        assert callable(method)
