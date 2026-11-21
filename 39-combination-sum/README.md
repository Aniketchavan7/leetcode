# 39. Combination Sum

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/combination-sum/)
[![Topic: Backtracking](https://img.shields.io/badge/Topic-Backtracking-blue)](https://leetcode.com/problems/combination-sum/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To find all unique combinations of candidates that sum to target where the same number may be chosen an unlimited number of times: We use Backtracking. At each step, from index `start` onwards, we can either choose candidate[i] (subtracting it from target and recurring with the same index i), or stop if candidate[i] exceeds the remaining target (since candidates can be sorted for early pruning). When remaining target is 0, add the path."

---

### 💡 Intuition & Core Insight
- **Re-using Elements**: Passing index `i` (not `i + 1`) allows unlimited reuse of the current candidate.
- **Avoiding Permutation Duplicates**: By only picking candidates at or after the current index `start`, combinations are generated in non-decreasing index order, guaranteeing uniqueness.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `candidates = [2, 3, 6, 7]`, `target = 7`
- Pick 2 -> target=5. Pick 2 -> target=3. Pick 2 -> target=1 (fails). Backtrack.
- At target=3, pick 3 -> target=0! Found `[2, 2, 3]`.
- Pick 7 -> target=0! Found `[7]`.
Result: `[[2, 2, 3], [7]]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> res = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), res);
        return res;
    }

    private void backtrack(int[] candidates, int remain, int start, List<Integer> path, List<List<Integer>> res) {
        if (remain == 0) {
            res.add(new ArrayList<>(path));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remain) break; // Prune branch (sorted)
            path.add(candidates[i]);
            backtrack(candidates, remain - candidates[i], i, path, res);
            path.remove(path.size() - 1); // Backtrack
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(remain, start, path):
            if remain == 0:
                res.append(list(path))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                backtrack(remain - candidates[i], i, path)
                path.pop()

        backtrack(target, 0, [])
        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(2^{T/M})$ — T is target, M is minimum candidate value; tree depth is bounded by T/M.
- **Space Complexity**: $\mathcal{O}(T/M)$ — Call stack and path list depth bounded by target / min_candidate.

---

### ⚠️ Edge Cases & Interview Traps
1. No combination possible: returns empty list.
2. Single element candidate matching target: returns [[target]].

---

### 💬 Follow-Up Questions You Might Get
- *What if each number can only be used once with duplicate inputs?* Skip duplicates via `if (i > start && candidates[i] == candidates[i-1]) continue;` (Combination Sum II).
