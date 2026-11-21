# 🚀 100 LeetCode Questions: Intuitive Explanations & Optimal Solutions

<div align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Graduation%20Cap.png" width="45" height="45" alt="Graduation Cap" />
  <p><strong>A curated repository of 100 essential LeetCode interview questions explained from first principles.</strong></p>
  <p>Each solution is tailored exactly to <em>how you would explain the problem to an interviewer</em>: the 30-second conversational pitch, core intuition, visual dry-run traces, edge cases, follow-up questions, and clean, production-ready solutions in both <strong>Java</strong> and <strong>Python 3</strong>.</p>

  <p>
    <img src="https://img.shields.io/badge/Total%20Problems-100-blue?style=for-the-badge" alt="Total Problems: 100" />
    <img src="https://img.shields.io/badge/Easy-37-brightgreen?style=for-the-badge" alt="Easy" />
    <img src="https://img.shields.io/badge/Medium-55-orange?style=for-the-badge" alt="Medium" />
    <img src="https://img.shields.io/badge/Hard-8-red?style=for-the-badge" alt="Hard" />
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

### 📌 1D Dynamic Programming

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | `Easy` | [70-climbing-stairs](./70-climbing-stairs) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 139 | [Word Break](https://leetcode.com/problems/word-break/) | `Medium` | [139-word-break](./139-word-break) | $\mathcal{O}(N^2 \cdot L)$ | $\mathcal{O}(N + M)$ |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | `Medium` | [152-maximum-product-subarray](./152-maximum-product-subarray) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | `Medium` | [198-house-robber](./198-house-robber) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | `Medium` | [322-coin-change](./322-coin-change) | $\mathcal{O}(A \cdot C)$ | $\mathcal{O}(A)$ |

### 📌 1D Dynamic Programming / Circular

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 213 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | `Medium` | [213-house-robber-ii](./213-house-robber-ii) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 2D Dynamic Programming

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 1143 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | `Medium` | [1143-longest-common-subsequence](./1143-longest-common-subsequence) | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(\min(M, N))$ |

### 📌 Arrays

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 485 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | `Easy` | [485-max-consecutive-ones](./485-max-consecutive-ones) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 1878 | [Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) | `Easy` | [1878-check-if-array-is-sorted-and-rotated](./1878-check-if-array-is-sorted-and-rotated) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Arrays & Hashing

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | `Easy` | [1-two-sum](./1-two-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | `Medium` | [49-group-anagrams](./49-group-anagrams) | $\mathcal{O}(N \cdot K \log K)$ | $\mathcal{O}(N \cdot K)$ |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | `Medium` | [128-longest-consecutive-sequence](./128-longest-consecutive-sequence) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | `Easy` | [217-contains-duplicate](./217-contains-duplicate) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | `Easy` | [242-valid-anagram](./242-valid-anagram) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Arrays / Math

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 4256 | [Construct Uniform Parity Array I](https://leetcode.com/problems/construct-uniform-parity-array-i/) | `Easy` | [4256-construct-uniform-parity-array-i](./4256-construct-uniform-parity-array-i) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Arrays / Prefix Minimums

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 4284 | [Smallest Stable Index I](https://leetcode.com/problems/smallest-stable-index-i/) | `Easy` | [4284-smallest-stable-index-i](./4284-smallest-stable-index-i) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Backtracking

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | `Medium` | [39-combination-sum](./39-combination-sum) | $\mathcal{O}(2^{T/M})$ | $\mathcal{O}(T/M)$ |
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | `Medium` | [46-permutations](./46-permutations) | $\mathcal{O}(N \cdot N!)$ | $\mathcal{O}(N)$ |
| 78 | [Subsets](https://leetcode.com/problems/subsets/) | `Medium` | [78-subsets](./78-subsets) | $\mathcal{O}(N \cdot 2^N)$ | $\mathcal{O}(N)$ |

### 📌 Backtracking / Matrix DFS

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 79 | [Word Search](https://leetcode.com/problems/word-search/) | `Medium` | [79-word-search](./79-word-search) | $\mathcal{O}(M \cdot N \cdot 3^L)$ | $\mathcal{O}(L)$ |

### 📌 Binary Search

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | `Medium` | [33-search-in-rotated-sorted-array](./33-search-in-rotated-sorted-array) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | `Medium` | [153-find-minimum-in-rotated-sorted-array](./153-find-minimum-in-rotated-sorted-array) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |

### 📌 Bit Manipulation

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 371 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | `Medium` | [371-sum-of-two-integers](./371-sum-of-two-integers) | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |

### 📌 Bit Manipulation / Math

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 268 | [Missing Number](https://leetcode.com/problems/missing-number/) | `Easy` | [268-missing-number](./268-missing-number) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Bit Manipulation / XOR

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | `Easy` | [136-single-number](./136-single-number) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Boyer-Moore Voting

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 169 | [Majority Element](https://leetcode.com/problems/majority-element/) | `Easy` | [169-majority-element](./169-majority-element) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Design / Doubly Linked List

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | `Medium` | [146-lru-cache](./146-lru-cache) | $\mathcal{O}(1)$ | $\mathcal{O}(C)$ |

### 📌 Dynamic Programming / Greedy

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 2559 | [Maximum Number of Non-Overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/) | `Hard` | [2559-maximum-number-of-non-overlapping-palindrome-substrings](./2559-maximum-number-of-non-overlapping-palindrome-substrings) | $\mathcal{O}(N \cdot k)$ | $\mathcal{O}(1)$ |

### 📌 Dynamic Programming / Kadane's Algorithm

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | `Medium` | [53-maximum-subarray](./53-maximum-subarray) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Dynamic Programming / Math

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 1013 | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | `Easy` | [1013-fibonacci-number](./1013-fibonacci-number) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Dynamic Programming / Patience Sorting

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | `Medium` | [300-longest-increasing-subsequence](./300-longest-increasing-subsequence) | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |

### 📌 Graph / BFS/DFS

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | `Medium` | [133-clone-graph](./133-clone-graph) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | `Medium` | [200-number-of-islands](./200-number-of-islands) | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(M \cdot N)$ |

### 📌 Graph / Multi-source BFS

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | `Medium` | [417-pacific-atlantic-water-flow](./417-pacific-atlantic-water-flow) | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(M \cdot N)$ |

### 📌 Graph / Topological Sort

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | `Medium` | [207-course-schedule](./207-course-schedule) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ |

### 📌 Greedy

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | `Medium` | [55-jump-game](./55-jump-game) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Greedy / Sorting

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 1574 | [Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/) | `Easy` | [1574-maximum-product-of-two-elements-in-an-array](./1574-maximum-product-of-two-elements-in-an-array) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 2042 | [Maximum Product Difference Between Two Pairs](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/) | `Easy` | [2042-maximum-product-difference-between-two-pairs](./2042-maximum-product-difference-between-two-pairs) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Hash Set / Combinatorics

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 3799 | [Unique 3-Digit Even Numbers](https://leetcode.com/problems/unique-3-digit-even-numbers/) | `Easy` | [3799-unique-3-digit-even-numbers](./3799-unique-3-digit-even-numbers) | $\mathcal{O}(N + 450)$ | $\mathcal{O}(1)$ |

### 📌 Hash Set / Math

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 4080 | [Smallest Missing Multiple of K](https://leetcode.com/problems/smallest-missing-multiple-of-k/) | `Easy` | [4080-smallest-missing-multiple-of-k](./4080-smallest-missing-multiple-of-k) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Hash Table / Greedy

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 409 | [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) | `Easy` | [409-longest-palindrome](./409-longest-palindrome) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Heap / Bucket Sort

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | `Medium` | [347-top-k-frequent-elements](./347-top-k-frequent-elements) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Heap / Priority Queue

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | `Hard` | [23-merge-k-sorted-lists](./23-merge-k-sorted-lists) | $\mathcal{O}(N \log k)$ | $\mathcal{O}(k)$ |

### 📌 Heap / QuickSelect

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | `Medium` | [215-kth-largest-element-in-an-array](./215-kth-largest-element-in-an-array) | $\mathcal{O}(N \log k)$ | $\mathcal{O}(k)$ |

### 📌 Intervals

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | `Medium` | [56-merge-intervals](./56-merge-intervals) | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
| 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | `Medium` | [57-insert-interval](./57-insert-interval) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Intervals / Greedy

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | `Medium` | [435-non-overlapping-intervals](./435-non-overlapping-intervals) | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ |

### 📌 Linked List

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | `Medium` | [19-remove-nth-node-from-end-of-list](./19-remove-nth-node-from-end-of-list) | $\mathcal{O}(L)$ | $\mathcal{O}(1)$ |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | `Easy` | [21-merge-two-sorted-lists](./21-merge-two-sorted-lists) | $\mathcal{O}(N + M)$ | $\mathcal{O}(1)$ |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | `Medium` | [143-reorder-list](./143-reorder-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | `Easy` | [206-reverse-linked-list](./206-reverse-linked-list) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Linked List / Fast & Slow Pointers

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | `Easy` | [141-linked-list-cycle](./141-linked-list-cycle) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Math

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | `Easy` | [9-palindrome-number](./9-palindrome-number) | $\mathcal{O}(\log_{10}(N))$ | $\mathcal{O}(1)$ |

### 📌 Math / Bit Manipulation

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | `Medium` | [7-reverse-integer](./7-reverse-integer) | $\mathcal{O}(\log_{10}(N))$ | $\mathcal{O}(1)$ |

### 📌 Math / Combinatorics

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 4248 | [Count Commas in Range II](https://leetcode.com/problems/count-commas-in-range-ii/) | `Medium` | [4248-count-commas-in-range-ii](./4248-count-commas-in-range-ii) | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |

### 📌 Math / Digit Counting

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 4245 | [Count Commas in Range](https://leetcode.com/problems/count-commas-in-range/) | `Easy` | [4245-count-commas-in-range](./4245-count-commas-in-range) | $\mathcal{O}(\log_{1000}(N))$ | $\mathcal{O}(1)$ |

### 📌 Math / Minimax DP

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 909 | [Stone Game](https://leetcode.com/problems/stone-game/) | `Medium` | [909-stone-game](./909-stone-game) | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |

### 📌 Math / Sorting

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 628 | [Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/) | `Easy` | [628-maximum-product-of-three-numbers](./628-maximum-product-of-three-numbers) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Matrix

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | `Medium` | [48-rotate-image](./48-rotate-image) | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ |
| 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | `Medium` | [54-spiral-matrix](./54-spiral-matrix) | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(1)$ |
| 73 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | `Medium` | [73-set-matrix-zeroes](./73-set-matrix-zeroes) | $\mathcal{O}(M \cdot N)$ | $\mathcal{O}(1)$ |

### 📌 Monotonic Stack

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | `Hard` | [84-largest-rectangle-in-histogram](./84-largest-rectangle-in-histogram) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Prefix & Suffix Products

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | `Medium` | [238-product-of-array-except-self](./238-product-of-array-except-self) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 SQL

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 584 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) | `Easy` | [584-find-customer-referee](./584-find-customer-referee) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 595 | [Big Countries](https://leetcode.com/problems/big-countries/) | `Easy` | [595-big-countries](./595-big-countries) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 1258 | [Article Views I](https://leetcode.com/problems/article-views-i/) | `Easy` | [1258-article-views-i](./1258-article-views-i) | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
| 1827 | [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/) | `Easy` | [1827-invalid-tweets](./1827-invalid-tweets) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 1908 | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) | `Easy` | [1908-recyclable-and-low-fat-products](./1908-recyclable-and-low-fat-products) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Sliding Window

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | `Medium` | [3-longest-substring-without-repeating-characters](./3-longest-substring-without-repeating-characters) | $\mathcal{O}(N)$ | $\mathcal{O}(\min(N, M))$ |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | `Hard` | [76-minimum-window-substring](./76-minimum-window-substring) | $\mathcal{O}(N + M)$ | $\mathcal{O}(N + M)$ |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | `Easy` | [121-best-time-to-buy-and-sell-stock](./121-best-time-to-buy-and-sell-stock) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | `Medium` | [424-longest-repeating-character-replacement](./424-longest-repeating-character-replacement) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Stack

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | `Easy` | [20-valid-parentheses](./20-valid-parentheses) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Stack Design

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | `Medium` | [155-min-stack](./155-min-stack) | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |

### 📌 Tree / BFS

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | `Medium` | [102-binary-tree-level-order-traversal](./102-binary-tree-level-order-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Tree / BST

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | `Medium` | [98-validate-binary-search-tree](./98-validate-binary-search-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 235 | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | `Medium` | [235-lowest-common-ancestor-of-a-binary-search-tree](./235-lowest-common-ancestor-of-a-binary-search-tree) | $\mathcal{O}(H)$ | $\mathcal{O}(1)$ |

### 📌 Tree / BST Inorder

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 230 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | `Medium` | [230-kth-smallest-element-in-a-bst](./230-kth-smallest-element-in-a-bst) | $\mathcal{O}(H + k)$ | $\mathcal{O}(H)$ |

### 📌 Tree / DFS

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 100 | [Same Tree](https://leetcode.com/problems/same-tree/) | `Easy` | [100-same-tree](./100-same-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | `Easy` | [104-maximum-depth-of-binary-tree](./104-maximum-depth-of-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |

### 📌 Tree / Divide & Conquer

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | `Medium` | [105-construct-binary-tree-from-preorder-and-inorder-traversal](./105-construct-binary-tree-from-preorder-and-inorder-traversal) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Tree / Post-order DFS

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | `Hard` | [124-binary-tree-maximum-path-sum](./124-binary-tree-maximum-path-sum) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |

### 📌 Tree / Postorder DFS

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 2347 | [Count Nodes Equal to Average of Subtree](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/) | `Medium` | [2347-count-nodes-equal-to-average-of-subtree](./2347-count-nodes-equal-to-average-of-subtree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |

### 📌 Tree / Recursion

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | `Easy` | [226-invert-binary-tree](./226-invert-binary-tree) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |

### 📌 Trie

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 208 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | `Medium` | [208-implement-trie-prefix-tree](./208-implement-trie-prefix-tree) | $\mathcal{O}(L)$ | $\mathcal{O}(N \cdot L)$ |

### 📌 Trie + Backtracking

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 212 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | `Hard` | [212-word-search-ii](./212-word-search-ii) | $\mathcal{O}(M \cdot N \cdot 4^{L})$ | $\mathcal{O}(W \cdot L)$ |

### 📌 Trie / DFS

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 211 | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | `Medium` | [211-design-add-and-search-words-data-structure](./211-design-add-and-search-words-data-structure) | $\mathcal{O}(M)$ | $\mathcal{O}(N \cdot M)$ |

### 📌 Two Heaps

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 295 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | `Hard` | [295-find-median-from-data-stream](./295-find-median-from-data-stream) | $\mathcal{O}(\log N)$ | $\mathcal{O}(N)$ |

### 📌 Two Pointers

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | `Medium` | [11-container-with-most-water](./11-container-with-most-water) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | `Medium` | [15-3sum](./15-3sum) | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | `Easy` | [26-remove-duplicates-from-sorted-array](./26-remove-duplicates-from-sorted-array) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 31 | [Next Permutation](https://leetcode.com/problems/next-permutation/) | `Medium` | [31-next-permutation](./31-next-permutation) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | `Hard` | [42-trapping-rain-water](./42-trapping-rain-water) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | `Medium` | [75-sort-colors](./75-sort-colors) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | `Easy` | [125-valid-palindrome](./125-valid-palindrome) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 189 | [Rotate Array](https://leetcode.com/problems/rotate-array/) | `Medium` | [189-rotate-array](./189-rotate-array) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | `Easy` | [283-move-zeroes](./283-move-zeroes) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | `Easy` | [344-reverse-string](./344-reverse-string) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

### 📌 Two Pointers / Arrays

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 2271 | [Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/) | `Medium` | [2271-rearrange-array-elements-by-sign](./2271-rearrange-array-elements-by-sign) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

### 📌 Two Pointers / DP

| # | Problem | Difficulty | Solution Folder | Time | Space |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 647 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | `Medium` | [647-palindromic-substrings](./647-palindromic-substrings) | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ |

---

## 📋 Complete Master Index (All 100 Problems)

| # | Problem Title | Topic | Difficulty | Deep Explanation & Walkthrough |
| :---: | :--- | :--- | :---: | :--- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Arrays & Hashing | `Easy` | [Two Sum Solution](./1-two-sum/README.md) |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding Window | `Medium` | [Longest Substring Without Repeating Characters Solution](./3-longest-substring-without-repeating-characters/README.md) |
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Math / Bit Manipulation | `Medium` | [Reverse Integer Solution](./7-reverse-integer/README.md) |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Math | `Easy` | [Palindrome Number Solution](./9-palindrome-number/README.md) |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Two Pointers | `Medium` | [Container With Most Water Solution](./11-container-with-most-water/README.md) |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | Two Pointers | `Medium` | [3Sum Solution](./15-3sum/README.md) |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Linked List | `Medium` | [Remove Nth Node From End of List Solution](./19-remove-nth-node-from-end-of-list/README.md) |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack | `Easy` | [Valid Parentheses Solution](./20-valid-parentheses/README.md) |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Linked List | `Easy` | [Merge Two Sorted Lists Solution](./21-merge-two-sorted-lists/README.md) |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Heap / Priority Queue | `Hard` | [Merge k Sorted Lists Solution](./23-merge-k-sorted-lists/README.md) |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Two Pointers | `Easy` | [Remove Duplicates from Sorted Array Solution](./26-remove-duplicates-from-sorted-array/README.md) |
| 31 | [Next Permutation](https://leetcode.com/problems/next-permutation/) | Two Pointers | `Medium` | [Next Permutation Solution](./31-next-permutation/README.md) |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Binary Search | `Medium` | [Search in Rotated Sorted Array Solution](./33-search-in-rotated-sorted-array/README.md) |
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Backtracking | `Medium` | [Combination Sum Solution](./39-combination-sum/README.md) |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Two Pointers | `Hard` | [Trapping Rain Water Solution](./42-trapping-rain-water/README.md) |
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | Backtracking | `Medium` | [Permutations Solution](./46-permutations/README.md) |
| 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Matrix | `Medium` | [Rotate Image Solution](./48-rotate-image/README.md) |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Arrays & Hashing | `Medium` | [Group Anagrams Solution](./49-group-anagrams/README.md) |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Dynamic Programming / Kadane's Algorithm | `Medium` | [Maximum Subarray Solution](./53-maximum-subarray/README.md) |
| 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Matrix | `Medium` | [Spiral Matrix Solution](./54-spiral-matrix/README.md) |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | Greedy | `Medium` | [Jump Game Solution](./55-jump-game/README.md) |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Intervals | `Medium` | [Merge Intervals Solution](./56-merge-intervals/README.md) |
| 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Intervals | `Medium` | [Insert Interval Solution](./57-insert-interval/README.md) |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | 1D Dynamic Programming | `Easy` | [Climbing Stairs Solution](./70-climbing-stairs/README.md) |
| 73 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Matrix | `Medium` | [Set Matrix Zeroes Solution](./73-set-matrix-zeroes/README.md) |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Two Pointers | `Medium` | [Sort Colors Solution](./75-sort-colors/README.md) |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Sliding Window | `Hard` | [Minimum Window Substring Solution](./76-minimum-window-substring/README.md) |
| 78 | [Subsets](https://leetcode.com/problems/subsets/) | Backtracking | `Medium` | [Subsets Solution](./78-subsets/README.md) |
| 79 | [Word Search](https://leetcode.com/problems/word-search/) | Backtracking / Matrix DFS | `Medium` | [Word Search Solution](./79-word-search/README.md) |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Monotonic Stack | `Hard` | [Largest Rectangle in Histogram Solution](./84-largest-rectangle-in-histogram/README.md) |
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Tree / BST | `Medium` | [Validate Binary Search Tree Solution](./98-validate-binary-search-tree/README.md) |
| 100 | [Same Tree](https://leetcode.com/problems/same-tree/) | Tree / DFS | `Easy` | [Same Tree Solution](./100-same-tree/README.md) |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Tree / BFS | `Medium` | [Binary Tree Level Order Traversal Solution](./102-binary-tree-level-order-traversal/README.md) |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Tree / DFS | `Easy` | [Maximum Depth of Binary Tree Solution](./104-maximum-depth-of-binary-tree/README.md) |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Tree / Divide & Conquer | `Medium` | [Construct Binary Tree from Preorder and Inorder Traversal Solution](./105-construct-binary-tree-from-preorder-and-inorder-traversal/README.md) |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Sliding Window | `Easy` | [Best Time to Buy and Sell Stock Solution](./121-best-time-to-buy-and-sell-stock/README.md) |
| 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Tree / Post-order DFS | `Hard` | [Binary Tree Maximum Path Sum Solution](./124-binary-tree-maximum-path-sum/README.md) |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Two Pointers | `Easy` | [Valid Palindrome Solution](./125-valid-palindrome/README.md) |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Arrays & Hashing | `Medium` | [Longest Consecutive Sequence Solution](./128-longest-consecutive-sequence/README.md) |
| 133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Graph / BFS/DFS | `Medium` | [Clone Graph Solution](./133-clone-graph/README.md) |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | Bit Manipulation / XOR | `Easy` | [Single Number Solution](./136-single-number/README.md) |
| 139 | [Word Break](https://leetcode.com/problems/word-break/) | 1D Dynamic Programming | `Medium` | [Word Break Solution](./139-word-break/README.md) |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Linked List / Fast & Slow Pointers | `Easy` | [Linked List Cycle Solution](./141-linked-list-cycle/README.md) |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | Linked List | `Medium` | [Reorder List Solution](./143-reorder-list/README.md) |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Design / Doubly Linked List | `Medium` | [LRU Cache Solution](./146-lru-cache/README.md) |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | 1D Dynamic Programming | `Medium` | [Maximum Product Subarray Solution](./152-maximum-product-subarray/README.md) |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Binary Search | `Medium` | [Find Minimum in Rotated Sorted Array Solution](./153-find-minimum-in-rotated-sorted-array/README.md) |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | Stack Design | `Medium` | [Min Stack Solution](./155-min-stack/README.md) |
| 169 | [Majority Element](https://leetcode.com/problems/majority-element/) | Boyer-Moore Voting | `Easy` | [Majority Element Solution](./169-majority-element/README.md) |
| 189 | [Rotate Array](https://leetcode.com/problems/rotate-array/) | Two Pointers | `Medium` | [Rotate Array Solution](./189-rotate-array/README.md) |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | 1D Dynamic Programming | `Medium` | [House Robber Solution](./198-house-robber/README.md) |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Graph / BFS/DFS | `Medium` | [Number of Islands Solution](./200-number-of-islands/README.md) |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Linked List | `Easy` | [Reverse Linked List Solution](./206-reverse-linked-list/README.md) |
| 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Graph / Topological Sort | `Medium` | [Course Schedule Solution](./207-course-schedule/README.md) |
| 208 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Trie | `Medium` | [Implement Trie (Prefix Tree) Solution](./208-implement-trie-prefix-tree/README.md) |
| 211 | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Trie / DFS | `Medium` | [Design Add and Search Words Data Structure Solution](./211-design-add-and-search-words-data-structure/README.md) |
| 212 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Trie + Backtracking | `Hard` | [Word Search II Solution](./212-word-search-ii/README.md) |
| 213 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | 1D Dynamic Programming / Circular | `Medium` | [House Robber II Solution](./213-house-robber-ii/README.md) |
| 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Heap / QuickSelect | `Medium` | [Kth Largest Element in an Array Solution](./215-kth-largest-element-in-an-array/README.md) |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Arrays & Hashing | `Easy` | [Contains Duplicate Solution](./217-contains-duplicate/README.md) |
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Tree / Recursion | `Easy` | [Invert Binary Tree Solution](./226-invert-binary-tree/README.md) |
| 230 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Tree / BST Inorder | `Medium` | [Kth Smallest Element in a BST Solution](./230-kth-smallest-element-in-a-bst/README.md) |
| 235 | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Tree / BST | `Medium` | [Lowest Common Ancestor of a Binary Search Tree Solution](./235-lowest-common-ancestor-of-a-binary-search-tree/README.md) |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Prefix & Suffix Products | `Medium` | [Product of Array Except Self Solution](./238-product-of-array-except-self/README.md) |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Arrays & Hashing | `Easy` | [Valid Anagram Solution](./242-valid-anagram/README.md) |
| 268 | [Missing Number](https://leetcode.com/problems/missing-number/) | Bit Manipulation / Math | `Easy` | [Missing Number Solution](./268-missing-number/README.md) |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Two Pointers | `Easy` | [Move Zeroes Solution](./283-move-zeroes/README.md) |
| 295 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Two Heaps | `Hard` | [Find Median from Data Stream Solution](./295-find-median-from-data-stream/README.md) |
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Dynamic Programming / Patience Sorting | `Medium` | [Longest Increasing Subsequence Solution](./300-longest-increasing-subsequence/README.md) |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | 1D Dynamic Programming | `Medium` | [Coin Change Solution](./322-coin-change/README.md) |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Two Pointers | `Easy` | [Reverse String Solution](./344-reverse-string/README.md) |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Heap / Bucket Sort | `Medium` | [Top K Frequent Elements Solution](./347-top-k-frequent-elements/README.md) |
| 371 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Bit Manipulation | `Medium` | [Sum of Two Integers Solution](./371-sum-of-two-integers/README.md) |
| 409 | [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) | Hash Table / Greedy | `Easy` | [Longest Palindrome Solution](./409-longest-palindrome/README.md) |
| 417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Graph / Multi-source BFS | `Medium` | [Pacific Atlantic Water Flow Solution](./417-pacific-atlantic-water-flow/README.md) |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Sliding Window | `Medium` | [Longest Repeating Character Replacement Solution](./424-longest-repeating-character-replacement/README.md) |
| 435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Intervals / Greedy | `Medium` | [Non-overlapping Intervals Solution](./435-non-overlapping-intervals/README.md) |
| 485 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | Arrays | `Easy` | [Max Consecutive Ones Solution](./485-max-consecutive-ones/README.md) |
| 584 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) | SQL | `Easy` | [Find Customer Referee Solution](./584-find-customer-referee/README.md) |
| 595 | [Big Countries](https://leetcode.com/problems/big-countries/) | SQL | `Easy` | [Big Countries Solution](./595-big-countries/README.md) |
| 628 | [Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/) | Math / Sorting | `Easy` | [Maximum Product of Three Numbers Solution](./628-maximum-product-of-three-numbers/README.md) |
| 647 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Two Pointers / DP | `Medium` | [Palindromic Substrings Solution](./647-palindromic-substrings/README.md) |
| 909 | [Stone Game](https://leetcode.com/problems/stone-game/) | Math / Minimax DP | `Medium` | [Stone Game Solution](./909-stone-game/README.md) |
| 1013 | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Dynamic Programming / Math | `Easy` | [Fibonacci Number Solution](./1013-fibonacci-number/README.md) |
| 1143 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | 2D Dynamic Programming | `Medium` | [Longest Common Subsequence Solution](./1143-longest-common-subsequence/README.md) |
| 1258 | [Article Views I](https://leetcode.com/problems/article-views-i/) | SQL | `Easy` | [Article Views I Solution](./1258-article-views-i/README.md) |
| 1574 | [Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/) | Greedy / Sorting | `Easy` | [Maximum Product of Two Elements in an Array Solution](./1574-maximum-product-of-two-elements-in-an-array/README.md) |
| 1827 | [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/) | SQL | `Easy` | [Invalid Tweets Solution](./1827-invalid-tweets/README.md) |
| 1878 | [Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) | Arrays | `Easy` | [Check if Array Is Sorted and Rotated Solution](./1878-check-if-array-is-sorted-and-rotated/README.md) |
| 1908 | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) | SQL | `Easy` | [Recyclable and Low Fat Products Solution](./1908-recyclable-and-low-fat-products/README.md) |
| 2042 | [Maximum Product Difference Between Two Pairs](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/) | Greedy / Sorting | `Easy` | [Maximum Product Difference Between Two Pairs Solution](./2042-maximum-product-difference-between-two-pairs/README.md) |
| 2271 | [Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/) | Two Pointers / Arrays | `Medium` | [Rearrange Array Elements by Sign Solution](./2271-rearrange-array-elements-by-sign/README.md) |
| 2347 | [Count Nodes Equal to Average of Subtree](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/) | Tree / Postorder DFS | `Medium` | [Count Nodes Equal to Average of Subtree Solution](./2347-count-nodes-equal-to-average-of-subtree/README.md) |
| 2559 | [Maximum Number of Non-Overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/) | Dynamic Programming / Greedy | `Hard` | [Maximum Number of Non-Overlapping Palindrome Substrings Solution](./2559-maximum-number-of-non-overlapping-palindrome-substrings/README.md) |
| 3799 | [Unique 3-Digit Even Numbers](https://leetcode.com/problems/unique-3-digit-even-numbers/) | Hash Set / Combinatorics | `Easy` | [Unique 3-Digit Even Numbers Solution](./3799-unique-3-digit-even-numbers/README.md) |
| 4080 | [Smallest Missing Multiple of K](https://leetcode.com/problems/smallest-missing-multiple-of-k/) | Hash Set / Math | `Easy` | [Smallest Missing Multiple of K Solution](./4080-smallest-missing-multiple-of-k/README.md) |
| 4245 | [Count Commas in Range](https://leetcode.com/problems/count-commas-in-range/) | Math / Digit Counting | `Easy` | [Count Commas in Range Solution](./4245-count-commas-in-range/README.md) |
| 4248 | [Count Commas in Range II](https://leetcode.com/problems/count-commas-in-range-ii/) | Math / Combinatorics | `Medium` | [Count Commas in Range II Solution](./4248-count-commas-in-range-ii/README.md) |
| 4256 | [Construct Uniform Parity Array I](https://leetcode.com/problems/construct-uniform-parity-array-i/) | Arrays / Math | `Easy` | [Construct Uniform Parity Array I Solution](./4256-construct-uniform-parity-array-i/README.md) |
| 4284 | [Smallest Stable Index I](https://leetcode.com/problems/smallest-stable-index-i/) | Arrays / Prefix Minimums | `Easy` | [Smallest Stable Index I Solution](./4284-smallest-stable-index-i/README.md) |

---

## 🛠️ Repository Structure

```
leetcode/
├── README.md                                    # Master catalog and study roadmap
├── 1-two-sum/
│   ├── README.md                                # 30-sec pitch, intuition, dry-run & analysis
│   ├── Solution.java                            # Commented Java solution
│   └── solution.py                              # Clean Python 3 solution
├── 3-longest-substring-without-repeating-characters/
│   ├── README.md
│   ├── Solution.java
│   └── solution.py
... (100 total curated problem folders)
```

---

## 🤝 Open Source & Contributions
Authored and maintained by [Aniket Chavan](https://github.com/Aniketchavan7). Contributions, optimizations, and new language translations (C++, Go, Rust, TypeScript) are warmly welcome!
