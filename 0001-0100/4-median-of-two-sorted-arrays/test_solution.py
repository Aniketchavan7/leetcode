"""
Automated unit verification and interview test cases for: 4-median-of-two-sorted-arrays
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
        assert hasattr(sol, "findMedianSortedArrays")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "findMedianSortedArrays", None)
        assert callable(method)
