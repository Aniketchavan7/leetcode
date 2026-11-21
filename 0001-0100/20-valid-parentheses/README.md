# 20. Valid Parentheses

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/valid-parentheses/)
[![Topic: Stack](https://img.shields.io/badge/Topic-Stack-blue)](https://leetcode.com/problems/valid-parentheses/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We use a Stack to enforce Last-In-First-Out matching of brackets. When we encounter an opening bracket `(`, `{`, `[`, we push the corresponding closing bracket `)`, `}`, `]` onto the stack. When we encounter a closing bracket, it must match the top of the stack. If the stack is empty or doesn't match, the string is invalid. At the end, the stack must be empty."

---

### 💡 Intuition & Core Insight
- **Pushing Expected Closer**: Pushing the closing bracket instead of the opening bracket allows a simple `c != stack.pop()` equality check, avoiding bulky switch statements on pop.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `s = "()[]{}"`
- '(' -> push ')' -> stack: `[')']`
- ')' -> pop ')' == ')' -> valid! stack: `[]`
- '[' -> push ']' -> stack: `[']']`
- ']' -> pop ']' == ']' -> valid! stack: `[]`
- '{' -> push '}' -> stack: `['}']`
- '}' -> pop '}' == '}' -> valid! stack: `[]`
Stack is empty -> return True.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(') stack.push(')');
            else if (c == '{') stack.push('}');
            else if (c == '[') stack.push(']');
            else if (stack.isEmpty() || stack.pop() != c) return false;
        }
        return stack.isEmpty();
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in matching:
                if not stack or stack.pop() != matching[char]:
                    return False
            else:
                stack.append(char)
        return not stack
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Iterates through each character in the string once with O(1) stack operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Stack holds at most N opening brackets in worst case.

---

### ⚠️ Edge Cases & Interview Traps
1. Odd length string: cannot be balanced (can exit in O(1) if len % 2 != 0).
2. Closing bracket first ")(": stack is empty on first pop -> returns false.

---

### 💬 Follow-Up Questions You Might Get
- *What if wildcards '*' are present that can match open, close, or empty?* Use two counters or greedy balance range [minOpen, maxOpen] (LeetCode 678).
