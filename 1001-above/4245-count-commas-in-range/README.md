# 4245. Count Commas in Range

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/count-commas-in-range/)
[![Topic: Math / Digit Counting](https://img.shields.io/badge/Topic-Math%20/%20Digit%20Counting-blue)](https://leetcode.com/problems/count-commas-in-range/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "In standard number formatting, commas are placed every three digits from the right: numbers 1..999 have 0 commas, 1,000..999,999 have 1 comma, 1,000,000..999,999,999 have 2 commas, etc. To count commas in range [1, n], count numbers in [1000, n] (each has 1 comma), count numbers in [1000000, n] (each has an additional comma), etc."

---

### 💡 Intuition & Core Insight
- **Tiered Slicing**: Every power of 1,000 (10^3, 10^6, 10^9) adds exactly one additional comma to every integer above it.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `n = 1005`
- Numbers >= 1,000: 1005 - 1000 + 1 = 6 numbers with >= 1 comma
- Numbers >= 1,000,000: 0
Total commas = 6.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public long countCommas(long n) {
        long commas = 0;
        long threshold = 1000;
        while (n >= threshold) {
            commas += (n - threshold + 1);
            if (threshold > Long.MAX_VALUE / 1000) break;
            threshold *= 1000;
        }
        return commas;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def countCommas(self, n: int) -> int:
        commas = 0
        threshold = 1000
        while n >= threshold:
            commas += (n - threshold + 1)
            threshold *= 1000
        return commas
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log_{1000}(N))$ — Loop executes at most 5 times for 64-bit numbers.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary variables.

---

### ⚠️ Edge Cases & Interview Traps
1. n < 1000: loop executes 0 times, returns 0.
2. Exact power of 1000: threshold arithmetic correctly includes the boundary.

---

### 💬 Follow-Up Questions You Might Get
- *Count commas in arbitrary range [low, high]?* Return countCommas(high) - countCommas(low - 1).
