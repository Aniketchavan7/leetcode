class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())
