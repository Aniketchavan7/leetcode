# 234. Palindrome Linked List

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/palindrome-linked-list)
[![Topic: Stack & Recursion & Linked List](https://img.shields.io/badge/Topic-Stack%20&%20Recursion%20&%20Linked%20List-blue)](https://leetcode.com/problems/palindrome-linked-list)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "When manipulating linked lists in **Palindrome Linked List**, pointer management and dummy head techniques allow in-place operations with O(1) auxiliary memory while avoiding boundary null-pointer checks."

---

### 💡 Intuition & Core Insight
- **Pointer Mechanics**: Using a dummy node simplifies edge cases where the head of the list changes.
- **Carry & Traversal**: Traversing node-by-node with carry propagation mirrors manual column addition.
- **In-place Re-wiring**: Reusing existing node pointers eliminates unnecessary heap allocations.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `head = [1,2,2,1]`  
**Expected Output**: `true`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `head = [1,2,2,1]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `true` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode cur = slow.next;
        slow.next = null;
        ListNode pre = null;
        while (cur != null) {
            ListNode t = cur.next;
            cur.next = pre;
            pre = cur;
            cur = t;
        }
        while (pre != null) {
            if (pre.val != head.val) {
                return false;
            }
            pre = pre.next;
            head = head.next;
        }
        return true;
    }
}
```

#### Python 3 Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        pre, cur = None, slow.next
        while cur:
            t = cur.next
            cur.next = pre
            pre, cur = cur, t
        while pre:
            if pre.val != head.val:
                return False
            pre, head = pre.next, head.next
        return True
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(1)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Null head or empty list edge cases.
2. Lists of unequal lengths.
3. Lingering carry value after exhausting both lists.

---

### 💬 Follow-Up Questions You Might Get
*What if the list contains cycles?* We can employ Floyd's Cycle-Finding algorithm (fast and slow pointers) to detect or break cycles.
