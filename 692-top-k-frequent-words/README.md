# 692. Top K Frequent Words

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/top-k-frequent-words)
[![Topic: Trie & Array & Hash Table](https://img.shields.io/badge/Topic-Trie%20&%20Array%20&%20Hash%20Table-blue)](https://leetcode.com/problems/top-k-frequent-words)

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
**Sample Input**: `words = [&quot;i&quot;,&quot;love&quot;,&quot;leetcode&quot;,&quot;i&quot;,&quot;love&quot;,&quot;coding&quot;], k = 2`  
**Expected Output**: `[&quot;i&quot;,&quot;love&quot;]`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `words = [&quot;i&quot;,&quot;love&quot;,&quot;leetcode&quot;,&quot;i&quot;,&quot;love&quot;,&quot;coding&quot;], k = 2` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `[&quot;i&quot;,&quot;love&quot;]` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> cnt = new HashMap<>();
        for (String w : words) {
            cnt.merge(w, 1, Integer::sum);
        }
        Arrays.sort(words, (a, b) -> {
            int c1 = cnt.get(a), c2 = cnt.get(b);
            return c1 == c2 ? a.compareTo(b) : c2 - c1;
        });
        List<String> ans = new ArrayList<>();
        for (int i = 0; i < words.length && ans.size() < k; ++i) {
            if (i == 0 || !words[i].equals(words[i - 1])) {
                ans.add(words[i]);
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        cnt = Counter(words)
        return sorted(cnt, key=lambda x: (-cnt[x], x))[:k]
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
