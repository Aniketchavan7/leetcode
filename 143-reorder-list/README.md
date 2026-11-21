# 143. Reorder List

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/reorder-list/)
[![Topic: Linked List](https://img.shields.io/badge/Topic-Linked%20List-blue)](https://leetcode.com/problems/reorder-list/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To reorder L0 -> L1 -> ... -> Ln into L0 -> Ln -> L1 -> Ln-1... in O(1) space: 1) Find the middle of the list using fast and slow pointers. 2) Reverse the second half of the list. 3) Interleave the first half and the reversed second half node by node."

---

### 💡 Intuition & Core Insight
- **Three Classic Linked List Primitives**: Combines 1) Middle finding, 2) In-place list reversal, 3) Two-pointer interleaving.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `1 -> 2 -> 3 -> 4 -> 5`
1. Find mid: `1 -> 2 -> 3`, second half: `4 -> 5`
2. Reverse second half: `5 -> 4`
3. Interleave `1 -> 2 -> 3` and `5 -> 4`:
   - 1 -> 5 -> 2 -> 4 -> 3
Result: `1 -> 5 -> 2 -> 4 -> 3`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;

        // Step 1: Find middle node
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Step 2: Reverse second half
        ListNode prev = null, curr = slow.next;
        slow.next = null; // Split lists
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        // Step 3: Merge two halves
        ListNode first = head, second = prev;
        while (second != null) {
            ListNode tmp1 = first.next, tmp2 = second.next;
            first.next = second;
            second.next = tmp1;
            first = tmp1;
            second = tmp2;
        }
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Interleave
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Three linear passes: N/2 for mid, N/2 for reverse, N/2 for merge.
- **Space Complexity**: $\mathcal{O}(1)$ — In-place pointer rewiring without extra node allocations.

---

### ⚠️ Edge Cases & Interview Traps
1. Length <= 2: unchanged.
2. Odd vs even length: handled cleanly by splitting at slow.next.

---

### 💬 Follow-Up Questions You Might Get
- *Can we solve this using a deque?* Yes, storing nodes in a deque takes O(N) space.
