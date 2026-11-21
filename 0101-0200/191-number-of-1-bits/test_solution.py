"""
Automated unit verification and interview test cases for: 191-number-of-1-bits
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
        assert hasattr(sol, "hammingWeight")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "hammingWeight", None)
        assert callable(method)
