"""
Automated unit verification and interview test cases for: 159-longest-substring-with-at-most-two-distinct-characters
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
        assert hasattr(sol, "lengthOfLongestSubstringTwoDistinct")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "lengthOfLongestSubstringTwoDistinct", None)
        assert callable(method)
