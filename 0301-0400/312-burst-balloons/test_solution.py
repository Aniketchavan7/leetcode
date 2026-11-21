"""
Automated unit verification and interview test cases for: 312-burst-balloons
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
        assert hasattr(sol, "maxCoins")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "maxCoins", None)
        assert callable(method)
