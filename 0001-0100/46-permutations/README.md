# 46. Permutations

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/permutations/)
[![Topic: Backtracking](https://img.shields.io/badge/Topic-Backtracking-blue)](https://leetcode.com/problems/permutations/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Given an array of distinct integers, we construct all N! permutations using Backtracking. At each recursion level, we iterate through all elements. If the element is not already in our current path (tracked in O(1) using a boolean `used` array), we choose it, recurse deeper, and unchoose it on backtrack. When path length equals nums.length, record the permutation."

---

### 💡 Intuition & Core Insight
- **State Space Tree**: The root has N choices, the next level has N-1 choices, down to 1 choice, forming an N! decision tree.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [1, 2, 3]`
- Path: `[1]`, next choices: 2, 3
  - Path: `[1, 2]`, next: 3 -> `[1, 2, 3]` (recorded!)
  - Path: `[1, 3]`, next: 2 -> `[1, 3, 2]` (recorded!)
- Path: `[2]` -> generates `[2, 1, 3]`, `[2, 3, 1]`
- Path: `[3]` -> generates `[3, 1, 2]`, `[3, 2, 1]`
Total 6 permutations.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(nums, used, new ArrayList<>(), res);
        return res;
    }

    private void backtrack(int[] nums, boolean[] used, List<Integer> path, List<List<Integer>> res) {
        if (path.size() == nums.length) {
            res.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            path.add(nums[i]);
            backtrack(nums, used, path, res);
            path.remove(path.size() - 1);
            used[i] = false;
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False

        backtrack([])
        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \cdot N!)$ — N! leaf nodes; copying each leaf path takes O(N) time.
- **Space Complexity**: $\mathcal{O}(N)$ — Recursion depth and path length are bounded by N.

---

### ⚠️ Edge Cases & Interview Traps
1. Single element [1]: returns [[1]].
2. Two elements: returns [[1, 2], [2, 1]].

---

### 💬 Follow-Up Questions You Might Get
- *What if duplicate elements are present?* Sort array and skip duplicate elements unless previous duplicate was used (Permutations II).
