# 56. Merge Intervals

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/merge-intervals/)
[![Topic: Intervals](https://img.shields.io/badge/Topic-Intervals-blue)](https://leetcode.com/problems/merge-intervals/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Given an array of intervals, we sort them by start time. We initialize a merged list with the first interval. For each subsequent interval: if its start time <= the end time of the last merged interval, they overlap, so we merge by updating the last interval's end to max(last.end, current.end). Otherwise, they don't overlap, so we append the current interval."

---

### 💡 Intuition & Core Insight
- **Sorting Enforces Ordering**: Sorting by start time guarantees that if interval B can overlap with interval A, it must appear after A, turning the problem into a linear scan comparing adjacent intervals.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `[[1,3],[2,6],[8,10],[15,18]]`
- Sorted: `[[1,3],[2,6],[8,10],[15,18]]`
- Merged: `[[1,3]]`
- `[2,6]`: 2 <= 3 -> Overlap! Merge: end = max(3, 6) = 6 -> Merged: `[[1,6]]`
- `[8,10]`: 8 > 6 -> No overlap! Append -> Merged: `[[1,6],[8,10]]`
- `[15,18]`: 15 > 10 -> No overlap! Append -> Merged: `[[1,6],[8,10],[15,18]]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) return intervals;
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> merged = new ArrayList<>();
        int[] current = intervals[0];
        merged.add(current);

        for (int[] interval : intervals) {
            if (interval[0] <= current[1]) {
                current[1] = Math.max(current[1], interval[1]);
            } else {
                current = interval;
                merged.add(current);
            }
        }
        return merged.toArray(new int[merged.size()][]);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log N)$ — Sorting N intervals takes O(N log N); linear merge pass takes O(N).
- **Space Complexity**: $\mathcal{O}(N)$ — Space required for sorting and output list.

---

### ⚠️ Edge Cases & Interview Traps
1. Single interval [[1, 4]]: returns [[1, 4]].
2. Fully contained interval [[1, 5], [2, 3]]: correctly absorbed into [1, 5].

---

### 💬 Follow-Up Questions You Might Get
- *What if the intervals are an unbounded stream?* Use an Interval Tree or Segment Tree to merge dynamically.
