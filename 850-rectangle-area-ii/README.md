# 850. Rectangle Area II

[![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red)](https://leetcode.com/problems/rectangle-area-ii)
[![Topic: Segment Tree & Array & Ordered Set](https://img.shields.io/badge/Topic-Segment%20Tree%20&%20Array%20&%20Ordered%20Set-blue)](https://leetcode.com/problems/rectangle-area-ii)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "We identify the core problem bottleneck and apply an optimal Segment Tree strategy. By trading minimal auxiliary space for instant lookups or streamlined state transitions, we achieve optimal time bounds."

---

### 💡 Intuition & Core Insight
- **Bottleneck Elimination**: Naive approaches repeatedly re-scan data; we eliminate redundant checks.
- **Data Structure Invariant**: Using appropriate hash sets, heaps, or stacks gives amortized optimal lookups.
- **Single-Pass Mechanics**: Processing data sequentially maintains clean linear invariants.

---

### 🔍 Step-by-Step Visual Dry Run
**Sample Input**: `rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]`  
**Expected Output**: `6`

| Step | State / Pointer | Operation | Result / Invariant |
| :---: | :--- | :--- | :--- |
| 1 | Initial State | Parse input `rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]` | Initialize tracking variables |
| 2 | Iteration / Processing | Evaluate current element against invariant | Update optimal candidate state |
| 3 | Final Step | Terminate traversal and construct output | Return `6` |

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Node {
    int l, r, cnt, length;
}

class SegmentTree {
    private Node[] tr;
    private int[] nums;

    public SegmentTree(int[] nums) {
        this.nums = nums;
        int n = nums.length - 1;
        tr = new Node[n << 2];
        for (int i = 0; i < tr.length; ++i) {
            tr[i] = new Node();
        }
        build(1, 0, n - 1);
    }

    private void build(int u, int l, int r) {
        tr[u].l = l;
        tr[u].r = r;
        if (l != r) {
            int mid = (l + r) >> 1;
            build(u << 1, l, mid);
            build(u << 1 | 1, mid + 1, r);
        }
    }

    public void modify(int u, int l, int r, int k) {
        if (tr[u].l >= l && tr[u].r <= r) {
            tr[u].cnt += k;
        } else {
            int mid = (tr[u].l + tr[u].r) >> 1;
            if (l <= mid) {
                modify(u << 1, l, r, k);
            }
            if (r > mid) {
                modify(u << 1 | 1, l, r, k);
            }
        }
        pushup(u);
    }

    private void pushup(int u) {
        if (tr[u].cnt > 0) {
            tr[u].length = nums[tr[u].r + 1] - nums[tr[u].l];
        } else if (tr[u].l == tr[u].r) {
            tr[u].length = 0;
        } else {
            tr[u].length = tr[u << 1].length + tr[u << 1 | 1].length;
        }
    }

    public int query() {
        return tr[1].length;
    }
}

class Solution {
    private static final int MOD = (int) 1e9 + 7;

    public int rectangleArea(int[][] rectangles) {
        int n = rectangles.length;
        int[][] segs = new int[n << 1][4];
        int i = 0;
        TreeSet<Integer> ts = new TreeSet<>();
        for (var e : rectangles) {
            int x1 = e[0], y1 = e[1], x2 = e[2], y2 = e[3];
            segs[i++] = new int[] {x1, y1, y2, 1};
            segs[i++] = new int[] {x2, y1, y2, -1};
            ts.add(y1);
            ts.add(y2);
        }
        Arrays.sort(segs, (a, b) -> a[0] - b[0]);
        Map<Integer, Integer> m = new HashMap<>(ts.size());
        i = 0;
        int[] nums = new int[ts.size()];
        for (int v : ts) {
            m.put(v, i);
            nums[i++] = v;
        }

        SegmentTree tree = new SegmentTree(nums);
        long ans = 0;
        for (i = 0; i < segs.length; ++i) {
            var e = segs[i];
            int x = e[0], y1 = e[1], y2 = e[2], k = e[3];
            if (i > 0) {
                ans += (long) tree.query() * (x - segs[i - 1][0]);
            }
            tree.modify(1, m.get(y1), m.get(y2) - 1, k);
        }
        ans %= MOD;
        return (int) ans;
    }
}
```

#### Python 3 Solution
```python
class Node:
    def __init__(self):
        self.l = self.r = 0
        self.cnt = self.length = 0


class SegmentTree:
    def __init__(self, nums):
        n = len(nums) - 1
        self.nums = nums
        self.tr = [Node() for _ in range(n << 2)]
        self.build(1, 0, n - 1)

    def build(self, u, l, r):
        self.tr[u].l, self.tr[u].r = l, r
        if l != r:
            mid = (l + r) >> 1
            self.build(u << 1, l, mid)
            self.build(u << 1 | 1, mid + 1, r)

    def modify(self, u, l, r, k):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            self.tr[u].cnt += k
        else:
            mid = (self.tr[u].l + self.tr[u].r) >> 1
            if l <= mid:
                self.modify(u << 1, l, r, k)
            if r > mid:
                self.modify(u << 1 | 1, l, r, k)
        self.pushup(u)

    def pushup(self, u):
        if self.tr[u].cnt:
            self.tr[u].length = self.nums[self.tr[u].r + 1] - self.nums[self.tr[u].l]
        elif self.tr[u].l == self.tr[u].r:
            self.tr[u].length = 0
        else:
            self.tr[u].length = self.tr[u << 1].length + self.tr[u << 1 | 1].length

    @property
    def length(self):
        return self.tr[1].length


class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        segs = []
        alls = set()
        for x1, y1, x2, y2 in rectangles:
            segs.append((x1, y1, y2, 1))
            segs.append((x2, y1, y2, -1))
            alls.update([y1, y2])

        segs.sort()
        alls = sorted(alls)
        tree = SegmentTree(alls)
        m = {v: i for i, v in enumerate(alls)}
        ans = 0
        for i, (x, y1, y2, k) in enumerate(segs):
            if i:
                ans += tree.length * (x - segs[i - 1][0])
            tree.modify(1, m[y1], m[y2] - 1, k)
        ans %= int(1e9 + 7)
        return ans
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
