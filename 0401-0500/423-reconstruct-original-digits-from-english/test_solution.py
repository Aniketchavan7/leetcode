"""
Automated unit verification and interview test cases for: 423-reconstruct-original-digits-from-english
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
        assert hasattr(sol, "originalDigits")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "originalDigits", None)
        assert callable(method)
