# 824. Goat Latin

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/goat-latin)
[![Topic: String](https://img.shields.io/badge/Topic-String-blue)](https://leetcode.com/problems/goat-latin)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal String strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `sentence = "I speak Goat Latin"`  
**Expected Output**: `"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `sentence = "I speak Goat Latin"` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public String toGoatLatin(String sentence) {
        List<String> ans = new ArrayList<>();
        Set<Character> vowels
            = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        int i = 1;
        for (String word : sentence.split(" ")) {
            StringBuilder t = new StringBuilder();
            if (!vowels.contains(word.charAt(0))) {
                t.append(word.substring(1));
                t.append(word.charAt(0));
            } else {
                t.append(word);
            }
            t.append("ma");
            for (int j = 0; j < i; ++j) {
                t.append("a");
            }
            ++i;
            ans.add(t.toString());
        }
        return String.join(" ", ans);
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = []
        for i, word in enumerate(sentence.split()):
            if word.lower()[0] not in ['a', 'e', 'i', 'o', 'u']:
                word = word[1:] + word[0]
            word += 'ma'
            word += 'a' * (i + 1)
            ans.append(word)
        return ' '.join(ans)
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
