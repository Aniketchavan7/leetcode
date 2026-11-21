# 160. Intersection of Two Linked Lists

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/intersection-of-two-linked-lists)
[![Topic: Hash Table & Linked List & Two Pointers](https://img.shields.io/badge/Topic-Hash%20Table%20&%20Linked%20List%20&%20Two%20Pointers-blue)](https://leetcode.com/problems/intersection-of-two-linked-lists)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "When manipulating linked lists in **Intersection of Two Linked Lists**, pointer management and dummy head techniques allow in-place operations with O(1) auxiliary memory while avoiding boundary null-pointer checks."

---

### 💡 Intuition & Core Insight
- **Pointer Mechanics**: Using a dummy node simplifies edge cases where the head of the list changes.
- **Carry & Traversal**: Traversing node-by-node with carry propagation mirrors manual column addition.
- **In-place Re-wiring**: Reusing existing node pointers eliminates unnecessary heap allocations.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3`  
**Expected Output**: `Intersected at &#39;8&#39;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `Intersected at &#39;8&#39;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA, b = headB;
        while (a != b) {
            a = a == null ? headB : a.next;
            b = b == null ? headA : b.next;
        }
        return a;
    }
}
```

#### Python 3 Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
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
