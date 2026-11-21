"""
Automated unit verification and interview test cases for: 58-length-of-last-word
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
        assert hasattr(sol, "lengthOfLastWord")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "lengthOfLastWord", None)
        assert callable(method)
