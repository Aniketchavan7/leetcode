# 1908. Recyclable and Low Fat Products

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/recyclable-and-low-fat-products/)
[![Topic: SQL](https://img.shields.io/badge/Topic-SQL-blue)](https://leetcode.com/problems/recyclable-and-low-fat-products/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Find product_id of products that are both low fat and recyclable: `SELECT product_id FROM Products WHERE low_fats = 'Y' AND recyclable = 'Y';`."

---

### 💡 Intuition & Core Insight
- **Conjunctive Filtering**: Standard AND condition filtering rows where both flag columns equal 'Y'.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: Product 0: low_fats='Y', recyclable='N' (excluded). Product 1: low_fats='Y', recyclable='Y' (included).

---

### 💻 Optimal Implementations

#### Java Solution
```java
// SQL:
// SELECT product_id 
// FROM Products 
// WHERE low_fats = 'Y' AND recyclable = 'Y';

class Solution {
    public List<Integer> findProducts(int[] ids, char[] lowFat, char[] recyclable) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < ids.length; i++) {
            if (lowFat[i] == 'Y' && recyclable[i] == 'Y') {
                res.add(ids[i]);
            }
        }
        return res;
    }
}
```

#### Python 3 Solution
```python
# SQL:
# SELECT product_id FROM Products WHERE low_fats = 'Y' AND recyclable = 'Y';

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')][['product_id']]
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — Linear scan over N rows.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant filter memory.

---

### ⚠️ Edge Cases & Interview Traps
1. No products meet criteria: returns empty table.
2. All meet criteria: returns all IDs.

---

### 💬 Follow-Up Questions You Might Get
- *How to index this table?* Composite index on (low_fats, recyclable).
