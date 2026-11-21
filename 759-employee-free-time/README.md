# 759. Employee Free Time

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/employee-free-time)
[![Topic: Array & Sorting & Sweep Line](https://img.shields.io/badge/Topic-Array%20&%20Sorting%20&%20Sweep%20Line-blue)](https://leetcode.com/problems/employee-free-time)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "By maintaining a min-heap or max-heap of size K, we process dynamic streams or Top-K queries in O(N log K) time without sorting the entire collection."

---

### 💡 Intuition & Core Insight
- **Bounded Memory**: Restricting heap size to K keeps space bounded and insertion at O(log K).
- **Extremum Access**: The root always exposes the current threshold in O(1) time.
- **Streaming Feasibility**: New incoming data is evaluated against the root in constant time before heapifying.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]`  
**Expected Output**: `[[3,4]]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[[3,4]]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
/*
// Definition for an Interval.
class Interval {
    public int start;
    public int end;

    public Interval() {}

    public Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};
*/

class Solution {
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        List<Interval> intervals = new ArrayList<>();
        for (List<Interval> e : schedule) {
            intervals.addAll(e);
        }

        intervals.sort((a, b) -> a.start == b.start ? a.end - b.end : a.start - b.start);

        List<Interval> merged = new ArrayList<>();
        merged.add(intervals.get(0));
        for (int i = 1; i < intervals.size(); ++i) {
            Interval last = merged.get(merged.size() - 1);
            Interval cur = intervals.get(i);
            if (last.end < cur.start) {
                merged.add(cur);
            } else {
                last.end = Math.max(last.end, cur.end);
            }
        }

        List<Interval> ans = new ArrayList<>();
        for (int i = 1; i < merged.size(); ++i) {
            Interval a = merged.get(i - 1);
            Interval b = merged.get(i);
            ans.add(new Interval(a.end, b.start));
        }

        return ans;
    }
}
```

#### Python 3 Solution
```python
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        intervals = []
        for e in schedule:
            intervals.extend(e)
        intervals.sort(key=lambda x: (x.start, x.end))
        merged = [intervals[0]]
        for x in intervals[1:]:
            if merged[-1].end < x.start:
                merged.append(x)
            else:
                merged[-1].end = max(merged[-1].end, x.end)
        ans = []
        for a, b in pairwise(merged):
            ans.append(Interval(a.end, b.start))
        return ans
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log K)$ — Optimal traversal through the input space without redundant operations.
- **Space Complexity**: $\mathcal{O}(K)$ — Space required for state tracking or call stack allocation.

---

### ⚠️ Edge Cases & Interview Traps
1. Inverting comparator logic (min-heap vs max-heap).
2. Handling duplicate frequency or tie-breaking order.
3. Empty heap exceptions.

---

### 💬 Follow-Up Questions You Might Get
*Can we do Top-K in O(N) average time?* Quickselect achieves O(N) average time complexity.
