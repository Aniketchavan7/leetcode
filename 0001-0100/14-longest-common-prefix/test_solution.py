"""
Automated unit verification and interview test cases for: 14-longest-common-prefix
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
        assert hasattr(sol, "longestCommonPrefix")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "longestCommonPrefix", None)
        assert callable(method)
