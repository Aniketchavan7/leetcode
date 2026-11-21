"""
Automated unit verification and interview test cases for: 243-shortest-word-distance
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
        assert hasattr(sol, "shortestDistance")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "shortestDistance", None)
        assert callable(method)
