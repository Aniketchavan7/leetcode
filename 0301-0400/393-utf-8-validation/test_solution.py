"""
Automated unit verification and interview test cases for: 393-utf-8-validation
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
        assert hasattr(sol, "validUtf8")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "validUtf8", None)
        assert callable(method)
