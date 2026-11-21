# 584. Find Customer Referee

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/find-customer-referee/)
[![Topic: SQL](https://img.shields.io/badge/Topic-SQL-blue)](https://leetcode.com/problems/find-customer-referee/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Find names of customer who are not referred by the customer with id = 2. In SQL three-valued logic, `referee_id != 2` evaluates to UNKNOWN for NULL values! Therefore, we must explicitly check `WHERE referee_id != 2 OR referee_id IS NULL` (or using `COALESCE(referee_id, 0) <> 2`)."

---

### 💡 Intuition & Core Insight
- **SQL NULL Trap**: In SQL, `NULL != 2` is NULL (neither true nor false). Omitting the NULL check silently filters out all customers who have no referee.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: Table with referee_id [null, null, 2, null, 2]
- Rows with null: referee_id IS NULL -> Included!
- Rows with 2: referee_id != 2 is False -> Excluded!
Returns names for customer 1, 2, 4, 5.

---

### 💻 Optimal Implementations

#### Java Solution
```java
// SQL Solution:
// SELECT name 
// FROM Customer 
// WHERE referee_id != 2 OR referee_id IS NULL;

class Solution {
    // Java representation of filtering customers not referred by id=2
    public List<String> findCustomers(int[][] customers, String[] names) {
        List<String> res = new ArrayList<>();
        for (int i = 0; i < customers.length; i++) {
            Integer refereeId = customers[i][1];
            if (refereeId == null || refereeId != 2) {
                res.add(names[i]);
            }
        }
        return res;
    }
}
```

#### Python 3 Solution
```python
# SQL:
# SELECT name FROM Customer WHERE referee_id != 2 OR referee_id IS NULL;

import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer[(customer['referee_id'] != 2) | (customer['referee_id'].isna())]
    return df[['name']]
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Full table scan or index scan over N rows.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary filter memory.

---

### ⚠️ Edge Cases & Interview Traps
1. All referee_ids are NULL: all rows returned.
2. All referee_ids are 2: empty result.

---

### 💬 Follow-Up Questions You Might Get
- *How to optimize for 100M rows?* Add index on (referee_id, name) or partition.
