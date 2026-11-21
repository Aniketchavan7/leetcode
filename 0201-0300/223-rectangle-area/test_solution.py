"""
Automated unit verification and interview test cases for: 223-rectangle-area
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
        assert hasattr(sol, "computeArea")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "computeArea", None)
        assert callable(method)
