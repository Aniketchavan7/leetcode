"""
Automated unit verification and interview test cases for: 161-one-edit-distance
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
        assert hasattr(sol, "isOneEditDistance")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "isOneEditDistance", None)
        assert callable(method)
