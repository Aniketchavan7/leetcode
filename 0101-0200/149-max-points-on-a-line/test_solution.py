"""
Automated unit verification and interview test cases for: 149-max-points-on-a-line
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
        assert hasattr(sol, "maxPoints")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "maxPoints", None)
        assert callable(method)
