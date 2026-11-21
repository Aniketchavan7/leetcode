# 913. Cat and Mouse

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/cat-and-mouse)
[![Topic: Graph & Topological Sort & Memoization](https://img.shields.io/badge/Topic-Graph%20&%20Topological%20Sort%20&%20Memoization-blue)](https://leetcode.com/problems/cat-and-mouse)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "In this problem, subproblems overlap and possess optimal substructure. Instead of an exponential recursive tree, we define a memoized state array where dp[i] captures the optimal decision up to index i, transitioning in polynomial time."

---

### 💡 Intuition & Core Insight
- **Brute Force Bottleneck**: Exploring all state combinations yields exponential O(2^N) or O(N!) complexity.
- **Optimal Substructure**: The optimal solution at state i depends strictly on already computed sub-states.
- **State Invariant**: Maintaining optimal transitions avoids re-evaluating subproblems.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]`  
**Expected Output**: `0`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `0` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int n;
    private int[][] g;
    private int[][][] ans;
    private int[][][] degree;

    private static final int HOLE = 0, MOUSE_START = 1, CAT_START = 2;
    private static final int MOUSE_TURN = 0, CAT_TURN = 1;
    private static final int MOUSE_WIN = 1, CAT_WIN = 2, TIE = 0;

    public int catMouseGame(int[][] graph) {
        n = graph.length;
        g = graph;
        ans = new int[n][n][2];
        degree = new int[n][n][2];
        for (int i = 0; i < n; ++i) {
            for (int j = 1; j < n; ++j) {
                degree[i][j][MOUSE_TURN] = g[i].length;
                degree[i][j][CAT_TURN] = g[j].length;
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j : g[HOLE]) {
                --degree[i][j][CAT_TURN];
            }
        }
        Deque<int[]> q = new ArrayDeque<>();
        for (int j = 1; j < n; ++j) {
            ans[0][j][MOUSE_TURN] = MOUSE_WIN;
            ans[0][j][CAT_TURN] = MOUSE_WIN;
            q.offer(new int[] {0, j, MOUSE_TURN});
            q.offer(new int[] {0, j, CAT_TURN});
        }
        for (int i = 1; i < n; ++i) {
            ans[i][i][MOUSE_TURN] = CAT_WIN;
            ans[i][i][CAT_TURN] = CAT_WIN;
            q.offer(new int[] {i, i, MOUSE_TURN});
            q.offer(new int[] {i, i, CAT_TURN});
        }
        while (!q.isEmpty()) {
            int[] state = q.poll();
            int t = ans[state[0]][state[1]][state[2]];
            List<int[]> prevStates = getPrevStates(state);
            for (var prevState : prevStates) {
                int pm = prevState[0], pc = prevState[1], pt = prevState[2];
                if (ans[pm][pc][pt] == TIE) {
                    boolean win
                        = (t == MOUSE_WIN && pt == MOUSE_TURN) || (t == CAT_WIN && pt == CAT_TURN);
                    if (win) {
                        ans[pm][pc][pt] = t;
                        q.offer(prevState);
                    } else {
                        if (--degree[pm][pc][pt] == 0) {
                            ans[pm][pc][pt] = t;
                            q.offer(prevState);
                        }
                    }
                }
            }
        }
        return ans[MOUSE_START][CAT_START][MOUSE_TURN];
    }

    private List<int[]> getPrevStates(int[] state) {
        List<int[]> pre = new ArrayList<>();
        int m = state[0], c = state[1], t = state[2];
        int pt = t ^ 1;
        if (pt == CAT_TURN) {
            for (int pc : g[c]) {
                if (pc != HOLE) {
                    pre.add(new int[] {m, pc, pt});
                }
            }
        } else {
            for (int pm : g[m]) {
                pre.add(new int[] {pm, c, pt});
            }
        }
        return pre;
    }
}
```

#### Python 3 Solution
```python
HOLE, MOUSE_START, CAT_START = 0, 1, 2
MOUSE_TURN, CAT_TURN = 0, 1
MOUSE_WIN, CAT_WIN, TIE = 1, 2, 0


class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        def get_prev_states(state):
            m, c, t = state
            pt = t ^ 1
            pre = []
            if pt == CAT_TURN:
                for pc in graph[c]:
                    if pc != HOLE:
                        pre.append((m, pc, pt))
            else:
                for pm in graph[m]:
                    pre.append((pm, c, pt))
            return pre

        n = len(graph)
        ans = [[[0, 0] for _ in range(n)] for _ in range(n)]
        degree = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(1, n):
                degree[i][j][MOUSE_TURN] = len(graph[i])
                degree[i][j][CAT_TURN] = len(graph[j])
            for j in graph[HOLE]:
                degree[i][j][CAT_TURN] -= 1
        q = deque()
        for j in range(1, n):
            ans[0][j][MOUSE_TURN] = ans[0][j][CAT_TURN] = MOUSE_WIN
            q.append((0, j, MOUSE_TURN))
            q.append((0, j, CAT_TURN))
        for i in range(1, n):
            ans[i][i][MOUSE_TURN] = ans[i][i][CAT_TURN] = CAT_WIN
            q.append((i, i, MOUSE_TURN))
            q.append((i, i, CAT_TURN))
        while q:
            state = q.popleft()
            t = ans[state[0]][state[1]][state[2]]
            for prev_state in get_prev_states(state):
                pm, pc, pt = prev_state
                if ans[pm][pc][pt] == TIE:
                    win = (t == MOUSE_WIN and pt == MOUSE_TURN) or (
                        t == CAT_WIN and pt == CAT_TURN
                    )
                    if win:
                        ans[pm][pc][pt] = t
                        q.append(prev_state)
                    else:
                        degree[pm][pc][pt] -= 1
                        if degree[pm][pc][pt] == 0:
                            ans[pm][pc][pt] = t
                            q.append(prev_state)
        return ans[MOUSE_START][CAT_START][MOUSE_TURN]
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Boundary states at index 0 and 1.
2. Integer overflow when accumulating large transitions.
3. Base case initialization of unreachable states.

---

### 💬 Follow-Up Questions You Might Get
*Can we optimize space?* Yes, if each state depends only on the previous k states, we can reduce space from O(N) to O(1) using rolling variables.
