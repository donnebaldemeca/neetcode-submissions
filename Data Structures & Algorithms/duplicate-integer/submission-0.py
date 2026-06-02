class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_hashmap = {}
        for num in nums:
            if num not in dup_hashmap:
                dup_hashmap[num] = 1
            elif num in dup_hashmap:
                return True
        return False



