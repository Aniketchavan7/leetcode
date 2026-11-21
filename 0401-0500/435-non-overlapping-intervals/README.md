# 435. Non-overlapping Intervals

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/non-overlapping-intervals/)
[![Topic: Intervals / Greedy](https://img.shields.io/badge/Topic-Intervals%20/%20Greedy-blue)](https://leetcode.com/problems/non-overlapping-intervals/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Minimizing removals to leave non-overlapping intervals is equivalent to maximizing the number of compatible intervals (classic Interval Scheduling). We sort intervals by end time. Always picking the interval that finishes earliest leaves the maximum possible room for remaining intervals. Any interval whose start time is earlier than the current end time must be removed."

---

### 💡 Intuition & Core Insight
- **Greedy Earliest Deadline**: If interval A finishes before interval B, picking A can never hurt us more than picking B, because A frees up space sooner.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `[[1,2],[2,3],[3,4],[1,3]]`
- Sort by end time: `[[1,2], [2,3], [1,3], [3,4]]`
- Pick `[1,2]`: prevEnd = 2, removed = 0
- Check `[2,3]`: 2 >= 2 -> compatible! prevEnd = 3
- Check `[1,3]`: 1 < 3 -> overlaps! removed = 1
- Check `[3,4]`: 3 >= 3 -> compatible! prevEnd = 4
Total removed: 1.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));

        int count = 0;
        int prevEnd = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < prevEnd) {
                count++; // Overlap detected: remove this interval
            } else {
                prevEnd = intervals[i][1];
            }
        }
        return count;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        prev_end = float('-inf')

        for start, end in intervals:
            if start < prev_end:
                count += 1
            else:
                prev_end = end
        return count
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log N)$ — Sorting N intervals by end time takes O(N log N); greedy scan takes O(N).
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary memory ignoring sorting stack.

---

### ⚠️ Edge Cases & Interview Traps
1. Touching intervals [1,2] and [2,3]: non-overlapping by definition.
2. All overlapping: removes N - 1.

---

### 💬 Follow-Up Questions You Might Get
- *Why sort by end time instead of start time?* Sorting by start time fails on wide intervals like [1, 100] followed by [2, 3].
