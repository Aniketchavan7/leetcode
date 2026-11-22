# Algorithmic Pattern: Trie (Prefix Tree) & Bitwise Trie

## 1. Overview
A Trie is an efficient tree-like search data structure used for prefix matching, dictionary lookups, and bitwise maximum XOR computations in $O(L)$ time.

## 2. Bitwise Maximum XOR Trie
```python
class BitwiseTrieNode:
    def __init__(self):
        self.children = [None, None]

class BitwiseTrie:
    def __init__(self, bit_length: int = 31):
        self.root = BitwiseTrieNode()
        self.bit_length = bit_length

    def insert(self, num: int) -> None:
        curr = self.root
        for i in range(self.bit_length, -1, -1):
            bit = (num >> i) & 1
            if not curr.children[bit]:
                curr.children[bit] = BitwiseTrieNode()
            curr = curr.children[bit]

    def find_max_xor(self, num: int) -> int:
        curr = self.root
        max_xor = 0
        for i in range(self.bit_length, -1, -1):
            bit = (num >> i) & 1
            opp_bit = 1 - bit
            if curr.children[opp_bit]:
                max_xor |= (1 << i)
                curr = curr.children[opp_bit]
            else:
                curr = curr.children[bit]
        return max_xor
```
