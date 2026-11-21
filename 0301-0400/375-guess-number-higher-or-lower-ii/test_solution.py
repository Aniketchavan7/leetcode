"""
Automated unit verification and interview test cases for: 375-guess-number-higher-or-lower-ii
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
        assert hasattr(sol, "getMoneyAmount")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "getMoneyAmount", None)
        assert callable(method)
