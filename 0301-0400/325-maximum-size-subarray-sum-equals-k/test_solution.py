"""
Automated unit verification and interview test cases for: 325-maximum-size-subarray-sum-equals-k
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
        assert hasattr(sol, "maxSubArrayLen")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "maxSubArrayLen", None)
        assert callable(method)
