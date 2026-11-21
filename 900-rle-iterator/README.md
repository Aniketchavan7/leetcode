# 900. RLE Iterator

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/rle-iterator)
[![Topic: Design & Array & Counting](https://img.shields.io/badge/Topic-Design%20&%20Array%20&%20Counting-blue)](https://leetcode.com/problems/rle-iterator)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Design strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

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
class RLEIterator {
    private int[] encoding;
    private int i;
    private int j;

    public RLEIterator(int[] encoding) {
        this.encoding = encoding;
    }

    public int next(int n) {
        while (i < encoding.length) {
            if (encoding[i] - j < n) {
                n -= (encoding[i] - j);
                i += 2;
                j = 0;
            } else {
                j += n;
                return encoding[i + 1];
            }
        }
        return -1;
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator obj = new RLEIterator(encoding);
 * int param_1 = obj.next(n);
 */
```

#### Python 3 Solution
```python
class RLEIterator:
    def __init__(self, encoding: list[int]):
        self.encoding = encoding
        self.i = 0
        self.j = 0

    def next(self, n: int) -> int:
        while self.i < len(self.encoding):
            if self.encoding[self.i] - self.j < n:
                n -= self.encoding[self.i] - self.j
                self.i += 2
                self.j = 0
            else:
                self.j += n
                return self.encoding[self.i + 1]
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
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
