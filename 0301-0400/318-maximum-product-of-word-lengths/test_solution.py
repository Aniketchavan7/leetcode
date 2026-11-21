"""
Automated unit verification and interview test cases for: 318-maximum-product-of-word-lengths
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
        assert hasattr(sol, "maxProduct")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "maxProduct", None)
        assert callable(method)
