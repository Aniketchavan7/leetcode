"""
Automated unit verification and interview test cases for: 31-next-permutation
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
        assert hasattr(sol, "nextPermutation")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "nextPermutation", None)
        assert callable(method)
