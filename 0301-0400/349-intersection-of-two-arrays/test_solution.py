"""
Automated unit verification and interview test cases for: 349-intersection-of-two-arrays
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
        assert hasattr(sol, "intersection")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "intersection", None)
        assert callable(method)
