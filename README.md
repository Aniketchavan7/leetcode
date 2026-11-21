# 🚀 1,000 LeetCode Questions: Intuitive Explanations & Optimal Solutions

<div align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Graduation%20Cap.png" width="45" height="45" alt="Graduation Cap" />
  <p><strong>A comprehensive repository of 1,000 essential LeetCode interview questions explained from first principles.</strong></p>
  <p>Each solution is tailored exactly to <em>how you would explain the problem to an interviewer</em>: the 30-second conversational pitch, core intuition, visual dry-run traces, edge cases, follow-up questions, and clean, production-ready solutions in both <strong>Java</strong> and <strong>Python 3</strong>.</p>

  <p>
    <img src="https://img.shields.io/badge/Total%20Problems-1000-blue?style=for-the-badge" alt="Total Problems: 1000" />
    <img src="https://img.shields.io/badge/Easy-244-brightgreen?style=for-the-badge" alt="Easy" />
    <img src="https://img.shields.io/badge/Medium-551-orange?style=for-the-badge" alt="Medium" />
    <img src="https://img.shields.io/badge/Hard-205-red?style=for-the-badge" alt="Hard" />
    <img src="https://img.shields.io/badge/Language-Java%20%7C%20Python-blueviolet?style=for-the-badge" alt="Languages" />
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License" />
  </p>
</div>

---

## 🧭 Interview Framework: How to Explain Problems in an Interview

When solving technical questions at Google, Meta, Amazon, Microsoft, and top startups, interviewers look for **communication, structured thinking, and tradeoff analysis** before code. Every problem in this repository follows this 6-stage blueprint:

1. **The 30-Second Elevator Pitch**: Verbalizing the problem statement, why naive brute-force is sub-optimal, and introducing the optimal technique in plain English.
2. **Intuition & The "Aha!" Moment**: Unpacking the geometric, algebraic, or invariant insight that eliminates redundant calculations.
3. **Visual Step-by-Step Dry Run**: Explicit tabular trace or diagram walking through state variables across array indices or recursion frames.
4. **Optimal Code**: Clean, well-commented, production-grade implementations in **Java** and **Python 3**.
5. **Rigorous Complexity Analysis**: Precise mathematical justifications for Time $\mathcal{O}(\dots)$ and Space $\mathcal{O}(\dots)$.
6. **Edge Cases & Follow-Up Questions**: Anticipating interviewer questions (*"What if memory is constrained?", "What if duplicates exist?", "What if numbers overflow?"*).

---

## 📚 Categorized Roadmap by Algorithm Pattern

### 📌 1D Dynamic Programming (5 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 70 | [Climbing Stairs](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [70-climbing-stairs](./70-climbing-stairs) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 139 | [Word Break](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [139-word-break](./139-word-break) | $\mathcal{O}(N^2 \cdot L)$ | $\mathcal{O}(N + M)$ |
| 152 | [Maximum Product Subarray](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [152-maximum-product-subarray](./152-maximum-product-subarray) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 198 | [House Robber](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [198-house-robber](./198-house-robber) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 322 | [Coin Change](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [322-coin-change](./322-coin-change) | $\mathcal{O}(A \cdot C)$ | $\mathcal{O}(A)$ |

### 📌 1D Dynamic Programming / Circular (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 213 | [House Robber II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [213-house-robber-ii](./213-house-robber-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 2D Dynamic Programming (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 1143 | [Longest Common Subsequence](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [1143-longest-common-subsequence](./1143-longest-common-subsequence) | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(\min(M, N))$ |

### 📌 Algorithms (10 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 2 | [Add Two Numbers](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [2-add-two-numbers](./2-add-two-numbers) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 4 | [Median of Two Sorted Arrays](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [4-median-of-two-sorted-arrays](./4-median-of-two-sorted-arrays) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 5 | [Longest Palindromic Substring](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [5-longest-palindromic-substring](./5-longest-palindromic-substring) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 6 | [Zigzag Conversion](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [6-zigzag-conversion](./6-zigzag-conversion) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 8 | [String to Integer (atoi)](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [8-string-to-integer-atoi](./8-string-to-integer-atoi) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 10 | [Regular Expression Matching](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [10-regular-expression-matching](./10-regular-expression-matching) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 12 | [Integer to Roman](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [12-integer-to-roman](./12-integer-to-roman) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 13 | [Roman to Integer](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [13-roman-to-integer](./13-roman-to-integer) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 14 | [Longest Common Prefix](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [14-longest-common-prefix](./14-longest-common-prefix) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 16 | [3Sum Closest](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [16-3sum-closest](./16-3sum-closest) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Array (217 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 18 | [4Sum](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [18-4sum](./18-4sum) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 27 | [Remove Element](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [27-remove-element](./27-remove-element) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 34 | [Find First and Last Position of Element in Sorted Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [34-find-first-and-last-position-of-element-in-sorted-array](./34-find-first-and-last-position-of-element-in-sorted-array) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 35 | [Search Insert Position](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [35-search-insert-position](./35-search-insert-position) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 36 | [Valid Sudoku](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [36-valid-sudoku](./36-valid-sudoku) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 37 | [Sudoku Solver](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [37-sudoku-solver](./37-sudoku-solver) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 40 | [Combination Sum II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [40-combination-sum-ii](./40-combination-sum-ii) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 41 | [First Missing Positive](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [41-first-missing-positive](./41-first-missing-positive) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 47 | [Permutations II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [47-permutations-ii](./47-permutations-ii) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 51 | [N-Queens](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [51-n-queens](./51-n-queens) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 59 | [Spiral Matrix II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [59-spiral-matrix-ii](./59-spiral-matrix-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 63 | [Unique Paths II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [63-unique-paths-ii](./63-unique-paths-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 64 | [Minimum Path Sum](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [64-minimum-path-sum](./64-minimum-path-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 66 | [Plus One](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [66-plus-one](./66-plus-one) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 68 | [Text Justification](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [68-text-justification](./68-text-justification) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 74 | [Search a 2D Matrix](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [74-search-a-2d-matrix](./74-search-a-2d-matrix) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 80 | [Remove Duplicates from Sorted Array II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [80-remove-duplicates-from-sorted-array-ii](./80-remove-duplicates-from-sorted-array-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 81 | [Search in Rotated Sorted Array II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [81-search-in-rotated-sorted-array-ii](./81-search-in-rotated-sorted-array-ii) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 88 | [Merge Sorted Array](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [88-merge-sorted-array](./88-merge-sorted-array) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 118 | [Pascal's Triangle](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [118-pascal-s-triangle](./118-pascal-s-triangle) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 119 | [Pascal's Triangle II](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [119-pascal-s-triangle-ii](./119-pascal-s-triangle-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 120 | [Triangle](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [120-triangle](./120-triangle) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 123 | [Best Time to Buy and Sell Stock III](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [123-best-time-to-buy-and-sell-stock-iii](./123-best-time-to-buy-and-sell-stock-iii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 154 | [Find Minimum in Rotated Sorted Array II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [154-find-minimum-in-rotated-sorted-array-ii](./154-find-minimum-in-rotated-sorted-array-ii) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 157 | [Read N Characters Given Read4](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [157-read-n-characters-given-read4](./157-read-n-characters-given-read4) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 158 | [Read N Characters Given read4 II - Call Multiple Times](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [158-read-n-characters-given-read4-ii-call-multiple-times](./158-read-n-characters-given-read4-ii-call-multiple-times) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 162 | [Find Peak Element](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [162-find-peak-element](./162-find-peak-element) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 163 | [Missing Ranges](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [163-missing-ranges](./163-missing-ranges) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 164 | [Maximum Gap](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [164-maximum-gap](./164-maximum-gap) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 167 | [Two Sum II - Input Array Is Sorted](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [167-two-sum-ii-input-array-is-sorted](./167-two-sum-ii-input-array-is-sorted) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 174 | [Dungeon Game](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [174-dungeon-game](./174-dungeon-game) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 188 | [Best Time to Buy and Sell Stock IV](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [188-best-time-to-buy-and-sell-stock-iv](./188-best-time-to-buy-and-sell-stock-iv) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 204 | [Count Primes](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [204-count-primes](./204-count-primes) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 209 | [Minimum Size Subarray Sum](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [209-minimum-size-subarray-sum](./209-minimum-size-subarray-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 216 | [Combination Sum III](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [216-combination-sum-iii](./216-combination-sum-iii) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 219 | [Contains Duplicate II](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [219-contains-duplicate-ii](./219-contains-duplicate-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 220 | [Contains Duplicate III](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [220-contains-duplicate-iii](./220-contains-duplicate-iii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 221 | [Maximal Square](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [221-maximal-square](./221-maximal-square) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 228 | [Summary Ranges](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [228-summary-ranges](./228-summary-ranges) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 229 | [Majority Element II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [229-majority-element-ii](./229-majority-element-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 240 | [Search a 2D Matrix II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [240-search-a-2d-matrix-ii](./240-search-a-2d-matrix-ii) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 243 | [Shortest Word Distance](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [243-shortest-word-distance](./243-shortest-word-distance) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 245 | [Shortest Word Distance III](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [245-shortest-word-distance-iii](./245-shortest-word-distance-iii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 249 | [Group Shifted Strings](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [249-group-shifted-strings](./249-group-shifted-strings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 252 | [Meeting Rooms](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [252-meeting-rooms](./252-meeting-rooms) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 256 | [Paint House](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [256-paint-house](./256-paint-house) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 259 | [3Sum Smaller](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [259-3sum-smaller](./259-3sum-smaller) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 265 | [Paint House II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [265-paint-house-ii](./265-paint-house-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 274 | [H-Index](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [274-h-index](./274-h-index) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 275 | [H-Index II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [275-h-index-ii](./275-h-index-ii) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 289 | [Game of Life](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [289-game-of-life](./289-game-of-life) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 296 | [Best Meeting Point](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [296-best-meeting-point](./296-best-meeting-point) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 309 | [Best Time to Buy and Sell Stock with Cooldown](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [309-best-time-to-buy-and-sell-stock-with-cooldown](./309-best-time-to-buy-and-sell-stock-with-cooldown) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 311 | [Sparse Matrix Multiplication](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [311-sparse-matrix-multiplication](./311-sparse-matrix-multiplication) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 312 | [Burst Balloons](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [312-burst-balloons](./312-burst-balloons) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 313 | [Super Ugly Number](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [313-super-ugly-number](./313-super-ugly-number) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 325 | [Maximum Size Subarray Sum Equals k](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [325-maximum-size-subarray-sum-equals-k](./325-maximum-size-subarray-sum-equals-k) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 349 | [Intersection of Two Arrays](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [349-intersection-of-two-arrays](./349-intersection-of-two-arrays) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 350 | [Intersection of Two Arrays II](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [350-intersection-of-two-arrays-ii](./350-intersection-of-two-arrays-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 354 | [Russian Doll Envelopes](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [354-russian-doll-envelopes](./354-russian-doll-envelopes) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 356 | [Line Reflection](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [356-line-reflection](./356-line-reflection) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 360 | [Sort Transformed Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [360-sort-transformed-array](./360-sort-transformed-array) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 361 | [Bomb Enemy](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [361-bomb-enemy](./361-bomb-enemy) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 363 | [Max Sum of Rectangle No Larger Than K](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [363-max-sum-of-rectangle-no-larger-than-k](./363-max-sum-of-rectangle-no-larger-than-k) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 368 | [Largest Divisible Subset](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [368-largest-divisible-subset](./368-largest-divisible-subset) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 370 | [Range Addition](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [370-range-addition](./370-range-addition) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 373 | [Find K Pairs with Smallest Sums](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [373-find-k-pairs-with-smallest-sums](./373-find-k-pairs-with-smallest-sums) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 377 | [Combination Sum IV](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [377-combination-sum-iv](./377-combination-sum-iv) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 378 | [Kth Smallest Element in a Sorted Matrix](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [378-kth-smallest-element-in-a-sorted-matrix](./378-kth-smallest-element-in-a-sorted-matrix) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 396 | [Rotate Function](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [396-rotate-function](./396-rotate-function) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 403 | [Frog Jump](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [403-frog-jump](./403-frog-jump) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 413 | [Arithmetic Slices](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [413-arithmetic-slices](./413-arithmetic-slices) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 414 | [Third Maximum Number](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [414-third-maximum-number](./414-third-maximum-number) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 416 | [Partition Equal Subset Sum](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [416-partition-equal-subset-sum](./416-partition-equal-subset-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 418 | [Sentence Screen Fitting](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [418-sentence-screen-fitting](./418-sentence-screen-fitting) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 422 | [Valid Word Square](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [422-valid-word-square](./422-valid-word-square) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 436 | [Find Right Interval](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [436-find-right-interval](./436-find-right-interval) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 442 | [Find All Duplicates in an Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [442-find-all-duplicates-in-an-array](./442-find-all-duplicates-in-an-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 446 | [Arithmetic Slices II - Subsequence](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [446-arithmetic-slices-ii-subsequence](./446-arithmetic-slices-ii-subsequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 447 | [Number of Boomerangs](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [447-number-of-boomerangs](./447-number-of-boomerangs) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 448 | [Find All Numbers Disappeared in an Array](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [448-find-all-numbers-disappeared-in-an-array](./448-find-all-numbers-disappeared-in-an-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 453 | [Minimum Moves to Equal Array Elements](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [453-minimum-moves-to-equal-array-elements](./453-minimum-moves-to-equal-array-elements) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 454 | [4Sum II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [454-4sum-ii](./454-4sum-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 457 | [Circular Array Loop](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [457-circular-array-loop](./457-circular-array-loop) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 462 | [Minimum Moves to Equal Array Elements II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [462-minimum-moves-to-equal-array-elements-ii](./462-minimum-moves-to-equal-array-elements-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 474 | [Ones and Zeroes](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [474-ones-and-zeroes](./474-ones-and-zeroes) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 475 | [Heaters](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [475-heaters](./475-heaters) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 480 | [Sliding Window Median](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [480-sliding-window-median](./480-sliding-window-median) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 487 | [Max Consecutive Ones II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [487-max-consecutive-ones-ii](./487-max-consecutive-ones-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 494 | [Target Sum](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [494-target-sum](./494-target-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 495 | [Teemo Attacking](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [495-teemo-attacking](./495-teemo-attacking) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 498 | [Diagonal Traverse](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [498-diagonal-traverse](./498-diagonal-traverse) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 500 | [Keyboard Row](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [500-keyboard-row](./500-keyboard-row) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 506 | [Relative Ranks](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [506-relative-ranks](./506-relative-ranks) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 518 | [Coin Change II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [518-coin-change-ii](./518-coin-change-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 522 | [Longest Uncommon Subsequence II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [522-longest-uncommon-subsequence-ii](./522-longest-uncommon-subsequence-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 523 | [Continuous Subarray Sum](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [523-continuous-subarray-sum](./523-continuous-subarray-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 524 | [Longest Word in Dictionary through Deleting](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [524-longest-word-in-dictionary-through-deleting](./524-longest-word-in-dictionary-through-deleting) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 525 | [Contiguous Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [525-contiguous-array](./525-contiguous-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 528 | [Random Pick with Weight](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [528-random-pick-with-weight](./528-random-pick-with-weight) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 531 | [Lonely Pixel I](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [531-lonely-pixel-i](./531-lonely-pixel-i) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 532 | [K-diff Pairs in an Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [532-k-diff-pairs-in-an-array](./532-k-diff-pairs-in-an-array) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 533 | [Lonely Pixel II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [533-lonely-pixel-ii](./533-lonely-pixel-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 539 | [Minimum Time Difference](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [539-minimum-time-difference](./539-minimum-time-difference) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 540 | [Single Element in a Sorted Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [540-single-element-in-a-sorted-array](./540-single-element-in-a-sorted-array) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 548 | [Split Array with Equal Sum](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [548-split-array-with-equal-sum](./548-split-array-with-equal-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 553 | [Optimal Division](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [553-optimal-division](./553-optimal-division) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 554 | [Brick Wall](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [554-brick-wall](./554-brick-wall) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 560 | [Subarray Sum Equals K](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [560-subarray-sum-equals-k](./560-subarray-sum-equals-k) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 562 | [Longest Line of Consecutive One in Matrix](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [562-longest-line-of-consecutive-one-in-matrix](./562-longest-line-of-consecutive-one-in-matrix) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 566 | [Reshape the Matrix](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [566-reshape-the-matrix](./566-reshape-the-matrix) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 568 | [Maximum Vacation Days](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [568-maximum-vacation-days](./568-maximum-vacation-days) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 573 | [Squirrel Simulation](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [573-squirrel-simulation](./573-squirrel-simulation) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 575 | [Distribute Candies](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [575-distribute-candies](./575-distribute-candies) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 594 | [Longest Harmonious Subsequence](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [594-longest-harmonious-subsequence](./594-longest-harmonious-subsequence) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 598 | [Range Addition II](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [598-range-addition-ii](./598-range-addition-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 599 | [Minimum Index Sum of Two Lists](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [599-minimum-index-sum-of-two-lists](./599-minimum-index-sum-of-two-lists) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 609 | [Find Duplicate File in System](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [609-find-duplicate-file-in-system](./609-find-duplicate-file-in-system) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 643 | [Maximum Average Subarray I](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [643-maximum-average-subarray-i](./643-maximum-average-subarray-i) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 644 | [Maximum Average Subarray II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [644-maximum-average-subarray-ii](./644-maximum-average-subarray-ii) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 656 | [Coin Path](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [656-coin-path](./656-coin-path) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 658 | [Find K Closest Elements](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [658-find-k-closest-elements](./658-find-k-closest-elements) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 661 | [Image Smoother](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [661-image-smoother](./661-image-smoother) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 665 | [Non-decreasing Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [665-non-decreasing-array](./665-non-decreasing-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 667 | [Beautiful Arrangement II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [667-beautiful-arrangement-ii](./667-beautiful-arrangement-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 674 | [Longest Continuous Increasing Subsequence](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [674-longest-continuous-increasing-subsequence](./674-longest-continuous-increasing-subsequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 679 | [24 Game](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [679-24-game](./679-24-game) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 689 | [Maximum Sum of 3 Non-Overlapping Subarrays](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [689-maximum-sum-of-3-non-overlapping-subarrays](./689-maximum-sum-of-3-non-overlapping-subarrays) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 697 | [Degree of an Array](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [697-degree-of-an-array](./697-degree-of-an-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 702 | [Search in a Sorted Array of Unknown Size](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [702-search-in-a-sorted-array-of-unknown-size](./702-search-in-a-sorted-array-of-unknown-size) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 704 | [Binary Search](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [704-binary-search](./704-binary-search) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 710 | [Random Pick with Blacklist](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [710-random-pick-with-blacklist](./710-random-pick-with-blacklist) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 713 | [Subarray Product Less Than K](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [713-subarray-product-less-than-k](./713-subarray-product-less-than-k) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 717 | [1-bit and 2-bit Characters](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [717-1-bit-and-2-bit-characters](./717-1-bit-and-2-bit-characters) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 718 | [Maximum Length of Repeated Subarray](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [718-maximum-length-of-repeated-subarray](./718-maximum-length-of-repeated-subarray) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 719 | [Find K-th Smallest Pair Distance](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [719-find-k-th-smallest-pair-distance](./719-find-k-th-smallest-pair-distance) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 722 | [Remove Comments](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [722-remove-comments](./722-remove-comments) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 723 | [Candy Crush](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [723-candy-crush](./723-candy-crush) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 724 | [Find Pivot Index](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [724-find-pivot-index](./724-find-pivot-index) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 734 | [Sentence Similarity](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [734-sentence-similarity](./734-sentence-similarity) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 740 | [Delete and Earn](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [740-delete-and-earn](./740-delete-and-earn) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 741 | [Cherry Pickup](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [741-cherry-pickup](./741-cherry-pickup) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 744 | [Find Smallest Letter Greater Than Target](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [744-find-smallest-letter-greater-than-target](./744-find-smallest-letter-greater-than-target) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 746 | [Min Cost Climbing Stairs](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [746-min-cost-climbing-stairs](./746-min-cost-climbing-stairs) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 747 | [Largest Number At Least Twice of Others](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [747-largest-number-at-least-twice-of-others](./747-largest-number-at-least-twice-of-others) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 748 | [Shortest Completing Word](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [748-shortest-completing-word](./748-shortest-completing-word) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 750 | [Number Of Corner Rectangles](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [750-number-of-corner-rectangles](./750-number-of-corner-rectangles) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 755 | [Pour Water](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [755-pour-water](./755-pour-water) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 759 | [Employee Free Time](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [759-employee-free-time](./759-employee-free-time) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 760 | [Find Anagram Mappings](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [760-find-anagram-mappings](./760-find-anagram-mappings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 764 | [Largest Plus Sign](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [764-largest-plus-sign](./764-largest-plus-sign) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 766 | [Toeplitz Matrix](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [766-toeplitz-matrix](./766-toeplitz-matrix) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 774 | [Minimize Max Distance to Gas Station](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [774-minimize-max-distance-to-gas-station](./774-minimize-max-distance-to-gas-station) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 775 | [Global and Local Inversions](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [775-global-and-local-inversions](./775-global-and-local-inversions) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 786 | [K-th Smallest Prime Fraction](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [786-k-th-smallest-prime-fraction](./786-k-th-smallest-prime-fraction) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 789 | [Escape The Ghosts](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [789-escape-the-ghosts](./789-escape-the-ghosts) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 794 | [Valid Tic-Tac-Toe State](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [794-valid-tic-tac-toe-state](./794-valid-tic-tac-toe-state) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 795 | [Number of Subarrays with Bounded Maximum](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [795-number-of-subarrays-with-bounded-maximum](./795-number-of-subarrays-with-bounded-maximum) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 798 | [Smallest Rotation with Highest Score](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [798-smallest-rotation-with-highest-score](./798-smallest-rotation-with-highest-score) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 801 | [Minimum Swaps To Make Sequences Increasing](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [801-minimum-swaps-to-make-sequences-increasing](./801-minimum-swaps-to-make-sequences-increasing) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 804 | [Unique Morse Code Words](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [804-unique-morse-code-words](./804-unique-morse-code-words) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 806 | [Number of Lines To Write String](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [806-number-of-lines-to-write-string](./806-number-of-lines-to-write-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 809 | [Expressive Words](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [809-expressive-words](./809-expressive-words) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 811 | [Subdomain Visit Count](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [811-subdomain-visit-count](./811-subdomain-visit-count) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 813 | [Largest Sum of Averages](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [813-largest-sum-of-averages](./813-largest-sum-of-averages) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 817 | [Linked List Components](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [817-linked-list-components](./817-linked-list-components) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 819 | [Most Common Word](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [819-most-common-word](./819-most-common-word) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 821 | [Shortest Distance to a Character](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [821-shortest-distance-to-a-character](./821-shortest-distance-to-a-character) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 822 | [Card Flipping Game](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [822-card-flipping-game](./822-card-flipping-game) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 823 | [Binary Trees With Factors](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [823-binary-trees-with-factors](./823-binary-trees-with-factors) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 825 | [Friends Of Appropriate Ages](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [825-friends-of-appropriate-ages](./825-friends-of-appropriate-ages) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 833 | [Find And Replace in String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [833-find-and-replace-in-string](./833-find-and-replace-in-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 835 | [Image Overlap](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [835-image-overlap](./835-image-overlap) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 840 | [Magic Squares In Grid](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [840-magic-squares-in-grid](./840-magic-squares-in-grid) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 845 | [Longest Mountain in Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [845-longest-mountain-in-array](./845-longest-mountain-in-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 848 | [Shifting Letters](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [848-shifting-letters](./848-shifting-letters) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 849 | [Maximize Distance to Closest Person](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [849-maximize-distance-to-closest-person](./849-maximize-distance-to-closest-person) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 852 | [Peak Index in a Mountain Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [852-peak-index-in-a-mountain-array](./852-peak-index-in-a-mountain-array) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 867 | [Transpose Matrix](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [867-transpose-matrix](./867-transpose-matrix) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 873 | [Length of Longest Fibonacci Subsequence](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [873-length-of-longest-fibonacci-subsequence](./873-length-of-longest-fibonacci-subsequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 874 | [Walking Robot Simulation](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [874-walking-robot-simulation](./874-walking-robot-simulation) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 875 | [Koko Eating Bananas](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [875-koko-eating-bananas](./875-koko-eating-bananas) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 879 | [Profitable Schemes](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [879-profitable-schemes](./879-profitable-schemes) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 885 | [Spiral Matrix III](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [885-spiral-matrix-iii](./885-spiral-matrix-iii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 888 | [Fair Candy Swap](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [888-fair-candy-swap](./888-fair-candy-swap) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 890 | [Find and Replace Pattern](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [890-find-and-replace-pattern](./890-find-and-replace-pattern) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 891 | [Sum of Subsequence Widths](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [891-sum-of-subsequence-widths](./891-sum-of-subsequence-widths) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 893 | [Groups of Special-Equivalent Strings](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [893-groups-of-special-equivalent-strings](./893-groups-of-special-equivalent-strings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 896 | [Monotonic Array](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [896-monotonic-array](./896-monotonic-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 902 | [Numbers At Most N Given Digit Set](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [902-numbers-at-most-n-given-digit-set](./902-numbers-at-most-n-given-digit-set) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 904 | [Fruit Into Baskets](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [904-fruit-into-baskets](./904-fruit-into-baskets) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 905 | [Sort Array By Parity](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [905-sort-array-by-parity](./905-sort-array-by-parity) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 908 | [Smallest Range I](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [908-smallest-range-i](./908-smallest-range-i) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 912 | [Sort an Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [912-sort-an-array](./912-sort-an-array) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 914 | [X of a Kind in a Deck of Cards](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [914-x-of-a-kind-in-a-deck-of-cards](./914-x-of-a-kind-in-a-deck-of-cards) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 915 | [Partition Array into Disjoint Intervals](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [915-partition-array-into-disjoint-intervals](./915-partition-array-into-disjoint-intervals) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 916 | [Word Subsets](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [916-word-subsets](./916-word-subsets) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 922 | [Sort Array By Parity II](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [922-sort-array-by-parity-ii](./922-sort-array-by-parity-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 923 | [3Sum With Multiplicity](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [923-3sum-with-multiplicity](./923-3sum-with-multiplicity) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 927 | [Three Equal Parts](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [927-three-equal-parts](./927-three-equal-parts) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 929 | [Unique Email Addresses](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [929-unique-email-addresses](./929-unique-email-addresses) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 930 | [Binary Subarrays With Sum](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [930-binary-subarrays-with-sum](./930-binary-subarrays-with-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 931 | [Minimum Falling Path Sum](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [931-minimum-falling-path-sum](./931-minimum-falling-path-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 932 | [Beautiful Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [932-beautiful-array](./932-beautiful-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 937 | [Reorder Data in Log Files](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [937-reorder-data-in-log-files](./937-reorder-data-in-log-files) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 941 | [Valid Mountain Array](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [941-valid-mountain-array](./941-valid-mountain-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 944 | [Delete Columns to Make Sorted](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [944-delete-columns-to-make-sorted](./944-delete-columns-to-make-sorted) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 949 | [Largest Time for Given Digits](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [949-largest-time-for-given-digits](./949-largest-time-for-given-digits) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 953 | [Verifying an Alien Dictionary](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [953-verifying-an-alien-dictionary](./953-verifying-an-alien-dictionary) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 956 | [Tallest Billboard](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [956-tallest-billboard](./956-tallest-billboard) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 960 | [Delete Columns to Make Sorted III](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [960-delete-columns-to-make-sorted-iii](./960-delete-columns-to-make-sorted-iii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 961 | [N-Repeated Element in Size 2N Array](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [961-n-repeated-element-in-size-2n-array](./961-n-repeated-element-in-size-2n-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 966 | [Vowel Spellchecker](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [966-vowel-spellchecker](./966-vowel-spellchecker) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 974 | [Subarray Sums Divisible by K](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [974-subarray-sums-divisible-by-k](./974-subarray-sums-divisible-by-k) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 977 | [Squares of a Sorted Array](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [977-squares-of-a-sorted-array](./977-squares-of-a-sorted-array) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 978 | [Longest Turbulent Subarray](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [978-longest-turbulent-subarray](./978-longest-turbulent-subarray) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 983 | [Minimum Cost For Tickets](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [983-minimum-cost-for-tickets](./983-minimum-cost-for-tickets) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Arrays (2 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 485 | [Max Consecutive Ones](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [485-max-consecutive-ones](./485-max-consecutive-ones) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 1878 | [Check if Array Is Sorted and Rotated](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [1878-check-if-array-is-sorted-and-rotated](./1878-check-if-array-is-sorted-and-rotated) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Arrays %26 Hashing (5 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 1 | [Two Sum](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [1-two-sum](./1-two-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 49 | [Group Anagrams](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [49-group-anagrams](./49-group-anagrams) | $\mathcal{O}(N \cdot K \log K)$ | $\mathcal{O}(N \cdot K)$ |
| 128 | [Longest Consecutive Sequence](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [128-longest-consecutive-sequence](./128-longest-consecutive-sequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 217 | [Contains Duplicate](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [217-contains-duplicate](./217-contains-duplicate) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 242 | [Valid Anagram](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [242-valid-anagram](./242-valid-anagram) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Arrays / Math (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 4256 | [Construct Uniform Parity Array I](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [4256-construct-uniform-parity-array-i](./4256-construct-uniform-parity-array-i) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Arrays / Prefix Minimums (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 4284 | [Smallest Stable Index I](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [4284-smallest-stable-index-i](./4284-smallest-stable-index-i) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Backtracking (7 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 39 | [Combination Sum](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [39-combination-sum](./39-combination-sum) | $\mathcal{O}(2^{T/M})$ | $\mathcal{O}(T/M)$ |
| 46 | [Permutations](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [46-permutations](./46-permutations) | $\mathcal{O}(N \cdot N!)$ | $\mathcal{O}(N)$ |
| 52 | [N-Queens II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [52-n-queens-ii](./52-n-queens-ii) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 77 | [Combinations](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [77-combinations](./77-combinations) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 78 | [Subsets](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [78-subsets](./78-subsets) | $\mathcal{O}(N \cdot 2^N)$ | $\mathcal{O}(N)$ |
| 254 | [Factor Combinations](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [254-factor-combinations](./254-factor-combinations) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 489 | [Robot Room Cleaner](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [489-robot-room-cleaner](./489-robot-room-cleaner) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |

### 📌 Backtracking / Matrix DFS (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 79 | [Word Search](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [79-word-search](./79-word-search) | $\mathcal{O}(M \cdot N \cdot 3^L)$ | $\mathcal{O}(L)$ |

### 📌 Binary Indexed Tree (7 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 218 | [The Skyline Problem](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [218-the-skyline-problem](./218-the-skyline-problem) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 315 | [Count of Smaller Numbers After Self](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [315-count-of-smaller-numbers-after-self](./315-count-of-smaller-numbers-after-self) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 327 | [Count of Range Sum](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [327-count-of-range-sum](./327-count-of-range-sum) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 406 | [Queue Reconstruction by Height](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [406-queue-reconstruction-by-height](./406-queue-reconstruction-by-height) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 493 | [Reverse Pairs](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [493-reverse-pairs](./493-reverse-pairs) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 673 | [Number of Longest Increasing Subsequence](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [673-number-of-longest-increasing-subsequence](./673-number-of-longest-increasing-subsequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 683 | [K Empty Slots](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [683-k-empty-slots](./683-k-empty-slots) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Binary Search (4 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 33 | [Search in Rotated Sorted Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [33-search-in-rotated-sorted-array](./33-search-in-rotated-sorted-array) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 153 | [Find Minimum in Rotated Sorted Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [153-find-minimum-in-rotated-sorted-array](./153-find-minimum-in-rotated-sorted-array) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 278 | [First Bad Version](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [278-first-bad-version](./278-first-bad-version) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 374 | [Guess Number Higher or Lower](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [374-guess-number-higher-or-lower](./374-guess-number-higher-or-lower) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |

### 📌 Bit Manipulation (57 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 29 | [Divide Two Integers](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [29-divide-two-integers](./29-divide-two-integers) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 67 | [Add Binary](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [67-add-binary](./67-add-binary) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 89 | [Gray Code](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [89-gray-code](./89-gray-code) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 90 | [Subsets II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [90-subsets-ii](./90-subsets-ii) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 137 | [Single Number II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [137-single-number-ii](./137-single-number-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 187 | [Repeated DNA Sequences](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [187-repeated-dna-sequences](./187-repeated-dna-sequences) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 190 | [Reverse Bits](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [190-reverse-bits](./190-reverse-bits) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 191 | [Number of 1 Bits](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [191-number-of-1-bits](./191-number-of-1-bits) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 201 | [Bitwise AND of Numbers Range](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [201-bitwise-and-of-numbers-range](./201-bitwise-and-of-numbers-range) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 222 | [Count Complete Tree Nodes](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [222-count-complete-tree-nodes](./222-count-complete-tree-nodes) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 231 | [Power of Two](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [231-power-of-two](./231-power-of-two) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 260 | [Single Number III](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [260-single-number-iii](./260-single-number-iii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 266 | [Palindrome Permutation](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [266-palindrome-permutation](./266-palindrome-permutation) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 287 | [Find the Duplicate Number](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [287-find-the-duplicate-number](./287-find-the-duplicate-number) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 318 | [Maximum Product of Word Lengths](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [318-maximum-product-of-word-lengths](./318-maximum-product-of-word-lengths) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 320 | [Generalized Abbreviation](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [320-generalized-abbreviation](./320-generalized-abbreviation) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 338 | [Counting Bits](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [338-counting-bits](./338-counting-bits) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 342 | [Power of Four](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [342-power-of-four](./342-power-of-four) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 351 | [Android Unlock Patterns](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [351-android-unlock-patterns](./351-android-unlock-patterns) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 371 | [Sum of Two Integers](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [371-sum-of-two-integers](./371-sum-of-two-integers) | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| 389 | [Find the Difference](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [389-find-the-difference](./389-find-the-difference) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 393 | [UTF-8 Validation](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [393-utf-8-validation](./393-utf-8-validation) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 401 | [Binary Watch](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [401-binary-watch](./401-binary-watch) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 405 | [Convert a Number to Hexadecimal](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [405-convert-a-number-to-hexadecimal](./405-convert-a-number-to-hexadecimal) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 411 | [Minimum Unique Word Abbreviation](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [411-minimum-unique-word-abbreviation](./411-minimum-unique-word-abbreviation) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 421 | [Maximum XOR of Two Numbers in an Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [421-maximum-xor-of-two-numbers-in-an-array](./421-maximum-xor-of-two-numbers-in-an-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 461 | [Hamming Distance](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [461-hamming-distance](./461-hamming-distance) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 464 | [Can I Win](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [464-can-i-win](./464-can-i-win) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 465 | [Optimal Account Balancing](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [465-optimal-account-balancing](./465-optimal-account-balancing) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 473 | [Matchsticks to Square](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [473-matchsticks-to-square](./473-matchsticks-to-square) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 476 | [Number Complement](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [476-number-complement](./476-number-complement) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 477 | [Total Hamming Distance](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [477-total-hamming-distance](./477-total-hamming-distance) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 491 | [Non-decreasing Subsequences](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [491-non-decreasing-subsequences](./491-non-decreasing-subsequences) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 526 | [Beautiful Arrangement](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [526-beautiful-arrangement](./526-beautiful-arrangement) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 638 | [Shopping Offers](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [638-shopping-offers](./638-shopping-offers) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 645 | [Set Mismatch](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [645-set-mismatch](./645-set-mismatch) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 672 | [Bulb Switcher II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [672-bulb-switcher-ii](./672-bulb-switcher-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 691 | [Stickers to Spell Word](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [691-stickers-to-spell-word](./691-stickers-to-spell-word) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 693 | [Binary Number with Alternating Bits](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [693-binary-number-with-alternating-bits](./693-binary-number-with-alternating-bits) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 698 | [Partition to K Equal Sum Subsets](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [698-partition-to-k-equal-sum-subsets](./698-partition-to-k-equal-sum-subsets) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 751 | [IP to CIDR](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [751-ip-to-cidr](./751-ip-to-cidr) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 756 | [Pyramid Transition Matrix](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [756-pyramid-transition-matrix](./756-pyramid-transition-matrix) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 762 | [Prime Number of Set Bits in Binary Representation](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [762-prime-number-of-set-bits-in-binary-representation](./762-prime-number-of-set-bits-in-binary-representation) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 779 | [K-th Symbol in Grammar](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [779-k-th-symbol-in-grammar](./779-k-th-symbol-in-grammar) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 782 | [Transform to Chessboard](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [782-transform-to-chessboard](./782-transform-to-chessboard) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 784 | [Letter Case Permutation](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [784-letter-case-permutation](./784-letter-case-permutation) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 805 | [Split Array With Same Average](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [805-split-array-with-same-average](./805-split-array-with-same-average) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 810 | [Chalkboard XOR Game](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [810-chalkboard-xor-game](./810-chalkboard-xor-game) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 832 | [Flipping an Image](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [832-flipping-an-image](./832-flipping-an-image) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 847 | [Shortest Path Visiting All Nodes](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [847-shortest-path-visiting-all-nodes](./847-shortest-path-visiting-all-nodes) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 864 | [Shortest Path to Get All Keys](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [864-shortest-path-to-get-all-keys](./864-shortest-path-to-get-all-keys) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 868 | [Binary Gap](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [868-binary-gap](./868-binary-gap) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 898 | [Bitwise ORs of Subarrays](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [898-bitwise-ors-of-subarrays](./898-bitwise-ors-of-subarrays) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 943 | [Find the Shortest Superstring](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [943-find-the-shortest-superstring](./943-find-the-shortest-superstring) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 957 | [Prison Cells After N Days](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [957-prison-cells-after-n-days](./957-prison-cells-after-n-days) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 980 | [Unique Paths III](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [980-unique-paths-iii](./980-unique-paths-iii) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 982 | [Triples with Bitwise AND Equal To Zero](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [982-triples-with-bitwise-and-equal-to-zero](./982-triples-with-bitwise-and-equal-to-zero) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Bit Manipulation / Math (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 268 | [Missing Number](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [268-missing-number](./268-missing-number) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Bit Manipulation / XOR (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 136 | [Single Number](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [136-single-number](./136-single-number) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Boyer (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 169 | [Majority Element](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [169-majority-element](./169-majority-element) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Brainteaser (2 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 292 | [Nim Game](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [292-nim-game](./292-nim-game) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 319 | [Bulb Switcher](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [319-bulb-switcher](./319-bulb-switcher) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Breadth (15 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 126 | [Word Ladder II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [126-word-ladder-ii](./126-word-ladder-ii) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 127 | [Word Ladder](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [127-word-ladder](./127-word-ladder) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 279 | [Perfect Squares](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [279-perfect-squares](./279-perfect-squares) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 286 | [Walls and Gates](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [286-walls-and-gates](./286-walls-and-gates) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 301 | [Remove Invalid Parentheses](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [301-remove-invalid-parentheses](./301-remove-invalid-parentheses) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 317 | [Shortest Distance from All Buildings](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [317-shortest-distance-from-all-buildings](./317-shortest-distance-from-all-buildings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 407 | [Trapping Rain Water II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [407-trapping-rain-water-ii](./407-trapping-rain-water-ii) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 433 | [Minimum Genetic Mutation](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [433-minimum-genetic-mutation](./433-minimum-genetic-mutation) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 542 | [01 Matrix](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [542-01-matrix](./542-01-matrix) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 675 | [Cut Off Trees for Golf Event](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [675-cut-off-trees-for-golf-event](./675-cut-off-trees-for-golf-event) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 752 | [Open the Lock](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [752-open-the-lock](./752-open-the-lock) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 773 | [Sliding Puzzle](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [773-sliding-puzzle](./773-sliding-puzzle) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 815 | [Bus Routes](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [815-bus-routes](./815-bus-routes) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 854 | [K-Similar Strings](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [854-k-similar-strings](./854-k-similar-strings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 967 | [Numbers With Same Consecutive Differences](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [967-numbers-with-same-consecutive-differences](./967-numbers-with-same-consecutive-differences) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |

### 📌 Database (44 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 175 | [Combine Two Tables](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [175-combine-two-tables](./175-combine-two-tables) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 176 | [Second Highest Salary](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [176-second-highest-salary](./176-second-highest-salary) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 177 | [Nth Highest Salary](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [177-nth-highest-salary](./177-nth-highest-salary) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 178 | [Rank Scores](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [178-rank-scores](./178-rank-scores) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 180 | [Consecutive Numbers](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [180-consecutive-numbers](./180-consecutive-numbers) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 181 | [Employees Earning More Than Their Managers](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [181-employees-earning-more-than-their-managers](./181-employees-earning-more-than-their-managers) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 182 | [Duplicate Emails](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [182-duplicate-emails](./182-duplicate-emails) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 183 | [Customers Who Never Order](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [183-customers-who-never-order](./183-customers-who-never-order) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 184 | [Department Highest Salary](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [184-department-highest-salary](./184-department-highest-salary) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 185 | [Department Top Three Salaries](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [185-department-top-three-salaries](./185-department-top-three-salaries) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 196 | [Delete Duplicate Emails](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [196-delete-duplicate-emails](./196-delete-duplicate-emails) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 197 | [Rising Temperature](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [197-rising-temperature](./197-rising-temperature) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 262 | [Trips and Users](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [262-trips-and-users](./262-trips-and-users) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 511 | [Game Play Analysis I](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [511-game-play-analysis-i](./511-game-play-analysis-i) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 512 | [Game Play Analysis II](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [512-game-play-analysis-ii](./512-game-play-analysis-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 534 | [Game Play Analysis III](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [534-game-play-analysis-iii](./534-game-play-analysis-iii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 550 | [Game Play Analysis IV](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [550-game-play-analysis-iv](./550-game-play-analysis-iv) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 569 | [Median Employee Salary](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [569-median-employee-salary](./569-median-employee-salary) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 570 | [Managers with at Least 5 Direct Reports](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [570-managers-with-at-least-5-direct-reports](./570-managers-with-at-least-5-direct-reports) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 571 | [Find Median Given Frequency of Numbers](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [571-find-median-given-frequency-of-numbers](./571-find-median-given-frequency-of-numbers) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 574 | [Winning Candidate](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [574-winning-candidate](./574-winning-candidate) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 577 | [Employee Bonus](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [577-employee-bonus](./577-employee-bonus) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 578 | [Get Highest Answer Rate Question](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [578-get-highest-answer-rate-question](./578-get-highest-answer-rate-question) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 579 | [Find Cumulative Salary of an Employee](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [579-find-cumulative-salary-of-an-employee](./579-find-cumulative-salary-of-an-employee) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 580 | [Count Student Number in Departments](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [580-count-student-number-in-departments](./580-count-student-number-in-departments) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 585 | [Investments in 2016](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [585-investments-in-2016](./585-investments-in-2016) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 586 | [Customer Placing the Largest Number of Orders](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [586-customer-placing-the-largest-number-of-orders](./586-customer-placing-the-largest-number-of-orders) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 596 | [Classes With at Least 5 Students](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [596-classes-with-at-least-5-students](./596-classes-with-at-least-5-students) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 597 | [Friend Requests I Overall Acceptance Rate](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [597-friend-requests-i-overall-acceptance-rate](./597-friend-requests-i-overall-acceptance-rate) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 601 | [Human Traffic of Stadium](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [601-human-traffic-of-stadium](./601-human-traffic-of-stadium) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 602 | [Friend Requests II Who Has the Most Friends](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [602-friend-requests-ii-who-has-the-most-friends](./602-friend-requests-ii-who-has-the-most-friends) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 603 | [Consecutive Available Seats](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [603-consecutive-available-seats](./603-consecutive-available-seats) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 607 | [Sales Person](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [607-sales-person](./607-sales-person) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 608 | [Tree Node](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [608-tree-node](./608-tree-node) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 610 | [Triangle Judgement](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [610-triangle-judgement](./610-triangle-judgement) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 612 | [Shortest Distance in a Plane](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [612-shortest-distance-in-a-plane](./612-shortest-distance-in-a-plane) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 613 | [Shortest Distance in a Line](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [613-shortest-distance-in-a-line](./613-shortest-distance-in-a-line) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 614 | [Second Degree Follower](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [614-second-degree-follower](./614-second-degree-follower) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 615 | [Average Salary Departments VS Company](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [615-average-salary-departments-vs-company](./615-average-salary-departments-vs-company) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 618 | [Students Report By Geography](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [618-students-report-by-geography](./618-students-report-by-geography) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 619 | [Biggest Single Number](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [619-biggest-single-number](./619-biggest-single-number) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 620 | [Not Boring Movies](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [620-not-boring-movies](./620-not-boring-movies) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 626 | [Exchange Seats](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [626-exchange-seats](./626-exchange-seats) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 627 | [Swap Sex of Employees](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [627-swap-sex-of-employees](./627-swap-sex-of-employees) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Depth (52 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 130 | [Surrounded Regions](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [130-surrounded-regions](./130-surrounded-regions) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 210 | [Course Schedule II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [210-course-schedule-ii](./210-course-schedule-ii) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 261 | [Graph Valid Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [261-graph-valid-tree](./261-graph-valid-tree) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 269 | [Alien Dictionary](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [269-alien-dictionary](./269-alien-dictionary) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 302 | [Smallest Rectangle Enclosing Black Pixels](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [302-smallest-rectangle-enclosing-black-pixels](./302-smallest-rectangle-enclosing-black-pixels) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 310 | [Minimum Height Trees](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [310-minimum-height-trees](./310-minimum-height-trees) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 323 | [Number of Connected Components in an Undirected Graph](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [323-number-of-connected-components-in-an-undirected-graph](./323-number-of-connected-components-in-an-undirected-graph) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 329 | [Longest Increasing Path in a Matrix](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [329-longest-increasing-path-in-a-matrix](./329-longest-increasing-path-in-a-matrix) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 332 | [Reconstruct Itinerary](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [332-reconstruct-itinerary](./332-reconstruct-itinerary) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 339 | [Nested List Weight Sum](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [339-nested-list-weight-sum](./339-nested-list-weight-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 365 | [Water and Jug Problem](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [365-water-and-jug-problem](./365-water-and-jug-problem) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 386 | [Lexicographical Numbers](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [386-lexicographical-numbers](./386-lexicographical-numbers) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 399 | [Evaluate Division](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [399-evaluate-division](./399-evaluate-division) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 419 | [Battleships in a Board](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [419-battleships-in-a-board](./419-battleships-in-a-board) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 430 | [Flatten a Multilevel Doubly Linked List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [430-flatten-a-multilevel-doubly-linked-list](./430-flatten-a-multilevel-doubly-linked-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 463 | [Island Perimeter](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [463-island-perimeter](./463-island-perimeter) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 472 | [Concatenated Words](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [472-concatenated-words](./472-concatenated-words) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 490 | [The Maze](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [490-the-maze](./490-the-maze) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 499 | [The Maze III](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [499-the-maze-iii](./499-the-maze-iii) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 505 | [The Maze II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [505-the-maze-ii](./505-the-maze-ii) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 514 | [Freedom Trail](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [514-freedom-trail](./514-freedom-trail) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 529 | [Minesweeper](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [529-minesweeper](./529-minesweeper) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 547 | [Number of Provinces](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [547-number-of-provinces](./547-number-of-provinces) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 565 | [Array Nesting](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [565-array-nesting](./565-array-nesting) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 642 | [Design Search Autocomplete System](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [642-design-search-autocomplete-system](./642-design-search-autocomplete-system) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 676 | [Implement Magic Dictionary](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [676-implement-magic-dictionary](./676-implement-magic-dictionary) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 684 | [Redundant Connection](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [684-redundant-connection](./684-redundant-connection) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 685 | [Redundant Connection II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [685-redundant-connection-ii](./685-redundant-connection-ii) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 694 | [Number of Distinct Islands](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [694-number-of-distinct-islands](./694-number-of-distinct-islands) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 695 | [Max Area of Island](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [695-max-area-of-island](./695-max-area-of-island) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 711 | [Number of Distinct Islands II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [711-number-of-distinct-islands-ii](./711-number-of-distinct-islands-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 721 | [Accounts Merge](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [721-accounts-merge](./721-accounts-merge) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 733 | [Flood Fill](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [733-flood-fill](./733-flood-fill) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 737 | [Sentence Similarity II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [737-sentence-similarity-ii](./737-sentence-similarity-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 743 | [Network Delay Time](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [743-network-delay-time](./743-network-delay-time) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 749 | [Contain Virus](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [749-contain-virus](./749-contain-virus) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 753 | [Cracking the Safe](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [753-cracking-the-safe](./753-cracking-the-safe) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 778 | [Swim in Rising Water](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [778-swim-in-rising-water](./778-swim-in-rising-water) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 785 | [Is Graph Bipartite](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [785-is-graph-bipartite](./785-is-graph-bipartite) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 787 | [Cheapest Flights Within K Stops](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [787-cheapest-flights-within-k-stops](./787-cheapest-flights-within-k-stops) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 797 | [All Paths From Source to Target](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [797-all-paths-from-source-to-target](./797-all-paths-from-source-to-target) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 802 | [Find Eventual Safe States](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [802-find-eventual-safe-states](./802-find-eventual-safe-states) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 827 | [Making A Large Island](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [827-making-a-large-island](./827-making-a-large-island) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 839 | [Similar String Groups](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [839-similar-string-groups](./839-similar-string-groups) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 841 | [Keys and Rooms](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [841-keys-and-rooms](./841-keys-and-rooms) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 851 | [Loud and Rich](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [851-loud-and-rich](./851-loud-and-rich) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 886 | [Possible Bipartition](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [886-possible-bipartition](./886-possible-bipartition) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 924 | [Minimize Malware Spread](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [924-minimize-malware-spread](./924-minimize-malware-spread) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 928 | [Minimize Malware Spread II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [928-minimize-malware-spread-ii](./928-minimize-malware-spread-ii) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 934 | [Shortest Bridge](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [934-shortest-bridge](./934-shortest-bridge) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 947 | [Most Stones Removed with Same Row or Column](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [947-most-stones-removed-with-same-row-or-column](./947-most-stones-removed-with-same-row-or-column) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 959 | [Regions Cut By Slashes](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [959-regions-cut-by-slashes](./959-regions-cut-by-slashes) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Design (43 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 170 | [Two Sum III - Data structure design](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [170-two-sum-iii-data-structure-design](./170-two-sum-iii-data-structure-design) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 244 | [Shortest Word Distance II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [244-shortest-word-distance-ii](./244-shortest-word-distance-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 251 | [Flatten 2D Vector](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [251-flatten-2d-vector](./251-flatten-2d-vector) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 271 | [Encode and Decode Strings](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [271-encode-and-decode-strings](./271-encode-and-decode-strings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 281 | [Zigzag Iterator](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [281-zigzag-iterator](./281-zigzag-iterator) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 284 | [Peeking Iterator](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [284-peeking-iterator](./284-peeking-iterator) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 288 | [Unique Word Abbreviation](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [288-unique-word-abbreviation](./288-unique-word-abbreviation) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 303 | [Range Sum Query - Immutable](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [303-range-sum-query-immutable](./303-range-sum-query-immutable) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 304 | [Range Sum Query 2D - Immutable](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [304-range-sum-query-2d-immutable](./304-range-sum-query-2d-immutable) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 307 | [Range Sum Query - Mutable](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [307-range-sum-query-mutable](./307-range-sum-query-mutable) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 308 | [Range Sum Query 2D - Mutable](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [308-range-sum-query-2d-mutable](./308-range-sum-query-2d-mutable) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 346 | [Moving Average from Data Stream](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [346-moving-average-from-data-stream](./346-moving-average-from-data-stream) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 348 | [Design Tic-Tac-Toe](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [348-design-tic-tac-toe](./348-design-tic-tac-toe) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 353 | [Design Snake Game](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [353-design-snake-game](./353-design-snake-game) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 355 | [Design Twitter](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [355-design-twitter](./355-design-twitter) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 359 | [Logger Rate Limiter](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [359-logger-rate-limiter](./359-logger-rate-limiter) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 362 | [Design Hit Counter](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [362-design-hit-counter](./362-design-hit-counter) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 379 | [Design Phone Directory](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [379-design-phone-directory](./379-design-phone-directory) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 380 | [Insert Delete GetRandom O(1)](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [380-insert-delete-getrandom-o-1](./380-insert-delete-getrandom-o-1) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 381 | [Insert Delete GetRandom O(1) - Duplicates allowed](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [381-insert-delete-getrandom-o-1-duplicates-allowed](./381-insert-delete-getrandom-o-1-duplicates-allowed) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 384 | [Shuffle an Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [384-shuffle-an-array](./384-shuffle-an-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 432 | [All O`one Data Structure](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [432-all-o-one-data-structure](./432-all-o-one-data-structure) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 460 | [LFU Cache](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [460-lfu-cache](./460-lfu-cache) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 535 | [Encode and Decode TinyURL](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [535-encode-and-decode-tinyurl](./535-encode-and-decode-tinyurl) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 588 | [Design In-Memory File System](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [588-design-in-memory-file-system](./588-design-in-memory-file-system) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 604 | [Design Compressed String Iterator](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [604-design-compressed-string-iterator](./604-design-compressed-string-iterator) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 622 | [Design Circular Queue](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [622-design-circular-queue](./622-design-circular-queue) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 635 | [Design Log Storage System](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [635-design-log-storage-system](./635-design-log-storage-system) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 641 | [Design Circular Deque](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [641-design-circular-deque](./641-design-circular-deque) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 677 | [Map Sum Pairs](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [677-map-sum-pairs](./677-map-sum-pairs) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 705 | [Design HashSet](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [705-design-hashset](./705-design-hashset) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 706 | [Design HashMap](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [706-design-hashmap](./706-design-hashmap) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 707 | [Design Linked List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [707-design-linked-list](./707-design-linked-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 715 | [Range Module](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [715-range-module](./715-range-module) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 729 | [My Calendar I](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [729-my-calendar-i](./729-my-calendar-i) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 731 | [My Calendar II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [731-my-calendar-ii](./731-my-calendar-ii) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 732 | [My Calendar III](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [732-my-calendar-iii](./732-my-calendar-iii) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 745 | [Prefix and Suffix Search](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [745-prefix-and-suffix-search](./745-prefix-and-suffix-search) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 855 | [Exam Room](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [855-exam-room](./855-exam-room) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 900 | [RLE Iterator](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [900-rle-iterator](./900-rle-iterator) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 911 | [Online Election](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [911-online-election](./911-online-election) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 933 | [Number of Recent Calls](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [933-number-of-recent-calls](./933-number-of-recent-calls) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 981 | [Time Based Key-Value Store](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [981-time-based-key-value-store](./981-time-based-key-value-store) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |

### 📌 Design / Doubly Linked List (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 146 | [LRU Cache](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [146-lru-cache](./146-lru-cache) | $\mathcal{O}(1)$ | $\mathcal{O}(C)$ |

### 📌 Dynamic Programming (10 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 276 | [Paint Fence](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [276-paint-fence](./276-paint-fence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 552 | [Student Attendance Record II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [552-student-attendance-record-ii](./552-student-attendance-record-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 576 | [Out of Boundary Paths](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [576-out-of-boundary-paths](./576-out-of-boundary-paths) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 600 | [Non-negative Integers without Consecutive Ones](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [600-non-negative-integers-without-consecutive-ones](./600-non-negative-integers-without-consecutive-ones) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 629 | [K Inverse Pairs Array](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [629-k-inverse-pairs-array](./629-k-inverse-pairs-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 688 | [Knight Probability in Chessboard](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [688-knight-probability-in-chessboard](./688-knight-probability-in-chessboard) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 790 | [Domino and Tromino Tiling](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [790-domino-and-tromino-tiling](./790-domino-and-tromino-tiling) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 799 | [Champagne Tower](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [799-champagne-tower](./799-champagne-tower) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 818 | [Race Car](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [818-race-car](./818-race-car) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 935 | [Knight Dialer](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [935-knight-dialer](./935-knight-dialer) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Dynamic Programming / Greedy (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 2559 | [Maximum Number of Non-Overlapping Palindrome Substrings](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [2559-maximum-number-of-non-overlapping-palindrome-substrings](./2559-maximum-number-of-non-overlapping-palindrome-substrings) | $\mathcal{O}(N \cdot k)$ | $\mathcal{O}(1)$ |

### 📌 Dynamic Programming / Kadane's Algorithm (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 53 | [Maximum Subarray](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [53-maximum-subarray](./53-maximum-subarray) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Dynamic Programming / Math (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 1013 | [Fibonacci Number](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [1013-fibonacci-number](./1013-fibonacci-number) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Dynamic Programming / Patience Sorting (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 300 | [Longest Increasing Subsequence](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [300-longest-increasing-subsequence](./300-longest-increasing-subsequence) | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |

### 📌 Geometry (16 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 149 | [Max Points on a Line](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [149-max-points-on-a-line](./149-max-points-on-a-line) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 223 | [Rectangle Area](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [223-rectangle-area](./223-rectangle-area) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 335 | [Self Crossing](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [335-self-crossing](./335-self-crossing) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 391 | [Perfect Rectangle](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [391-perfect-rectangle](./391-perfect-rectangle) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 469 | [Convex Polygon](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [469-convex-polygon](./469-convex-polygon) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 478 | [Generate Random Point in a Circle](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [478-generate-random-point-in-a-circle](./478-generate-random-point-in-a-circle) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 587 | [Erect the Fence](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [587-erect-the-fence](./587-erect-the-fence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 593 | [Valid Square](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [593-valid-square](./593-valid-square) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 812 | [Largest Triangle Area](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [812-largest-triangle-area](./812-largest-triangle-area) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 836 | [Rectangle Overlap](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [836-rectangle-overlap](./836-rectangle-overlap) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 858 | [Mirror Reflection](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [858-mirror-reflection](./858-mirror-reflection) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 883 | [Projection Area of 3D Shapes](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [883-projection-area-of-3d-shapes](./883-projection-area-of-3d-shapes) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 892 | [Surface Area of 3D Shapes](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [892-surface-area-of-3d-shapes](./892-surface-area-of-3d-shapes) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 939 | [Minimum Area Rectangle](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [939-minimum-area-rectangle](./939-minimum-area-rectangle) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 963 | [Minimum Area Rectangle II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [963-minimum-area-rectangle-ii](./963-minimum-area-rectangle-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 973 | [K Closest Points to Origin](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [973-k-closest-points-to-origin](./973-k-closest-points-to-origin) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |

### 📌 Graph (5 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 277 | [Find the Celebrity](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [277-find-the-celebrity](./277-find-the-celebrity) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 444 | [Sequence Reconstruction](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [444-sequence-reconstruction](./444-sequence-reconstruction) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 631 | [Design Excel Sum Formula](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [631-design-excel-sum-formula](./631-design-excel-sum-formula) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 882 | [Reachable Nodes In Subdivided Graph](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [882-reachable-nodes-in-subdivided-graph](./882-reachable-nodes-in-subdivided-graph) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 913 | [Cat and Mouse](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [913-cat-and-mouse](./913-cat-and-mouse) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Graph / BFS/DFS (2 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 133 | [Clone Graph](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [133-clone-graph](./133-clone-graph) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 200 | [Number of Islands](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [200-number-of-islands](./200-number-of-islands) | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(M \cdot N)$ |

### 📌 Graph / Multi (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 417 | [Pacific Atlantic Water Flow](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [417-pacific-atlantic-water-flow](./417-pacific-atlantic-water-flow) | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(M \cdot N)$ |

### 📌 Graph / Topological Sort (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 207 | [Course Schedule](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [207-course-schedule](./207-course-schedule) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ |

### 📌 Greedy (60 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 44 | [Wildcard Matching](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [44-wildcard-matching](./44-wildcard-matching) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 45 | [Jump Game II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [45-jump-game-ii](./45-jump-game-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 55 | [Jump Game](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [55-jump-game](./55-jump-game) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 122 | [Best Time to Buy and Sell Stock II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [122-best-time-to-buy-and-sell-stock-ii](./122-best-time-to-buy-and-sell-stock-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 134 | [Gas Station](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [134-gas-station](./134-gas-station) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 135 | [Candy](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [135-candy](./135-candy) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 179 | [Largest Number](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [179-largest-number](./179-largest-number) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 253 | [Meeting Rooms II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [253-meeting-rooms-ii](./253-meeting-rooms-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 280 | [Wiggle Sort](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [280-wiggle-sort](./280-wiggle-sort) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 324 | [Wiggle Sort II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [324-wiggle-sort-ii](./324-wiggle-sort-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 330 | [Patching Array](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [330-patching-array](./330-patching-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 334 | [Increasing Triplet Subsequence](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [334-increasing-triplet-subsequence](./334-increasing-triplet-subsequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 358 | [Rearrange String k Distance Apart](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [358-rearrange-string-k-distance-apart](./358-rearrange-string-k-distance-apart) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 376 | [Wiggle Subsequence](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [376-wiggle-subsequence](./376-wiggle-subsequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 397 | [Integer Replacement](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [397-integer-replacement](./397-integer-replacement) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 410 | [Split Array Largest Sum](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [410-split-array-largest-sum](./410-split-array-largest-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 420 | [Strong Password Checker](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [420-strong-password-checker](./420-strong-password-checker) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 452 | [Minimum Number of Arrows to Burst Balloons](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [452-minimum-number-of-arrows-to-burst-balloons](./452-minimum-number-of-arrows-to-burst-balloons) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 455 | [Assign Cookies](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [455-assign-cookies](./455-assign-cookies) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 502 | [IPO](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [502-ipo](./502-ipo) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 517 | [Super Washing Machines](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [517-super-washing-machines](./517-super-washing-machines) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 527 | [Word Abbreviation](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [527-word-abbreviation](./527-word-abbreviation) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 555 | [Split Concatenated Strings](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [555-split-concatenated-strings](./555-split-concatenated-strings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 561 | [Array Partition](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [561-array-partition](./561-array-partition) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 605 | [Can Place Flowers](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [605-can-place-flowers](./605-can-place-flowers) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 611 | [Valid Triangle Number](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [611-valid-triangle-number](./611-valid-triangle-number) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 621 | [Task Scheduler](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [621-task-scheduler](./621-task-scheduler) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 624 | [Maximum Distance in Arrays](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [624-maximum-distance-in-arrays](./624-maximum-distance-in-arrays) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 625 | [Minimum Factorization](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [625-minimum-factorization](./625-minimum-factorization) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 630 | [Course Schedule III](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [630-course-schedule-iii](./630-course-schedule-iii) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 632 | [Smallest Range Covering Elements from K Lists](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [632-smallest-range-covering-elements-from-k-lists](./632-smallest-range-covering-elements-from-k-lists) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 646 | [Maximum Length of Pair Chain](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [646-maximum-length-of-pair-chain](./646-maximum-length-of-pair-chain) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 649 | [Dota2 Senate](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [649-dota2-senate](./649-dota2-senate) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 659 | [Split Array into Consecutive Subsequences](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [659-split-array-into-consecutive-subsequences](./659-split-array-into-consecutive-subsequences) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 670 | [Maximum Swap](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [670-maximum-swap](./670-maximum-swap) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 680 | [Valid Palindrome II](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [680-valid-palindrome-ii](./680-valid-palindrome-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 714 | [Best Time to Buy and Sell Stock with Transaction Fee](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [714-best-time-to-buy-and-sell-stock-with-transaction-fee](./714-best-time-to-buy-and-sell-stock-with-transaction-fee) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 738 | [Monotone Increasing Digits](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [738-monotone-increasing-digits](./738-monotone-increasing-digits) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 757 | [Set Intersection Size At Least Two](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [757-set-intersection-size-at-least-two](./757-set-intersection-size-at-least-two) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 763 | [Partition Labels](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [763-partition-labels](./763-partition-labels) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 765 | [Couples Holding Hands](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [765-couples-holding-hands](./765-couples-holding-hands) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 767 | [Reorganize String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [767-reorganize-string](./767-reorganize-string) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 781 | [Rabbits in Forest](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [781-rabbits-in-forest](./781-rabbits-in-forest) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 807 | [Max Increase to Keep City Skyline](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [807-max-increase-to-keep-city-skyline](./807-max-increase-to-keep-city-skyline) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 826 | [Most Profit Assigning Work](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [826-most-profit-assigning-work](./826-most-profit-assigning-work) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 846 | [Hand of Straights](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [846-hand-of-straights](./846-hand-of-straights) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 857 | [Minimum Cost to Hire K Workers](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [857-minimum-cost-to-hire-k-workers](./857-minimum-cost-to-hire-k-workers) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 860 | [Lemonade Change](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [860-lemonade-change](./860-lemonade-change) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 861 | [Score After Flipping Matrix](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [861-score-after-flipping-matrix](./861-score-after-flipping-matrix) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 870 | [Advantage Shuffle](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [870-advantage-shuffle](./870-advantage-shuffle) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 871 | [Minimum Number of Refueling Stops](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [871-minimum-number-of-refueling-stops](./871-minimum-number-of-refueling-stops) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 881 | [Boats to Save People](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [881-boats-to-save-people](./881-boats-to-save-people) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 910 | [Smallest Range II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [910-smallest-range-ii](./910-smallest-range-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 942 | [DI String Match](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [942-di-string-match](./942-di-string-match) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 945 | [Minimum Increment to Make Array Unique](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [945-minimum-increment-to-make-array-unique](./945-minimum-increment-to-make-array-unique) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 948 | [Bag of Tokens](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [948-bag-of-tokens](./948-bag-of-tokens) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 954 | [Array of Doubled Pairs](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [954-array-of-doubled-pairs](./954-array-of-doubled-pairs) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 955 | [Delete Columns to Make Sorted II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [955-delete-columns-to-make-sorted-ii](./955-delete-columns-to-make-sorted-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 969 | [Pancake Sorting](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [969-pancake-sorting](./969-pancake-sorting) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 976 | [Largest Perimeter Triangle](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [976-largest-perimeter-triangle](./976-largest-perimeter-triangle) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Greedy / Sorting (2 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 1574 | [Maximum Product of Two Elements in an Array](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [1574-maximum-product-of-two-elements-in-an-array](./1574-maximum-product-of-two-elements-in-an-array) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 2042 | [Maximum Product Difference Between Two Pairs](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [2042-maximum-product-difference-between-two-pairs](./2042-maximum-product-difference-between-two-pairs) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Hash Set / Combinatorics (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 3799 | [Unique 3-Digit Even Numbers](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [3799-unique-3-digit-even-numbers](./3799-unique-3-digit-even-numbers) | $\mathcal{O}(N + 450)$ | $\mathcal{O}(1)$ |

### 📌 Hash Set / Math (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 4080 | [Smallest Missing Multiple of K](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [4080-smallest-missing-multiple-of-k](./4080-smallest-missing-multiple-of-k) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Hash Table (30 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 17 | [Letter Combinations of a Phone Number](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [17-letter-combinations-of-a-phone-number](./17-letter-combinations-of-a-phone-number) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 30 | [Substring with Concatenation of All Words](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [30-substring-with-concatenation-of-all-words](./30-substring-with-concatenation-of-all-words) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 138 | [Copy List with Random Pointer](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [138-copy-list-with-random-pointer](./138-copy-list-with-random-pointer) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 142 | [Linked List Cycle II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [142-linked-list-cycle-ii](./142-linked-list-cycle-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 159 | [Longest Substring with At Most Two Distinct Characters](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [159-longest-substring-with-at-most-two-distinct-characters](./159-longest-substring-with-at-most-two-distinct-characters) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 160 | [Intersection of Two Linked Lists](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [160-intersection-of-two-linked-lists](./160-intersection-of-two-linked-lists) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 166 | [Fraction to Recurring Decimal](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [166-fraction-to-recurring-decimal](./166-fraction-to-recurring-decimal) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 202 | [Happy Number](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [202-happy-number](./202-happy-number) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 205 | [Isomorphic Strings](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [205-isomorphic-strings](./205-isomorphic-strings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 246 | [Strobogrammatic Number](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [246-strobogrammatic-number](./246-strobogrammatic-number) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 264 | [Ugly Number II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [264-ugly-number-ii](./264-ugly-number-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 267 | [Palindrome Permutation II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [267-palindrome-permutation-ii](./267-palindrome-permutation-ii) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 290 | [Word Pattern](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [290-word-pattern](./290-word-pattern) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 291 | [Word Pattern II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [291-word-pattern-ii](./291-word-pattern-ii) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 299 | [Bulls and Cows](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [299-bulls-and-cows](./299-bulls-and-cows) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 340 | [Longest Substring with At Most K Distinct Characters](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [340-longest-substring-with-at-most-k-distinct-characters](./340-longest-substring-with-at-most-k-distinct-characters) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 383 | [Ransom Note](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [383-ransom-note](./383-ransom-note) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 395 | [Longest Substring with At Least K Repeating Characters](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [395-longest-substring-with-at-least-k-repeating-characters](./395-longest-substring-with-at-least-k-repeating-characters) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 423 | [Reconstruct Original Digits from English](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [423-reconstruct-original-digits-from-english](./423-reconstruct-original-digits-from-english) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 438 | [Find All Anagrams in a String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [438-find-all-anagrams-in-a-string](./438-find-all-anagrams-in-a-string) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 451 | [Sort Characters By Frequency](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [451-sort-characters-by-frequency](./451-sort-characters-by-frequency) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 567 | [Permutation in String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [567-permutation-in-string](./567-permutation-in-string) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 681 | [Next Closest Time](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [681-next-closest-time](./681-next-closest-time) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 771 | [Jewels and Stones](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [771-jewels-and-stones](./771-jewels-and-stones) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 791 | [Custom Sort String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [791-custom-sort-string](./791-custom-sort-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 828 | [Count Unique Characters of All Substrings of a Given String](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [828-count-unique-characters-of-all-substrings-of-a-given-string](./828-count-unique-characters-of-all-substrings-of-a-given-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 859 | [Buddy Strings](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [859-buddy-strings](./859-buddy-strings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 869 | [Reordered Power of 2](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [869-reordered-power-of-2](./869-reordered-power-of-2) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 884 | [Uncommon Words from Two Sentences](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [884-uncommon-words-from-two-sentences](./884-uncommon-words-from-two-sentences) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 970 | [Powerful Integers](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [970-powerful-integers](./970-powerful-integers) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Hash Table / Greedy (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 409 | [Longest Palindrome](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [409-longest-palindrome](./409-longest-palindrome) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Heap / Bucket Sort (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 347 | [Top K Frequent Elements](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [347-top-k-frequent-elements](./347-top-k-frequent-elements) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Heap / Priority Queue (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 23 | [Merge k Sorted Lists](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [23-merge-k-sorted-lists](./23-merge-k-sorted-lists) | $\mathcal{O}(N \log k)$ | $\mathcal{O}(k)$ |

### 📌 Heap / QuickSelect (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 215 | [Kth Largest Element in an Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [215-kth-largest-element-in-an-array](./215-kth-largest-element-in-an-array) | $\mathcal{O}(N \log k)$ | $\mathcal{O}(k)$ |

### 📌 Intervals (2 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 56 | [Merge Intervals](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [56-merge-intervals](./56-merge-intervals) | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
| 57 | [Insert Interval](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [57-insert-interval](./57-insert-interval) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Intervals / Greedy (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 435 | [Non-overlapping Intervals](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [435-non-overlapping-intervals](./435-non-overlapping-intervals) | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ |

### 📌 Linked List (17 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 19 | [Remove Nth Node From End of List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [19-remove-nth-node-from-end-of-list](./19-remove-nth-node-from-end-of-list) | $\mathcal{O}(L)$ | $\mathcal{O}(1)$ |
| 21 | [Merge Two Sorted Lists](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [21-merge-two-sorted-lists](./21-merge-two-sorted-lists) | $\mathcal{O}(N + M)$ | $\mathcal{O}(1)$ |
| 61 | [Rotate List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [61-rotate-list](./61-rotate-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 82 | [Remove Duplicates from Sorted List II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [82-remove-duplicates-from-sorted-list-ii](./82-remove-duplicates-from-sorted-list-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 83 | [Remove Duplicates from Sorted List](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [83-remove-duplicates-from-sorted-list](./83-remove-duplicates-from-sorted-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 86 | [Partition List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [86-partition-list](./86-partition-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 92 | [Reverse Linked List II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [92-reverse-linked-list-ii](./92-reverse-linked-list-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 143 | [Reorder List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [143-reorder-list](./143-reorder-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 147 | [Insertion Sort List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [147-insertion-sort-list](./147-insertion-sort-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 148 | [Sort List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [148-sort-list](./148-sort-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 206 | [Reverse Linked List](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [206-reverse-linked-list](./206-reverse-linked-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 237 | [Delete Node in a Linked List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [237-delete-node-in-a-linked-list](./237-delete-node-in-a-linked-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 328 | [Odd Even Linked List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [328-odd-even-linked-list](./328-odd-even-linked-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 369 | [Plus One Linked List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [369-plus-one-linked-list](./369-plus-one-linked-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 708 | [Insert into a Sorted Circular Linked List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [708-insert-into-a-sorted-circular-linked-list](./708-insert-into-a-sorted-circular-linked-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 725 | [Split Linked List in Parts](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [725-split-linked-list-in-parts](./725-split-linked-list-in-parts) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 876 | [Middle of the Linked List](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [876-middle-of-the-linked-list](./876-middle-of-the-linked-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Linked List / Fast %26 Slow Pointers (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 141 | [Linked List Cycle](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [141-linked-list-cycle](./141-linked-list-cycle) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Math (52 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 9 | [Palindrome Number](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [9-palindrome-number](./9-palindrome-number) | $\mathcal{O}(\log_{10}(N))$ | $\mathcal{O}(1)$ |
| 43 | [Multiply Strings](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [43-multiply-strings](./43-multiply-strings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 62 | [Unique Paths](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [62-unique-paths](./62-unique-paths) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 69 | [Sqrt(x)](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [69-sqrt-x](./69-sqrt-x) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 168 | [Excel Sheet Column Title](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [168-excel-sheet-column-title](./168-excel-sheet-column-title) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 171 | [Excel Sheet Column Number](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [171-excel-sheet-column-number](./171-excel-sheet-column-number) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 172 | [Factorial Trailing Zeroes](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [172-factorial-trailing-zeroes](./172-factorial-trailing-zeroes) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 258 | [Add Digits](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [258-add-digits](./258-add-digits) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 263 | [Ugly Number](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [263-ugly-number](./263-ugly-number) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 282 | [Expression Add Operators](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [282-expression-add-operators](./282-expression-add-operators) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 343 | [Integer Break](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [343-integer-break](./343-integer-break) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 357 | [Count Numbers with Unique Digits](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [357-count-numbers-with-unique-digits](./357-count-numbers-with-unique-digits) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 367 | [Valid Perfect Square](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [367-valid-perfect-square](./367-valid-perfect-square) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 372 | [Super Pow](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [372-super-pow](./372-super-pow) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 400 | [Nth Digit](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [400-nth-digit](./400-nth-digit) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 412 | [Fizz Buzz](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [412-fizz-buzz](./412-fizz-buzz) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 415 | [Add Strings](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [415-add-strings](./415-add-strings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 441 | [Arranging Coins](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [441-arranging-coins](./441-arranging-coins) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 458 | [Poor Pigs](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [458-poor-pigs](./458-poor-pigs) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 470 | [Implement Rand10() Using Rand7()](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [470-implement-rand10-using-rand7](./470-implement-rand10-using-rand7) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 479 | [Largest Palindrome Product](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [479-largest-palindrome-product](./479-largest-palindrome-product) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 483 | [Smallest Good Base](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [483-smallest-good-base](./483-smallest-good-base) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 492 | [Construct the Rectangle](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [492-construct-the-rectangle](./492-construct-the-rectangle) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 504 | [Base 7](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [504-base-7](./504-base-7) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 507 | [Perfect Number](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [507-perfect-number](./507-perfect-number) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 537 | [Complex Number Multiplication](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [537-complex-number-multiplication](./537-complex-number-multiplication) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 556 | [Next Greater Element III](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [556-next-greater-element-iii](./556-next-greater-element-iii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 564 | [Find the Closest Palindrome](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [564-find-the-closest-palindrome](./564-find-the-closest-palindrome) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 592 | [Fraction Addition and Subtraction](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [592-fraction-addition-and-subtraction](./592-fraction-addition-and-subtraction) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 633 | [Sum of Square Numbers](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [633-sum-of-square-numbers](./633-sum-of-square-numbers) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 634 | [Find the Derangement of An Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [634-find-the-derangement-of-an-array](./634-find-the-derangement-of-an-array) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 640 | [Solve the Equation](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [640-solve-the-equation](./640-solve-the-equation) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 650 | [2 Keys Keyboard](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [650-2-keys-keyboard](./650-2-keys-keyboard) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 651 | [4 Keys Keyboard](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [651-4-keys-keyboard](./651-4-keys-keyboard) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 660 | [Remove 9](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [660-remove-9](./660-remove-9) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 668 | [Kth Smallest Number in Multiplication Table](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [668-kth-smallest-number-in-multiplication-table](./668-kth-smallest-number-in-multiplication-table) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 728 | [Self Dividing Numbers](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [728-self-dividing-numbers](./728-self-dividing-numbers) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 754 | [Reach a Number](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [754-reach-a-number](./754-reach-a-number) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 780 | [Reaching Points](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [780-reaching-points](./780-reaching-points) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 788 | [Rotated Digits](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [788-rotated-digits](./788-rotated-digits) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 793 | [Preimage Size of Factorial Zeroes Function](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [793-preimage-size-of-factorial-zeroes-function](./793-preimage-size-of-factorial-zeroes-function) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 800 | [Similar RGB Color](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [800-similar-rgb-color](./800-similar-rgb-color) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 808 | [Soup Servings](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [808-soup-servings](./808-soup-servings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 829 | [Consecutive Numbers Sum](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [829-consecutive-numbers-sum](./829-consecutive-numbers-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 837 | [New 21 Game](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [837-new-21-game](./837-new-21-game) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 866 | [Prime Palindrome](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [866-prime-palindrome](./866-prime-palindrome) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 878 | [Nth Magical Number](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [878-nth-magical-number](./878-nth-magical-number) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 887 | [Super Egg Drop](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [887-super-egg-drop](./887-super-egg-drop) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 899 | [Orderly Queue](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [899-orderly-queue](./899-orderly-queue) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 906 | [Super Palindromes](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [906-super-palindromes](./906-super-palindromes) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 920 | [Number of Music Playlists](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [920-number-of-music-playlists](./920-number-of-music-playlists) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 972 | [Equal Rational Numbers](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [972-equal-rational-numbers](./972-equal-rational-numbers) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Math / Bit Manipulation (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 7 | [Reverse Integer](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [7-reverse-integer](./7-reverse-integer) | $\mathcal{O}(\log_{10}(N))$ | $\mathcal{O}(1)$ |

### 📌 Math / Combinatorics (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 4248 | [Count Commas in Range II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [4248-count-commas-in-range-ii](./4248-count-commas-in-range-ii) | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |

### 📌 Math / Digit Counting (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 4245 | [Count Commas in Range](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [4245-count-commas-in-range](./4245-count-commas-in-range) | $\mathcal{O}(\log_{1000}(N))$ | $\mathcal{O}(1)$ |

### 📌 Math / Minimax DP (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 909 | [Stone Game](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [909-stone-game](./909-stone-game) | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |

### 📌 Math / Sorting (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 628 | [Maximum Product of Three Numbers](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [628-maximum-product-of-three-numbers](./628-maximum-product-of-three-numbers) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Matrix (3 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 48 | [Rotate Image](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [48-rotate-image](./48-rotate-image) | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ |
| 54 | [Spiral Matrix](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [54-spiral-matrix](./54-spiral-matrix) | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(1)$ |
| 73 | [Set Matrix Zeroes](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [73-set-matrix-zeroes](./73-set-matrix-zeroes) | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(1)$ |

### 📌 Memoization (3 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 294 | [Flip Game II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [294-flip-game-ii](./294-flip-game-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 546 | [Remove Boxes](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [546-remove-boxes](./546-remove-boxes) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 964 | [Least Operators to Express Number](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [964-least-operators-to-express-number](./964-least-operators-to-express-number) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Minimax (3 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 375 | [Guess Number Higher or Lower II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [375-guess-number-higher-or-lower-ii](./375-guess-number-higher-or-lower-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 843 | [Guess the Word](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [843-guess-the-word](./843-guess-the-word) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 877 | [Stone Game](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [877-stone-game](./877-stone-game) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Monotonic Stack (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 84 | [Largest Rectangle in Histogram](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [84-largest-rectangle-in-histogram](./84-largest-rectangle-in-histogram) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Prefix %26 Suffix Products (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 238 | [Product of Array Except Self](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [238-product-of-array-except-self](./238-product-of-array-except-self) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Queue (5 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 239 | [Sliding Window Maximum](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [239-sliding-window-maximum](./239-sliding-window-maximum) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 387 | [First Unique Character in a String](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [387-first-unique-character-in-a-string](./387-first-unique-character-in-a-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 862 | [Shortest Subarray with Sum at Least K](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [862-shortest-subarray-with-sum-at-least-k](./862-shortest-subarray-with-sum-at-least-k) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 918 | [Maximum Sum Circular Subarray](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [918-maximum-sum-circular-subarray](./918-maximum-sum-circular-subarray) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 950 | [Reveal Cards In Increasing Order](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [950-reveal-cards-in-increasing-order](./950-reveal-cards-in-increasing-order) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Recursion (15 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 24 | [Swap Nodes in Pairs](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [24-swap-nodes-in-pairs](./24-swap-nodes-in-pairs) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 25 | [Reverse Nodes in k-Group](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [25-reverse-nodes-in-k-group](./25-reverse-nodes-in-k-group) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 50 | [Pow(x, n)](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [50-pow-x-n](./50-pow-x-n) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 60 | [Permutation Sequence](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [60-permutation-sequence](./60-permutation-sequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 203 | [Remove Linked List Elements](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [203-remove-linked-list-elements](./203-remove-linked-list-elements) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 233 | [Number of Digit One](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [233-number-of-digit-one](./233-number-of-digit-one) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 241 | [Different Ways to Add Parentheses](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [241-different-ways-to-add-parentheses](./241-different-ways-to-add-parentheses) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 247 | [Strobogrammatic Number II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [247-strobogrammatic-number-ii](./247-strobogrammatic-number-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 248 | [Strobogrammatic Number III](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [248-strobogrammatic-number-iii](./248-strobogrammatic-number-iii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 273 | [Integer to English Words](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [273-integer-to-english-words](./273-integer-to-english-words) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 326 | [Power of Three](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [326-power-of-three](./326-power-of-three) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 390 | [Elimination Game](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [390-elimination-game](./390-elimination-game) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 486 | [Predict the Winner](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [486-predict-the-winner](./486-predict-the-winner) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 509 | [Fibonacci Number](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [509-fibonacci-number](./509-fibonacci-number) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 544 | [Output Contest Matches](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [544-output-contest-matches](./544-output-contest-matches) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Reservoir Sampling (4 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 382 | [Linked List Random Node](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [382-linked-list-random-node](./382-linked-list-random-node) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 398 | [Random Pick Index](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [398-random-pick-index](./398-random-pick-index) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 497 | [Random Point in Non-overlapping Rectangles](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [497-random-point-in-non-overlapping-rectangles](./497-random-point-in-non-overlapping-rectangles) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 519 | [Random Flip Matrix](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [519-random-flip-matrix](./519-random-flip-matrix) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 SQL (5 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 584 | [Find Customer Referee](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [584-find-customer-referee](./584-find-customer-referee) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 595 | [Big Countries](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [595-big-countries](./595-big-countries) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 1258 | [Article Views I](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [1258-article-views-i](./1258-article-views-i) | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
| 1827 | [Invalid Tweets](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [1827-invalid-tweets](./1827-invalid-tweets) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 1908 | [Recyclable and Low Fat Products](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [1908-recyclable-and-low-fat-products](./1908-recyclable-and-low-fat-products) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Segment Tree (2 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 699 | [Falling Squares](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [699-falling-squares](./699-falling-squares) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 850 | [Rectangle Area II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [850-rectangle-area-ii](./850-rectangle-area-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Shell (4 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 192 | [Word Frequency](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [192-word-frequency](./192-word-frequency) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 193 | [Valid Phone Numbers](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [193-valid-phone-numbers](./193-valid-phone-numbers) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 194 | [Transpose File](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [194-transpose-file](./194-transpose-file) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 195 | [Tenth Line](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [195-tenth-line](./195-tenth-line) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Sliding Window (4 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 3 | [Longest Substring Without Repeating Characters](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [3-longest-substring-without-repeating-characters](./3-longest-substring-without-repeating-characters) | $\mathcal{O}(N)$ | $\mathcal{O}(\min(N, M))$ |
| 76 | [Minimum Window Substring](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [76-minimum-window-substring](./76-minimum-window-substring) | $\mathcal{O}(N + M)$ | $\mathcal{O}(N + M)$ |
| 121 | [Best Time to Buy and Sell Stock](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [121-best-time-to-buy-and-sell-stock](./121-best-time-to-buy-and-sell-stock) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 424 | [Longest Repeating Character Replacement](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [424-longest-repeating-character-replacement](./424-longest-repeating-character-replacement) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Stack (65 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 20 | [Valid Parentheses](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [20-valid-parentheses](./20-valid-parentheses) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 32 | [Longest Valid Parentheses](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [32-longest-valid-parentheses](./32-longest-valid-parentheses) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 71 | [Simplify Path](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [71-simplify-path](./71-simplify-path) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 85 | [Maximal Rectangle](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [85-maximal-rectangle](./85-maximal-rectangle) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 94 | [Binary Tree Inorder Traversal](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [94-binary-tree-inorder-traversal](./94-binary-tree-inorder-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 114 | [Flatten Binary Tree to Linked List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [114-flatten-binary-tree-to-linked-list](./114-flatten-binary-tree-to-linked-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 144 | [Binary Tree Preorder Traversal](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [144-binary-tree-preorder-traversal](./144-binary-tree-preorder-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 145 | [Binary Tree Postorder Traversal](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [145-binary-tree-postorder-traversal](./145-binary-tree-postorder-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 150 | [Evaluate Reverse Polish Notation](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [150-evaluate-reverse-polish-notation](./150-evaluate-reverse-polish-notation) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 173 | [Binary Search Tree Iterator](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [173-binary-search-tree-iterator](./173-binary-search-tree-iterator) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 224 | [Basic Calculator](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [224-basic-calculator](./224-basic-calculator) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 225 | [Implement Stack using Queues](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [225-implement-stack-using-queues](./225-implement-stack-using-queues) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 227 | [Basic Calculator II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [227-basic-calculator-ii](./227-basic-calculator-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 232 | [Implement Queue using Stacks](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [232-implement-queue-using-stacks](./232-implement-queue-using-stacks) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 234 | [Palindrome Linked List](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [234-palindrome-linked-list](./234-palindrome-linked-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 255 | [Verify Preorder Sequence in Binary Search Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [255-verify-preorder-sequence-in-binary-search-tree](./255-verify-preorder-sequence-in-binary-search-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 272 | [Closest Binary Search Tree Value II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [272-closest-binary-search-tree-value-ii](./272-closest-binary-search-tree-value-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 316 | [Remove Duplicate Letters](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [316-remove-duplicate-letters](./316-remove-duplicate-letters) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 321 | [Create Maximum Number](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [321-create-maximum-number](./321-create-maximum-number) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 331 | [Verify Preorder Serialization of a Binary Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [331-verify-preorder-serialization-of-a-binary-tree](./331-verify-preorder-serialization-of-a-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 341 | [Flatten Nested List Iterator](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [341-flatten-nested-list-iterator](./341-flatten-nested-list-iterator) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 364 | [Nested List Weight Sum II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [364-nested-list-weight-sum-ii](./364-nested-list-weight-sum-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 385 | [Mini Parser](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [385-mini-parser](./385-mini-parser) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 388 | [Longest Absolute File Path](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [388-longest-absolute-file-path](./388-longest-absolute-file-path) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 394 | [Decode String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [394-decode-string](./394-decode-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 402 | [Remove K Digits](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [402-remove-k-digits](./402-remove-k-digits) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 426 | [Convert Binary Search Tree to Sorted Doubly Linked List](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [426-convert-binary-search-tree-to-sorted-doubly-linked-list](./426-convert-binary-search-tree-to-sorted-doubly-linked-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 439 | [Ternary Expression Parser](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [439-ternary-expression-parser](./439-ternary-expression-parser) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 445 | [Add Two Numbers II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [445-add-two-numbers-ii](./445-add-two-numbers-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 456 | [132 Pattern](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [456-132-pattern](./456-132-pattern) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 484 | [Find Permutation](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [484-find-permutation](./484-find-permutation) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 488 | [Zuma Game](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [488-zuma-game](./488-zuma-game) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 496 | [Next Greater Element I](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [496-next-greater-element-i](./496-next-greater-element-i) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 503 | [Next Greater Element II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [503-next-greater-element-ii](./503-next-greater-element-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 536 | [Construct Binary Tree from String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [536-construct-binary-tree-from-string](./536-construct-binary-tree-from-string) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 581 | [Shortest Unsorted Continuous Subarray](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [581-shortest-unsorted-continuous-subarray](./581-shortest-unsorted-continuous-subarray) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 589 | [N-ary Tree Preorder Traversal](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [589-n-ary-tree-preorder-traversal](./589-n-ary-tree-preorder-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 590 | [N-ary Tree Postorder Traversal](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [590-n-ary-tree-postorder-traversal](./590-n-ary-tree-postorder-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 591 | [Tag Validator](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [591-tag-validator](./591-tag-validator) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 636 | [Exclusive Time of Functions](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [636-exclusive-time-of-functions](./636-exclusive-time-of-functions) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 654 | [Maximum Binary Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [654-maximum-binary-tree](./654-maximum-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 678 | [Valid Parenthesis String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [678-valid-parenthesis-string](./678-valid-parenthesis-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 682 | [Baseball Game](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [682-baseball-game](./682-baseball-game) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 716 | [Max Stack](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [716-max-stack](./716-max-stack) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 726 | [Number of Atoms](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [726-number-of-atoms](./726-number-of-atoms) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 735 | [Asteroid Collision](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [735-asteroid-collision](./735-asteroid-collision) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 736 | [Parse Lisp Expression](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [736-parse-lisp-expression](./736-parse-lisp-expression) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 739 | [Daily Temperatures](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [739-daily-temperatures](./739-daily-temperatures) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 768 | [Max Chunks To Make Sorted II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [768-max-chunks-to-make-sorted-ii](./768-max-chunks-to-make-sorted-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 769 | [Max Chunks To Make Sorted](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [769-max-chunks-to-make-sorted](./769-max-chunks-to-make-sorted) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 770 | [Basic Calculator IV](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [770-basic-calculator-iv](./770-basic-calculator-iv) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 772 | [Basic Calculator III](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [772-basic-calculator-iii](./772-basic-calculator-iii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 844 | [Backspace String Compare](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [844-backspace-string-compare](./844-backspace-string-compare) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 853 | [Car Fleet](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [853-car-fleet](./853-car-fleet) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 856 | [Score of Parentheses](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [856-score-of-parentheses](./856-score-of-parentheses) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 880 | [Decoded String at Index](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [880-decoded-string-at-index](./880-decoded-string-at-index) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 895 | [Maximum Frequency Stack](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [895-maximum-frequency-stack](./895-maximum-frequency-stack) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 897 | [Increasing Order Search Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [897-increasing-order-search-tree](./897-increasing-order-search-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 901 | [Online Stock Span](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [901-online-stock-span](./901-online-stock-span) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 907 | [Sum of Subarray Minimums](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [907-sum-of-subarray-minimums](./907-sum-of-subarray-minimums) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 921 | [Minimum Add to Make Parentheses Valid](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [921-minimum-add-to-make-parentheses-valid](./921-minimum-add-to-make-parentheses-valid) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 936 | [Stamping The Sequence](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [936-stamping-the-sequence](./936-stamping-the-sequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 946 | [Validate Stack Sequences](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [946-validate-stack-sequences](./946-validate-stack-sequences) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 962 | [Maximum Width Ramp](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [962-maximum-width-ramp](./962-maximum-width-ramp) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 975 | [Odd Even Jump](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [975-odd-even-jump](./975-odd-even-jump) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Stack Design (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 155 | [Min Stack](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [155-min-stack](./155-min-stack) | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |

### 📌 String (44 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 22 | [Generate Parentheses](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [22-generate-parentheses](./22-generate-parentheses) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 38 | [Count and Say](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [38-count-and-say](./38-count-and-say) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 58 | [Length of Last Word](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [58-length-of-last-word](./58-length-of-last-word) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 65 | [Valid Number](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [65-valid-number](./65-valid-number) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 72 | [Edit Distance](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [72-edit-distance](./72-edit-distance) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 87 | [Scramble String](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [87-scramble-string](./87-scramble-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 91 | [Decode Ways](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [91-decode-ways](./91-decode-ways) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 93 | [Restore IP Addresses](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [93-restore-ip-addresses](./93-restore-ip-addresses) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 97 | [Interleaving String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [97-interleaving-string](./97-interleaving-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 115 | [Distinct Subsequences](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [115-distinct-subsequences](./115-distinct-subsequences) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 131 | [Palindrome Partitioning](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [131-palindrome-partitioning](./131-palindrome-partitioning) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 132 | [Palindrome Partitioning II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [132-palindrome-partitioning-ii](./132-palindrome-partitioning-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 214 | [Shortest Palindrome](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [214-shortest-palindrome](./214-shortest-palindrome) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 293 | [Flip Game](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [293-flip-game](./293-flip-game) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 306 | [Additive Number](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [306-additive-number](./306-additive-number) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 434 | [Number of Segments in a String](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [434-number-of-segments-in-a-string](./434-number-of-segments-in-a-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 459 | [Repeated Substring Pattern](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [459-repeated-substring-pattern](./459-repeated-substring-pattern) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 467 | [Unique Substrings in Wraparound String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [467-unique-substrings-in-wraparound-string](./467-unique-substrings-in-wraparound-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 468 | [Validate IP Address](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [468-validate-ip-address](./468-validate-ip-address) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 471 | [Encode String with Shortest Length](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [471-encode-string-with-shortest-length](./471-encode-string-with-shortest-length) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 482 | [License Key Formatting](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [482-license-key-formatting](./482-license-key-formatting) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 516 | [Longest Palindromic Subsequence](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [516-longest-palindromic-subsequence](./516-longest-palindromic-subsequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 520 | [Detect Capital](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [520-detect-capital](./520-detect-capital) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 521 | [Longest Uncommon Subsequence I](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [521-longest-uncommon-subsequence-i](./521-longest-uncommon-subsequence-i) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 551 | [Student Attendance Record I](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [551-student-attendance-record-i](./551-student-attendance-record-i) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 583 | [Delete Operation for Two Strings](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [583-delete-operation-for-two-strings](./583-delete-operation-for-two-strings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 639 | [Decode Ways II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [639-decode-ways-ii](./639-decode-ways-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 657 | [Robot Return to Origin](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [657-robot-return-to-origin](./657-robot-return-to-origin) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 664 | [Strange Printer](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [664-strange-printer](./664-strange-printer) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 686 | [Repeated String Match](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [686-repeated-string-match](./686-repeated-string-match) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 709 | [To Lower Case](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [709-to-lower-case](./709-to-lower-case) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 712 | [Minimum ASCII Delete Sum for Two Strings](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [712-minimum-ascii-delete-sum-for-two-strings](./712-minimum-ascii-delete-sum-for-two-strings) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 727 | [Minimum Window Subsequence](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [727-minimum-window-subsequence](./727-minimum-window-subsequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 730 | [Count Different Palindromic Subsequences](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [730-count-different-palindromic-subsequences](./730-count-different-palindromic-subsequences) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 761 | [Special Binary String](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [761-special-binary-string](./761-special-binary-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 796 | [Rotate String](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [796-rotate-string](./796-rotate-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 816 | [Ambiguous Coordinates](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [816-ambiguous-coordinates](./816-ambiguous-coordinates) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 824 | [Goat Latin](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [824-goat-latin](./824-goat-latin) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 830 | [Positions of Large Groups](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [830-positions-of-large-groups](./830-positions-of-large-groups) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 831 | [Masking Personal Information](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [831-masking-personal-information](./831-masking-personal-information) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 842 | [Split Array into Fibonacci Sequence](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [842-split-array-into-fibonacci-sequence](./842-split-array-into-fibonacci-sequence) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 903 | [Valid Permutations for DI Sequence](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [903-valid-permutations-for-di-sequence](./903-valid-permutations-for-di-sequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 926 | [Flip String to Monotone Increasing](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [926-flip-string-to-monotone-increasing](./926-flip-string-to-monotone-increasing) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 940 | [Distinct Subsequences II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [940-distinct-subsequences-ii](./940-distinct-subsequences-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Tree (87 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 95 | [Unique Binary Search Trees II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [95-unique-binary-search-trees-ii](./95-unique-binary-search-trees-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 96 | [Unique Binary Search Trees](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [96-unique-binary-search-trees](./96-unique-binary-search-trees) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 99 | [Recover Binary Search Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [99-recover-binary-search-tree](./99-recover-binary-search-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 101 | [Symmetric Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [101-symmetric-tree](./101-symmetric-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 103 | [Binary Tree Zigzag Level Order Traversal](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [103-binary-tree-zigzag-level-order-traversal](./103-binary-tree-zigzag-level-order-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 106 | [Construct Binary Tree from Inorder and Postorder Traversal](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [106-construct-binary-tree-from-inorder-and-postorder-traversal](./106-construct-binary-tree-from-inorder-and-postorder-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 107 | [Binary Tree Level Order Traversal II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [107-binary-tree-level-order-traversal-ii](./107-binary-tree-level-order-traversal-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 108 | [Convert Sorted Array to Binary Search Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [108-convert-sorted-array-to-binary-search-tree](./108-convert-sorted-array-to-binary-search-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 109 | [Convert Sorted List to Binary Search Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [109-convert-sorted-list-to-binary-search-tree](./109-convert-sorted-list-to-binary-search-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 110 | [Balanced Binary Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [110-balanced-binary-tree](./110-balanced-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 111 | [Minimum Depth of Binary Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [111-minimum-depth-of-binary-tree](./111-minimum-depth-of-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 112 | [Path Sum](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [112-path-sum](./112-path-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 113 | [Path Sum II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [113-path-sum-ii](./113-path-sum-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 116 | [Populating Next Right Pointers in Each Node](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [116-populating-next-right-pointers-in-each-node](./116-populating-next-right-pointers-in-each-node) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 117 | [Populating Next Right Pointers in Each Node II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [117-populating-next-right-pointers-in-each-node-ii](./117-populating-next-right-pointers-in-each-node-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 129 | [Sum Root to Leaf Numbers](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [129-sum-root-to-leaf-numbers](./129-sum-root-to-leaf-numbers) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 156 | [Binary Tree Upside Down](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [156-binary-tree-upside-down](./156-binary-tree-upside-down) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 199 | [Binary Tree Right Side View](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [199-binary-tree-right-side-view](./199-binary-tree-right-side-view) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 236 | [Lowest Common Ancestor of a Binary Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [236-lowest-common-ancestor-of-a-binary-tree](./236-lowest-common-ancestor-of-a-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 250 | [Count Univalue Subtrees](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [250-count-univalue-subtrees](./250-count-univalue-subtrees) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 257 | [Binary Tree Paths](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [257-binary-tree-paths](./257-binary-tree-paths) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 270 | [Closest Binary Search Tree Value](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [270-closest-binary-search-tree-value](./270-closest-binary-search-tree-value) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 285 | [Inorder Successor in BST](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [285-inorder-successor-in-bst](./285-inorder-successor-in-bst) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 297 | [Serialize and Deserialize Binary Tree](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [297-serialize-and-deserialize-binary-tree](./297-serialize-and-deserialize-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 298 | [Binary Tree Longest Consecutive Sequence](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [298-binary-tree-longest-consecutive-sequence](./298-binary-tree-longest-consecutive-sequence) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 314 | [Binary Tree Vertical Order Traversal](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [314-binary-tree-vertical-order-traversal](./314-binary-tree-vertical-order-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 333 | [Largest BST Subtree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [333-largest-bst-subtree](./333-largest-bst-subtree) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 337 | [House Robber III](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [337-house-robber-iii](./337-house-robber-iii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 366 | [Find Leaves of Binary Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [366-find-leaves-of-binary-tree](./366-find-leaves-of-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 404 | [Sum of Left Leaves](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [404-sum-of-left-leaves](./404-sum-of-left-leaves) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 427 | [Construct Quad Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [427-construct-quad-tree](./427-construct-quad-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 428 | [Serialize and Deserialize N-ary Tree](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [428-serialize-and-deserialize-n-ary-tree](./428-serialize-and-deserialize-n-ary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 429 | [N-ary Tree Level Order Traversal](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [429-n-ary-tree-level-order-traversal](./429-n-ary-tree-level-order-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 431 | [Encode N-ary Tree to Binary Tree](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [431-encode-n-ary-tree-to-binary-tree](./431-encode-n-ary-tree-to-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 437 | [Path Sum III](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [437-path-sum-iii](./437-path-sum-iii) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 449 | [Serialize and Deserialize BST](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [449-serialize-and-deserialize-bst](./449-serialize-and-deserialize-bst) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 450 | [Delete Node in a BST](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [450-delete-node-in-a-bst](./450-delete-node-in-a-bst) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 501 | [Find Mode in Binary Search Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [501-find-mode-in-binary-search-tree](./501-find-mode-in-binary-search-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 508 | [Most Frequent Subtree Sum](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [508-most-frequent-subtree-sum](./508-most-frequent-subtree-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 510 | [Inorder Successor in BST II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [510-inorder-successor-in-bst-ii](./510-inorder-successor-in-bst-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 513 | [Find Bottom Left Tree Value](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [513-find-bottom-left-tree-value](./513-find-bottom-left-tree-value) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 515 | [Find Largest Value in Each Tree Row](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [515-find-largest-value-in-each-tree-row](./515-find-largest-value-in-each-tree-row) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 530 | [Minimum Absolute Difference in BST](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [530-minimum-absolute-difference-in-bst](./530-minimum-absolute-difference-in-bst) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 538 | [Convert BST to Greater Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [538-convert-bst-to-greater-tree](./538-convert-bst-to-greater-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 543 | [Diameter of Binary Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [543-diameter-of-binary-tree](./543-diameter-of-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 545 | [Boundary of Binary Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [545-boundary-of-binary-tree](./545-boundary-of-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 549 | [Binary Tree Longest Consecutive Sequence II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [549-binary-tree-longest-consecutive-sequence-ii](./549-binary-tree-longest-consecutive-sequence-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 558 | [Logical OR of Two Binary Grids Represented as Quad-Trees](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [558-logical-or-of-two-binary-grids-represented-as-quad-trees](./558-logical-or-of-two-binary-grids-represented-as-quad-trees) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 559 | [Maximum Depth of N-ary Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [559-maximum-depth-of-n-ary-tree](./559-maximum-depth-of-n-ary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 563 | [Binary Tree Tilt](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [563-binary-tree-tilt](./563-binary-tree-tilt) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 572 | [Subtree of Another Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [572-subtree-of-another-tree](./572-subtree-of-another-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 582 | [Kill Process](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [582-kill-process](./582-kill-process) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 606 | [Construct String from Binary Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [606-construct-string-from-binary-tree](./606-construct-string-from-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 617 | [Merge Two Binary Trees](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [617-merge-two-binary-trees](./617-merge-two-binary-trees) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 623 | [Add One Row to Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [623-add-one-row-to-tree](./623-add-one-row-to-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 637 | [Average of Levels in Binary Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [637-average-of-levels-in-binary-tree](./637-average-of-levels-in-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 652 | [Find Duplicate Subtrees](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [652-find-duplicate-subtrees](./652-find-duplicate-subtrees) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 653 | [Two Sum IV - Input is a BST](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [653-two-sum-iv-input-is-a-bst](./653-two-sum-iv-input-is-a-bst) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 655 | [Print Binary Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [655-print-binary-tree](./655-print-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 662 | [Maximum Width of Binary Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [662-maximum-width-of-binary-tree](./662-maximum-width-of-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 663 | [Equal Tree Partition](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [663-equal-tree-partition](./663-equal-tree-partition) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 666 | [Path Sum IV](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [666-path-sum-iv](./666-path-sum-iv) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 669 | [Trim a Binary Search Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [669-trim-a-binary-search-tree](./669-trim-a-binary-search-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 671 | [Second Minimum Node In a Binary Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [671-second-minimum-node-in-a-binary-tree](./671-second-minimum-node-in-a-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 687 | [Longest Univalue Path](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [687-longest-univalue-path](./687-longest-univalue-path) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 690 | [Employee Importance](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [690-employee-importance](./690-employee-importance) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 700 | [Search in a Binary Search Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [700-search-in-a-binary-search-tree](./700-search-in-a-binary-search-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 701 | [Insert into a Binary Search Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [701-insert-into-a-binary-search-tree](./701-insert-into-a-binary-search-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 703 | [Kth Largest Element in a Stream](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [703-kth-largest-element-in-a-stream](./703-kth-largest-element-in-a-stream) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 742 | [Closest Leaf in a Binary Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [742-closest-leaf-in-a-binary-tree](./742-closest-leaf-in-a-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 776 | [Split BST](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [776-split-bst](./776-split-bst) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 783 | [Minimum Distance Between BST Nodes](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [783-minimum-distance-between-bst-nodes](./783-minimum-distance-between-bst-nodes) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 814 | [Binary Tree Pruning](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [814-binary-tree-pruning](./814-binary-tree-pruning) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 834 | [Sum of Distances in Tree](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [834-sum-of-distances-in-tree](./834-sum-of-distances-in-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 863 | [All Nodes Distance K in Binary Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [863-all-nodes-distance-k-in-binary-tree](./863-all-nodes-distance-k-in-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 865 | [Smallest Subtree with all the Deepest Nodes](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [865-smallest-subtree-with-all-the-deepest-nodes](./865-smallest-subtree-with-all-the-deepest-nodes) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 872 | [Leaf-Similar Trees](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [872-leaf-similar-trees](./872-leaf-similar-trees) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 889 | [Construct Binary Tree from Preorder and Postorder Traversal](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [889-construct-binary-tree-from-preorder-and-postorder-traversal](./889-construct-binary-tree-from-preorder-and-postorder-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 894 | [All Possible Full Binary Trees](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [894-all-possible-full-binary-trees](./894-all-possible-full-binary-trees) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 919 | [Complete Binary Tree Inserter](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [919-complete-binary-tree-inserter](./919-complete-binary-tree-inserter) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 938 | [Range Sum of BST](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [938-range-sum-of-bst](./938-range-sum-of-bst) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 951 | [Flip Equivalent Binary Trees](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [951-flip-equivalent-binary-trees](./951-flip-equivalent-binary-trees) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 958 | [Check Completeness of a Binary Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [958-check-completeness-of-a-binary-tree](./958-check-completeness-of-a-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 965 | [Univalued Binary Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [965-univalued-binary-tree](./965-univalued-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 968 | [Binary Tree Cameras](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [968-binary-tree-cameras](./968-binary-tree-cameras) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 971 | [Flip Binary Tree To Match Preorder Traversal](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [971-flip-binary-tree-to-match-preorder-traversal](./971-flip-binary-tree-to-match-preorder-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 979 | [Distribute Coins in Binary Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [979-distribute-coins-in-binary-tree](./979-distribute-coins-in-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |

### 📌 Tree / BFS (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 102 | [Binary Tree Level Order Traversal](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [102-binary-tree-level-order-traversal](./102-binary-tree-level-order-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Tree / BST (2 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 98 | [Validate Binary Search Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [98-validate-binary-search-tree](./98-validate-binary-search-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 235 | [Lowest Common Ancestor of a Binary Search Tree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [235-lowest-common-ancestor-of-a-binary-search-tree](./235-lowest-common-ancestor-of-a-binary-search-tree) | $\mathcal{O}(H)$ | $\mathcal{O}(1)$ |

### 📌 Tree / BST Inorder (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 230 | [Kth Smallest Element in a BST](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [230-kth-smallest-element-in-a-bst](./230-kth-smallest-element-in-a-bst) | $\mathcal{O}(H + k)$ | $\mathcal{O}(H)$ |

### 📌 Tree / DFS (2 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 100 | [Same Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [100-same-tree](./100-same-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 104 | [Maximum Depth of Binary Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [104-maximum-depth-of-binary-tree](./104-maximum-depth-of-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |

### 📌 Tree / Divide %26 Conquer (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [105-construct-binary-tree-from-preorder-and-inorder-traversal](./105-construct-binary-tree-from-preorder-and-inorder-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Tree / Post (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 124 | [Binary Tree Maximum Path Sum](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [124-binary-tree-maximum-path-sum](./124-binary-tree-maximum-path-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |

### 📌 Tree / Postorder DFS (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 2347 | [Count Nodes Equal to Average of Subtree](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [2347-count-nodes-equal-to-average-of-subtree](./2347-count-nodes-equal-to-average-of-subtree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |

### 📌 Tree / Recursion (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 226 | [Invert Binary Tree](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [226-invert-binary-tree](./226-invert-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |

### 📌 Trie (12 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 140 | [Word Break II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [140-word-break-ii](./140-word-break-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 208 | [Implement Trie (Prefix Tree)](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [208-implement-trie-prefix-tree](./208-implement-trie-prefix-tree) | $\mathcal{O}(L)$ | $\mathcal{O}(N \cdot L)$ |
| 336 | [Palindrome Pairs](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [336-palindrome-pairs](./336-palindrome-pairs) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 425 | [Word Squares](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [425-word-squares](./425-word-squares) | $\mathcal{O}(2^N \text{ or } N!)$ | $\mathcal{O}(N)$ |
| 440 | [K-th Smallest in Lexicographical Order](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [440-k-th-smallest-in-lexicographical-order](./440-k-th-smallest-in-lexicographical-order) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 616 | [Add Bold Tag in String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [616-add-bold-tag-in-string](./616-add-bold-tag-in-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 648 | [Replace Words](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [648-replace-words](./648-replace-words) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 692 | [Top K Frequent Words](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [692-top-k-frequent-words](./692-top-k-frequent-words) | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| 720 | [Longest Word in Dictionary](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [720-longest-word-in-dictionary](./720-longest-word-in-dictionary) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 758 | [Bold Words in String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [758-bold-words-in-string](./758-bold-words-in-string) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 792 | [Number of Matching Subsequences](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [792-number-of-matching-subsequences](./792-number-of-matching-subsequences) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 820 | [Short Encoding of Words](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [820-short-encoding-of-words](./820-short-encoding-of-words) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Trie + Backtracking (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 212 | [Word Search II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [212-word-search-ii](./212-word-search-ii) | $\mathcal{O}(M \cdot N \cdot 4^{L})$ | $\mathcal{O}(W \cdot L)$ |

### 📌 Trie / DFS (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 211 | [Design Add and Search Words Data Structure](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [211-design-add-and-search-words-data-structure](./211-design-add-and-search-words-data-structure) | $\mathcal{O}(M)$ | $\mathcal{O}(N \cdot M)$ |

### 📌 Two Heaps (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 295 | [Find Median from Data Stream](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [295-find-median-from-data-stream](./295-find-median-from-data-stream) | $\mathcal{O}(\log N)$ | $\mathcal{O}(N)$ |

### 📌 Two Pointers (28 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 11 | [Container With Most Water](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [11-container-with-most-water](./11-container-with-most-water) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 15 | [3Sum](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [15-3sum](./15-3sum) | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ |
| 26 | [Remove Duplicates from Sorted Array](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [26-remove-duplicates-from-sorted-array](./26-remove-duplicates-from-sorted-array) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 28 | [Find the Index of the First Occurrence in a String](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [28-find-the-index-of-the-first-occurrence-in-a-string](./28-find-the-index-of-the-first-occurrence-in-a-string) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 31 | [Next Permutation](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [31-next-permutation](./31-next-permutation) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 42 | [Trapping Rain Water](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [42-trapping-rain-water](./42-trapping-rain-water) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 75 | [Sort Colors](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [75-sort-colors](./75-sort-colors) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 125 | [Valid Palindrome](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [125-valid-palindrome](./125-valid-palindrome) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 151 | [Reverse Words in a String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [151-reverse-words-in-a-string](./151-reverse-words-in-a-string) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 161 | [One Edit Distance](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [161-one-edit-distance](./161-one-edit-distance) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 165 | [Compare Version Numbers](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [165-compare-version-numbers](./165-compare-version-numbers) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 186 | [Reverse Words in a String II](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [186-reverse-words-in-a-string-ii](./186-reverse-words-in-a-string-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 189 | [Rotate Array](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [189-rotate-array](./189-rotate-array) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 283 | [Move Zeroes](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [283-move-zeroes](./283-move-zeroes) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 344 | [Reverse String](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [344-reverse-string](./344-reverse-string) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 345 | [Reverse Vowels of a String](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [345-reverse-vowels-of-a-string](./345-reverse-vowels-of-a-string) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 392 | [Is Subsequence](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [392-is-subsequence](./392-is-subsequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 408 | [Valid Word Abbreviation](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [408-valid-word-abbreviation](./408-valid-word-abbreviation) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 443 | [String Compression](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [443-string-compression](./443-string-compression) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 466 | [Count The Repetitions](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [466-count-the-repetitions](./466-count-the-repetitions) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 481 | [Magical String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [481-magical-string](./481-magical-string) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 541 | [Reverse String II](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [541-reverse-string-ii](./541-reverse-string-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 557 | [Reverse Words in a String III](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [557-reverse-words-in-a-string-iii](./557-reverse-words-in-a-string-iii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 696 | [Count Binary Substrings](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [696-count-binary-substrings](./696-count-binary-substrings) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 777 | [Swap Adjacent in LR String](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [777-swap-adjacent-in-lr-string](./777-swap-adjacent-in-lr-string) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 838 | [Push Dominoes](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [838-push-dominoes](./838-push-dominoes) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 917 | [Reverse Only Letters](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [917-reverse-only-letters](./917-reverse-only-letters) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 925 | [Long Pressed Name](https://img.shields.io/badge/Difficulty-Easy-brightgreen) | `Easy` | [925-long-pressed-name](./925-long-pressed-name) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Two Pointers / Arrays (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 2271 | [Rearrange Array Elements by Sign](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [2271-rearrange-array-elements-by-sign](./2271-rearrange-array-elements-by-sign) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Two Pointers / DP (1 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 647 | [Palindromic Substrings](https://img.shields.io/badge/Difficulty-Medium-orange) | `Medium` | [647-palindromic-substrings](./647-palindromic-substrings) | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ |

### 📌 Union Find (4 problems)

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 305 | [Number of Islands II](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [305-number-of-islands-ii](./305-number-of-islands-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 352 | [Data Stream as Disjoint Intervals](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [352-data-stream-as-disjoint-intervals](./352-data-stream-as-disjoint-intervals) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 803 | [Bricks Falling When Hit](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [803-bricks-falling-when-hit](./803-bricks-falling-when-hit) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 952 | [Largest Component Size by Common Factor](https://img.shields.io/badge/Difficulty-Hard-red) | `Hard` | [952-largest-component-size-by-common-factor](./952-largest-component-size-by-common-factor) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
