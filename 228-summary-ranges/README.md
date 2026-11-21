# 228. Summary Ranges

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/summary-ranges)
[![Topic: Array](https://img.shields.io/badge/Topic-Array-blue)](https://leetcode.com/problems/summary-ranges)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Array strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `nums = [0,1,2,4,5,7]`  
**Expected Output**: `[&quot;0-&gt;2&quot;,&quot;4-&gt;5&quot;,&quot;7&quot;]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums = [0,1,2,4,5,7]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[&quot;0-&gt;2&quot;,&quot;4-&gt;5&quot;,&quot;7&quot;]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> ans = new ArrayList<>();
        for (int i = 0, j, n = nums.length; i < n; i = j + 1) {
            j = i;
            while (j + 1 < n && nums[j + 1] == nums[j] + 1) {
                ++j;
            }
            ans.add(f(nums, i, j));
        }
        return ans;
    }

    private String f(int[] nums, int i, int j) {
        return i == j ? nums[i] + "" : String.format("%d->%d", nums[i], nums[j]);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        def f(i: int, j: int) -> str:
            return str(nums[i]) if i == j else f'{nums[i]}->{nums[j]}'

        i = 0
        n = len(nums)
        ans = []
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            ans.append(f(i, j))
            i = j + 1
        return ans
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Handling empty or single-element inputs.
2. Boundary index arithmetic and potential overflow.
3. Duplicate or negative values in input collections.

---

### 💬 Follow-Up Questions You Might Get
*How does this scale to distributed streams?* Hash partitioning across shards or MapReduce pipelines can process data in parallel.
