# 78. Subsets

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/subsets/)
[![Topic: Backtracking](https://img.shields.io/badge/Topic-Backtracking-blue)](https://leetcode.com/problems/subsets/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To generate all 2^N subsets (the power set) of an array of unique integers: In our backtracking function, every state reached in the search tree is a valid subset, so we immediately add a snapshot of `path` to the result list. We then loop from index `start` to n - 1, including `nums[i]`, recursing with `i + 1`, and backtracking."

---

### 💡 Intuition & Core Insight
- **Binary Inclusion Choice**: For every element, we have two choices: include or exclude, resulting in 2^N total subsets.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [1, 2, 3]`
- start=0, path=[] -> record `[]`
  - pick 1 -> path=[1] -> record `[1]`
    - pick 2 -> path=[1,2] -> record `[1,2]`
      - pick 3 -> path=[1,2,3] -> record `[1,2,3]`
    - pick 3 -> path=[1,3] -> record `[1,3]`
  - pick 2 -> path=[2] -> record `[2]`, `[2,3]`
  - pick 3 -> path=[3] -> record `[3]`
Total 8 subsets.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), res);
        return res;
    }

    private void backtrack(int[] nums, int start, List<Integer> path, List<List<Integer>> res) {
        res.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrack(nums, i + 1, path, res);
            path.remove(path.size() - 1);
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(start, path):
            res.append(list(path))
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \cdot 2^N)$ — 2^N total subsets, each taking O(N) to copy into result list.
- **Space Complexity**: $\mathcal{O}(N)$ — Recursion depth is at most N.

---

### ⚠️ Edge Cases & Interview Traps
1. Empty input: returns [[]].
2. Single element [0]: returns [[], [0]].

---

### 💬 Follow-Up Questions You Might Get
- *Can we generate subsets using Bit Manipulation?* Yes, iterate from 0 to 2^N - 1, checking bit j to include nums[j].
