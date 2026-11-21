# 185. Department Top Three Salaries

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/department-top-three-salaries)
[![Topic: Database](https://img.shields.io/badge/Topic-Database-blue)](https://leetcode.com/problems/department-top-three-salaries)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Database strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `Employee table:`  
**Expected Output**: `+------------+----------+--------+`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `Employee table:` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `+------------+----------+--------+` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
// Implementation provided in Solution.java
```

#### Python 3 Solution
```python
import pandas as pd


def top_three_salaries(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    salary_cutoff = (
        employee.drop_duplicates(["salary", "departmentId"])
        .groupby("departmentId")["salary"]
        .nlargest(3)
        .groupby("departmentId")
        .min()
    )
    employee["Department"] = department.set_index("id")["name"][
        employee["departmentId"]
    ].values
    employee["cutoff"] = salary_cutoff[employee["departmentId"]].values
    return employee[employee["salary"] >= employee["cutoff"]].rename(
        columns={"name": "Employee", "salary": "Salary"}
    )[["Department", "Employee", "Salary"]]
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
