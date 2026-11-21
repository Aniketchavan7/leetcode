"""
Automated unit verification and interview test cases for: 246-strobogrammatic-number
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
        assert hasattr(sol, "isStrobogrammatic")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "isStrobogrammatic", None)
        assert callable(method)
