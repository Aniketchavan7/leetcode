# 295. Find Median from Data Stream

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/find-median-from-data-stream/)
[![Topic: Two Heaps](https://img.shields.io/badge/Topic-Two%20Heaps-blue)](https://leetcode.com/problems/find-median-from-data-stream/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To compute the median dynamically in O(1) from an incoming data stream, we divide all numbers into two equal halves: a Max-Heap `small` storing the smaller half, and a Min-Heap `large` storing the larger half. We maintain the invariant that small.size() == large.size() or small.size() == large.size() + 1. If sizes are equal, median is (small.peek() + large.peek()) / 2.0. If small has one extra element, median is small.peek()."

---

### 💡 Intuition & Core Insight
- **Pivoting on the Median**: The median element is always the maximum of the lower half or the minimum of the upper half.

---

### 🔍 Step-by-Step Visual Dry Run
- addNum(1): small=[1], large=[] -> median = 1.0
- addNum(2): small=[1], large=[2] -> median = (1+2)/2.0 = 1.5
- addNum(3): small=[2, 1], large=[3] -> median = 2.0.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class MedianFinder {
    private final PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder()); // Max-heap
    private final PriorityQueue<Integer> large = new PriorityQueue<>(); // Min-heap

    public MedianFinder() {}

    public void addNum(int num) {
        small.add(num);
        large.add(small.poll()); // Balance values

        // Maintain size invariant: small >= large
        if (small.size() < large.size()) {
            small.add(large.poll());
        }
    }

    public double findMedian() {
        if (small.size() > large.size()) {
            return small.peek();
        }
        return (small.peek() + large.peek()) / 2.0;
    }
}
```

#### Python 3 Solution
```python
class MedianFinder:
    def __init__(self):
        self.small = [] # Max-heap (stored as negative values)
        self.large = [] # Min-heap

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        heappush(self.large, -heappop(self.small))

        if len(self.small) < len(self.large):
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log N)$ — addNum takes O(log N) heap operations; findMedian is O(1).
- **Space Complexity**: $\mathcal{O}(N)$ — Stores all N numbers from the stream across the two heaps.

---

### ⚠️ Edge Cases & Interview Traps
1. Negative numbers: max-heap and min-heap compare correctly.
2. Even count vs odd count: size balancing handles parity automatically.

---

### 💬 Follow-Up Questions You Might Get
- *What if numbers are bounded between 0 and 100?* Use a 101-element bucket frequency array for O(1) add and O(1) median search.
