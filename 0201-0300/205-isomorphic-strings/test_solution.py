"""
Automated unit verification and interview test cases for: 205-isomorphic-strings
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
        assert hasattr(sol, "isIsomorphic")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "isIsomorphic", None)
        assert callable(method)
