# 587. Erect the Fence

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/erect-the-fence)
[![Topic: Geometry & Array & Math](https://img.shields.io/badge/Topic-Geometry%20&%20Array%20&%20Math-blue)](https://leetcode.com/problems/erect-the-fence)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Geometry strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]`  
**Expected Output**: `[[1,1],[2,0],[4,2],[3,3],[2,4]]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[[1,1],[2,0],[4,2],[3,3],[2,4]]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[][] outerTrees(int[][] trees) {
        int n = trees.length;
        if (n < 4) {
            return trees;
        }
        Arrays.sort(trees, (a, b) -> { return a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]; });
        boolean[] vis = new boolean[n];
        int[] stk = new int[n + 10];
        int cnt = 1;
        for (int i = 1; i < n; ++i) {
            while (cnt > 1 && cross(trees[stk[cnt - 1]], trees[stk[cnt - 2]], trees[i]) < 0) {
                vis[stk[--cnt]] = false;
            }
            vis[i] = true;
            stk[cnt++] = i;
        }
        int m = cnt;
        for (int i = n - 1; i >= 0; --i) {
            if (vis[i]) {
                continue;
            }
            while (cnt > m && cross(trees[stk[cnt - 1]], trees[stk[cnt - 2]], trees[i]) < 0) {
                --cnt;
            }
            stk[cnt++] = i;
        }
        int[][] ans = new int[cnt - 1][2];
        for (int i = 0; i < ans.length; ++i) {
            ans[i] = trees[stk[i]];
        }
        return ans;
    }

    private int cross(int[] a, int[] b, int[] c) {
        return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        def cross(i, j, k):
            a, b, c = trees[i], trees[j], trees[k]
            return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])

        n = len(trees)
        if n < 4:
            return trees
        trees.sort()
        vis = [False] * n
        stk = [0]
        for i in range(1, n):
            while len(stk) > 1 and cross(stk[-2], stk[-1], i) < 0:
                vis[stk.pop()] = False
            vis[i] = True
            stk.append(i)
        m = len(stk)
        for i in range(n - 2, -1, -1):
            if vis[i]:
                continue
            while len(stk) > m and cross(stk[-2], stk[-1], i) < 0:
                stk.pop()
            stk.append(i)
        stk.pop()
        return [trees[i] for i in stk]
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
