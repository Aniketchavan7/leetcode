# 57. Insert Interval

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/insert-interval/)
[![Topic: Intervals](https://img.shields.io/badge/Topic-Intervals-blue)](https://leetcode.com/problems/insert-interval/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "The input intervals are already sorted and non-overlapping. We can solve this in a single O(N) pass divided into three phases: 1) Add all intervals that end before newInterval begins. 2) Merge all intervals that overlap with newInterval (start <= newInterval.end) by updating newInterval's bounds. 3) Add the merged newInterval, then append all remaining intervals that start after newInterval ends."

---

### 💡 Intuition & Core Insight
- **Pre-Sorted Advantage**: No need to resort! We can partition the intervals into strictly before, overlapping, and strictly after.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `intervals = [[1,3],[6,9]]`, `newInterval = [2,5]`
- Phase 1 (before 2): none.
- Phase 2 (overlapping with [2, 5]):
  - [1, 3]: start=min(2, 1)=1, end=max(5, 3)=5 -> newInterval=[1, 5]
- Phase 3 (append remaining):
  - Add [1, 5]
  - [6, 9] starts after 5 -> append [6, 9]
Result: `[[1,5],[6,9]]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        int i = 0, n = intervals.length;

        // Phase 1: All intervals before newInterval
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.add(intervals[i++]);
        }

        // Phase 2: Merge overlapping intervals
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.add(newInterval);

        // Phase 3: All intervals after newInterval
        while (i < n) {
            result.add(intervals[i++]);
        }

        return result.toArray(new int[result.size()][]);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Single linear pass through the N intervals.
- **Space Complexity**: $\mathcal{O}(N)$ — Output list storing merged intervals.

---

### ⚠️ Edge Cases & Interview Traps
1. Empty intervals list []: returns [newInterval].
2. newInterval goes at the very beginning or end: cleanly captured by phases 1 or 3.

---

### 💬 Follow-Up Questions You Might Get
- *Can we use Binary Search?* Binary search can find insertion points in O(log N), but shifting elements in an array still takes O(N).
