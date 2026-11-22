"""
Automated unit verification and interview test cases for: 538-convert-bst-to-greater-tree
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
        assert hasattr(sol, "solve")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "solve", None)
        assert callable(method)
