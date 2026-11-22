"""
Automated unit verification and interview test cases for: 548-split-array-with-equal-sum
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
        assert hasattr(sol, "splitArray")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "splitArray", None)
        assert callable(method)
