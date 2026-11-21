# 420. Strong Password Checker

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/strong-password-checker)
[![Topic: Greedy & String & Heap (Priority Queue)](https://img.shields.io/badge/Topic-Greedy%20&%20String%20&%20Heap%20(Priority%20Queue)-blue)](https://leetcode.com/problems/strong-password-checker)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "By maintaining a min-heap or max-heap of size K, we process dynamic streams or Top-K queries in O(N log K) time without sorting the entire collection."

---

### 💡 Intuition & Core Insight
- **Bounded Memory**: Restricting heap size to K keeps space bounded and insertion at O(log K).
- **Extremum Access**: The root always exposes the current threshold in O(1) time.
- **Streaming Feasibility**: New incoming data is evaluated against the root in constant time before heapifying.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `password = "a"`  
**Expected Output**: `5`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `password = "a"` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `5` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int strongPasswordChecker(String password) {
        int types = countTypes(password);
        int n = password.length();
        if (n < 6) {
            return Math.max(6 - n, 3 - types);
        }
        char[] chars = password.toCharArray();
        if (n <= 20) {
            int replace = 0;
            int cnt = 0;
            char prev = '~';
            for (char curr : chars) {
                if (curr == prev) {
                    ++cnt;
                } else {
                    replace += cnt / 3;
                    cnt = 1;
                    prev = curr;
                }
            }
            replace += cnt / 3;
            return Math.max(replace, 3 - types);
        }
        int replace = 0, remove = n - 20;
        int remove2 = 0;
        int cnt = 0;
        char prev = '~';
        for (char curr : chars) {
            if (curr == prev) {
                ++cnt;
            } else {
                if (remove > 0 && cnt >= 3) {
                    if (cnt % 3 == 0) {
                        --remove;
                        --replace;
                    } else if (cnt % 3 == 1) {
                        ++remove2;
                    }
                }
                replace += cnt / 3;
                cnt = 1;
                prev = curr;
            }
        }
        if (remove > 0 && cnt >= 3) {
            if (cnt % 3 == 0) {
                --remove;
                --replace;
            } else if (cnt % 3 == 1) {
                ++remove2;
            }
        }
        replace += cnt / 3;

        int use2 = Math.min(Math.min(replace, remove2), remove / 2);
        replace -= use2;
        remove -= use2 * 2;

        int use3 = Math.min(replace, remove / 3);
        replace -= use3;
        remove -= use3 * 3;
        return (n - 20) + Math.max(replace, 3 - types);
    }

    private int countTypes(String s) {
        int a = 0, b = 0, c = 0;
        for (char ch : s.toCharArray()) {
            if (Character.isLowerCase(ch)) {
                a = 1;
            } else if (Character.isUpperCase(ch)) {
                b = 1;
            } else if (Character.isDigit(ch)) {
                c = 1;
            }
        }
        return a + b + c;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        def countTypes(s):
            a = b = c = 0
            for ch in s:
                if ch.islower():
                    a = 1
                elif ch.isupper():
                    b = 1
                elif ch.isdigit():
                    c = 1
            return a + b + c

        types = countTypes(password)
        n = len(password)
        if n < 6:
            return max(6 - n, 3 - types)
        if n <= 20:
            replace = cnt = 0
            prev = '~'
            for curr in password:
                if curr == prev:
                    cnt += 1
                else:
                    replace += cnt // 3
                    cnt = 1
                    prev = curr
            replace += cnt // 3
            return max(replace, 3 - types)
        replace = cnt = 0
        remove, remove2 = n - 20, 0
        prev = '~'
        for curr in password:
            if curr == prev:
                cnt += 1
            else:
                if remove > 0 and cnt >= 3:
                    if cnt % 3 == 0:
                        remove -= 1
                        replace -= 1
                    elif cnt % 3 == 1:
                        remove2 += 1
                replace += cnt // 3
                cnt = 1
                prev = curr
        if remove > 0 and cnt >= 3:
            if cnt % 3 == 0:
                remove -= 1
                replace -= 1
            elif cnt % 3 == 1:
                remove2 += 1
        replace += cnt // 3
        use2 = min(replace, remove2, remove // 2)
        replace -= use2
        remove -= use2 * 2

        use3 = min(replace, remove // 3)
        replace -= use3
        remove -= use3 * 3
        return n - 20 + max(replace, 3 - types)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log K)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(K)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Inverting comparator logic (min-heap vs max-heap).
2. Handling duplicate frequency or tie-breaking order.
3. Empty heap exceptions.

---

### 💬 Follow-Up Questions You Might Get
*Can we do Top-K in O(N) average time?* Quickselect achieves O(N) average time complexity.
