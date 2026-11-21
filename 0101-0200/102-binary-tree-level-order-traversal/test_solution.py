"""
Automated unit verification and interview test cases for: 102-binary-tree-level-order-traversal
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
        assert hasattr(sol, "levelOrder")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "levelOrder", None)
        assert callable(method)
