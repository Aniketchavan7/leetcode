# 981. Time Based Key-Value Store

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/time-based-key-value-store)
[![Topic: Design & Hash Table & String](https://img.shields.io/badge/Topic-Design%20&%20Hash%20Table%20&%20String-blue)](https://leetcode.com/problems/time-based-key-value-store)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Given a monotonic condition or sorted space, we eliminate half the search candidates at each iteration, achieving optimal logarithmic time."

---

### 💡 Intuition & Core Insight
- **Search Space Invariant**: The target value or optimal boundary always lies within [left, right].
- **Mid Calculation**: Using left + (right - left) // 2 prevents 32-bit integer overflow.
- **Termination**: Strict comparison bounds avoid infinite loops on 2-element ranges.

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
class TimeMap {
    private Map<String, TreeMap<Integer, String>> ktv = new HashMap<>();

    public TimeMap() {
    }

    public void set(String key, String value, int timestamp) {
        ktv.computeIfAbsent(key, k -> new TreeMap<>()).put(timestamp, value);
    }

    public String get(String key, int timestamp) {
        if (!ktv.containsKey(key)) {
            return "";
        }
        var tv = ktv.get(key);
        Integer t = tv.floorKey(timestamp);
        return t == null ? "" : tv.get(t);
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
```

#### Python 3 Solution
```python
class TimeMap:
    def __init__(self):
        self.ktv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ktv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ktv:
            return ''
        tv = self.ktv[key]
        i = bisect_right(tv, (timestamp, chr(127)))
        return tv[i - 1][1] if i else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log N)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(1)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Integer overflow in (left + right) / 2 in Java/C++.
2. Choosing between left < right vs left <= right.
3. Updating left = mid vs left = mid + 1 depending on target inclusion.

---

### 💬 Follow-Up Questions You Might Get
*Can binary search be applied to unsorted inputs?* Yes, if the answer space possesses a monotonic predicate (Binary Search on Answer).
