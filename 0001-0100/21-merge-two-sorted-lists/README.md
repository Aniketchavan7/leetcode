# 21. Merge Two Sorted Lists

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/merge-two-sorted-lists/)
[![Topic: Linked List](https://img.shields.io/badge/Topic-Linked%20List-blue)](https://leetcode.com/problems/merge-two-sorted-lists/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We maintain a dummy head and a current pointer. While both lists have nodes, compare their values and attach the smaller node to current.next, advancing the chosen list. When one list is exhausted, splice the entire remainder of the other list directly in O(1)."

---

### 💡 Intuition & Core Insight
- **Splice Remaining Sublist**: Because both lists are already sorted, once one terminates, the rest of the other is already sorted and can be attached in one pointer assignment.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `l1 = 1->2->4`, `l2 = 1->3->4`
- Dummy -> 0
- Compare 1 & 1: attach l1's 1 -> Dummy -> 1
- Compare 2 & 1: attach l2's 1 -> Dummy -> 1 -> 1
- Compare 2 & 3: attach l1's 2 -> Dummy -> 1 -> 1 -> 2
- Compare 4 & 3: attach l2's 3 -> Dummy -> 1 -> 1 -> 2 -> 3
- Compare 4 & 4: attach l1's 4
- Attach remaining l2's 4
Result: `1->1->2->3->4->4`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(-1);
        ListNode current = dummy;

        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }

        current.next = (list1 != null) ? list1 : list2;
        return dummy.next;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N + M)$ — Traverses through each node in both lists of lengths N and M once.
- **Space Complexity**: $\mathcal{O}(1)$ — Re-wires existing pointers in-place with zero new node allocations.

---

### ⚠️ Edge Cases & Interview Traps
1. One list is null: returns the other list immediately.
2. Both lists null: returns null.

---

### 💬 Follow-Up Questions You Might Get
- *How to do this recursively?* Return smaller node with its next pointing to mergeTwoLists(smaller.next, other).
