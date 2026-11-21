"""
Automated unit verification and interview test cases for: 302-smallest-rectangle-enclosing-black-pixels
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
        assert hasattr(sol, "minArea")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "minArea", None)
        assert callable(method)
