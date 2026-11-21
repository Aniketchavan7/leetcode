# 382. Linked List Random Node

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/linked-list-random-node)
[![Topic: Reservoir Sampling & Linked List & Math](https://img.shields.io/badge/Topic-Reservoir%20Sampling%20&%20Linked%20List%20&%20Math-blue)](https://leetcode.com/problems/linked-list-random-node)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "When manipulating linked lists in **Linked List Random Node**, pointer management and dummy head techniques allow in-place operations with O(1) auxiliary memory while avoiding boundary null-pointer checks."

---

### 💡 Intuition & Core Insight
- **Pointer Mechanics**: Using a dummy node simplifies edge cases where the head of the list changes.
- **Carry & Traversal**: Traversing node-by-node with carry propagation mirrors manual column addition.
- **In-place Re-wiring**: Reusing existing node pointers eliminates unnecessary heap allocations.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `Standard sample testcase`  
**Expected Output**: `Computed result`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `Input elements` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `Optimal Result` |

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
    private ListNode head;
    private Random random = new Random();

    public Solution(ListNode head) {
        this.head = head;
    }

    public int getRandom() {
        int ans = 0, n = 0;
        for (ListNode node = head; node != null; node = node.next) {
            ++n;
            int x = 1 + random.nextInt(n);
            if (n == x) {
                ans = node.val;
            }
        }
        return ans;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
```

#### Python 3 Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        n = ans = 0
        head = self.head
        while head:
            n += 1
            x = random.randint(1, n)
            if n == x:
                ans = head.val
            head = head.next
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
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
