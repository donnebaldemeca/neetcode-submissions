class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for s in strs:
            sort_str = "".join(sorted(s))
            if sort_str in my_dict:
                my_dict[sort_str].append(s)
            else:
                my_dict.setdefault(sort_str, []).append(s)
        
        return [v for v in my_dict.values()]