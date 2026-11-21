# 207. Course Schedule

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/course-schedule/)
[![Topic: Graph / Topological Sort](https://img.shields.io/badge/Topic-Graph%20/%20Topological%20Sort-blue)](https://leetcode.com/problems/course-schedule/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Prerequisites define a directed graph where an edge `b -> a` means course b must be taken before a. Can all courses be finished? Only if the graph has NO directed cycles. We use Kahn's Algorithm (BFS Topological Sort): 1) Compute in-degrees of all courses. 2) Enqueue all courses with in-degree 0 (no prerequisites). 3) Dequeue a course, decrement in-degrees of its dependent neighbors; if a neighbor reaches in-degree 0, enqueue it. If total processed courses == numCourses, finish is possible."

---

### 💡 Intuition & Core Insight
- **Cycle Detection via Unresolvable In-Degrees**: Nodes trapped in a cycle can never reduce their in-degrees to 0, so they will never enter the queue.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `numCourses = 2`, `prerequisites = [[1, 0]]` (0 -> 1)
- In-degrees: 0: 0, 1: 1
- Queue starts with `[0]` (in-degree 0)
- Process 0: processed=1, neighbor 1 in-degree becomes 0 -> Queue: `[1]`
- Process 1: processed=2 -> Queue empty.
processed (2) == numCourses (2) -> True!

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        int[] inDegree = new int[numCourses];

        for (int[] pre : prerequisites) {
            adj.get(pre[1]).add(pre[0]);
            inDegree[pre[0]]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) queue.add(i);
        }

        int count = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            count++;
            for (int neighbor : adj.get(course)) {
                if (--inDegree[neighbor] == 0) {
                    queue.add(neighbor);
                }
            }
        }
        return count == numCourses;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0

        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(V + E)$ — V courses and E prerequisite pairs are each processed once.
- **Space Complexity**: $\mathcal{O}(V + E)$ — Adjacency list stores E edges and inDegree array stores V vertices.

---

### ⚠️ Edge Cases & Interview Traps
1. Mutual dependency [[1, 0], [0, 1]]: all in-degrees >= 1, queue empty, returns false.
2. No prerequisites: all courses have in-degree 0, returns true.

---

### 💬 Follow-Up Questions You Might Get
- *How to return the actual course order?* Record the order courses are dequeued (Course Schedule II).
