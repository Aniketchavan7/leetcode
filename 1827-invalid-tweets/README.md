# 1827. Invalid Tweets

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/invalid-tweets/)
[![Topic: SQL](https://img.shields.io/badge/Topic-SQL-blue)](https://leetcode.com/problems/invalid-tweets/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Find the IDs of invalid tweets whose content exceeds 15 characters. In SQL, use `LENGTH(content) > 15` or `CHAR_LENGTH(content) > 15`: `SELECT tweet_id FROM Tweets WHERE CHAR_LENGTH(content) > 15;`."

---

### 💡 Intuition & Core Insight
- **CHAR_LENGTH vs LENGTH**: In multi-byte character sets (UTF-8), `CHAR_LENGTH` counts characters while `LENGTH` counts bytes. For character limit validation, `CHAR_LENGTH` is correct.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: Tweet 1: "Vote for Biden" (len 14 <= 15). Tweet 2: "Let us make America great again!" (len 32 > 15) -> Tweet 2 is returned.

---

### 💻 Optimal Implementations

#### Java Solution
```java
// SQL:
// SELECT tweet_id 
// FROM Tweets 
// WHERE CHAR_LENGTH(content) > 15;

class Solution {
    public List<Integer> invalidTweets(int[] tweetIds, String[] contents) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < tweetIds.length; i++) {
            if (contents[i].length() > 15) {
                res.add(tweetIds[i]);
            }
        }
        return res;
    }
}
```

#### Python 3 Solution
```python
# SQL:
# SELECT tweet_id FROM Tweets WHERE CHAR_LENGTH(content) > 15;

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets['content'].str.len() > 15][['tweet_id']]
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Inspects length of N tweet contents.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant filter memory.

---

### ⚠️ Edge Cases & Interview Traps
1. Exactly 15 characters: strictly valid (not > 15).
2. Empty tweets: length 0 <= 15.

---

### 💬 Follow-Up Questions You Might Get
- *What about Twitter-style weighted character counting (emojis = 2 units)?* Custom UDF or regex counting.
