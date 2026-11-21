# 288. Unique Word Abbreviation

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/unique-word-abbreviation)
[![Topic: Design & Array & Hash Table](https://img.shields.io/badge/Topic-Design%20&%20Array%20&%20Hash%20Table-blue)](https://leetcode.com/problems/unique-word-abbreviation)

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
class ValidWordAbbr {
    private Map<String, Set<String>> d = new HashMap<>();

    public ValidWordAbbr(String[] dictionary) {
        for (var s : dictionary) {
            d.computeIfAbsent(abbr(s), k -> new HashSet<>()).add(s);
        }
    }

    public boolean isUnique(String word) {
        var ws = d.get(abbr(word));
        return ws == null || (ws.size() == 1 && ws.contains(word));
    }

    private String abbr(String s) {
        int n = s.length();
        return n < 3 ? s : s.substring(0, 1) + (n - 2) + s.substring(n - 1);
    }
}

/**
 * Your ValidWordAbbr object will be instantiated and called as such:
 * ValidWordAbbr obj = new ValidWordAbbr(dictionary);
 * boolean param_1 = obj.isUnique(word);
 */
```

#### Python 3 Solution
```python
class ValidWordAbbr:
    def __init__(self, dictionary: list[str]):
        self.d = defaultdict(set)
        for s in dictionary:
            self.d[self.abbr(s)].add(s)

    def isUnique(self, word: str) -> bool:
        s = self.abbr(word)
        return s not in self.d or all(word == t for t in self.d[s])

    def abbr(self, s: str) -> str:
        return s if len(s) < 3 else s[0] + str(len(s) - 2) + s[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
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
