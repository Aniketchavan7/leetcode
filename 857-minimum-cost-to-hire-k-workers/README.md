# 857. Minimum Cost to Hire K Workers

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/minimum-cost-to-hire-k-workers)
[![Topic: Greedy & Array & Sorting](https://img.shields.io/badge/Topic-Greedy%20&%20Array%20&%20Sorting-blue)](https://leetcode.com/problems/minimum-cost-to-hire-k-workers)

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
**Sample Input**: `quality = [10,20,5], wage = [70,50,30], k = 2`  
**Expected Output**: `105.00000`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `quality = [10,20,5], wage = [70,50,30], k = 2` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `105.00000` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        int n = quality.length;
        Pair<Double, Integer>[] t = new Pair[n];
        for (int i = 0; i < n; ++i) {
            t[i] = new Pair<>((double) wage[i] / quality[i], quality[i]);
        }
        Arrays.sort(t, (a, b) -> Double.compare(a.getKey(), b.getKey()));
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        double ans = 1e18;
        int tot = 0;
        for (var e : t) {
            tot += e.getValue();
            pq.offer(e.getValue());
            if (pq.size() == k) {
                ans = Math.min(ans, tot * e.getKey());
                tot -= pq.poll();
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def mincostToHireWorkers(
        self, quality: list[int], wage: list[int], k: int
    ) -> float:
        t = sorted(zip(quality, wage), key=lambda x: x[1] / x[0])
        ans, tot = inf, 0
        h = []
        for q, w in t:
            tot += q
            heappush(h, -q)
            if len(h) == k:
                ans = min(ans, w / q * tot)
                tot += heappop(h)
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
