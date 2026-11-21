# 121. Best Time to Buy and Sell Stock

[![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
[![Topic: Sliding Window](https://img.shields.io/badge/Topic-Sliding%20Window-blue)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "To maximize single-transaction profit, we need to buy at a historical low and sell on a future day. In a single scan, we maintain the minimum price seen so far (`minPrice`). For each day's price, the profit if sold today is `price - minPrice`. We track the maximum profit observed."

---

### 💡 Intuition & Core Insight
- **Peak-Valley Observation**: Any profitable sale today must have bought at the minimum price on or before today.
- **No Future Knowledge Needed**: By updating `minPrice = min(minPrice, current)` and `maxProfit = max(maxProfit, current - minPrice)`, we naturally enforce causality (buy before sell).

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `prices = [7, 1, 5, 3, 6, 4]`

| Day | Price | Min Price So Far | Profit If Sold Today | Max Profit So Far |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 7 | 7 | 0 | 0 |
| 2 | 1 | 1 | 0 | 0 |
| 3 | 5 | 1 | 4 | 4 |
| 4 | 3 | 1 | 2 | 4 |
| 5 | 6 | 1 | 5 | **5** |
| 6 | 4 | 1 | 3 | 5 |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }
        return maxProfit;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ — One single linear scan through the array.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant auxiliary variables.

---

### ⚠️ Edge Cases & Interview Traps
1. Strictly decreasing prices [7, 6, 4, 3, 1]: profit remains 0.
2. Length 1: loop runs once, returns 0.

---

### 💬 Follow-Up Questions You Might Get
- *What if multiple transactions are allowed?* Greedily capture every positive day-to-day difference (LeetCode 122).
