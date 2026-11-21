# 914. X of a Kind in a Deck of Cards

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards)
[![Topic: Array & Hash Table & Math](https://img.shields.io/badge/Topic-Array%20&%20Hash%20Table%20&%20Math-blue)](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Array strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `deck = [1,2,3,4,4,3,2,1]`  
**Expected Output**: `true`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `deck = [1,2,3,4,4,3,2,1]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `true` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int x : deck) {
            cnt.merge(x, 1, Integer::sum);
        }
        int g = cnt.get(deck[0]);
        for (int x : cnt.values()) {
            g = gcd(g, x);
        }
        return g >= 2;
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        cnt = Counter(deck)
        return reduce(gcd, cnt.values()) >= 2
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
