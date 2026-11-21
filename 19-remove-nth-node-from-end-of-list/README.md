# 19. Remove Nth Node From End of List

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
[![Topic: Linked List](https://img.shields.io/badge/Topic-Linked%20List-blue)](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We use a two-pointer technique with a `dummy` node before the head. Advance the `fast` pointer n + 1 steps ahead of `slow`. Then move both pointers together one step at a time until `fast` reaches null. `slow` will now point directly to the node right before the one to be deleted, allowing in-place removal via `slow.next = slow.next.next`."

---

### 💡 Intuition & Core Insight
- **The Fixed-Gap Sliding Ruler**: Maintaining an exact gap of n between two pointers ensures that when the leading pointer falls off the list, the trailing pointer is positioned exactly at the target predecessor.
- **Dummy Node Eliminates Head Edge Case**: Prepended dummy node simplifies deleting the head without special-case branching.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `head = [1, 2, 3, 4, 5]`, `n = 2`
- Dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> null
- Advance fast n + 1 = 3 steps: fast points to 3.
- Advance fast and slow together until fast is null:
  - fast=4, slow=1
  - fast=5, slow=2
  - fast=null, slow=3
- slow is at 3! Remove next: `3.next = 5`.
Result: `[1, 2, 3, 5]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode fast = dummy, slow = dummy;

        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }

        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }

        slow.next = slow.next.next;
        return dummy.next;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(L)$ — One single traversal of the linked list of length L.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary pointers.

---

### ⚠️ Edge Cases & Interview Traps
1. Deleting head node (n == length): dummy node cleanly handles it without null pointer exceptions.
2. Single-node list: returns null.

---

### 💬 Follow-Up Questions You Might Get
- *Can this be done in two passes?* Yes, count length L first, then delete node at L - n + 1, but one-pass is cleaner.
