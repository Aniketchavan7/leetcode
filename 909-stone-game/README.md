# 909. Stone Game

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/stone-game/)
[![Topic: Math / Minimax DP](https://img.shields.io/badge/Topic-Math%20/%20Minimax%20DP-blue)](https://leetcode.com/problems/stone-game/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Alice and Bob play a game with piles of stones in a row. Alice goes first. Piles sum to an odd number and total number of piles is even. Alice can ALWAYS win! Why? Because the number of piles is even, Alice can choose to take either ALL the even-indexed piles or ALL the odd-indexed piles. One of those two sets is strictly larger than the other. Therefore, Alice simply returns true in O(1) mathematically (or solved via interval DP)."

---

### 💡 Intuition & Core Insight
- **The Parity Monopoly**: Alice controls whether Bob is forced to take even or odd piles on every single turn.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `piles = [5, 3, 4, 5]`
- Even-indexed sum (piles 0 and 2): 5 + 4 = 9
- Odd-indexed sum (piles 1 and 3): 3 + 5 = 8
Alice chooses even-indexed piles on every turn, ending with 9 vs Bob's 8 -> Alice wins!

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public boolean stoneGame(int[] piles) {
        // Mathematically, Alice can always force a win by controlling parity
        return true;
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        # Alice always wins due to parity selection control
        return True
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(1)$ — O(1) mathematical guarantee.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant memory.

---

### ⚠️ Edge Cases & Interview Traps
1. Two piles [3, 7]: Alice takes 7, wins.
2. Four piles: Alice takes higher parity sum.

---

### 💬 Follow-Up Questions You Might Get
- *What if piles count can be odd or sums can tie?* 2D Interval DP `dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])`.
