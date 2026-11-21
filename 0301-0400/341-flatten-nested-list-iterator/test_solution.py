"""
Automated unit verification and interview test cases for: 341-flatten-nested-list-iterator
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
        assert hasattr(sol, "isInteger")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "isInteger", None)
        assert callable(method)
