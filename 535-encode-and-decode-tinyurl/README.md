# 535. Encode and Decode TinyURL

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/encode-and-decode-tinyurl)
[![Topic: Design & Hash Table & String](https://img.shields.io/badge/Topic-Design%20&%20Hash%20Table%20&%20String-blue)](https://leetcode.com/problems/encode-and-decode-tinyurl)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Design strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `url = &quot;https://leetcode.com/problems/design-tinyurl&quot;`  
**Expected Output**: `&quot;https://leetcode.com/problems/design-tinyurl&quot;`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `url = &quot;https://leetcode.com/problems/design-tinyurl&quot;` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `&quot;https://leetcode.com/problems/design-tinyurl&quot;` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
public class Codec {
    private Map<String, String> m = new HashMap<>();
    private int idx = 0;
    private String domain = "https://tinyurl.com/";

    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        String v = String.valueOf(++idx);
        m.put(v, longUrl);
        return domain + v;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        int i = shortUrl.lastIndexOf('/') + 1;
        return m.get(shortUrl.substring(i));
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));
```

#### Python 3 Solution
```python
class Codec:
    def __init__(self):
        self.m = defaultdict()
        self.idx = 0
        self.domain = 'https://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        self.idx += 1
        self.m[str(self.idx)] = longUrl
        return f'{self.domain}{self.idx}'

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        idx = shortUrl.split('/')[-1]
        return self.m[idx]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
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
