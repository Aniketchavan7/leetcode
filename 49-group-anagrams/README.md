# 49. Group Anagrams

[![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)](https://leetcode.com/problems/group-anagrams/)
[![Topic: Arrays & Hashing](https://img.shields.io/badge/Topic-Arrays%20%26%20Hashing-blue)](https://leetcode.com/problems/group-anagrams/)

---

### 🎯 How to Explain This to an Interviewer (The 30-Second Pitch)
> "Anagrams contain the exact same characters with the same frequencies. If we normalize each string into a canonical key (either by sorting its characters or by counting letter frequencies into a 26-element tuple), all anagrams will produce the identical key. We group them into a Hash Map keyed by this canonical form."

---

### 💡 Intuition & Core Insight
- **Equivalence Relation**: Anagram is an equivalence relation. An equivalence class can be uniquely represented by its sorted string (e.g. 'eat', 'tea', 'ate' all sort to 'aet').
- **Counting Array Alternative**: For strings of length K, frequency counting creates a key in O(K) without sorting.

---

### 🔍 Step-by-Step Visual Dry Run
**Input**: `["eat", "tea", "tan", "ate", "nat", "bat"]`
- 'eat' -> key 'aet' -> map['aet'] = ['eat']
- 'tea' -> key 'aet' -> map['aet'] = ['eat', 'tea']
- 'tan' -> key 'ant' -> map['ant'] = ['tan']
- 'ate' -> key 'aet' -> map['aet'] = ['eat', 'tea', 'ate']
- 'nat' -> key 'ant' -> map['ant'] = ['tan', 'nat']
- 'bat' -> key 'abt' -> map['abt'] = ['bat']
Output: `[["eat","tea","ate"], ["tan","nat"], ["bat"]]`.

---

### 💻 Optimal Implementations

#### Java Solution
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
```

#### Python 3 Solution
```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())
```

---

### ⚡ Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \cdot K \log K)$ — N strings of maximum length K sorted in O(K log K) each. (Or O(N * K) using frequency tuples).
- **Space Complexity**: $\mathcal{O}(N \cdot K)$ — Hash map stores all characters across all strings.

---

### ⚠️ Edge Cases & Interview Traps
1. Empty string [""]: groups as [[""]].
2. Single character strings: groups identical characters together.

---

### 💬 Follow-Up Questions You Might Get
- *What if strings contain Unicode/emojis?* Use a HashMap<Integer, Integer> codepoint counter as the key.
