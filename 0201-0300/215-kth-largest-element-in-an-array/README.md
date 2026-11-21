# 215. Kth Largest Element in an Array

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/kth-largest-element-in-an-array/)
[![Topic: Heap / QuickSelect](https://img.shields.io/badge/Topic-Heap%20/%20QuickSelect-blue)](https://leetcode.com/problems/kth-largest-element-in-an-array/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To find the kth largest element without sorting in O(N log N): We can maintain a Min-Heap of size k. For each element in the array, push it into the heap; if the heap size exceeds k, pop the smallest. At the end, the root of the min-heap is the kth largest element. Alternatively, QuickSelect achieves average O(N) linear time."

---

### 💡 Intuition & Core Insight
- **Min-Heap of Size K**: The top of a min-heap of size k is the smallest among the k largest elements, which is by definition the kth largest overall.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [3, 2, 1, 5, 6, 4]`, `k = 2`
- num=3: heap=[3]
- num=2: heap=[2, 3]
- num=1: push 1 -> [1, 3, 2], size > 2 -> poll 1 -> heap=[2, 3]
- num=5: push 5 -> [2, 3, 5], poll 2 -> heap=[3, 5]
- num=6: push 6 -> [3, 5, 6], poll 3 -> heap=[5, 6]
- num=4: push 4 -> [4, 6, 5], poll 4 -> heap=[5, 6]
Root of min-heap = 5.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int num : nums) {
            minHeap.add(num);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        return minHeap.peek();
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heappush(min_heap, num)
            if len(min_heap) > k:
                heappop(min_heap)
        return min_heap[0]
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log k)$ — N insertions and deletions into a heap of fixed size k.
- **Space Complexity**: $\mathcal{O}(k)$ — Min-heap maintains at most k elements.

---

### ⚠️ Edge Cases & Interview Traps
1. k = 1: returns array maximum.
2. k = N: returns array minimum.

---

### 💬 Follow-Up Questions You Might Get
- *Can we achieve average O(N) time?* Yes, using QuickSelect with random pivot selection.
