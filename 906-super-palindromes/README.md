# 906. Super Palindromes

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/super-palindromes)
[![Topic: Math & String & Enumeration](https://img.shields.io/badge/Topic-Math%20&%20String%20&%20Enumeration-blue)](https://leetcode.com/problems/super-palindromes)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Math strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `left = &quot;4&quot;, right = &quot;1000&quot;`  
**Expected Output**: `4`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `left = &quot;4&quot;, right = &quot;1000&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `4` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private static long[] ps;

    static {
        ps = new long[2 * (int) 1e5];
        for (int i = 1; i <= 1e5; i++) {
            String s = Integer.toString(i);
            String t1 = new StringBuilder(s).reverse().toString();
            String t2 = new StringBuilder(s.substring(0, s.length() - 1)).reverse().toString();
            ps[2 * i - 2] = Long.parseLong(s + t1);
            ps[2 * i - 1] = Long.parseLong(s + t2);
        }
    }

    public int superpalindromesInRange(String left, String right) {
        long l = Long.parseLong(left);
        long r = Long.parseLong(right);
        int ans = 0;
        for (long p : ps) {
            long x = p * p;
            if (x >= l && x <= r && isPalindrome(x)) {
                ++ans;
            }
        }
        return ans;
    }

    private boolean isPalindrome(long x) {
        long y = 0;
        for (long t = x; t > 0; t /= 10) {
            y = y * 10 + t % 10;
        }
        return x == y;
    }
}
```

#### Python 3 Solution
```python
ps = []
for i in range(1, 10**5 + 1):
    s = str(i)
    t1 = s[::-1]
    t2 = s[:-1][::-1]
    ps.append(int(s + t1))
    ps.append(int(s + t2))


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(x: int) -> bool:
            y, t = 0, x
            while t:
                y = y * 10 + t % 10
                t //= 10
            return x == y

        l, r = int(left), int(right)
        return sum(l <= x <= r and is_palindrome(x) for x in map(lambda x: x * x, ps))
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Handling empty or single-element inputs.
2. Boundary index arithmetic and potential overflow.
3. Duplicate or negative values in input collections.

---

### 💬 Follow-Up Questions You Might Get
*How does this scale to distributed streams?* Hash partitioning across shards or MapReduce pipelines can process data in parallel.
