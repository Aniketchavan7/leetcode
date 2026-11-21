# 468. Validate IP Address

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/validate-ip-address)
[![Topic: String](https://img.shields.io/badge/Topic-String-blue)](https://leetcode.com/problems/validate-ip-address)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal String strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `queryIP = &quot;172.16.254.1&quot;`  
**Expected Output**: `&quot;IPv4&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `queryIP = &quot;172.16.254.1&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;IPv4&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String validIPAddress(String queryIP) {
        if (isIPv4(queryIP)) {
            return "IPv4";
        }
        if (isIPv6(queryIP)) {
            return "IPv6";
        }
        return "Neither";
    }

    private boolean isIPv4(String s) {
        if (s.endsWith(".")) {
            return false;
        }
        String[] ss = s.split("\\.");
        if (ss.length != 4) {
            return false;
        }
        for (String t : ss) {
            if (t.length() == 0 || t.length() > 1 && t.charAt(0) == '0') {
                return false;
            }
            int x = convert(t);
            if (x < 0 || x > 255) {
                return false;
            }
        }
        return true;
    }

    private boolean isIPv6(String s) {
        if (s.endsWith(":")) {
            return false;
        }
        String[] ss = s.split(":");
        if (ss.length != 8) {
            return false;
        }
        for (String t : ss) {
            if (t.length() < 1 || t.length() > 4) {
                return false;
            }
            for (char c : t.toCharArray()) {
                if (!Character.isDigit(c)
                    && !"0123456789abcdefABCDEF".contains(String.valueOf(c))) {
                    return false;
                }
            }
        }
        return true;
    }

    private int convert(String s) {
        int x = 0;
        for (char c : s.toCharArray()) {
            if (!Character.isDigit(c)) {
                return -1;
            }
            x = x * 10 + (c - '0');
            if (x > 255) {
                return x;
            }
        }
        return x;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_ipv4(s: str) -> bool:
            ss = s.split(".")
            if len(ss) != 4:
                return False
            for t in ss:
                if len(t) > 1 and t[0] == "0":
                    return False
                if not t.isdigit() or not 0 <= int(t) <= 255:
                    return False
            return True

        def is_ipv6(s: str) -> bool:
            ss = s.split(":")
            if len(ss) != 8:
                return False
            for t in ss:
                if not 1 <= len(t) <= 4:
                    return False
                if not all(c in "0123456789abcdefABCDEF" for c in t):
                    return False
            return True

        if is_ipv4(queryIP):
            return "IPv4"
        if is_ipv6(queryIP):
            return "IPv6"
        return "Neither"
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
