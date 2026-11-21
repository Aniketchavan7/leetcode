# 3799. Unique 3-Digit Even Numbers

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/unique-3-digit-even-numbers/)
[![Topic: Hash Set / Combinatorics](https://img.shields.io/badge/Topic-Hash%20Set%20/%20Combinatorics-blue)](https://leetcode.com/problems/unique-3-digit-even-numbers/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To find all unique 3-digit even numbers that can be formed using digits from the array: The search space of 3-digit even numbers is tiny—strictly between 100 and 998 with step 2 (at most 450 numbers!). Instead of generating all permutations of the input array, we invert the check: iterate through every even integer from 100 to 998, count its three digits, and check if our input digit frequency array contains enough of each digit."

---

### 💡 Intuition & Core Insight
- **Looping Over Solution Space vs Input Combinations**: Iterating over 450 candidate numbers is O(1) constant time, eliminating sorting, duplicate permutation generation, and recursion.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `digits = [2, 1, 3, 0]`
- Count map: `{0:1, 1:1, 2:1, 3:1}`
- Check 102: digits 1, 0, 2 are in map -> valid!
- Check 120: digits 1, 2, 0 are in map -> valid!
- Check 130, 132, 210, 230, 310, 312, 320 -> collected in sorted order.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] findEvenNumbers(int[] digits) {
        int[] freq = new int[10];
        for (int d : digits) freq[d]++;

        List<Integer> list = new ArrayList<>();
        for (int num = 100; num <= 998; num += 2) {
            int d1 = num / 100;
            int d2 = (num / 10) % 10;
            int d3 = num % 10;

            int[] needed = new int[10];
            needed[d1]++;
            needed[d2]++;
            needed[d3]++;

            boolean valid = true;
            for (int i = 0; i < 10; i++) {
                if (needed[i] > freq[i]) {
                    valid = false;
                    break;
                }
            }
            if (valid) list.add(num);
        }

        int[] res = new int[list.size()];
        for (int i = 0; i < list.size(); i++) res[i] = list.get(i);
        return res;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        counts = Counter(digits)
        res = []
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            needed = Counter([d1, d2, d3])
            if all(counts[d] >= needed[d] for d in needed):
                res.append(num)
        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N + 450)$ — O(N) to count digits, followed by checking exactly 450 candidate numbers.
- **Space Complexity**: $\mathcal{O}(1)$ — Fixed 10-element digit frequency array.

---

### ⚠️ Edge Cases & Interview Traps
1. Cannot have leading zeroes: range starts at 100.
2. Must be even: loop step is 2.

---

### 💬 Follow-Up Questions You Might Get
- *What if K-digit numbers are requested?* For large K, backtrack through the digit frequency counts.
