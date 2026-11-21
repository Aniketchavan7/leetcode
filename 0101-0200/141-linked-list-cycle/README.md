# 141. Linked List Cycle

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/linked-list-cycle/)
[![Topic: Linked List / Fast & Slow Pointers](https://img.shields.io/badge/Topic-Linked%20List%20/%20Fast%20%26%20Slow%20Pointers-blue)](https://leetcode.com/problems/linked-list-cycle/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We use Floyd's Tortoise and Hare cycle detection algorithm. We advance a `slow` pointer one step at a time and a `fast` pointer two steps at a time. If the list contains a cycle, the fast pointer will eventually lap the slow pointer and they will collide. If the fast pointer reaches null, there is no cycle."

---

### 💡 Intuition & Core Insight
- **Relative Speed**: Inside a cycle, with each step fast gains 1 node on slow. If they are separated by distance D, after D steps the gap closes to 0. They must meet.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `3 -> 2 -> 0 -> -4 -> (loops back to 2)`
- Step 1: slow=2, fast=0
- Step 2: slow=0, fast=2
- Step 3: slow=-4, fast=-4 (slow == fast!)
Cycle detected -> return True.

---

### 💻 Optimal Implementations

#### Java Solution
```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Non-cyclic path takes O(N); cyclic catching up takes at most the cycle length C <= N.
- **Space Complexity**: $\mathcal{O}(1)$ — Two pointer references without hash sets.

---

### ⚠️ Edge Cases & Interview Traps
1. head is null or single node without cycle: returns false immediately.
2. Cycle of length 1 (points to itself): detected on step 1.

---

### 💬 Follow-Up Questions You Might Get
- *How to find the node where the cycle begins?* Reset slow to head; move both 1 step at a time; their meeting point is the cycle start (LeetCode 142).
