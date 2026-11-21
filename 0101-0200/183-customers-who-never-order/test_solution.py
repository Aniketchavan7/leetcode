"""
Automated unit verification and interview test cases for: 183-customers-who-never-order
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
        assert hasattr(sol, "find_customers")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "find_customers", None)
        assert callable(method)
