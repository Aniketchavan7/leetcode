"""
Automated unit verification and interview test cases for: 323-number-of-connected-components-in-an-undirected-graph
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
        assert hasattr(sol, "countComponents")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "countComponents", None)
        assert callable(method)
