"""
Automated unit verification and interview test cases for: 187-repeated-dna-sequences
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
        assert hasattr(sol, "findRepeatedDnaSequences")

def test_interface_signature():
    if Solution is not None:
        sol = Solution()
        method = getattr(sol, "findRepeatedDnaSequences", None)
        assert callable(method)
