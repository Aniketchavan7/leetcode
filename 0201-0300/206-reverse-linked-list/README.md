# 206. Reverse Linked List

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/reverse-linked-list/)
[![Topic: Linked List](https://img.shields.io/badge/Topic-Linked%20List-blue)](https://leetcode.com/problems/reverse-linked-list/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To reverse a singly linked list iteratively in O(1) space, we maintain three pointers: `prev` (initially null), `curr` (initially head), and `next`. In each iteration, save `next = curr.next`, point `curr.next = prev`, then shift `prev = curr` and `curr = next`. When curr is null, prev is the new head."

---

### 💡 Intuition & Core Insight
- **In-Place Reversal**: Each node simply reverses its arrow to point to its predecessor instead of its successor.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `1 -> 2 -> 3 -> null`
- Start: prev = null, curr = 1
- Step 1: next = 2; 1.next = null; prev = 1; curr = 2
- Step 2: next = 3; 2.next = 1; prev = 2; curr = 3
- Step 3: next = null; 3.next = 2; prev = 3; curr = null
Return prev (3 -> 2 -> 1 -> null).

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Single linear pass visiting each node once.
- **Space Complexity**: $\mathcal{O}(1)$ — O(1) extra space using constant pointers.

---

### ⚠️ Edge Cases & Interview Traps
1. Empty list: returns null.
2. Single node: loop runs once, returns head.

---

### 💬 Follow-Up Questions You Might Get
- *Can this be done recursively?* `head.next.next = head; head.next = null;` achieves it with O(N) call stack.
