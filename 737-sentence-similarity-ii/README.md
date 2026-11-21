# 737. Sentence Similarity II

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/sentence-similarity-ii)
[![Topic: Depth-First Search & Breadth-First Search & Union Find](https://img.shields.io/badge/Topic-Depth-First%20Search%20&%20Breadth-First%20Search%20&%20Union%20Find-blue)](https://leetcode.com/problems/sentence-similarity-ii)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Depth-First Search strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `sentence1 = [&quot;great&quot;,&quot;acting&quot;,&quot;skills&quot;], sentence2 = [&quot;fine&quot;,&quot;drama&quot;,&quot;talent&quot;], similarPairs = [[&quot;great&quot;,&quot;good&quot;],[&quot;fine&quot;,&quot;good&quot;],[&quot;drama&quot;,&quot;acting&quot;],[&quot;skills&quot;,&quot;talent&quot;]]`  
**Expected Output**: `true`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `sentence1 = [&quot;great&quot;,&quot;acting&quot;,&quot;skills&quot;], sentence2 = [&quot;fine&quot;,&quot;drama&quot;,&quot;talent&quot;], similarPairs = [[&quot;great&quot;,&quot;good&quot;],[&quot;fine&quot;,&quot;good&quot;],[&quot;drama&quot;,&quot;acting&quot;],[&quot;skills&quot;,&quot;talent&quot;]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `true` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    private int[] p;

    public boolean areSentencesSimilarTwo(
        String[] sentence1, String[] sentence2, List<List<String>> similarPairs) {
        if (sentence1.length != sentence2.length) {
            return false;
        }
        int n = similarPairs.size();
        p = new int[n << 1];
        for (int i = 0; i < p.length; ++i) {
            p[i] = i;
        }
        Map<String, Integer> words = new HashMap<>();
        int idx = 0;
        for (List<String> e : similarPairs) {
            String a = e.get(0), b = e.get(1);
            if (!words.containsKey(a)) {
                words.put(a, idx++);
            }
            if (!words.containsKey(b)) {
                words.put(b, idx++);
            }
            p[find(words.get(a))] = find(words.get(b));
        }
        for (int i = 0; i < sentence1.length; ++i) {
            if (Objects.equals(sentence1[i], sentence2[i])) {
                continue;
            }
            if (!words.containsKey(sentence1[i]) || !words.containsKey(sentence2[i])
                || find(words.get(sentence1[i])) != find(words.get(sentence2[i]))) {
                return false;
            }
        }
        return true;
    }

    private int find(int x) {
        if (p[x] != x) {
            p[x] = find(p[x]);
        }
        return p[x];
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def areSentencesSimilarTwo(
        self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        n = len(similarPairs)
        p = list(range(n << 1))

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        words = {}
        idx = 0
        for a, b in similarPairs:
            if a not in words:
                words[a] = idx
                idx += 1
            if b not in words:
                words[b] = idx
                idx += 1
            p[find(words[a])] = find(words[b])

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            if (
                sentence1[i] not in words
                or sentence2[i] not in words
                or find(words[sentence1[i]]) != find(words[sentence2[i]])
            ):
                return False
        return True
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
