# 347. Top K Frequent Elements

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/top-k-frequent-elements/)
[![Topic: Heap / Bucket Sort](https://img.shields.io/badge/Topic-Heap%20/%20Bucket%20Sort-blue)](https://leetcode.com/problems/top-k-frequent-elements/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To find the k most frequent elements in better than O(N log N): 1) Count element frequencies in a Hash Map. 2) Use Bucket Sort where the index of the bucket represents the frequency (at most N). 3) Iterate backwards from bucket N down to 1, collecting elements until we have collected k numbers. This achieves optimal O(N) linear time."

---

### 💡 Intuition & Core Insight
- **Frequency is Bounded by N**: No element can appear more than N times. Using frequency as array indices achieves O(N) non-comparative sorting.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `nums = [1, 1, 1, 2, 2, 3]`, `k = 2`
- Frequencies: `{1: 3, 2: 2, 3: 1}`
- Buckets: index 1: `[3]`, index 2: `[2]`, index 3: `[1]`
- Iterate backwards from index 3 down:
  - Bucket 3 has `[1]` -> collect 1
  - Bucket 2 has `[2]` -> collect 2
Collected 2 elements -> return `[1, 2]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : nums) countMap.put(num, countMap.getOrDefault(num, 0) + 1);

        List<Integer>[] buckets = new List[nums.length + 1];
        for (int key : countMap.keySet()) {
            int freq = countMap.get(key);
            if (buckets[freq] == null) buckets[freq] = new ArrayList<>();
            buckets[freq].add(key);
        }

        int[] res = new int[k];
        int idx = 0;
        for (int i = buckets.length - 1; i >= 0 && idx < k; i--) {
            if (buckets[i] != null) {
                for (int num : buckets[i]) {
                    res[idx++] = num;
                    if (idx == k) break;
                }
            }
        }
        return res;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Counting takes O(N), bucket distribution takes O(N), reverse bucket scan takes O(N).
- **Space Complexity**: $\mathcal{O}(N)$ — Hash map and bucket lists store at most N elements.

---

### ⚠️ Edge Cases & Interview Traps
1. k equals number of unique elements: returns all unique elements.
2. All elements identical: bucket[N] contains that element.

---

### 💬 Follow-Up Questions You Might Get
- *What if memory is constrained?* Use a Min-Heap of size k for O(N log k) time and O(k) extra space.
