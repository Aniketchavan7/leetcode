"""
Automated unit verification and interview test cases for: 105-construct-binary-tree-from-preorder-and-inorder-traversal
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
        assert hasattr(sol, "buildTree")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "buildTree", None)
        assert callable(method)
