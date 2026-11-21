# 819. Most Common Word

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/most-common-word)
[![Topic: Array & Hash Table & String](https://img.shields.io/badge/Topic-Array%20&%20Hash%20Table%20&%20String-blue)](https://leetcode.com/problems/most-common-word)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Array strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `paragraph = &quot;Bob hit a ball, the hit BALL flew far after it was hit.&quot;, banned = [&quot;hit&quot;]`  
**Expected Output**: `&quot;ball&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `paragraph = &quot;Bob hit a ball, the hit BALL flew far after it was hit.&quot;, banned = [&quot;hit&quot;]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;ball&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {
    private static Pattern pattern = Pattern.compile("[a-z]+");

    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> bannedWords = new HashSet<>();
        for (String word : banned) {
            bannedWords.add(word);
        }
        Map<String, Integer> counter = new HashMap<>();
        Matcher matcher = pattern.matcher(paragraph.toLowerCase());
        while (matcher.find()) {
            String word = matcher.group();
            if (bannedWords.contains(word)) {
                continue;
            }
            counter.put(word, counter.getOrDefault(word, 0) + 1);
        }
        int max = Integer.MIN_VALUE;
        String ans = null;
        for (Map.Entry<String, Integer> entry : counter.entrySet()) {
            if (entry.getValue() > max) {
                max = entry.getValue();
                ans = entry.getKey();
            }
        }
        return ans;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        s = set(banned)
        p = Counter(re.findall('[a-z]+', paragraph.lower()))
        return next(word for word, _ in p.most_common() if word not in s)
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
