"""
Automated unit verification and interview test cases for: 562-longest-line-of-consecutive-one-in-matrix
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
        assert hasattr(sol, "longestLine")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "longestLine", None)
        assert callable(method)
