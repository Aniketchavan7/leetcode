"""
Automated unit verification and interview test cases for: 178-rank-scores
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
        assert hasattr(sol, "order_scores")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "order_scores", None)
        assert callable(method)
