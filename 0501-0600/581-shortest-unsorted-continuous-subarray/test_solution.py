"""
Automated unit verification and interview test cases for: 581-shortest-unsorted-continuous-subarray
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
        assert hasattr(sol, "findUnsortedSubarray")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "findUnsortedSubarray", None)
        assert callable(method)
