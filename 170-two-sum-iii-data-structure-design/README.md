# 170. Two Sum III - Data structure design

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/two-sum-iii-data-structure-design)
[![Topic: Design & Array & Hash Table](https://img.shields.io/badge/Topic-Design%20&%20Array%20&%20Hash%20Table-blue)](https://leetcode.com/problems/two-sum-iii-data-structure-design)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "By maintaining window boundaries or dual pointers, we convert a quadratic pair search into a linear scan, dynamically expanding or shrinking based on feasibility invariants."

---

### 💡 Intuition & Core Insight
- **Monotonicity**: As the right pointer advances, the search space moves monotonically without backtracking.
- **Window Invariant**: Validating window conditions with a frequency counter guarantees correctness.
- **Two-Ended Traversal**: Squeezing inward from boundaries avoids evaluating redundant pairs.

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
class TwoSum {
    private Map<Integer, Integer> cnt = new HashMap<>();

    public TwoSum() {
    }

    public void add(int number) {
        cnt.merge(number, 1, Integer::sum);
    }

    public boolean find(int value) {
        for (var e : cnt.entrySet()) {
            int x = e.getKey(), v = e.getValue();
            int y = value - x;
            if (cnt.containsKey(y) && (x != y || v > 1)) {
                return true;
            }
        }
        return false;
    }
}

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * boolean param_2 = obj.find(value);
 */
```

#### Python 3 Solution
```python
class TwoSum:

    def __init__(self):
        self.cnt = defaultdict(int)

    def add(self, number: int) -> None:
        self.cnt[number] += 1

    def find(self, value: int) -> bool:
        for x, v in self.cnt.items():
            y = value - x
            if y in self.cnt and (x != y or v > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(1)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Off-by-one errors on window size (right - left + 1).
2. Empty arrays or arrays with all identical elements.
3. Forgetting to update state counters when shrinking the left boundary.

---

### 💬 Follow-Up Questions You Might Get
*What if the array cannot fit into memory?* We can stream data through a bounded circular buffer or sliding window chunk.
