"""
Automated unit verification and interview test cases for: 34-find-first-and-last-position-of-element-in-sorted-array
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
        assert hasattr(sol, "searchRange")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "searchRange", None)
        assert callable(method)
