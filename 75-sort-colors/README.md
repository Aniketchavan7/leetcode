# 75. Sort Colors

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/sort-colors/)
[![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-blue)](https://leetcode.com/problems/sort-colors/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We need to sort an array containing 0s (red), 1s (white), and 2s (blue) in-place in a single pass. This is Dijkstra's 3-way Dutch National Flag partition algorithm. We maintain three pointers: low (boundary for 0s), mid (current element), and high (boundary for 2s). When nums[mid] == 0, swap with low; when nums[mid] == 2, swap with high; when 1, simply advance mid."

---

### 💡 Intuition & Core Insight
- **Partition Invariants**:
  - `[0, low - 1]` contains 0s
  - `[low, mid - 1]` contains 1s
  - `[mid, high]` is unexamined
  - `[high + 1, n - 1]` contains 2s
- **No mid++ on High Swap**: Swapping with `high` brings an unexamined element to `mid`, so `mid` must NOT advance until checked.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [2, 0, 2, 1, 1, 0]`
- low=0, mid=0, high=5: nums[0]=2 -> swap(mid, high), high=4 -> `[0, 0, 2, 1, 1, 2]`
- low=0, mid=0, high=4: nums[0]=0 -> swap(mid, low), low=1, mid=1 -> `[0, 0, 2, 1, 1, 2]`
- low=1, mid=1, high=4: nums[1]=0 -> swap(mid, low), low=2, mid=2 -> `[0, 0, 2, 1, 1, 2]`
- low=2, mid=2, high=4: nums[2]=2 -> swap(mid, high), high=3 -> `[0, 0, 1, 1, 2, 2]`
- mid=2, 3: nums[mid]=1 -> mid++ -> terminates when mid > high.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums, low++, mid++);
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                swap(nums, mid, high--);
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — One single pass; every step either increments mid or decrements high.
- **Space Complexity**: $\mathcal{O}(1)$ — In-place swaps with three pointer variables.

---

### ⚠️ Edge Cases & Interview Traps
1. Already sorted array [0, 1, 2]: mid traverses without swaps.
2. All 2s or all 0s: correctly partitioned without out-of-bounds error.

---

### 💬 Follow-Up Questions You Might Get
- *What if there are K colors?* Counting sort in O(N + K) time, or quicksort 3-way partition.
