# 322. Coin Change

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/coin-change/)
[![Topic: 1D Dynamic Programming](https://img.shields.io/badge/Topic-1D%20Dynamic%20Programming-blue)](https://leetcode.com/problems/coin-change/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We define `dp[i]` as the minimum number of coins needed to make amount `i`. Initialize dp with amount + 1 (infinity), and `dp[0] = 0`. For each amount from 1 to target, and for each coin: if coin <= amount, `dp[i] = Math.min(dp[i], 1 + dp[i - coin])`. If dp[amount] > amount, return -1; otherwise return dp[amount]."

---

### 💡 Intuition & Core Insight
- **Unbounded Knapsack**: You can choose any coin, paying 1 coin and reducing the subproblem to `amount - coin`.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `coins = [1, 2, 5]`, `amount = 11`
- dp[0] = 0
- dp[1] = 1 (1)
- dp[2] = 1 (2)
- dp[5] = 1 (5)
- dp[6] = 1 + dp[1] = 2 (5+1)
- ...
- dp[11] = 1 + dp[6] = 3 (5+5+1)
Result: 3.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        int max = amount + 1;
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, max);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], 1 + dp[i - coin]);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != float('inf') else -1
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(A \cdot C)$ — Amount A times C coins in nested loops.
- **Space Complexity**: $\mathcal{O}(A)$ — dp array of size amount + 1.

---

### ⚠️ Edge Cases & Interview Traps
1. amount = 0: returns 0.
2. Amount cannot be reached: returns -1.

---

### 💬 Follow-Up Questions You Might Get
- *What if we need to count total number of combinations to make amount?* Coin Change II (LeetCode 518).
