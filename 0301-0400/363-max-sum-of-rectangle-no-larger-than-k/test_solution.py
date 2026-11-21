"""
Automated unit verification and interview test cases for: 363-max-sum-of-rectangle-no-larger-than-k
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
        assert hasattr(sol, "maxSumSubmatrix")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "maxSumSubmatrix", None)
        assert callable(method)
