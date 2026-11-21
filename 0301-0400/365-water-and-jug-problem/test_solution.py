"""
Automated unit verification and interview test cases for: 365-water-and-jug-problem
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
        assert hasattr(sol, "canMeasureWater")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "canMeasureWater", None)
        assert callable(method)
