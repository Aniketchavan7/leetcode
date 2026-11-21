# 1258. Article Views I

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/article-views-i/)
[![Topic: SQL](https://img.shields.io/badge/Topic-SQL-blue)](https://leetcode.com/problems/article-views-i/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Find all the authors that viewed at least one of their own articles. An author views their own article when `author_id = viewer_id`. We select distinct author_id aliased as `id` and sort in ascending order: `SELECT DISTINCT author_id AS id FROM Views WHERE author_id = viewer_id ORDER BY id ASC`."

---

### 💡 Intuition & Core Insight
- **Self-Referential Column Equality**: Comparing two columns in the same row filters self-views.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: Views table with pairs (author_id, viewer_id) = (3, 4), (7, 7), (7, 6), (4, 4)
- (7, 7): match!
- (4, 4): match!
Output: `[4, 7]` in ascending order.

---

### 💻 Optimal Implementations

#### Java Solution
```java
// SQL:
// SELECT DISTINCT author_id AS id 
// FROM Views 
// WHERE author_id = viewer_id 
// ORDER BY id ASC;

class Solution {
    public List<Integer> articleViews(int[][] views) {
        Set<Integer> authors = new TreeSet<>();
        for (int[] v : views) {
            if (v[1] == v[2]) { // author_id == viewer_id
                authors.add(v[1]);
            }
        }
        return new ArrayList<>(authors);
    }
}
```

#### Python 3 Solution
```python
# SQL:
# SELECT DISTINCT author_id AS id FROM Views WHERE author_id = viewer_id ORDER BY id ASC;

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    self_views = views[views['author_id'] == views['viewer_id']]
    unique_authors = self_views['author_id'].unique()
    unique_authors.sort()
    return pd.DataFrame({'id': unique_authors})
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log N)$ — Sorting unique author IDs in ascending order.
- **Space Complexity**: $\mathcal{O}(N)$ — Set/DataFrame storing unique IDs.

---

### ⚠️ Edge Cases & Interview Traps
1. No author viewed their own article: returns empty result set.
2. Same author viewed their article multiple times: DISTINCT ensures single entry.

---

### 💬 Follow-Up Questions You Might Get
- *What if we want authors who viewed more than 3 of their articles?* Add `GROUP BY author_id HAVING COUNT(DISTINCT article_id) >= 3`.
