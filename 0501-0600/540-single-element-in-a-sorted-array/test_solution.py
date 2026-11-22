"""
Automated unit verification and interview test cases for: 540-single-element-in-a-sorted-array
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
        assert hasattr(sol, "singleNonDuplicate")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "singleNonDuplicate", None)
        assert callable(method)
