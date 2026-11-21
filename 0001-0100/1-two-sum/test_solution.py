import pytest
from solution import Solution

def test_basic():
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]

def test_duplicates():
    sol = Solution()
    assert sol.twoSum([3, 3], 6) == [0, 1]

def test_negative_numbers():
    sol = Solution()
    assert sol.twoSum([-3, 4, 3, 90], 0) == [0, 2]
