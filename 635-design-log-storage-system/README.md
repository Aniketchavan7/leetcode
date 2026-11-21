# 635. Design Log Storage System

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/design-log-storage-system)
[![Topic: Design & Hash Table & String](https://img.shields.io/badge/Topic-Design%20&%20Hash%20Table%20&%20String-blue)](https://leetcode.com/problems/design-log-storage-system)

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
class LogSystem {
    private List<Log> logs = new ArrayList<>();
    private Map<String, Integer> d = new HashMap<>();

    public LogSystem() {
        d.put("Year", 4);
        d.put("Month", 7);
        d.put("Day", 10);
        d.put("Hour", 13);
        d.put("Minute", 16);
        d.put("Second", 19);
    }

    public void put(int id, String timestamp) {
        logs.add(new Log(id, timestamp));
    }

    public List<Integer> retrieve(String start, String end, String granularity) {
        List<Integer> ans = new ArrayList<>();
        int i = d.get(granularity);
        String s = start.substring(0, i);
        String e = end.substring(0, i);
        for (var log : logs) {
            String t = log.ts.substring(0, i);
            if (s.compareTo(t) <= 0 && t.compareTo(e) <= 0) {
                ans.add(log.id);
            }
        }
        return ans;
    }
}

class Log {
    int id;
    String ts;

    Log(int id, String ts) {
        this.id = id;
        this.ts = ts;
    }
}

/**
 * Your LogSystem object will be instantiated and called as such:
 * LogSystem obj = new LogSystem();
 * obj.put(id,timestamp);
 * List<Integer> param_2 = obj.retrieve(start,end,granularity);
 */
```

#### Python 3 Solution
```python
class LogSystem:
    def __init__(self):
        self.logs = []
        self.d = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19,
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> list[int]:
        i = self.d[granularity]
        return [id for id, ts in self.logs if start[:i] <= ts[:i] <= end[:i]]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
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
