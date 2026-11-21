# 373. Find K Pairs with Smallest Sums

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/find-k-pairs-with-smallest-sums)
[![Topic: Array & Heap (Priority Queue)](https://img.shields.io/badge/Topic-Array%20&%20Heap%20(Priority%20Queue)-blue)](https://leetcode.com/problems/find-k-pairs-with-smallest-sums)

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
**Sample Input**: `nums1 = [1,7,11], nums2 = [2,4,6], k = 3`  
**Expected Output**: `[[1,2],[1,4],[1,6]]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `nums1 = [1,7,11], nums2 = [2,4,6], k = 3` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[[1,2],[1,4],[1,6]]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        for (int i = 0; i < Math.min(nums1.length, k); ++i) {
            q.offer(new int[] {nums1[i] + nums2[0], i, 0});
        }
        List<List<Integer>> ans = new ArrayList<>();
        while (!q.isEmpty() && k > 0) {
            int[] e = q.poll();
            ans.add(Arrays.asList(nums1[e[1]], nums2[e[2]]));
            --k;
            if (e[2] + 1 < nums2.length) {
                q.offer(new int[] {nums1[e[1]] + nums2[e[2] + 1], e[1], e[2] + 1});
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        q = [[u + nums2[0], i, 0] for i, u in enumerate(nums1[:k])]
        heapify(q)
        ans = []
        while q and k > 0:
            _, i, j = heappop(q)
            ans.append([nums1[i], nums2[j]])
            k -= 1
            if j + 1 < len(nums2):
                heappush(q, [nums1[i] + nums2[j + 1], i, j + 1])
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
