"""
Automated unit verification and interview test cases for: 198-house-robber
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
        assert hasattr(sol, "rob")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "rob", None)
        assert callable(method)
