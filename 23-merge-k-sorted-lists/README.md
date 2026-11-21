# 23. Merge k Sorted Lists

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/merge-k-sorted-lists/)
[![Topic: Heap / Priority Queue](https://img.shields.io/badge/Topic-Heap%20/%20Priority%20Queue-blue)](https://leetcode.com/problems/merge-k-sorted-lists/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We have k sorted lists. We insert the head of each non-empty list into a Min-Heap (Priority Queue). The minimum element across all active lists is always at the top of the heap. We pop the smallest node, attach it to our merged list, and if that node has a next pointer, push next into the heap. Repeating this until the heap is empty merges all N total nodes in O(N log k) time."

---

### 💡 Intuition & Core Insight
- **Tournament Selection**: At any moment, we only need to compare the current frontrunner of each list (at most k nodes in the heap at any time).
- **Alternative Divide and Conquer**: Pairwise merging lists like Merge Sort achieves the same O(N log k) without heap overhead.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `[[1->4->5], [1->3->4], [2->6]]`
- Heap holds heads: `{1(L1), 1(L2), 2(L3)}`
- Pop 1(L1), attach to list. Push 4(L1) -> Heap: `{1(L2), 2(L3), 4(L1)}`
- Pop 1(L2), attach. Push 3(L2) -> Heap: `{2(L3), 3(L2), 4(L1)}`
- Continue until all nodes drained.
Result: `1->1->2->3->4->4->5->6`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;

        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.val, b.val));
        for (ListNode node : lists) {
            if (node != null) pq.add(node);
        }

        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

        while (!pq.isEmpty()) {
            ListNode smallest = pq.poll();
            tail.next = smallest;
            tail = tail.next;

            if (smallest.next != null) {
                pq.add(smallest.next);
            }
        }
        return dummy.next;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log k)$ — N total nodes across all lists; each insertion and deletion in a heap of size k takes O(log k).
- **Space Complexity**: $\mathcal{O}(k)$ — Min-heap holds at most k elements simultaneously.

---

### ⚠️ Edge Cases & Interview Traps
1. lists array is empty []: returns null.
2. lists contains empty lists [null, null]: handled gracefully without adding to heap.

---

### 💬 Follow-Up Questions You Might Get
- *Can we solve this without a PriorityQueue?* Yes, divide-and-conquer merge pairs in O(1) space.
