# 281. Zigzag Iterator

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/zigzag-iterator)
[![Topic: Design & Queue & Array](https://img.shields.io/badge/Topic-Design%20&%20Queue%20&%20Array-blue)](https://leetcode.com/problems/zigzag-iterator)

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
**Sample Input**: `v1 = [1,2], v2 = [3,4,5,6]`  
**Expected Output**: `[1,3,2,4,5,6]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `v1 = [1,2], v2 = [3,4,5,6]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[1,3,2,4,5,6]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
public class ZigzagIterator {
    private int cur;
    private int size;
    private List<Integer> indexes = new ArrayList<>();
    private List<List<Integer>> vectors = new ArrayList<>();

    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        cur = 0;
        size = 2;
        indexes.add(0);
        indexes.add(0);
        vectors.add(v1);
        vectors.add(v2);
    }

    public int next() {
        List<Integer> vector = vectors.get(cur);
        int index = indexes.get(cur);
        int res = vector.get(index);
        indexes.set(cur, index + 1);
        cur = (cur + 1) % size;
        return res;
    }

    public boolean hasNext() {
        int start = cur;
        while (indexes.get(cur) == vectors.get(cur).size()) {
            cur = (cur + 1) % size;
            if (start == cur) {
                return false;
            }
        }
        return true;
    }
}

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i = new ZigzagIterator(v1, v2);
 * while (i.hasNext()) v[f()] = i.next();
 */
```

#### Python 3 Solution
```python
class ZigzagIterator:
    def __init__(self, v1: list[int], v2: list[int]):
        self.cur = 0
        self.size = 2
        self.indexes = [0] * self.size
        self.vectors = [v1, v2]

    def next(self) -> int:
        vector = self.vectors[self.cur]
        index = self.indexes[self.cur]
        res = vector[index]
        self.indexes[self.cur] = index + 1
        self.cur = (self.cur + 1) % self.size
        return res

    def hasNext(self) -> bool:
        start = self.cur
        while self.indexes[self.cur] == len(self.vectors[self.cur]):
            self.cur = (self.cur + 1) % self.size
            if self.cur == start:
                return False
        return True


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
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
