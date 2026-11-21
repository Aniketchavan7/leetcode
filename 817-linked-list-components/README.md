# 817. Linked List Components

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/linked-list-components)
[![Topic: Array & Hash Table & Linked List](https://img.shields.io/badge/Topic-Array%20&%20Hash%20Table%20&%20Linked%20List-blue)](https://leetcode.com/problems/linked-list-components)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "When manipulating linked lists in **Linked List Components**, pointer management and dummy head techniques allow in-place operations with O(1) auxiliary memory while avoiding boundary null-pointer checks."

---

### 💡 Intuition & Core Insight
- **Pointer Mechanics**: Using a dummy node simplifies edge cases where the head of the list changes.
- **Carry & Traversal**: Traversing node-by-node with carry propagation mirrors manual column addition.
- **In-place Re-wiring**: Reusing existing node pointers eliminates unnecessary heap allocations.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `head = [0,1,2,3], nums = [0,1,3]`  
**Expected Output**: `2`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `head = [0,1,2,3], nums = [0,1,3]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `2` |

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
    public int numComponents(ListNode head, int[] nums) {
        int ans = 0;
        Set<Integer> s = new HashSet<>();
        for (int v : nums) {
            s.add(v);
        }
        while (head != null) {
            while (head != null && !s.contains(head.val)) {
                head = head.next;
            }
            ans += head != null ? 1 : 0;
            while (head != null && s.contains(head.val)) {
                head = head.next;
            }
        }
        return ans;
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
    def numComponents(self, head: Optional[ListNode], nums: list[int]) -> int:
        ans = 0
        s = set(nums)
        while head:
            while head and head.val not in s:
                head = head.next
            ans += head is not None
            while head and head.val in s:
                head = head.next
        return ans
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
