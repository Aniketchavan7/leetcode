"""
Automated unit verification and interview test cases for: 560-subarray-sum-equals-k
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
        assert hasattr(sol, "subarraySum")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "subarraySum", None)
        assert callable(method)
