# 675. Cut Off Trees for Golf Event

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/cut-off-trees-for-golf-event)
[![Topic: Breadth-First Search & Array & Matrix](https://img.shields.io/badge/Topic-Breadth-First%20Search%20&%20Array%20&%20Matrix-blue)](https://leetcode.com/problems/cut-off-trees-for-golf-event)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "By maintaining a min-heap or max-heap of size K, we process dynamic streams or Top-K queries in O(N log K) time without sorting the entire collection."

---

### 💡 Intuition & Core Insight
- **Bounded Memory**: Restricting heap size to K keeps space bounded and insertion at O(log K).
- **Extremum Access**: The root always exposes the current threshold in O(1) time.
- **Streaming Feasibility**: New incoming data is evaluated against the root in constant time before heapifying.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `forest = [[1,2,3],[0,0,4],[7,6,5]]`  
**Expected Output**: `6`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `forest = [[1,2,3],[0,0,4],[7,6,5]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `6` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int[] dist = new int[3600];
    private List<List<Integer>> forest;
    private int m;
    private int n;

    public int cutOffTree(List<List<Integer>> forest) {
        this.forest = forest;
        m = forest.size();
        n = forest.get(0).size();
        List<int[]> trees = new ArrayList<>();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (forest.get(i).get(j) > 1) {
                    trees.add(new int[] {forest.get(i).get(j), i * n + j});
                }
            }
        }
        trees.sort(Comparator.comparingInt(a -> a[0]));
        int ans = 0;
        int start = 0;
        for (int[] tree : trees) {
            int end = tree[1];
            int t = bfs(start, end);
            if (t == -1) {
                return -1;
            }
            ans += t;
            start = end;
        }
        return ans;
    }

    private int bfs(int start, int end) {
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        q.offer(new int[] {f(start, end), start});
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;
        int[] dirs = {-1, 0, 1, 0, -1};
        while (!q.isEmpty()) {
            int state = q.poll()[1];
            if (state == end) {
                return dist[state];
            }
            for (int k = 0; k < 4; ++k) {
                int x = state / n + dirs[k];
                int y = state % n + dirs[k + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && forest.get(x).get(y) > 0) {
                    if (dist[x * n + y] > dist[state] + 1) {
                        dist[x * n + y] = dist[state] + 1;
                        q.offer(new int[] {dist[x * n + y] + f(x * n + y, end), x * n + y});
                    }
                }
            }
        }
        return -1;
    }

    private int f(int start, int end) {
        int a = start / n;
        int b = start % n;
        int c = end / n;
        int d = end % n;
        return Math.abs(a - c) + Math.abs(b - d);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        def f(i, j, x, y):
            return abs(i - x) + abs(j - y)

        def bfs(i, j, x, y):
            q = [(f(i, j, x, y), i, j)]
            dist = {i * n + j: 0}
            while q:
                _, i, j = heappop(q)
                step = dist[i * n + j]
                if (i, j) == (x, y):
                    return step
                for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    c, d = i + a, j + b
                    if 0 <= c < m and 0 <= d < n and forest[c][d] > 0:
                        if c * n + d not in dist or dist[c * n + d] > step + 1:
                            dist[c * n + d] = step + 1
                            heappush(q, (dist[c * n + d] + f(c, d, x, y), c, d))
            return -1

        m, n = len(forest), len(forest[0])
        trees = [
            (forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1
        ]
        trees.sort()
        i = j = 0
        ans = 0
        for _, x, y in trees:
            t = bfs(i, j, x, y)
            if t == -1:
                return -1
            ans += t
            i, j = x, y
        return ans
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log K)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(K)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Inverting comparator logic (min-heap vs max-heap).
2. Handling duplicate frequency or tie-breaking order.
3. Empty heap exceptions.

---

### 💬 Follow-Up Questions You Might Get
*Can we do Top-K in O(N) average time?* Quickselect achieves O(N) average time complexity.
