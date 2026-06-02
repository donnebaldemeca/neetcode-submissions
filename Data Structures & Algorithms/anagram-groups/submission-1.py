class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            sort_str = "".join(sorted(s))
            if sort_str in hashmap:
                hashmap[sort_str].append(s)
            else:
                hashmap[sort_str] = [s]
        return list(hashmap.values())