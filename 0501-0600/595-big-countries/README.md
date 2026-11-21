# 595. Big Countries

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/big-countries/)
[![Topic: SQL](https://img.shields.io/badge/Topic-SQL-blue)](https://leetcode.com/problems/big-countries/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "A country is big if it has an area of at least 3,000,000 sq km or a population of at least 25,000,000. In SQL: `SELECT name, population, area FROM World WHERE area >= 3000000 OR population >= 25000000`. Using `UNION` can also allow MySQL to utilize separate indexes on area and population."

---

### 💡 Intuition & Core Insight
- **Simple Boolean Predicate**: Direct disjunction filter selecting rows meeting either threshold.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: Country A (area 3M, pop 10M) -> Included. Country B (area 1M, pop 20M) -> Excluded.

---

### 💻 Optimal Implementations

#### Java Solution
```java
// SQL Solution:
// SELECT name, population, area 
// FROM World 
// WHERE area >= 3000000 OR population >= 25000000;

class Solution {
    public List<String[]> findBigCountries(String[][] world) {
        List<String[]> res = new ArrayList<>();
        for (String[] row : world) {
            long area = Long.parseLong(row[1]);
            long pop = Long.parseLong(row[2]);
            if (area >= 3000000 || pop >= 25000000) {
                res.add(new String[]{row[0], row[2], row[1]});
            }
        }
        return res;
    }
}
```

#### Python 3 Solution
```python
# SQL:
# SELECT name, population, area FROM World WHERE area >= 3000000 OR population >= 25000000;

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return df[['name', 'population', 'area']]
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Evaluates predicate for N rows.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant filter memory.

---

### ⚠️ Edge Cases & Interview Traps
1. Country qualifies under both area and population: included exactly once.

---

### 💬 Follow-Up Questions You Might Get
- *Why use UNION over OR in older MySQL engines?* UNION enables index merge when separate single-column indexes exist.
