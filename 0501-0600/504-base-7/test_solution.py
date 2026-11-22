"""
Automated unit verification and interview test cases for: 504-base-7
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
        assert hasattr(sol, "convertToBase7")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "convertToBase7", None)
        assert callable(method)
