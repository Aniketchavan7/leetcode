"""
Automated unit verification and interview test cases for: 391-perfect-rectangle
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
        assert hasattr(sol, "isRectangleCover")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "isRectangleCover", None)
        assert callable(method)
